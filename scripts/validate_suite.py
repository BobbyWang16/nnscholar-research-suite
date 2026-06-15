from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    test_file = repo_root / "tests" / "test_suite_structure.py"
    result = subprocess.run(
        [sys.executable, str(test_file)],
        cwd=repo_root,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
