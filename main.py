from modules.character import Character
from modules.leveling import LevelSystem
from modules.ui import GamificationApp

class GameManager:
    def __init__(self):
        self.character = Character()
        self.level_system = LevelSystem()
        
    def add_experience(self, amount):
        self.level_system.add_experience(amount)
        
    def upgrade_stat(self, stat_name):
        return self.character.increase_stat(stat_name)

if __name__ == '__main__':
    game = GameManager()
    GamificationApp(game_manager=game).run()
