<p align="center">
  <img src="https://raw.githubusercontent.com/Jah-yee/OpentheClaw/main/logo.svg" width="520" height="289" alt="OpentheClaw logo" />
</p>

<p align="center">
  One‑click SSH tunnel + Web UI starter.
  <br>
  No terminal needed. Every day Use.
</p>

<p align="center">
  <a href="https://github.com/Jah-yee/OpentheClaw">
    <img src="https://img.shields.io/github/stars/Jah-yee/OpentheClaw?style=social" alt="GitHub stars" />
  </a>
  <img src="https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-111827" alt="Supported platforms" />

 <p align="center"> 
  <a href="https://www.producthunt.com/products/opentheclaw?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-opentheclaw" target="_blank" rel="noopener noreferrer">
    <img alt="OpentheClaw - One-click launcher for OpenClaw Web UI over SSH | Product Hunt" width="250" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1089439&amp;theme=light&amp;t=1772620723494">
  </a>
</p>

---

# OpenClaw SSH Launcher

Your app's Web UI only listens on the server (e.g. `http://127.0.0.1:18789/`). You SSH in anyway—so why type commands every time? **Set it up once, then launch tunnel + browser with one double‑click.**

A tiny Python HTTP server: web config UI, then it runs your system `ssh` and opens the URL.

**✗ You never have to:**

- Open a terminal  
- Type SSH commands  
- Enter your password  
- Switch tabs

## Layout

```text
opentheclaw/
  launch.py               # one-click entry (run from project root; see below)
  logo.svg
  mac/
    OpenClaw.command      # start Web UI (double‑click)
    OpenClawShell.command # interactive SSH shell
    Click-once-OpenClawConfig.command  # open config UI

  linux/
    OpenClaw.sh           # start Web UI (./OpenClaw.sh or double‑click)
    Click-OpenClawConfig-linux.sh      # open config UI

  windows/
    OpenClaw.bat          # start Web UI (double‑click)
    Click-OpenClawConfig-windows.bat   # open config UI

  launcher/
    openclaw_launcher.py
    openclaw_launcher.json   # written by the web config UI

  README.md
  LICENSE
```

**One-click start**

- **Simplest (Linux / Windows):** From the project root, run `python3 launch.py` or `python launch.py`. This is the same as using the OS-specific launchers below and works without opening `mac/`, `linux/`, or `windows/`.
- **By OS:** Double‑click `mac/OpenClaw.command` (macOS), run `linux/OpenClaw.sh` (Linux), or double‑click `windows/OpenClaw.bat` (Windows). Each invokes `launch.py` at the project root.

## Requirements

- Python 3
- An `ssh` client available on `PATH`
  - macOS: built‑in OpenSSH works fine
  - Linux: any standard OpenSSH client
  - Windows: OpenSSH (Windows 10+), Git for Windows SSH, or another compatible `ssh`

## Getting started

Download the project as a ZIP from [Releases](https://github.com/Jah-yee/OpentheClaw/releases) or clone it:

```bash
git clone https://github.com/Jah-yee/OpentheClaw.git
cd OpentheClaw
```

You can move the project folder anywhere; keep its internal structure unchanged.

Think of the flow in two steps: (1) **Configure once** in the browser. (2) **Use the launcher** to start the Web UI whenever you need it. On the config page, fill in **connection name**, **SSH address** (e.g. `root@43.210.12.345`), and **Web UI URL** (e.g. `http://127.0.0.1:18789/`). Use “Show advanced options” for ports and optional password, then **Save** or **Save & start Web UI**.

### Mac

- **Configure once:** Double‑click `mac/Click-once-OpenClawConfig.command`. Your browser opens the config page.
- **Start Web UI:** Double‑click `mac/OpenClaw.command`. The launcher starts the tunnel and opens the Web UI; if the tunnel fails, the config page opens so you can fix credentials.
- **SSH shell (optional):** Double‑click `mac/OpenClawShell.command` for an interactive SSH session with the same port forwarding.

### Linux

- **Configure once:** Double‑click `linux/Click-OpenClawConfig-linux.sh` (or right‑click → Run). If your desktop asks “Run in terminal” or “Display”, choose **Run** or **Execute**. Your browser opens the config page.
- **Start Web UI:** Double‑click `linux/OpenClaw.sh`, or run `./linux/OpenClaw.sh` from the project folder in a terminal. If the tunnel fails, the config page opens so you can fix credentials.

### Windows

- **Configure once:** Double‑click `windows/Click-OpenClawConfig-windows.bat`. A console window may briefly appear; your browser opens the config page.
- **Start Web UI:** Double‑click `windows/OpenClaw.bat`. If the tunnel fails, run the config batch again to fix credentials. If you see “Python not found”, install Python 3 from [python.org](https://www.python.org/) and ensure it is in PATH.

### Terminal (any platform)

From the project root you can open the config UI, start the Web UI, or open an interactive SSH shell. The config and launch commands open your browser when needed.

| Goal           | Command |
|----------------|---------|
| Open config UI | `python3 launcher/openclaw_launcher.py config` |
| Start Web UI   | `python3 launch.py` |
| SSH shell      | `python3 launcher/openclaw_launcher.py shell` |

On Windows use `python` instead of `python3` if that’s what’s on your PATH.

## Config file

Stored in `launcher/openclaw_launcher.json`. Example:

```json
{
  "name": "OpenClaw",
  "host": "43.159.36.166",
  "user": "root",
  "local_port": 18789,
  "remote_host": "127.0.0.1",
  "remote_port": 18789,
  "web_url": "http://127.0.0.1:18789/",
  "password": ""
}
```

Edit via the web config UI. Important fields: `user`/`host` (SSH), `web_url` (browser target); ports default to 18789.

## Security

Prefer SSH keys; the launcher supports key-based auth. The `password` field is stored in plain text in the local JSON—use only on trusted machines. Intended for personal/dev/test use.

## Dependencies

Python 3 stdlib, system `ssh`, and a default browser. All logic is in `launcher/openclaw_launcher.py`.

**Releases:** [GitHub Releases](https://github.com/Jah-yee/OpentheClaw/releases) — download a version’s **Source code (zip)** or **tar.gz**, unpack, and use as in Getting started. To cut a release: tag and push (`git tag -a v1.1.0 -m "Release v1.1.0"` then `git push origin v1.1.0`), then create the release and attach the source zip in the GitHub UI.

**Package / deployment:** Not on PyPI; the repo or a release archive is the distributable. Unpack (or clone) and run; no server to deploy—the launcher runs on the user’s machine. For scripts, run `python3 launch.py` from the project root; config is in `launcher/openclaw_launcher.json`.

## License

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE) (AGPL-3.0). You may use, modify, and distribute it under the terms of that license; modified versions must remain under the AGPL. The full text is in the repository. Contributions and forks are welcome.

