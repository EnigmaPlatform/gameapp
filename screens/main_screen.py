from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, RoundedRectangle
import json
import os
import random

class MainScreen(Screen):
    total_points = NumericProperty(10)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stats = {
            'Сила': 2,
            'Ловкость': 2,
            'Интеллект': 2,
            'Выносливость': 2,
            'Харизма': 2,
        }
        self.jokes = self.load_jokes()
        self.logs = self.load_logs()
        Clock.schedule_once(self.create_ui, 0.1)
    
    def load_jokes(self):
        default_jokes = {
            "Сила": [
                "Ты сможешь открыть банку из-под огурцов!",
                "Ты сильнее среднестатистического кота!",
                "Ты можешь поднять пакет с молоком... если он полный!"
            ],
            "Ловкость": [
                "Ты не уронишь телефон... наверное",
                "Ты сможешь поймать летающую тарелку!",
                "Ты ловок как ниндзя... в своих мечтах"
            ],
            "Интеллект": [
                "Ты знаешь что 2+2=4!",
                "Ты можешь вспомнить что ел на завтрак!",
                "Ты понимаешь сарказм... иногда"
            ],
            "Выносливость": [
                "Ты можешь простоять в очереди 10 минут!",
                "Ты выдержишь просмотр одного сериала за раз!",
                "Ты не умрешь от переизбытка кофеина!"
            ],
            "Харизма": [
                "Ты можешь улыбнуться фотографу!",
                "Ты не испугаешься говорить 'алло' по телефону!",
                "Ты способен на комплимент погоде!"
            ]
        }
        
        jokes_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'jokes.json')
        if os.path.exists(jokes_file):
            try:
                with open(jokes_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return default_jokes
        return default_jokes
    
    def load_logs(self):
        default_logs = [
            "[INFO] Создание нового персонажа...",
            "[DEBUG] Распределение очков: 10/10",
            "[SYSTEM] Генерация личности...",
            "[WARNING] Обнаружена подозрительная активность: слишком много кликов!",
            "[ERROR] Не удалось загрузить аватар - используется стандартный",
            "[SUCCESS] Персонаж создан успешно!",
            "[LOG] Пользователь нажал кнопку 'Сброс' - это нормально",
            "[HACK] Активирован режим 'Супергерой' - шутка!"
        ]
        
        logs_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'logs.json')
        if os.path.exists(logs_file):
            try:
                with open(logs_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get('logs', default_logs)
            except:
                return default_logs
        return default_logs
    
    def create_ui(self, dt):
        # Фон
        with self.canvas.before:
            Color(0.06, 0.1, 0.18, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        
        main_layout = BoxLayout(orientation='vertical', padding=25, spacing=20)
        
        # Заголовок
        title = Label(
            text='ГЕНЕРАТОР ГЕРОЕВ',
            font_size='28sp',
            color=(0, 0.9, 1, 1),
            size_hint_y=None,
            height=60,
            bold=True
        )
        main_layout.add_widget(title)
        
        # Очки
        self.points_label = Label(
            text=f'Очки: {self.total_points}',
            font_size='24sp',
            color=(0, 0.9, 1, 1),
            size_hint_y=None,
            height=50,
            bold=True
        )
        main_layout.add_widget(self.points_label)
        
        # Характеристики
        self.stat_labels = {}
        self.value_labels = {}
        self.joke_labels = {}
        
        for stat_name in self.stats:
            # Контейнер для характеристики
            stat_container = BoxLayout(size_hint_y=None, height=80, orientation='vertical')
            
            # Верхняя часть - характеристика и кнопки
            top_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
            
            stat_label = Label(
                text=stat_name,
                font_size='20sp',
                color=(0.8, 0.8, 0.8, 1),
                size_hint_x=0.4,
                bold=True
            )
            top_layout.add_widget(stat_label)
            
            minus_btn = Button(
                text='-',
                size_hint_x=None,
                width=50,
                background_color=(0.8, 0.2, 0.2, 1)
            )
            minus_btn.bind(on_press=lambda btn, s=stat_name: self.change_stat(s, -1))
            top_layout.add_widget(minus_btn)
            
            value_label = Label(
                text=str(self.stats[stat_name]),
                font_size='20sp',
                color=(1, 1, 1, 1),
                size_hint_x=None,
                width=40,
                bold=True
            )
            self.value_labels[stat_name] = value_label
            top_layout.add_widget(value_label)
            
            plus_btn = Button(
                text='+',
                size_hint_x=None,
                width=50,
                background_color=(0.2, 0.8, 0.2, 1)
            )
            plus_btn.bind(on_press=lambda btn, s=stat_name: self.change_stat(s, 1))
            top_layout.add_widget(plus_btn)
            
            stat_container.add_widget(top_layout)
            
            # Нижняя часть - шутка
            joke_label = Label(
                text='',
                font_size='14sp',
                color=(0.6, 0.6, 0.6, 1),
                size_hint_y=None,
                height=30,
                text_size=(self.width - 50, None),
                halign='center'
            )
            self.joke_labels[stat_name] = joke_label
            stat_container.add_widget(joke_label)
            
            main_layout.add_widget(stat_container)
        
        # Кнопки
        buttons_layout = BoxLayout(size_hint_y=None, height=60, spacing=15)
        
        reset_btn = Button(
            text='Сброс',
            background_color=(0.8, 0.2, 0.2, 1)
        )
        reset_btn.bind(on_press=self.reset_stats)
        buttons_layout.add_widget(reset_btn)
        
        random_btn = Button(
            text='Случайно',
            background_color=(0.6, 0.4, 0.8, 1)
        )
        random_btn.bind(on_press=self.randomize_stats)
        buttons_layout.add_widget(random_btn)
        
        finish_btn = Button(
            text='Создать героя',
            background_color=(0.2, 0.7, 0.2, 1)
        )
        finish_btn.bind(on_press=self.finish_distribution)
        buttons_layout.add_widget(finish_btn)
        
        main_layout.add_widget(buttons_layout)
        
        # Навигационные кнопки
        nav_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        logs_btn = Button(
            text='Логи системы',
            background_color=(0.3, 0.3, 0.3, 1),
            font_size='16sp'
        )
        logs_btn.bind(on_press=lambda x: self.manager.current('logs'))
        nav_layout.add_widget(logs_btn)
        
        main_layout.add_widget(nav_layout)
        
        self.add_widget(main_layout)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def change_stat(self, stat, delta):
        if delta > 0 and self.total_points > 0:
            self.stats[stat] += delta
            self.total_points -= delta
        elif delta < 0 and self.stats[stat] > 0:
            self.stats[stat] += delta
            self.total_points -= delta
        
        # Обновляем отображение
        self.value_labels[stat].text = str(self.stats[stat])
        self.points_label.text = f'Очки: {self.total_points}'
        
        # Показываем шутку
        if stat in self.jokes:
            jokes = self.jokes[stat]
            if jokes:
                joke = random.choice(jokes)
                self.joke_labels[stat].text = joke
    
    def reset_stats(self, instance):
        self.total_points = 10
        for stat in self.stats:
            self.stats[stat] = 2
            self.value_labels[stat].text = '2'
            self.joke_labels[stat].text = ''
        self.points_label.text = f'Очки: {self.total_points}'
    
    def randomize_stats(self, instance):
        # Сбросим сначала
        self.reset_stats(None)
        
        # Распределим случайно
        points_to_distribute = 10
        stats_list = list(self.stats.keys())
        
        while points_to_distribute > 0:
            stat = random.choice(stats_list)
            if self.stats[stat] < 10:  # Максимум 10 на характеристику
                self.stats[stat] += 1
                points_to_distribute -= 1
        
        # Обновим отображение
        for stat in self.stats:
            self.value_labels[stat].text = str(self.stats[stat])
        self.total_points = 0
        self.points_label.text = f'Очки: {self.total_points}'
    
    def finish_distribution(self, instance):
        if self.total_points == 0:
            # Сохраняем данные персонажа
            character_data = {
                'stats': self.stats,
                'logs': self.logs
            }
            
            # Сохраняем в app_data
            if hasattr(self.manager, 'app_data'):
                self.manager.app_data = character_data
            else:
                self.manager.app_data = character_data
            
            self.manager.current = 'character'
