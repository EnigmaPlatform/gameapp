from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.config import Config

# Неоновые стили
Config.set('graphics', 'background_color', '000000')
Window.clearcolor = (0, 0, 0, 1)

class NeonButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 1)
        self.color = (0.2, 0.6, 1, 1)  # Неоновый синий
        self.font_size = '18sp'
        self.bold = True
        self.size_hint = (1, None)
        self.height = 50
        
        with self.canvas.before:
            Color(0.2, 0.6, 1, 0.3)  # Неоновое свечение
            RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
            
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.2, 0.6, 1, 0.3)
            RoundedRectangle(size=self.size, pos=self.pos, radius=[10])

class StatDisplay(BoxLayout):
    def __init__(self, stat_name, stat_value, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 40
        
        self.stat_name = Label(
            text=stat_name,
            color=(0.2, 0.8, 1, 1),
            font_size='16sp',
            size_hint=(0.6, 1)
        )
        
        self.stat_value = Label(
            text=str(stat_value),
            color=(0.2, 0.8, 1, 1),
            font_size='16sp',
            size_hint=(0.2, 1)
        )
        
        self.upgrade_btn = NeonButton(
            text="+",
            size_hint=(0.2, 1),
            on_press=self.upgrade_stat
        )
        
        self.add_widget(self.stat_name)
        self.add_widget(self.stat_value)
        self.add_widget(self.upgrade_btn)
    
    def upgrade_stat(self, instance):
        # Здесь будет логика улучшения характеристики
        pass

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
            text="Уровень: 1",
            color=(0.2, 0.8, 1, 1),
            font_size='18sp',
            size_hint=(1, None),
            height=40
        )
        
        self.exp_bar = ProgressBar(
            max=100,
            value=0,
            size_hint=(1, None),
            height=30
        )
        
        # Очки талантов
        self.talent_label = Label(
            text="Очки талантов: 10",
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

class GamificationApp(App):
    def build(self):
        return MainUI()

if __name__ == '__main__':
    GamificationApp().run()
