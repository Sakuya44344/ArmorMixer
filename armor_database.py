import json

ARMOR_FILE = "armor_data.json"

def load_armors():
    """Memuat data armor dari file JSON."""
    try:
        with open(ARMOR_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_armors(armors):
    """Menyimpan data armor ke file JSON."""
    with open(ARMOR_FILE, "w") as f:
        json.dump(armors, f, indent=4)