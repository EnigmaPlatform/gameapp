class Character:
    def __init__(self):
        self.stats = {
            'strength': 1,
            'agility': 1,
            'intelligence': 1,
            'charisma': 1,
            'endurance': 1
        }
        self.talent_points = 10  # Начальные очки
        
    def increase_stat(self, stat_name):
        if self.talent_points > 0 and stat_name in self.stats:
            self.stats[stat_name] += 1
            self.talent_points -= 1
            return True
        return False
    
    def get_stats(self):
        return self.stats.copy()
    
    def get_talent_points(self):
        return self.talent_points

    def increase_stat(self, stat_name):
        if self.talent_points > 0 and stat_name in self.stats:
            self.stats[stat_name] += 1
            self.talent_points -= 1
            return True
        return False
