#!/usr/bin/env python
"""Small robust plotting helper for NNScholar 4.1.

This script intentionally covers common chart types only. For complex
multi-panel publication figures, use the skill workflow with custom code.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def read_table(path: Path, sheet: str | None = None) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix in {".csv"}:
        return pd.read_csv(path)
    if suffix in {".tsv", ".txt"}:
        return pd.read_csv(path, sep="\t")
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path, sheet_name=sheet or 0)
    if suffix == ".json":
        return pd.read_json(path)
    raise ValueError(f"Unsupported input file type: {suffix}")


def require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    missing = [col for col in columns if col and col not in df.columns]
    if missing:
        raise ValueError(f"Missing required column(s): {', '.join(missing)}")


def apply_style() -> None:
    sns.set_theme(style="ticks", context="paper")
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "DejaVu Sans"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.dpi": 150,
            "savefig.dpi": 300,
        }
    )


def make_plot(df: pd.DataFrame, args: argparse.Namespace) -> plt.Figure:
    require_columns(df, [args.x, args.y, args.group, args.facet, args.estimate, args.lower, args.upper, args.label, args.pvalue])
    apply_style()

    fig, ax = plt.subplots(figsize=(args.width, args.height))
    chart = args.chart.lower()
    palette = args.palette

    if chart == "scatter":
        sns.scatterplot(data=df, x=args.x, y=args.y, hue=args.group or None, ax=ax, palette=palette)
    elif chart == "line":
        sns.lineplot(data=df, x=args.x, y=args.y, hue=args.group or None, marker="o", errorbar=("ci", 95), ax=ax, palette=palette)
    elif chart == "bar":
        sns.barplot(data=df, x=args.x, y=args.y, hue=args.group or None, errorbar=("ci", 95), ax=ax, palette=palette)
    elif chart == "point":
        sns.pointplot(data=df, x=args.x, y=args.y, hue=args.group or None, errorbar=("ci", 95), dodge=bool(args.group), ax=ax, palette=palette)
    elif chart == "box":
        sns.boxplot(data=df, x=args.x, y=args.y, hue=args.group or None, ax=ax, palette=palette)
        sns.stripplot(data=df, x=args.x, y=args.y, hue=None, ax=ax, color="black", alpha=0.35, size=3)
    elif chart == "violin":
        sns.violinplot(data=df, x=args.x, y=args.y, hue=args.group or None, inner="box", cut=0, ax=ax, palette=palette)
    elif chart == "hist":
        require_columns(df, [args.x])
        sns.histplot(data=df, x=args.x, hue=args.group or None, kde=args.kde, ax=ax, palette=palette)
    elif chart == "heatmap":
        if args.y:
            matrix = df.pivot_table(index=args.y, columns=args.x, values=args.value or args.group, aggfunc="mean")
        else:
            numeric = df.select_dtypes(include="number")
            if numeric.empty:
                raise ValueError("Heatmap requires numeric columns or x/y/value columns.")
            matrix = numeric.corr()
        sns.heatmap(matrix, cmap=args.cmap, ax=ax, cbar_kws={"shrink": 0.8})
    elif chart in {"forest", "coef"}:
        label_col = args.label or args.y
        require_columns(df, [label_col, args.estimate, args.lower, args.upper])
        plot_df = df[[label_col, args.estimate, args.lower, args.upper]].dropna().copy()
        plot_df = plot_df.iloc[::-1]
        y_pos = np.arange(len(plot_df))
        estimates = plot_df[args.estimate].astype(float)
        lower = plot_df[args.lower].astype(float)
        upper = plot_df[args.upper].astype(float)
        ax.errorbar(
            estimates,
            y_pos,
            xerr=[estimates - lower, upper - estimates],
            fmt="o",
            color=args.color,
            ecolor=args.color,
            elinewidth=1.5,
            capsize=3,
        )
        ax.axvline(args.reference, color="0.5", linestyle="--", linewidth=1)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(plot_df[label_col])
        ax.set_xlabel(args.xlabel or args.estimate)
        ax.set_ylabel("")
    elif chart == "volcano":
        require_columns(df, [args.x, args.pvalue])
        p = pd.to_numeric(df[args.pvalue], errors="coerce").clip(lower=1e-300)
        x = pd.to_numeric(df[args.x], errors="coerce")
        y = -np.log10(p)
        sig = (p <= args.alpha) & (x.abs() >= args.fc_threshold)
        ax.scatter(x[~sig], y[~sig], s=14, color="0.65", alpha=0.75, edgecolors="none", label="Other")
        ax.scatter(x[sig], y[sig], s=18, color=args.color, alpha=0.9, edgecolors="none", label="Selected")
        ax.axhline(-math.log10(args.alpha), color="0.5", linestyle="--", linewidth=1)
        ax.axvline(args.fc_threshold, color="0.5", linestyle="--", linewidth=1)
        ax.axvline(-args.fc_threshold, color="0.5", linestyle="--", linewidth=1)
        ax.set_xlabel(args.xlabel or args.x)
        ax.set_ylabel(args.ylabel or f"-log10({args.pvalue})")
    elif chart == "roc":
        require_columns(df, [args.x or "fpr", args.y or "tpr"])
        x_col = args.x or "fpr"
        y_col = args.y or "tpr"
        if args.group:
            for name, group_df in df.groupby(args.group):
                group_df = group_df.sort_values(x_col)
                ax.plot(group_df[x_col], group_df[y_col], marker=None, label=str(name))
        else:
            plot_df = df.sort_values(x_col)
            ax.plot(plot_df[x_col], plot_df[y_col], color=args.color)
        ax.plot([0, 1], [0, 1], color="0.6", linestyle="--", linewidth=1)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel(args.xlabel or "False positive rate")
        ax.set_ylabel(args.ylabel or "True positive rate")
    elif chart == "stacked_bar":
        value_col = args.y or args.value
        if not value_col:
            raise ValueError("stacked_bar requires --y or --value to specify the numeric column.")
        require_columns(df, [args.x, args.group, value_col])
        table = df.pivot_table(index=args.x, columns=args.group, values=value_col, aggfunc="sum", fill_value=0)
        if args.normalize:
            table = table.div(table.sum(axis=1).replace(0, np.nan), axis=0) * 100
        table.plot(kind="bar", stacked=True, ax=ax, colormap=args.cmap)
        ax.set_xlabel(args.xlabel or args.x)
        ax.set_ylabel(args.ylabel or ("Percent" if args.normalize else value_col))
    else:
        raise ValueError(f"Unsupported chart type: {args.chart}")

    if args.title:
        ax.set_title(args.title)
    if args.xlabel:
        ax.set_xlabel(args.xlabel)
    if args.ylabel:
        ax.set_ylabel(args.ylabel)
    if args.rotate_x:
        ax.tick_params(axis="x", rotation=args.rotate_x)
    if ax.get_legend() is not None:
        ax.legend(frameon=False, title=args.group or None)
    sns.despine(ax=ax)
    fig.tight_layout()
    return fig


def write_manifest(output_dir: Path, args: argparse.Namespace, outputs: list[str]) -> None:
    manifest = {
        "input": str(args.input),
        "chart": args.chart,
        "x": args.x,
        "y": args.y,
        "group": args.group,
        "facet": args.facet,
        "outputs": outputs,
    }
    (output_dir / "plot_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a basic scientific plot from a structured table.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--sheet", default=None)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--basename", default="figure")
    parser.add_argument(
        "--chart",
        required=True,
        choices=["scatter", "line", "bar", "point", "box", "violin", "hist", "heatmap", "forest", "coef", "volcano", "roc", "stacked_bar"],
    )
    parser.add_argument("--x", default=None)
    parser.add_argument("--y", default=None)
    parser.add_argument("--group", default=None)
    parser.add_argument("--facet", default=None)
    parser.add_argument("--value", default=None)
    parser.add_argument("--label", default=None)
    parser.add_argument("--estimate", default=None)
    parser.add_argument("--lower", default=None)
    parser.add_argument("--upper", default=None)
    parser.add_argument("--pvalue", default=None)
    parser.add_argument("--title", default=None)
    parser.add_argument("--xlabel", default=None)
    parser.add_argument("--ylabel", default=None)
    parser.add_argument("--palette", default="colorblind")
    parser.add_argument("--cmap", default="viridis")
    parser.add_argument("--color", default="#1f77b4")
    parser.add_argument("--reference", default=0.0, type=float)
    parser.add_argument("--alpha", default=0.05, type=float)
    parser.add_argument("--fc-threshold", default=1.0, type=float)
    parser.add_argument("--normalize", action="store_true")
    parser.add_argument("--width", default=4.8, type=float)
    parser.add_argument("--height", default=3.6, type=float)
    parser.add_argument("--rotate-x", default=0, type=float)
    parser.add_argument("--kde", action="store_true")
    parser.add_argument("--formats", default="png,svg,pdf")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = read_table(args.input, args.sheet)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    fig = make_plot(df, args)

    outputs: list[str] = []
    for fmt in [item.strip().lower() for item in args.formats.split(",") if item.strip()]:
        out = args.output_dir / f"{args.basename}.{fmt}"
        fig.savefig(out, bbox_inches="tight")
        outputs.append(str(out))
    write_manifest(args.output_dir, args, outputs)
    print(json.dumps({"outputs": outputs}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
