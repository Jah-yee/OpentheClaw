#!/bin/zsh
ROOT_DIR=\"$(cd \"$(dirname \"$0\")\"/.. && pwd)\"
python3 \"$ROOT_DIR/launcher/openclaw_launcher.py\" webui
