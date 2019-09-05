class Warrior:
    def __init__(self, experience):
        self.exp = experience
        self.achiev = ['']

    @property
    def level(self):
        return self.exp // 100

    @property
    def achievements(self):
        return self.achiev

    @property
    def check_level(self):
        if self.exp > 10000:
            self.exp = 100000
        return self.exp

    @property
    def experience(self):
        return self.exp

    @property
    def level(self):
        return self.exp // 100

    @property
    def rank(self):
        level = self.level
        if 1 <= level < 10:
            rank = "Pushover"
        elif 10 <= level < 20:
            rank = "Novice"
        elif 20 <= level < 30:
            rank = "Fighter"
        elif 30 <= level < 40:
            rank = "Warrior"
        elif 40 <= level < 50:
            rank = "Veteran"
        elif 50 <= level < 60:
            rank = "Sage"
        elif 60 <= level < 70:
            rank = "Elite"
        elif 70 <= level < 80:
            rank = "Conqueror"
        elif 80 <= level < 90:
            rank = "Champion"
        elif 90 <= level < 100:
            rank = "Master"
        else:
            rank = "Greatest"
        return rank

    def battle(self, enemy_level):
        level = self.level
        difference_of_levels = abs(enemy_level - level)
        if difference_of_levels == 0:
            self.exp += 10
            self.check_level
            return "A good fight"
        elif difference_of_levels == 1 and level > enemy_level:
            self.exp += 5
            self.check_level
            return "A good fight"
        elif difference_of_levels <= 5 and level < enemy_level:
            self.exp += 20 * difference_of_levels * difference_of_levels
            self.check_level
            return "An intense fight"
        elif difference_of_levels >= 2 and level > enemy_level:
            return "Easy fight"
        else:
            return "You`ve been defeated"

    def training(self, training_name, exp_cost, necessary_lvl):
        if self.level >= necessary_lvl:
            self.achiev.append(training_name)
            self.exp += exp_cost
            self.check_level
            return training_name
        else:
            return "Not strong enough"


if __name__ == "__main__":
    sponge_bob = Warrior(100)
    Patric = Warrior(100)

    print(sponge_bob.training('Box', 500, 1))
    print(sponge_bob.battle(11))
    print(sponge_bob.training('MMA', 900, 11))
    print(sponge_bob.exp)
