from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.config import Config
from kivy.properties import ObjectProperty

Config.set('graphics', 'background_color', '000000')
Window.clearcolor = (0, 0, 0, 1)

class NeonButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 1)
        self.color = (0.2, 0.6, 1, 1)
        self.font_size = '18sp'
        self.bold = True
        self.size_hint = (1, None)
        self.height = 50
        
        with self.canvas.before:
            Color(0.2, 0.6, 1, 0.3)
            RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
            
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.2, 0.6, 1, 0.3)
            RoundedRectangle(size=self.size, pos=self.pos, radius=[10])

class StatDisplay(BoxLayout):
    def __init__(self, stat_name, stat_value, on_upgrade, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 40
        self.stat_name = stat_name
        self.on_upgrade_callback = on_upgrade
        
        self.stat_label = Label(
            text=f"{stat_name}: {stat_value}",
            color=(0.2, 0.8, 1, 1),
            font_size='16sp',
            size_hint=(0.8, 1)
        )
        
        self.upgrade_btn = NeonButton(
            text="+",
            size_hint=(0.2, 1),
            on_press=self.upgrade_stat
        )
        
        self.add_widget(self.stat_label)
        self.add_widget(self.upgrade_btn)
    
    def upgrade_stat(self, instance):
        if self.on_upgrade_callback(self.stat_name):
            self.update_display()
    
    def update_display(self):
        # Это будет обновлено после реализации обратных вызовов
        pass

class MainUI(BoxLayout):
    game_manager = ObjectProperty(None)
    
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15
        
        # Заголовок
        self.title = Label(
            text="ГЕЙМИФИКАЦИЯ ПОВСЕДНЕВНОСТИ",
            color=(0, 0.8, 1, 1),
            font_size='24sp',
            bold=True,
            size_hint=(1, None),
            height=60
        )
        
        # Уровень и опыт
        self.level_label = Label(
            text=f"Уровень: {self.game_manager.get_level_info()['level']}",
            color=(0.2, 0.8, 1, 1),
            font_size='18sp',
            size_hint=(1, None),
            height=40
        )
        
        level_info = self.game_manager.get_level_info()
        self.exp_bar = ProgressBar(
            max=level_info['next_level'],
            value=level_info['experience'],
            size_hint=(1, None),
            height=30
        )
        
        # Очки талантов
        self.talent_label = Label(
            text=f"Очки талантов: {self.game_manager.get_talent_points()}",
            color=(0.2, 0.8, 1, 1),
            font_size='18sp',
            size_hint=(1, None),
            height=40
        )
        
        # Характеристики
        self.stats_container = BoxLayout(
            orientation='vertical',
            spacing=10,
            size_hint=(1, 0.7)
        )
        
        self.add_widget(self.title)
        self.add_widget(self.level_label)
        self.add_widget(self.exp_bar)
        self.add_widget(self.talent_label)
        self.add_widget(self.stats_container)
        
        self.update_stats_display()
    
    def update_stats_display(self):
        self.stats_container.clear_widgets()
        stats = self.game_manager.get_character_stats()
        
        for stat_name, stat_value in stats.items():
            stat_display = StatDisplay(
                stat_name=stat_name,
                stat_value=stat_value,
                on_upgrade=self.game_manager.upgrade_stat,
                size_hint=(1, None),
                height=40
            )
            self.stats_container.add_widget(stat_display)

class GamificationApp(App):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager
    
    def build(self):
        return MainUI(game_manager=self.game_manager)

if __name__ == '__main__':
    from modules.character import Character
    from modules.leveling import LevelSystem
    from main import GameManager  # Добавлен импорт GameManager
    game_manager = GameManager()  # Используем GameManager вместо отдельных классов
    GamificationApp(game_manager=game_manager).run()
