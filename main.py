from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import logic  # Pastikan logic.py ada dalam satu folder

class ArmorMixerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")

        # Label Judul
        self.layout.add_widget(Label(text="🏹 Armor Mixer 🏹", font_size=24))

        # Tombol Menu
        self.layout.add_widget(Button(text="Tambah Armor", on_press=self.open_add_armor))
        self.layout.add_widget(Button(text="Tambah Earned Skill", on_press=self.open_add_skill))
        self.layout.add_widget(Button(text="Cari Armor Berdasarkan Skill", on_press=self.open_search_armor))
        self.layout.add_widget(Button(text="Keluar", on_press=self.stop))

        return self.layout

    def back_to_main(self, instance):
        """ Fungsi untuk kembali ke menu utama """
        self.layout.clear_widgets()  # Hapus semua widget
        self.__init__()  # Inisialisasi ulang aplikasi
        self.layout.add_widget(self.build())  # Bangun ulang tampilan utama

    def open_add_armor(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Tambah Armor"))

        self.name_input = TextInput(hint_text="Nama Armor")
        self.type_input = TextInput(hint_text="Jenis Armor (Head, Chest, Arms, Waist, Legs)")
        self.defense_input = TextInput(hint_text="Defense", input_filter="int")
        self.skill_input = TextInput(hint_text="Skill dan Poin (contoh: FireResist 5, DefenseBoost 3)")

        self.layout.add_widget(self.name_input)
        self.layout.add_widget(self.type_input)
        self.layout.add_widget(self.defense_input)
        self.layout.add_widget(self.skill_input)

        self.layout.add_widget(Button(text="Simpan Armor", on_press=self.save_armor))
        self.layout.add_widget(Button(text="Kembali", on_press=self.back_to_main))  # FIXED

    def save_armor(self, instance):
        name = self.name_input.text
        armor_type = self.type_input.text
        defense = int(self.defense_input.text) if self.defense_input.text.isdigit() else 0
        skills = {}

        for skill in self.skill_input.text.split(", "):
            try:
                skill_name, skill_points = skill.rsplit(" ", 1)
                skills[skill_name] = int(skill_points)
            except ValueError:
                pass

        logic.add_armor(name, armor_type, defense, skills)
        self.back_to_main(None)  # FIXED

    def open_add_skill(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Tambah Earned Skill"))

        self.skill_name_input = TextInput(hint_text="Nama Skill")
        self.threshold_input = TextInput(hint_text="Total Poin yang Dibutuhkan", input_filter="int")
        self.earned_name_input = TextInput(hint_text="Nama Earned Skill")

        self.layout.add_widget(self.skill_name_input)
        self.layout.add_widget(self.threshold_input)
        self.layout.add_widget(self.earned_name_input)

        self.layout.add_widget(Button(text="Simpan Skill", on_press=self.save_skill))
        self.layout.add_widget(Button(text="Kembali", on_press=self.back_to_main))  # FIXED

    def save_skill(self, instance):
        skill_name = self.skill_name_input.text
        threshold = int(self.threshold_input.text) if self.threshold_input.text.isdigit() else 0
        earned_name = self.earned_name_input.text

        logic.add_earned_skill(skill_name, threshold, earned_name)
        self.back_to_main(None)  # FIXED

    def open_search_armor(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Cari Armor Berdasarkan Skill"))

        self.search_input = TextInput(hint_text="Masukkan Nama Skill")
        self.talisman_input = TextInput(hint_text="Poin dari Talisman (0 jika tidak ada)", input_filter="int")

        self.layout.add_widget(self.search_input)
        self.layout.add_widget(self.talisman_input)

        self.layout.add_widget(Button(text="Cari", on_press=self.show_search_results))
        self.layout.add_widget(Button(text="Kembali", on_press=self.back_to_main))  # FIXED

    def show_search_results(self, instance):
        skill_name = self.search_input.text
        talisman_points = int(self.talisman_input.text) if self.talisman_input.text.isdigit() else 0

        results, earned_skill, total_points = logic.find_armor_by_skill(skill_name, talisman_points)

        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Hasil Pencarian", font_size=20))

        scroll_view = ScrollView()
        result_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=5)  # Tambahkan spacing

        result_layout.bind(minimum_height=result_layout.setter('height'))

        if results:
            for armor in results:
                result_layout.add_widget(Label(
                    text=f"{armor['name']} ({armor['type']}) - {armor['skill']}",
                    size_hint_y=None, height=40, padding=(10, 10)))  # Tambahkan padding

            result_layout.add_widget(Label(
                text=f"🔢 Total Skill Points: {total_points}",
                size_hint_y=None, height=40, padding=(10, 10)))

            if earned_skill:
                result_layout.add_widget(Label(
                    text=f"🏆 Earned Skill: {earned_skill}",
                    size_hint_y=None, height=40, padding=(10, 10)))
        else:
            result_layout.add_widget(Label(
                text="⚠️ Tidak ada armor dengan skill tersebut.",
                size_hint_y=None, height=40, padding=(10, 10)))

        scroll_view.add_widget(result_layout)
        self.layout.add_widget(scroll_view)
        self.layout.add_widget(Button(text="Kembali", on_press=self.back_to_main))  # FIXED

if __name__ == "__main__":
    ArmorMixerApp().run()