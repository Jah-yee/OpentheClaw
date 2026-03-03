#!/bin/zsh
ROOT_DIR="$(cd "$(dirname "$0")"/.. && pwd)"
python3 "$ROOT_DIR/launcher/openclaw_launcher.py" config

#!/bin/zsh
SCRIPT_DIR=\"$(cd \"$(dirname \"$0\")\" && pwd)\"
python3 \"$SCRIPT_DIR/launcher/openclaw_launcher.py\" config

