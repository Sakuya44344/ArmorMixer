import json

EARNED_SKILL_FILE = "earned_skills.json"

def load_earned_skills():
    """Memuat data earned skills dari file JSON."""
    try:
        with open(EARNED_SKILL_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_earned_skills(earned_skills):
    """Menyimpan data earned skills ke file JSON."""
    with open(EARNED_SKILL_FILE, "w") as f:
        json.dump(earned_skills, f, indent=4)
