from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import os

# Импортируем экраны
from screens.main_screen import MainScreen
from screens.character_screen import CharacterScreen
from screens.logs_screen import LogsScreen

# Загружаем стили
kv_path = os.path.join(os.path.dirname(__file__), 'ui', 'styles.kv')
if os.path.exists(kv_path):
    Builder.load_file(kv_path)

class StatMasterApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CharacterScreen(name='character'))
        sm.add_widget(LogsScreen(name='logs'))
        return sm

if __name__ == '__main__':
    StatMasterApp().run()
