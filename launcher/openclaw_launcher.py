#!/usr/bin/env python3
import http.server
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import webbrowser
import html


CONFIG_PATH = os.path.join(os.path.dirname(__file__), "openclaw_launcher.json")

DEFAULT_CONFIG = {
    "name": "OpenClaw",
    "host": "43.159.36.166",
    "user": "root",
    "local_port": 18789,
    "remote_host": "127.0.0.1",
    "remote_port": 18789,
    "web_url": "http://127.0.0.1:18789/",
    "password": "",
}


def load_config():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    cfg = DEFAULT_CONFIG.copy()
    cfg.update(data)
    return cfg


def save_config(cfg):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)


def build_ssh_command(cfg, for_webui: bool):
    """
    Build the SSH command for either the web UI tunnel or an interactive shell.

    If a password is provided in the config and sshpass is available, sshpass
    will be used to provide the password automatically.
    """

    base_cmd = ["ssh"]

    # Avoid interactive host key prompts for this helper.
    base_cmd += ["-o", "StrictHostKeyChecking=no"]

    if for_webui:
        # Background tunnel only, no interactive shell.
        base_cmd += ["-fN"]

    # Port forwarding
    base_cmd += [
        "-L",
        f"{cfg['local_port']}:{cfg['remote_host']}:{cfg['remote_port']}",
        f"{cfg['user']}@{cfg['host']}",
    ]

    password = (cfg.get("password") or "").strip()
    if password and shutil.which("sshpass"):
        # Use sshpass to provide the password non‑interactively when available.
        return ["sshpass", "-p", password] + base_cmd

    return base_cmd


class ConfigHandler(http.server.BaseHTTPRequestHandler):
    def _read_config(self):
        cfg = load_config()
        if cfg is None:
            cfg = DEFAULT_CONFIG.copy()
        return cfg

    def _render_form(self, cfg, message=""):
        """Render the configuration form as HTML (kept intentionally minimal)."""

        def esc(val):
            return html.escape(str(val if val is not None else ""))

        user = cfg.get("user") or ""
        host = cfg.get("host") or ""
        if user and host:
            ssh_address = f"{user}@{host}"
        else:
            ssh_address = host or user

        body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>OpenClaw connection</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #f3f4f6;
      color: #111827;
    }}
    .card {{
      width: 100%;
      max-width: 460px;
      background: #ffffff;
      border-radius: 16px;
      padding: 22px 22px 18px;
      box-shadow: 0 16px 32px rgba(15, 23, 42, 0.08);
      border: 1px solid #e5e7eb;
    }}
    .header-title {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
      font-size: 18px;
      font-weight: 600;
    }}
    .header-subtitle {{
      font-size: 13px;
      color: #6b7280;
      margin-bottom: 12px;
    }}
    .logo-word {{
      display: inline-block;
      padding: 2px 10px;
      border-radius: 999px;
      background: #0b1120;
      color: #e5e7eb;
      font-size: 11px;
      font-weight: 500;
    }}
    .field {{
      margin-top: 12px;
    }}
    .field label {{
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: #111827;
      margin-bottom: 4px;
    }}
    .field input[type="text"],
    .field input[type="number"],
    .field input[type="password"] {{
      width: 100%;
      padding: 7px 10px;
      border-radius: 10px;
      border: 1px solid #d1d5db;
      background: #ffffff;
      color: #111827;
      font-size: 13px;
      outline: none;
      transition: border-color 0.12s ease, box-shadow 0.12s ease;
    }}
    .field input::placeholder {{
      color: #9ca3af;
    }}
    .field input:focus {{
      border-color: #2563eb;
      box-shadow: 0 0 0 1px rgba(37, 99, 235, 0.4);
    }}
    .hint {{
      margin-top: 4px;
      font-size: 11px;
      color: #6b7280;
    }}
    .hint code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      font-size: 11px;
    }}
    .message {{
      margin-top: 6px;
      font-size: 12px;
      color: #2563eb;
    }}
    .advanced-toggle {{
      margin-top: 14px;
      font-size: 11px;
      color: #6b7280;
      cursor: pointer;
      user-select: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .advanced {{
      display: none;
      margin-top: 8px;
      padding-top: 10px;
      border-top: 1px solid #e5e7eb;
    }}
    .advanced.visible {{
      display: block;
    }}
    .form-row {{
      display: flex;
      gap: 10px;
    }}
    .actions {{
      display: flex;
      justify-content: flex-end;
      gap: 10px;
      margin-top: 18px;
    }}
    .btn {{
      border-radius: 999px;
      padding: 7px 14px;
      font-size: 13px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }}
    .btn-secondary {{
      background: #ffffff;
      color: #111827;
      border: 1px solid #d1d5db;
    }}
    .btn-primary {{
      background: #2563eb;
      color: #ffffff;
      border: 1px solid #2563eb;
    }}
    .btn-primary:hover {{
      filter: brightness(1.05);
    }}
    .btn-secondary:hover {{
      background: #f9fafb;
    }}
    .field-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 4px;
    }}
    .link-button {{
      border: none;
      background: none;
      padding: 0;
      margin: 0;
      font-size: 11px;
      color: #2563eb;
      cursor: pointer;
    }}
    .link-button:hover {{
      text-decoration: underline;
    }}
    small {{
      font-size: 11px;
    }}
    .footer {{
      margin-top: 16px;
      font-size: 11px;
      color: #9ca3af;
      text-align: right;
    }}
  </style>
