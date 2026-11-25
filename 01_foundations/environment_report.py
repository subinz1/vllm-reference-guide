"""Print a non-secret environment baseline before installing vLLM."""

from __future__ import annotations

import platform
import shutil
import sys


def location(command: str) -> str:
    return shutil.which(command) or "not found"


print(f"python={sys.version.split()[0]}")
print(f"platform={platform.platform()}")
print(f"machine={platform.machine()}")
print(f"nvidia-smi={location('nvidia-smi')}")
print(f"rocminfo={location('rocminfo')}")
print(f"sycl-ls={location('sycl-ls')}")
