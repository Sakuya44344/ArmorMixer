import json
import os

ARMOR_FILE = "armors.json"
EARNED_SKILL_FILE = "earned_skills.json"

def load_armors():
    if not os.path.exists(ARMOR_FILE):
        return []
    with open(ARMOR_FILE, "r") as file:
        return json.load(file)

def save_armors(armors):
    with open(ARMOR_FILE, "w") as file:
        json.dump(armors, file, indent=4)

def load_earned_skills():
    if not os.path.exists(EARNED_SKILL_FILE):
        return {}
    with open(EARNED_SKILL_FILE, "r") as file:
        return json.load(file)

def save_earned_skills(earned_skills):
    with open(EARNED_SKILL_FILE, "w") as file:
        json.dump(earned_skills, file, indent=4)

def add_armor(name, armor_type, defense, skills):
    armors = load_armors()
    armors.append({
        "name": name,
        "type": armor_type,
        "defense": defense,
        "skills": skills
    })
    save_armors(armors)

def add_earned_skill(skill_name, threshold, earned_name):
    earned_skills = load_earned_skills()
    earned_skills[skill_name] = {"threshold": int(threshold), "earned_skill": earned_name}
    save_earned_skills(earned_skills)

def find_armor_by_skill(skill_name, talisman_points=0):
    armors = load_armors()
    earned_skills = load_earned_skills()
    
    armor_parts = {"Head": None, "Chest": None, "Arms": None, "Waist": None, "Legs": None}
    total_skill_points = talisman_points

    sorted_armors = sorted(
        [a for a in armors if skill_name in a["skills"]],
        key=lambda a: a["skills"][skill_name],
        reverse=True
    )

    for armor in sorted_armors:
        armor_type = armor["type"]
        if armor_parts[armor_type] is None:
            armor_parts[armor_type] = {
                "name": armor["name"],
                "type": armor_type,
                "skill": f"{skill_name} {armor['skills'][skill_name]}"
            }
            total_skill_points += armor["skills"][skill_name]

    results = [armor_parts[part] for part in armor_parts if armor_parts[part] is not None]
    results = results[:5]  

    earned_skill = None
    if skill_name in earned_skills:
        required_points = earned_skills[skill_name]["threshold"]
        if total_skill_points >= required_points:
            earned_skill = earned_skills[skill_name]["earned_skill"]

    return results, earned_skill, total_skill_points