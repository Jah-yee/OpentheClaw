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

You can either download this project as a ZIP from GitHub or clone it:

```bash
git clone https://github.com/Jah-yee/OpentheClaw.git
cd OpentheClaw/opentheclaw
```

You can move the project folder anywhere; keep its internal structure unchanged.

**Flow:** (1) Configure once in the browser. (2) Use the one-click launcher (or `launch.py`) daily. No terminal or SSH typing needed.

### 1. Configure once

Open the config UI: double‑click `mac/Click-once-OpenClawConfig.command` (macOS), `linux/Click-OpenClawConfig-linux.sh` (Linux; choose “Run” if asked), or `windows\Click-OpenClawConfig-windows.bat` (Windows). Your browser opens the config page. Fill in:

- **Connection name** — any label (e.g. OpenClaw).
- **SSH address** — same `user@host` as in a terminal (e.g. `root@43.210.12.345`).
- **Web UI URL** — URL to open after the tunnel is up (e.g. `http://127.0.0.1:18789/`).

Use “Show advanced options” for ports and optional password. Then **Save** or **Save & start Web UI**.

### 2. Daily usage

- **Start Web UI:** Run `launch.py` from the project root, or use `mac/OpenClaw.command`, `linux/OpenClaw.sh`, or `windows/OpenClaw.bat`. The launcher starts the SSH tunnel from `launcher/openclaw_launcher.json`, opens the Web UI in your browser, and optionally warms the page (best effort). If the tunnel fails, the config UI opens so you can fix credentials.
- **Interactive SSH shell (macOS):** Double‑click `mac/OpenClawShell.command` for a normal SSH session with the same port forwarding.

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

Python 3 stdlib plus system `ssh` and a default browser. All logic is in `launcher/openclaw_launcher.py`; porting only requires changing how SSH or the browser is invoked.

## Releases

Stable versions are published as [GitHub Releases](https://github.com/Jah-yee/OpentheClaw/releases). Each release is tagged (e.g. `v1.0.0`) and includes a source archive so users can download a tarball or zip without cloning the repo.

- **Users:** Go to [Releases](https://github.com/Jah-yee/OpentheClaw/releases), pick a version, and download **Source code (zip)** or **Source code (tar.gz)**. Unpack and use the project as described in Getting started.
- **Maintainers:** To cut a new release, tag the commit and push. The release workflow (see `.github/workflows/release.yml`) creates the GitHub Release and attaches the source archive. Example:
  ```bash
  git tag -a v1.1.0 -m "Release v1.1.0"
  git push origin v1.1.0
  ```
  Write the release notes in the GitHub UI after the workflow runs, or use a changelog.

## Package

This project is **not** published to PyPI or any package registry. The distributable unit is the repository (or a release archive): the tree is self-contained and runnable as-is. No `pip install` step; just unpack (or clone) and run `launch.py` or the OS-specific launchers. That keeps setup minimal and avoids dependency management. If you need to ship it inside another system, bundle the repo or a release zip and ensure Python 3 and `ssh` are available on the target.

## Deployments

There is no server to deploy: the launcher runs on the user’s machine and connects out via SSH. “Deployment” here means getting the app onto a machine and running it.

- **End users:** Download a [release](https://github.com/Jah-yee/OpentheClaw/releases) (zip/tar.gz) or clone the repo, then follow [Getting started](#getting-started). No daemon or system service; run the launcher when needed.
- **Automation / scripts:** You can clone a specific tag or download a release archive and run `python3 launch.py` (or the appropriate `.command` / `.sh` / `.bat`) from the project root. Config is stored in `launcher/openclaw_launcher.json`; replicate or generate that file if you need a non-interactive setup.

## License

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE) (AGPL-3.0). You may use, modify, and distribute it under the terms of that license; modified versions must remain under the AGPL. The full text is in the repository. Contributions and forks are welcome.

