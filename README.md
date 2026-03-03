<p align="center">
  <svg width="220" height="56" viewBox="0 0 220 56" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
    <title id="title">OpenTheClaw</title>
    <rect x="0" y="8" width="220" height="40" rx="20" fill="#111827"/>
    <text x="50%" y="52%" text-anchor="middle"
          font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
          font-size="20" fill="#e5e7eb">
      OpenTheClaw
    </text>
  </svg>
</p>

<p align="center">
  One‑click SSH tunnel + Web UI starter.
</p>

<p align="center">
  <a href="https://github.com/your-name/openclaw-ssh-launcher">
    <img src="https://img.shields.io/github/stars/your-name/openclaw-ssh-launcher?style=social" alt="GitHub stars" />
  </a>
  <a href="https://github.com/your-name/openclaw-ssh-launcher/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/your-name/openclaw-ssh-launcher/ci.yml?label=CI&logo=github" alt="Build status" />
  </a>
  <img src="https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-111827" alt="Supported platforms" />
</p>

---

# OpenClaw SSH Launcher

A small, minimal launcher that turns “SSH port forwarding + open a Web UI” into a **one‑click / double‑click** experience, without asking users to touch the terminal.

Typical use cases (not limited to OpenClaw):

- You have a remote server whose Web UI is only reachable from inside that server (e.g. `http://127.0.0.1:18789/`).
- You can SSH into that server.
- You want: configure once, then just double‑click an icon to bring up the SSH tunnel and browser every day.

The core is a tiny Python HTTP server that exposes a browser‑based config page and then shells out to the system `ssh` client.

## Layout

```text
opentheclaw/
  mac/
    Click-OpenClaw.command           # macOS launcher (Web UI + SSH tunnel)
    Click-OpenClawShell.command      # macOS launcher for interactive SSH shell
    Click-OpenClawConfig.command     # macOS launcher for config UI

  linux/
    Click-OpenClaw-linux.sh          # Linux launcher (Web UI + SSH tunnel)
    Click-OpenClawConfig-linux.sh    # Linux launcher for config UI

  windows/
    Click-OpenClaw-windows.bat       # Windows launcher (Web UI + SSH tunnel)
    Click-OpenClawConfig-windows.bat # Windows launcher for config UI

  launcher/
    openclaw_launcher.py   # core: config UI + SSH/Web UI orchestration
    openclaw_launcher.json # JSON config, written by the web UI

  README.md
  LICENSE
  .gitignore
```

Most users only need to see and double‑click the launchers at the top level.

## Requirements

- Python 3
- An `ssh` client available on `PATH`
  - macOS: built‑in OpenSSH works fine
  - Linux: any standard OpenSSH client
  - Windows: OpenSSH (Windows 10+), Git for Windows SSH, or another compatible `ssh`

## Getting started

```bash
git clone https://github.com/your-name/openclaw-ssh-launcher.git
cd openclaw-ssh-launcher/opentheclaw
```

You can keep the `opentheclaw` folder anywhere (desktop, home directory, etc.) as long as the internal structure stays the same.

### 1. Configure via the browser

On macOS:

- Double‑click `mac/Click-OpenClawConfig.command`.

On Linux / Windows:

- From a terminal, run:

  ```bash
  # Linux
  cd opentheclaw/linux
  ./Click-OpenClawConfig-linux.sh

  # Windows (in Command Prompt or PowerShell)
  cd opentheclaw\windows
  .\Click-OpenClawConfig-windows.bat
  ```

Your browser will open a minimal panel where you only need to fill a few fields:

- **Connection name** – any label you like, e.g. `OpenClaw` or `Staging server`.
- **SSH address** – exactly what you would type in a terminal, e.g. `root@43.159.36.166`.
- **Web UI URL** – for example `http://127.0.0.1:18789/` (this is the common OpenClaw case).

Advanced options (ports, remote host, password) are hidden behind a “Show advanced options” toggle and usually don’t need to be changed.

You can:

- Click **Save** to just update the JSON config.
- Click **Save & start Web UI** to save and immediately bring up the SSH tunnel and open the Web UI in your default browser.

### 2. Daily usage

Once configured, you usually don’t need the config UI anymore.

- **Open Web UI (most common)**  
  - macOS: double‑click `mac/Click-OpenClaw.command`.
  - Linux: run `linux/Click-OpenClaw-linux.sh`.
  - Windows: double‑click `windows/Click-OpenClaw-windows.bat`.

  The launcher will:

  - Start an SSH tunnel according to `launcher/openclaw_launcher.json`.
  - Open the configured Web UI URL in your default browser.
  - Optionally “warm up” the page with a silent HTTP request so the first paint feels faster (best effort).

- **Open an interactive SSH shell (macOS)**  
  - Double‑click `mac/Click-OpenClawShell.command`.
  - Uses the same config, but gives you a normal SSH session with port forwarding.

## Config file (short overview)

Config lives in:

- `launcher/openclaw_launcher.json`

A typical file looks like this:

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

In most setups you only need to care about:

- `user` / `host`: corresponds to the `user@host` you use with SSH.
- `web_url`: the Web UI URL to open in your browser.
- `local_port` / `remote_port` / `remote_host`: defaults usually work out of the box.

It is recommended to edit this through the web UI rather than manually changing the JSON.

## Security notes

- Prefer **SSH keys** over passwords. The launcher works fine with key‑based auth.
- If you choose to use the `password` field, remember it is stored in plain text in the local JSON file. Only do this on machines you fully trust.
- Intended for personal/dev/test environments. Avoid putting production credentials in long‑lived configs.

## Dependencies

This project only uses the Python standard library and basic system tools:

- Python 3 (`http.server`, `json`, `subprocess`, etc.)
- `ssh` client
- A default browser (opened via Python’s `webbrowser` module)

To port it to other environments, you mainly need to adjust how SSH is invoked or how the browser is opened; all application logic is in `launcher/openclaw_launcher.py`.

## License

MIT License. Adjust the copyright line to your own name or organization.


