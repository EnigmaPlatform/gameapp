import json
import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

class MainScreen(Screen):
    total_points = NumericProperty(100)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stats = {
            'Сила': 10,
            'Ловкость': 10,
            'Интеллект': 10,
            'Выносливость': 10,
            'Харизма': 10,
        }
        self.sound = SoundLoader.load('sounds/click.wav')
        self.load_stats()
        Clock.schedule_once(self.populate_ui, 0.1)
    
    def load_stats(self):
        if os.path.exists('stats.json'):
            with open('stats.json', 'r') as f:
                data = json.load(f)
                self.stats = data.get('stats', self.stats)
                self.total_points = data.get('points', 100)
    
    def save_stats(self):
        data = {
            'stats': self.stats,
            'points': self.total_points
        }
        with open('stats.json', 'w') as f:
            json.dump(data, f)
    
    def populate_ui(self, dt):
        self.ids.points_label.text = f'Очки: {self.total_points}'
        for stat in self.stats:
            if stat in self.ids:
                self.ids[stat].text = str(self.stats[stat])
    
    def change_stat(self, stat, delta):
        if self.sound:
            self.sound.play()
            
        if delta > 0 and self.total_points > 0:
            self.stats[stat] += delta
            self.total_points -= delta
        elif delta < 0 and self.stats[stat] > 0:
            self.stats[stat] += delta
            self.total_points -= delta
        
        # Анимация изменения чисел
        self.animate_number(stat)
        self.ids.points_label.text = f'Очки: {self.total_points}'
        
        # Автосохранение
        self.save_stats()
    
    def animate_number(self, stat):
        current = int(self.ids[stat].text)
        target = self.stats[stat]
        
        def update_number(dt):
            if current < target:
                current_val = int(self.ids[stat].text)
                if current_val < target:
                    self.ids[stat].text = str(current_val + 1)
                else:
                    return False
            elif current > target:
                current_val = int(self.ids[stat].text)
                if current_val > target:
                    self.ids[stat].text = str(current_val - 1)
                else:
                    return False
            return True
        
        for i in range(abs(current - target)):
            Clock.schedule_once(lambda dt, func=update_number: func(dt), i * 0.05)
    
    def reset_stats(self):
        if self.sound:
            self.sound.play()
        self.total_points = 100
        for stat in self.stats:
            self.stats[stat] = 10
        self.populate_ui(0)
        self.save_stats()
    
    def finish_distribution(self):
        if self.total_points == 0:
            if self.sound:
                self.sound.play()
            self.save_stats()
            self.manager.current = 'final'

class FinalScreen(Screen):
    def on_enter(self):
        # Закрытие приложения через 10 секунд
        Clock.schedule_once(self.close_app, 10)
    
    def close_app(self, dt):
        App.get_running_app().stop()

class StatMasterApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FinalScreen(name='final'))
        return sm

StatMasterApp().run()
