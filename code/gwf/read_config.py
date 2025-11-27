import yaml
from pathlib import Path

def load_config():
    """Load project configuration from config/config.yaml."""
    root = Path(__file__).resolve().parents[2]  # project root
    with open(root / "config" / "config.yaml") as f:
        return yaml.safe_load(f)