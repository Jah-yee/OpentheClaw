<p align="center">
  <img src="https://raw.githubusercontent.com/Jah-yee/OpentheClaw/main/logo.svg" width="520" height="289" alt="OpentheClaw logo" />
</p>

<p align="center">
<a href="https://www.producthunt.com/products/opentheclaw?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-opentheclaw" target="_blank" rel="noopener noreferrer"><img alt="OpentheClaw - One-click launcher for OpenClaw Web UI over SSH | Product Hunt" width="250" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1089439&amp;theme=light&amp;t=1772620723494"></a>

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
  logo.svg              # project logo (used at top of this README)
  mac/
    Click-default-OpenClaw.command           # macOS launcher (Web UI + SSH tunnel)
    OpenClawShell.command      # macOS launcher for interactive SSH shell
    Click-once-OpenClawConfig.command     # macOS launcher for config UI

  linux/
    OpenClaw-linux.sh                # Linux launcher (Web UI + SSH tunnel)
    Click-OpenClawConfig-linux.sh    # Linux launcher for config UI

  windows/
    OpenClaw-windows.bat             # Windows launcher (Web UI + SSH tunnel)
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

You can either download this project as a ZIP from GitHub or clone it:

```bash
git clone https://github.com/Jah-yee/OpentheClaw.git
cd OpentheClaw/opentheclaw
```

You can move the `opentheclaw` folder wherever you like (Desktop, home directory, etc.) as long as you keep its internal structure the same.

Think of the flow in three steps:

1. **Configure once in your browser** (tell it how you SSH and what Web UI to open).
2. **Double‑click the right launcher for your OS**.
3. **Use that launcher every day** instead of typing SSH commands by hand.

### 1. Configure via the browser

- **On macOS**  
  > Double‑click `mac/Click-once-OpenClawConfig.command`.

- **On Linux**  
  > In your file manager, double‑click `linux/Click-OpenClawConfig-linux.sh`.  
  > If your desktop environment asks whether to "Run in terminal" or "Display", choose **Run** / **Execute**.

- **On Windows**  
  > In Explorer, double‑click `windows\Click-OpenClawConfig-windows.bat`.  
  > A console window may briefly appear while the browser opens.

Your browser will open a simple configuration page. You only need to fill three things:

- **Connection name** – any label you like, for example `OpenClaw` or `Staging server`.
- **SSH address** – the same `user@host` you normally type in a terminal, for example `root@43.210.12.345`.
- **Web UI URL** – the URL you want in your browser after the SSH tunnel is ready, e.g. `http://127.0.0.1:18789/`.

If you click "Show advanced options", you can also adjust ports, remote host and an optional password, but the defaults are fine for most setups.

At the bottom of the page you can:

- Click **Save** to just store the configuration for later.
- Click **Save & start Web UI** to save and immediately start the SSH tunnel and open the Web UI in your browser.

### 2. Daily usage

Once configured, you usually don't need to change the settings very often.

- **Open Web UI (most common)**  
  - macOS: double‑click `mac/Click-default-OpenClaw.command`.
  - Linux: run `linux/OpenClaw-linux.sh`.
  - Windows: run `windows/OpenClaw-windows.bat`.

  The launcher will:

  - Start an SSH tunnel according to `launcher/openclaw_launcher.json`.
  - Open the configured Web UI URL in your default browser.
  - Optionally "warm up" the page with a silent HTTP request so the first paint feels faster (best effort).

- **Open an interactive SSH shell (macOS)**  
  - Double‑click `mac/OpenClawShell.command`.
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
- A default browser (opened via Python's `webbrowser` module)

To port it to other environments, you mainly need to adjust how SSH is invoked or how the browser is opened; all application logic is in `launcher/openclaw_launcher.py`.

## License

Business Source License 1.1 (BSL 1.1). See [LICENSE](LICENSE). © 2026 Jah-yee.

