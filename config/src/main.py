Python

import yaml
from rich import print

from connection import connect_device

def load_devices():
      with open("config/devices.yaml","r",encoding="utf-8") as f:
        return yaml.safe_load(f)["devices"]

def main():
    devices = load_devices()

    for device in devices:
        print(f"\n[bold cyan]Connection to {device['name']}...[/bold cyan]")
        try:
          conn = connect_device(devices)
          hostname = conn.sent_command("display version")
          print("[green]Connection successful[/green]")
          print(hostname[:500])
          conn.disconnect()
        except Exception as e:
          print(f"[red]Connection failed:{e}[/red]")
if __name__ == "__main__":
  main()
