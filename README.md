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

Download the project as a ZIP from GitHub (e.g. from [Releases](https://github.com/Jah-yee/OpentheClaw/releases)) or clone it:

```bash
git clone https://github.com/Jah-yee/OpentheClaw.git
cd OpentheClaw
```

You can move the project folder anywhere (Desktop, Documents, etc.); keep its internal structure unchanged.

After you have the folder, do two things: (1) **configure once** in the browser, then (2) **use the launcher** whenever you want to open the Web UI. Below is the exact guidance for each platform and for the terminal.

---

### 1. Mac (macOS)

**Configure once (first time only)**

1. Open Finder and go to the project folder (the one that contains `launch.py`, `mac/`, `linux/`, `windows/`).
2. Open the `mac` folder.
3. Double‑click **`Click-once-OpenClawConfig.command`**. A Terminal window may flash; your default browser will open the config page.
4. On the config page, fill in:
   - **Connection name** — any label you like (e.g. OpenClaw or Staging server).
   - **SSH address** — the same `user@host` you use in a terminal (e.g. `root@43.210.12.345`).
   - **Web UI URL** — the URL that should open in the browser after the tunnel is ready (e.g. `http://127.0.0.1:18789/`).
5. Optionally click “Show advanced options (ports)” to set local port, remote port, remote host, or an SSH password.
6. Click **Save** to only save, or **Save & start Web UI** to save and start the tunnel and open the Web UI in the browser.

**Daily usage (start Web UI)**

1. Go to the project folder in Finder.
2. Open the `mac` folder.
3. Double‑click **`OpenClaw.command`**. The launcher starts the SSH tunnel, opens the Web UI in your browser, and (if the tunnel fails) opens the config page so you can fix credentials.

**Interactive SSH shell (optional)**

- Double‑click **`mac/OpenClawShell.command`** for a normal SSH session with the same port forwarding and config.

---

### 2. Linux

**Configure once (first time only)**

1. Open your file manager and go to the project folder (the one that contains `launch.py`, `mac/`, `linux/`, `windows/`).
2. Open the `linux` folder.
3. Double‑click **`Click-OpenClawConfig-linux.sh`** (or right‑click → Run / Execute). If your desktop asks “Run in terminal”, “Execute”, or “Display”, choose **Run** or **Execute** (not “Display”).
4. Your browser will open the config page. Fill in:
   - **Connection name** — any label (e.g. OpenClaw).
   - **SSH address** — same `user@host` as in a terminal (e.g. `root@43.210.12.345`).
   - **Web UI URL** — URL to open after the tunnel is ready (e.g. `http://127.0.0.1:18789/`).
5. Optionally use “Show advanced options (ports)” for ports and optional password.
6. Click **Save** or **Save & start Web UI**.

**Daily usage (start Web UI)**

1. Go to the project folder in your file manager.
2. Open the `linux` folder.
3. Double‑click **`OpenClaw.sh`** (or right‑click → Run / Execute). Choose **Run** or **Execute** if prompted. The launcher starts the tunnel and opens the Web UI; if the tunnel fails, the config page opens so you can fix credentials.

Alternatively, open a terminal, `cd` into the project folder, and run:  
`./linux/OpenClaw.sh`  
(or `bash linux/OpenClaw.sh` if needed).

---

### 3. Windows

**Configure once (first time only)**

1. Open File Explorer and go to the project folder (the one that contains `launch.py`, `mac/`, `linux/`, `windows/`).
2. Open the `windows` folder.
3. Double‑click **`Click-OpenClawConfig-windows.bat`**. A console window may appear briefly; your default browser will open the config page.
4. On the config page, fill in:
   - **Connection name** — any label (e.g. OpenClaw).
   - **SSH address** — same `user@host` you use in a terminal (e.g. `root@43.210.12.345`).
   - **Web UI URL** — URL to open after the tunnel is ready (e.g. `http://127.0.0.1:18789/`).
5. Optionally use “Show advanced options (ports)” for ports and optional password.
6. Click **Save** or **Save & start Web UI**.

**Daily usage (start Web UI)**

1. Go to the project folder in File Explorer.
2. Open the `windows` folder.
3. Double‑click **`OpenClaw.bat`**. The launcher starts the SSH tunnel and opens the Web UI in your browser. If the tunnel fails, you’ll see an error in the console and can run the config batch again to fix credentials.

If you see “Python not found” or similar, install Python 3 from [python.org](https://www.python.org/) and ensure “Add Python to PATH” was checked during installation.

---

### 4. Terminal (any platform)

If you prefer the command line for everything:

**Get the project (if you haven’t already)**

```bash
git clone https://github.com/Jah-yee/OpentheClaw.git
cd OpentheClaw
```

**Configure once (first time only)**

From the project root (the folder that contains `launch.py`):

```bash
python3 launcher/openclaw_launcher.py config
```

(or `python launcher/openclaw_launcher.py config` on Windows if that’s how Python is invoked). Your browser opens the config page. Fill in connection name, SSH address, and Web UI URL; use “Show advanced options” if needed, then **Save** or **Save & start Web UI**. The config is written to `launcher/openclaw_launcher.json`.

**Daily usage (start Web UI)**

From the project root:

```bash
python3 launch.py
```

(or `python launch.py` on Windows). This starts the SSH tunnel and opens the Web UI in your browser. If the tunnel fails, the launcher prints an error and opens the config UI so you can fix credentials.

**Interactive SSH shell (with port forwarding)**

From the project root:

```bash
python3 launcher/openclaw_launcher.py shell
```

(or `python launcher/openclaw_launcher.py shell` on Windows). This opens an interactive SSH session using the same config and port forwarding.

**Summary of terminal commands**

| Goal              | Command (from project root)                    |
|-------------------|------------------------------------------------|
| Open config UI    | `python3 launcher/openclaw_launcher.py config` |
| Start Web UI      | `python3 launch.py`                            |
| SSH shell         | `python3 launcher/openclaw_launcher.py shell`  |

On Windows, use `python` instead of `python3` if that’s what’s on your PATH.

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

