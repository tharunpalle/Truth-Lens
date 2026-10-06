"""
Environment Setup Script.
Copies .env.example to .env if .env does not already exist.
"""

import shutil
from pathlib import Path


def setup_env():
    root_dir = Path(__file__).resolve().parent.parent
    example_env = root_dir / ".env.example"
    target_env = root_dir / ".env"

    if not example_env.exists():
        print("[!] Error: .env.example file not found at project root.")
        return False

    if target_env.exists():
        print("[*] .env already exists. Preserving existing configuration.")
        return True

    shutil.copyfile(example_env, target_env)
    print(f"[+] Successfully generated .env from template at: {target_env}")
    return True


if __name__ == "__main__":
    setup_env()
