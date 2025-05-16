from modules.character import Character
from modules.leveling import LevelSystem
from modules.ui import GamificationApp

class GameManager:
    def __init__(self):
        self.character = Character()
        self.level_system = LevelSystem()
        
    def add_experience(self, amount):
        return self.level_system.add_experience(amount)
        
    def upgrade_stat(self, stat_name):
        return self.character.increase_stat(stat_name)
    
    def get_character_stats(self):
        return self.character.get_stats()
    
    def get_talent_points(self):
        return self.character.get_talent_points()
    
    def get_level_info(self):
        return self.level_system.get_level_info()

if __name__ == '__main__':
    game = GameManager()
    GamificationApp(game_manager=game).run()
