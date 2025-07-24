from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.animation import Animation

class MainScreen(Screen):
    total_points = NumericProperty(10)  # Теперь 10 очков
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stats = {
            'Сила': 2,  # Начальные значения характеристик
            'Ловкость': 2,
            'Интеллект': 2,
            'Выносливость': 2,
            'Харизма': 2,
        }
        Clock.schedule_once(self.create_ui, 0.1)
    
    def create_ui(self, dt):
        # Фон для главного экрана
        with self.canvas.before:
            Color(0.06, 0.1, 0.18, 1)  # Темно-синий (#0F1A2D)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        # Основной layout
        main_layout = BoxLayout(orientation='vertical', padding=25, spacing=20)
        
        # Заголовок с очками
        self.points_label = Label(
            text=f'Очки: {self.total_points}',
            font_size='26sp',
            color=(0, 0.9, 1, 1),  # Неоново-голубой
            size_hint_y=None,
            height=60,
            bold=True
        )
        main_layout.add_widget(self.points_label)
        
        # Создаем строки характеристик
        self.stat_labels = {}
        
        stat_colors = {
            'Сила': (0.9, 0.3, 0.3, 1),        # Красный
            'Ловкость': (0.3, 0.9, 0.3, 1),    # Зеленый
            'Интеллект': (0.3, 0.6, 0.9, 1),   # Голубой
            'Выносливость': (0.9, 0.7, 0.3, 1), # Желтый
            'Харизма': (0.8, 0.3, 0.8, 1)      # Фиолетовый
        }
        
        for stat_name in self.stats:
            # Фон для строки характеристики
            stat_container = BoxLayout(size_hint_y=None, height=60)
            with stat_container.canvas.before:
                Color(0.11, 0.12, 0.15, 0.7)  # Темно-серый с прозрачностью
                RoundedRectangle(pos=stat_container.pos, size=stat_container.size, radius=[10])
            stat_container.bind(size=self._update_stat_container, pos=self._update_stat_container)
            
            stat_layout = BoxLayout(size_hint_y=None, height=60, spacing=15)
            
            # Название характеристики
            stat_label = Label(
                text=stat_name,
                font_size='22sp',
                color=stat_colors[stat_name],
                size_hint_x=0.4,
                bold=True
            )
            stat_layout.add_widget(stat_label)
            
            # Кнопка минус
            minus_btn = Button(
                text='-',
                size_hint_x=None,
                width=60,
                background_color=(0.2, 0.6, 0.8, 1),
                color=(1, 1, 1, 1),
                font_size='24sp',
                bold=True
            )
            minus_btn.bind(on_press=lambda btn, s=stat_name: self.change_stat(s, -1))
            stat_layout.add_widget(minus_btn)
            
            # Значение характеристики
            value_label = Label(
                text=str(self.stats[stat_name]),
                font_size='24sp',
                color=(1, 1, 1, 1),
                size_hint_x=None,
                width=60,
                bold=True
            )
            self.stat_labels[stat_name] = value_label
            stat_layout.add_widget(value_label)
            
            # Кнопка плюс
            plus_btn = Button(
                text='+',
                size_hint_x=None,
                width=60,
                background_color=(0.2, 0.8, 0.2, 1),
                color=(1, 1, 1, 1),
                font_size='24sp',
                bold=True
            )
            plus_btn.bind(on_press=lambda btn, s=stat_name: self.change_stat(s, 1))
            stat_layout.add_widget(plus_btn)
            
            stat_container.add_widget(stat_layout)
            main_layout.add_widget(stat_container)
        
        # Кнопки управления
        buttons_layout = BoxLayout(size_hint_y=None, height=60, spacing=15)
        
        # Кнопка сброса
        reset_btn = Button(
            text='Сброс',
            size_hint_x=0.5,
            background_color=(0.8, 0.2, 0.2, 1),
            color=(1, 1, 1, 1),
            font_size='20sp',
            bold=True
        )
        reset_btn.bind(on_press=self.reset_stats)
        buttons_layout.add_widget(reset_btn)
        
        # Кнопка завершения
        finish_btn = Button(
            text='Завершить',
            size_hint_x=0.5,
            background_color=(0.2, 0.7, 0.2, 1),
            color=(1, 1, 1, 1),
            font_size='20sp',
            bold=True
        )
        finish_btn.bind(on_press=self.finish_distribution)
        buttons_layout.add_widget(finish_btn)
        
        main_layout.add_widget(buttons_layout)
        self.add_widget(main_layout)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def _update_stat_container(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0.11, 0.12, 0.15, 0.7)
            RoundedRectangle(pos=instance.pos, size=instance.size, radius=[10])
    
    def change_stat(self, stat, delta):
        if delta > 0 and self.total_points > 0:
            self.stats[stat] += delta
            self.total_points -= delta
        elif delta < 0 and self.stats[stat] > 0:
            self.stats[stat] += delta
            self.total_points -= delta
        
        # Обновляем отображение
        self.stat_labels[stat].text = str(self.stats[stat])
        self.points_label.text = f'Очки: {self.total_points}'
    
    def reset_stats(self, instance):
        self.total_points = 10  # Сброс очков
        for stat in self.stats:
            self.stats[stat] = 2  # Сброс характеристик
            self.stat_labels[stat].text = '2'
        self.points_label.text = f'Очки: {self.total_points}'
    
    def finish_distribution(self, instance):
        if self.total_points == 0:
            self.manager.current = 'final'

class FinalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create_ui, 0.1)
    
    def create_ui(self, dt):
        # Черный фон с неоновым градиентом
        with self.canvas.before:
            # Основной черный фон
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            
            # Неоновые линии
            Color(0, 0.9, 1, 1)  # Неоново-голубой
            Line(points=[0, 0, self.width, 0], width=2)
            Line(points=[0, 0, 0, self.height], width=2)
            Line(points=[self.width, 0, self.width, self.height], width=2)
            Line(points=[0, self.height, self.width, self.height], width=2)
            
            # Декоративные элементы
            Color(0.1, 0, 0, 0.3)
            from kivy.graphics import Ellipse
            Ellipse(pos=(self.width*0.2, self.height*0.7), size=(100, 100))
            Ellipse(pos=(self.width*0.7, self.height*0.3), size=(150, 150))
            
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        # Центральный текст
        main_text = Label(
            text='Теперь ты часть игры',
            font_size='36sp',
            color=(0.8, 0, 0, 1),  # Кроваво-красный
            bold=True,
            halign='center'
        )
        self.add_widget(main_text)
        
        # Дополнительный декоративный текст
        sub_text = Label(
            text='[Добро пожаловать в реальность]',
            font_size='18sp',
            color=(0.5, 0, 0, 0.7),
            pos_hint={'center_x': 0.5, 'y': 0.2}
        )
        self.add_widget(sub_text)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
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