</head>
<body>
  <div class="card">
    {"<div class='message'>" + esc(message) + "</div>" if message else ""}
    <form method="POST">
      <div class="field">
        <label>Connection name</label>
        <input
          type="text"
          name="name"
          placeholder="e.g. OpenClaw / Staging server"
          value="{esc(cfg.get("name", ""))}"
        />
      </div>

      <div class="field">
        <label>SSH address</label>
        <input
          type="text"
          name="ssh_address"
          placeholder="e.g. root@43.210.12.345"
          value="{esc(ssh_address)}"
        />
        <div class="hint">
          The same <code>user@host</code> you would type in a terminal,
          for example <code>root@43.210.12.345</code>.
        </div>
      </div>

      <div class="field">
        <label>Web UI URL</label>
        <input
          type="text"
          name="web_url"
          placeholder="e.g. http://127.0.0.1:18789/"
          value="{esc(cfg.get("web_url", ""))}"
        />
        <div class="hint">
          This is the URL that will be opened in your browser after the tunnel is ready.
          For OpenClaw it is usually <code>http://127.0.0.1:18789/</code>.
        </div>
      </div>

      <div class="field">
        <div class="field-header">
          <label>SSH password (optional)</label>
          <button type="button" id="password-toggle" class="link-button" onclick="togglePasswordVisibility()">
            Show
          </button>
        </div>
        <input
          type="password"
          id="password-input"
          name="password"
          placeholder="Using SSH keys is recommended; password is only for special cases"
          value="{esc(cfg.get("password", ""))}"
        />
        <div class="hint">
          The password is stored only in a local JSON file on this machine. Prefer SSH keys on shared or untrusted devices.
        </div>
      </div>

      <div class="advanced-toggle" onclick="toggleAdvanced()" id="advanced-toggle">
        <span>▸</span><small>Show advanced options (ports)</small>
      </div>

      <div class="advanced" id="advanced">
        <div class="form-row">
          <div class="field" style="flex: 1;">
            <label>Local port</label>
            <input
              type="number"
              name="local_port"
              placeholder="18789"
              value="{esc(cfg.get("local_port", 18789))}"
            />
            <div class="hint">Port exposed on your machine. Default is usually fine.</div>
          </div>
          <div class="field" style="flex: 1;">
            <label>Remote port</label>
            <input
              type="number"
              name="remote_port"
              placeholder="18789"
              value="{esc(cfg.get("remote_port", 18789))}"
            />
            <div class="hint">Port where the Web UI is listening on the server.</div>
          </div>
        </div>

        <div class="field">
          <label>Remote host</label>
          <input
            type="text"
            name="remote_host"
            placeholder="typically 127.0.0.1"
            value="{esc(cfg.get("remote_host", "127.0.0.1"))}"
          />
          <div class="hint">
            Host where the Web UI listens on the server, usually <code>127.0.0.1</code>.
          </div>
        </div>
      </div>

      <div class="actions">
        <button class="btn btn-secondary" type="submit" name="action" value="save">
          Save
        </button>
        <button class="btn btn-primary" type="submit" name="action" value="save_and_connect">
          Save &amp; start Web UI
        </button>
      </div>
    </form>
    <div class="footer">
      Build with ❤ and &lt;/&gt; by
      <a href="https://github.com/Jah-yee" target="_blank" rel="noreferrer">RoomWithOutRoof</a>.
    </div>
  </div>
  <script>
    function toggleAdvanced() {{
      const adv = document.getElementById('advanced');
      const toggle = document.getElementById('advanced-toggle');
      if (!adv || !toggle) return;
      const visible = adv.classList.toggle('visible');
      toggle.querySelector('span').textContent = visible ? '▾' : '▸';
      toggle.querySelector('small').textContent = visible
        ? 'Hide advanced options'
        : 'Show advanced options (ports)';
    }}

    function togglePasswordVisibility() {{
      const input = document.getElementById('password-input');
      const toggle = document.getElementById('password-toggle');
      if (!input || !toggle) return;
      const isHidden = input.type === 'password';
      input.type = isHidden ? 'text' : 'password';
      toggle.textContent = isHidden ? 'Hide' : 'Show';
    }}
  </script>
