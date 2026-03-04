#!/usr/bin/env python3
"""One-click entry: run OpenClaw Web UI. Use from project root (e.g. python3 launch.py)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
launcher = os.path.join("launcher", "openclaw_launcher.py")
code = subprocess.run([sys.executable, launcher, "webui"]).returncode
sys.exit(code)
