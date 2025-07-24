from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
import random
import datetime

class LogsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logs = []
        self.generate_logs()
        Clock.schedule_once(self.create_ui, 0.1)
    
    def generate_logs(self):
        # Генерируем забавные системные логи
        base_logs = [
            "[INFO] Система запущена",
            "[DEBUG] Проверка целостности данных...",
            "[SYSTEM] Генерация персонажа...",
            "[WARNING] Обнаружено подозрительное поведение пользователя",
            "[ERROR] Не удалось загрузить аватар - используется стандартный",
            "[SUCCESS] Персонаж успешно создан!",
            "[LOG] Пользователь нажал кнопку 'Сброс'",
            "[HACK] Активирован режим 'Супергерой'",
            "[INFO] Загрузка базы данных...",
            "[DEBUG] Проверка лицензии...",
            "[SYSTEM] Синхронизация с облаком...",
            "[WARNING] Низкий уровень заряда батареи",
            "[ERROR] 404: Шутка не найдена",
            "[SUCCESS] Все системы работают нормально",
            "[LOG] Пользователь активен",
            "[HACK] Обнаружен читер!",
            "[INFO] Обновление системы...",
            "[DEBUG] Тестирование характеристик...",
            "[SYSTEM] Генерация случайных событий...",
            "[WARNING] Слишком много кликов!",
            "[ERROR] StackOverflowError: слишком много шуток",
            "[SUCCESS] Миссия выполнена!",
            "[LOG] Создание резервной копии...",
            "[HACK] Взлом системы... Шутка! Это всего лишь игра.",
            "[INFO] Подключение к серверу...",
            "[DEBUG] Проверка скорости интернета...",
            "[SYSTEM] Оптимизация производительности...",
            "[WARNING] Обнаружен кот на клавиатуре",
            "[ERROR] Не удалось найти смысл жизни",
            "[SUCCESS] Смысл жизни найден: создавать персонажей!",
            "[LOG] Пользователь улыбнулся - это хорошо",
            "[HACK] Активирован режим 'Бог персонажей'",
            "[INFO] Загрузка шуток...",
            "[DEBUG] Проверка уровня сарказма...",
            "[SYSTEM] Генерация случайных чисел...",
            "[WARNING] Слишком высокий IQ для этой игры",
            "[ERROR] DivisionByZeroException: попытка делить на кофе",
            "[SUCCESS] Кофе найден! Продолжаем работу.",
            "[LOG] Пользователь прочитал это сообщение - паразит!",
            "[HACK] Взлом мозга пользователя... успешно!",
            "[INFO] Подсчет статистики...",
            "[DEBUG] Анализ поведения...",
            "[SYSTEM] Генерация предсказаний...",
            "[WARNING] Обнаружена аномалия в матрице",
            "[ERROR] MatrixError: красная таблетка не найдена",
            "[SUCCESS] Матрица стабилизирована!",
            "[LOG] Создание виртуальной реальности...",
            "[HACK] Активирован режим 'Реальность 2.0'",
            "[INFO] Загрузка дополнительных функций...",
            "[DEBUG] Проверка совместимости...",
            "[SYSTEM] Обновление интерфейса...",
            "[WARNING] Интерфейс слишком красив!",
            "[ERROR] BeautyOverloadException: система ослеплена красотой",
            "[SUCCESS] Защита от красоты активирована!",
            "[LOG] Пользователь доволен - миссия выполнена",
            "[HACK] Взлом сердца пользователя... ❤️"
        ]
        
        # Генерируем временные метки
        self.logs = []
        current_time = datetime.datetime.now()
        
        for i, log in enumerate(base_logs):
            timestamp = current_time - datetime.timedelta(minutes=i*5)
            formatted_time = timestamp.strftime("%H:%M:%S")
            self.logs.append(f"[{formatted_time}] {log}")
    
    def create_ui(self, dt):
        # Фон
        with self.canvas.before:
            Color(0.02, 0.02, 0.02, 1)  # Почти черный
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.uix.scrollview import ScrollView
        from kivy.uix.gridlayout import GridLayout
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Заголовок
        title = Label(
            text='СИСТЕМНЫЕ ЛОГИ',
            font_size='28sp',
            color=(0, 0.9, 1, 1),  # Неоново-голубой
            size_hint_y=None,
            height=50,
            bold=True
        )
        main_layout.add_widget(title)
        
        # Создаем ScrollView для логов
        scroll = ScrollView()
        
        # Контейнер для логов
        logs_layout = GridLayout(cols=1, spacing=2, size_hint_y=None)
        logs_layout.bind(minimum_height=logs_layout.setter('height'))
        
        # Добавляем логи
        for log in self.logs:
            # Определяем цвет по типу лога
            if '[ERROR]' in log:
                color = (0.9, 0.3, 0.3, 1)  # Красный
            elif '[WARNING]' in log:
                color = (0.9, 0.7, 0.3, 1)  # Желтый
            elif '[SUCCESS]' in log:
                color = (0.3, 0.9, 0.3, 1)  # Зеленый
            elif '[HACK]' in log:
                color = (0.8, 0.3, 0.8, 1)  # Фиолетовый
            else:
                color = (0.7, 0.7, 0.7, 1)  # Серый
            
            log_label = Label(
                text=log,
                font_size='14sp',
                color=color,
                size_hint_y=None,
                height=30,
                text_size=(self.width - 30, None),
                halign='left',
                valign='middle'
            )
            log_label.bind(size=log_label.setter('text_size'))
            logs_layout.add_widget(log_label)
        
        scroll.add_widget(logs_layout)
        main_layout.add_widget(scroll)
        
        # Кнопки
        buttons_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        back_btn = Button(
            text='Назад',
            background_color=(0.3, 0.3, 0.3, 1)
        )
        back_btn.bind(on_press=lambda x: self.manager.current('main'))
        buttons_layout.add_widget(back_btn)
        
        refresh_btn = Button(
            text='Обновить логи',
            background_color=(0.2, 0.6, 0.8, 1)
        )
        refresh_btn.bind(on_press=self.refresh_logs)
        buttons_layout.add_widget(refresh_btn)
        
        main_layout.add_widget(buttons_layout)
        
        self.add_widget(main_layout)
    
    def refresh_logs(self, instance):
        # Генерируем новые логи и обновляем экран
        self.generate_logs()
        # Пересоздаем UI
        self.clear_widgets()
        Clock.schedule_once(self.create_ui, 0.1)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