</body>
</html>
"""
        return body.encode("utf-8")

    def do_GET(self):
        cfg = self._read_config()
        body = self._render_form(cfg)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length).decode("utf-8")
        params = urllib.parse.parse_qs(raw)

        action = params.get("action", ["save"])[0]

        base_cfg = load_config() or DEFAULT_CONFIG.copy()
        cfg = base_cfg.copy()

        # Parse SSH address, e.g. root@43.159.36.166
        ssh_address = params.get("ssh_address", [""])[0].strip()
        if ssh_address:
            if "@" in ssh_address:
                user_part, host_part = ssh_address.split("@", 1)
                user_part = user_part.strip()
                host_part = host_part.strip()
                if user_part:
                    cfg["user"] = user_part
                if host_part:
                    cfg["host"] = host_part
            else:
                cfg["host"] = ssh_address

        # Basic string fields
        for key in ("name", "web_url", "password"):
            if key in DEFAULT_CONFIG:
                val = params.get(key, [str(cfg.get(key, DEFAULT_CONFIG[key]))])[0].strip()
                if val:
                    cfg[key] = val

        # Port number fields
        for key in ("local_port", "remote_port"):
            if key in DEFAULT_CONFIG:
                raw_val = params.get(key, [str(cfg.get(key, DEFAULT_CONFIG[key]))])[0].strip()
                if raw_val:
                    try:
                        cfg[key] = int(raw_val)
                    except ValueError:
                        pass

        # Remote host field
        if "remote_host" in DEFAULT_CONFIG:
            val = params.get("remote_host", [str(cfg.get("remote_host", DEFAULT_CONFIG["remote_host"]))])[0].strip()
            if val:
                cfg["remote_host"] = val

        save_config(cfg)
        if action == "save_and_connect":
            ok, error_msg = run_webui(cfg)
            if ok:
                msg = "Configuration saved. Attempting to start the Web UI..."
            else:
                msg = (
                    "Configuration saved, but starting the Web UI failed. "
                    f"{error_msg}"
                )
        else:
            msg = "Configuration saved."

        body = self._render_form(cfg, message=msg)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Silence HTTP access logs to keep the terminal output clean.
        pass


def start_config_server():
    port = 18888
    url = f"http://127.0.0.1:{port}/"

    # If the config UI is already running, do not start another instance
    try:
        with urllib.request.urlopen(url, timeout=1):
            print(f"Config UI already running at {url}")
            return
    except Exception:
        pass

    server = http.server.HTTPServer(("127.0.0.1", port), ConfigHandler)
    print(f"Opening config UI in your browser: {url}")
    try:
        webbrowser.open(url)
    except Exception:
        pass

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


def ensure_config_or_open_ui():
    cfg = load_config()
    if cfg is None:
        print("No valid config found. Opening the local web UI to set it up.")
        start_config_server()
        return None
    return cfg


def run_shell(cfg):
    cmd = build_ssh_command(cfg, for_webui=False)
    subprocess.call(cmd)


def run_webui(cfg):
    """
    Start an SSH tunnel for the configured ports and open the Web UI URL.

    Returns:
        (ok: bool, error_message: Optional[str])
    """

    ssh_cmd = build_ssh_command(cfg, for_webui=True)
    result = subprocess.run(
        ssh_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False
    )

    if result.returncode != 0:
        error_msg = (
            f"SSH tunnel failed with exit code {result.returncode}. "
            "Please check your SSH address, credentials, or local port."
        )
        print(error_msg, file=sys.stderr)
        return False, error_msg

    web_url = cfg.get("web_url") or f"http://127.0.0.1:{cfg['local_port']}/"

    # Open in the default browser in a cross‑platform way
    try:
        webbrowser.open(web_url)
    except Exception:
        # Browser could not be opened automatically; this is non‑fatal.
        pass

    # Best‑effort warm‑up so that the first paint feels faster
    time.sleep(1)
    try:
        subprocess.run(
            ["curl", "-s", web_url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except FileNotFoundError:
        # If curl is not available on this machine, just skip the warm‑up
        pass

    return True, None


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "webui"

    if mode == "config":
        start_config_server()
        return

    if mode not in ("shell", "webui"):
        print("Usage:")
        print("  python3 openclaw_launcher.py shell   # open interactive SSH session with port forwarding")
        print("  python3 openclaw_launcher.py webui   # start SSH tunnel and open Web UI (default)")
        print("  python3 openclaw_launcher.py config  # open the browser-based config UI")
        return

    cfg = ensure_config_or_open_ui()
    if cfg is None:
        return

    if mode == "shell":
        run_shell(cfg)
    else:
        ok, _ = run_webui(cfg)
        if not ok:
            sys.exit(1)


if __name__ == "__main__":
    main()

