from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
import random

class CharacterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create_ui, 0.1)
    
    def create_ui(self, dt):
        # Фон
        with self.canvas.before:
            Color(0.05, 0.05, 0.1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.uix.image import Image
        
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Заголовок
        title = Label(
            text='ВАШ ГЕРОЙ СОЗДАН!',
            font_size='32sp',
            color=(0, 0.9, 1, 1),
            size_hint_y=None,
            height=60,
            bold=True
        )
        main_layout.add_widget(title)
        
        # Контент
        content_layout = BoxLayout(spacing=20)
        
        # Левая колонка - характеристики
        left_layout = BoxLayout(orientation='vertical', size_hint_x=0.6, spacing=10)
        
        # Заголовок характеристик
        stats_title = Label(
            text='ХАРАКТЕРИСТИКИ',
            font_size='24sp',
            color=(0.8, 0.8, 0.8, 1),
            size_hint_y=None,
            height=40,
            bold=True
        )
        left_layout.add_widget(stats_title)
        
        # Список характеристик
        self.stats_layout = BoxLayout(orientation='vertical', spacing=5)
        left_layout.add_widget(self.stats_layout)
        
        # Класс героя
        self.class_label = Label(
            text='',
            font_size='20sp',
            color=(1, 0.8, 0.2, 1),
            size_hint_y=None,
            height=40,
            bold=True
        )
        left_layout.add_widget(self.class_label)
        
        content_layout.add_widget(left_layout)
        
        # Правая колонка - информация
        right_layout = BoxLayout(orientation='vertical', size_hint_x=0.4, spacing=10)
        
        # Аватар (пока заглушка)
        avatar_label = Label(
            text='[АВАТАР]',
            font_size='18sp',
            color=(0.6, 0.6, 0.6, 1),
            size_hint_y=0.3
        )
        right_layout.add_widget(avatar_label)
        
        # Описание
        self.description_label = Label(
            text='',
            font_size='16sp',
            color=(0.8, 0.8, 0.8, 1),
            text_size=(None, None),
            halign='left',
            valign='top'
        )
        right_layout.add_widget(self.description_label)
        
        content_layout.add_widget(right_layout)
        
        main_layout.add_widget(content_layout)
        
        # Кнопки
        buttons_layout = BoxLayout(size_hint_y=None, height=60, spacing=15)
        
        back_btn = Button(
            text='Назад',
            background_color=(0.5, 0.5, 0.5, 1)
        )
        back_btn.bind(on_press=lambda x: self.manager.current('main'))
        buttons_layout.add_widget(back_btn)
        
        logs_btn = Button(
            text='Логи системы',
            background_color=(0.3, 0.3, 0.3, 1)
        )
        logs_btn.bind(on_press=lambda x: self.manager.current('logs'))
        buttons_layout.add_widget(logs_btn)
        
        main_layout.add_widget(buttons_layout)
        
        self.add_widget(main_layout)
    
    def on_enter(self):
        # Получаем данные персонажа
        if hasattr(self.manager, 'app_data'):
            character_data = self.manager.app_data
            self.display_character(character_data)
    
    def display_character(self, character_data):
        # Очищаем предыдущие данные
        self.stats_layout.clear_widgets()
        
        from kivy.uix.label import Label
        
        # Отображаем характеристики
        stats = character_data.get('stats', {})
        for stat_name, value in stats.items():
            stat_layout = self.create_stat_row(stat_name, value)
            self.stats_layout.add_widget(stat_layout)
        
        # Определяем класс героя
        hero_class = self.determine_hero_class(stats)
        self.class_label.text = f'Класс: {hero_class}'
        
        # Генерируем описание
        description = self.generate_description(stats, hero_class)
        self.description_label.text = description
    
    def create_stat_row(self, stat_name, value):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        
        layout = BoxLayout(size_hint_y=None, height=35, spacing=10)
        
        name_label = Label(
            text=stat_name,
            font_size='18sp',
            color=(0.8, 0.8, 0.8, 1),
            size_hint_x=0.6,
            halign='left'
        )
        
        value_label = Label(
            text=str(value),
            font_size='18sp',
            color=(0, 0.9, 1, 1),
            size_hint_x=0.4,
            bold=True
        )
        
        layout.add_widget(name_label)
        layout.add_widget(value_label)
        
        return layout
    
    def determine_hero_class(self, stats):
        # Определяем класс на основе характеристик
        max_stat = max(stats, key=stats.get)
        max_value = stats[max_stat]
        
        if max_value >= 8:
            classes = {
                'Сила': ['Викинг', 'Берсерк', 'Гладиатор'],
                'Ловкость': ['Ниндзя', 'Вор', 'Акробат'],
                'Интеллект': ['Маг', 'Ученый', 'Хакер'],
                'Выносливость': ['Танк', 'Марathonец', 'Железный человек'],
                'Харизма': ['Лидер', 'Дипломат', 'Звезда шоу']
            }
        elif max_value >= 6:
            classes = {
                'Сила': ['Спортсмен', 'Охранник', 'Плотник'],
                'Ловкость': ['Танцор', 'Механик', 'Курьер'],
                'Интеллект': ['Студент', 'Программист', 'Инженер'],
                'Выносливость': ['Бегун', 'Пловец', 'Йог'],
                'Харизма': ['Продавец', 'Ведущий', 'Актер']
            }
        else:
            classes = {
                'Сила': ['Новичок', 'Стажер', 'Ученик'],
                'Ловкость': ['Новичок', 'Стажер', 'Ученик'],
                'Интеллект': ['Новичок', 'Стажер', 'Ученик'],
                'Выносливость': ['Новичок', 'Стажер', 'Ученик'],
                'Харизма': ['Новичок', 'Стажер', 'Ученик']
            }
        
        return random.choice(classes.get(max_stat, ['Обычный человек']))
    
    def generate_description(self, stats, hero_class):
        descriptions = {
            'Викинг': 'Сильный воин северных земель. Способен поднять бочку эля одной рукой!',
            'Берсерк': 'Неистовый боец, впадающий в ярость. Осторожно: может перепутать друзей с врагами.',
            'Гладиатор': 'Мастер меча и арены. Выиграл 100 боев подряд (в своей голове).',
            'Ниндзя': 'Мастер скрытности. Может исчезнуть, даже когда его никто не видит.',
            'Вор': 'Эксперт по карманной краже. Особенно эффективен в пробках.',
            'Акробат': 'Грациозный performer. Может упасть с ног, не задевая пол.',
            'Маг': 'Повелитель стихий. Особенно воды из крана.',
            'Ученый': 'Гений мысли. Способен объяснить, почему не работает Wi-Fi.',
            'Хакер': 'Повелитель кода. Взломает любой WiFi... если будет пароль.',
            'Танк': 'Непробиваемая защита. Даже очередь в магазин не берет.',
            'Марафонец': 'Мастер выносливости. Способен смотреть сериалы без перерыва.',
            'Железный человек': 'Технологический гений. Создал робота... который не работает.',
            'Лидер': 'Вдохновляющий на подвиги. Особенно на кухню.',
            'Дипломат': 'Мастер компромиссов. Может договориться даже с кофе.',
            'Звезда шоу': 'Харизматичный персонаж. Даже в зеркале улыбается.',
            'Обычный человек': 'Среднестатистический герой. Способен удивляться скидкам.'
        }
        
        base_desc = descriptions.get(hero_class, f'Уникальный персонаж класса {hero_class}')
        
        # Добавляем случайные особенности
        features = [
            'Любит кофе',
            'Боится пауков',
            'Обожает музыку',
            'Собирает мемы',
            'Мечтает о коте',
            'Знает 5 фактов о космосе',
            'Может жонглировать',
            'Говорит на 3 языках (включая эльфийский)'
        ]
        
        feature = random.choice(features)
        
        return f"{base_desc}\n\nОсобенность: {feature}"
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
