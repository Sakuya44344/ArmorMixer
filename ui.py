import logic

def main_menu():
    while True:
        print("\n===== 🏹 Armor Manager 🏹 =====")
        print("1️⃣ Tambah Armor")
        print("2️⃣ Tambah Earned Skill")
        print("3️⃣ Cari Armor Berdasarkan Skill")
        print("4️⃣ Keluar")

        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == "1":
            add_armor_ui()
        elif choice == "2":
            add_earned_skill_ui()
        elif choice == "3":
            search_armor_by_skill()
        elif choice == "4":
            print("Keluar dari program.")
            break
        else:
            print("⚠️ Pilihan tidak valid, coba lagi!")

def add_armor_ui():
    print("\n=== Tambah Armor Baru ===")
    name = input("Nama Armor: ")
    armor_type = input("Jenis Armor (Head, Chest, Arms, Waist, Legs): ")
    defense = int(input("Defense: "))

    skills = {}
    for i in range(8):
        skill_name = input(f"Skill {i+1} (kosongkan jika tidak ada): ")
        if not skill_name:
            break
        skill_points = int(input(f"  Poin {skill_name}: "))
        skills[skill_name] = skill_points

    logic.add_armor(name, armor_type, defense, skills)
    print(f"✅ Armor '{name}' berhasil ditambahkan!")

def add_earned_skill_ui():
    print("\n=== Tambah Earned Skill ===")
    skill_name = input("Nama Skill: ")
    threshold = int(input("Total Poin yang Dibutuhkan: "))
    earned_name = input("Nama Earned Skill: ")

    logic.add_earned_skill(skill_name, threshold, earned_name)
    print(f"✅ Earned Skill '{earned_name}' untuk skill '{skill_name}' berhasil ditambahkan!")

def search_armor_by_skill():
    skill_name = input("Masukkan nama skill: ")
    talisman_points = int(input("Masukkan poin dari talisman (0 jika tidak ada): "))

    results, earned_skill, total_points = logic.find_armor_by_skill(skill_name, talisman_points)

    if not results:
        print("⚠️ Tidak ada armor dengan skill tersebut.")
        return

    print("\n📜 Hasil Pencarian (Top 5 Armor):")
    for armor in results:
        print(f"{armor['name']} ({armor['type']}), {armor['skill']}")

    print(f"\n🔢 Total Skill Points (termasuk talisman): {total_points}")
    if earned_skill:
        print(f"🏆 Earned Skill: {earned_skill}")

if __name__ == "__main__":
    main_menu()