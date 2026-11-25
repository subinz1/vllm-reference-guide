"""Print a non-secret baseline before choosing a vLLM installation path."""

from __future__ import annotations

import platform
import shutil
import sys


def command_version(command: str) -> str:
    path = shutil.which(command)
    return path if path is not None else "not found"


print(f"python={sys.version.split()[0]}")
print(f"platform={platform.platform()}")
print(f"machine={platform.machine()}")
print(f"nvidia-smi={command_version('nvidia-smi')}")
print(f"rocminfo={command_version('rocminfo')}")
print(f"sycl-ls={command_version('sycl-ls')}")
