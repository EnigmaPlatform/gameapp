class LevelSystem:
    def __init__(self):
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100
        
    def add_experience(self, amount):
        self.experience += amount
        if self.experience >= self.experience_to_next_level:
            self.level_up()
            
    def level_up(self):
        self.level += 1
        self.experience -= self.experience_to_next_level
        self.experience_to_next_level = int(self.experience_to_next_level * 1.2)
        return True  # Для сигнала о новом уровне
    
    def get_level_info(self):
        return {
            'level': self.level,
            'experience': self.experience,
            'next_level': self.experience_to_next_level
        }
