import random

class Chef:
    def __init__(self, name, skill, speed, creativity):
        self.name = name
        self.skill = skill
        self.speed = speed
        self.creativity = creativity
        self.score = 0
        self.active = True

    def compete(self, opponent):
            points = self.skill + self.creativity - opponent.speed
            if points < 1:
                points = 1
            self.score += points
            print(f'{self.name} earns {points} points!')

            opponent.take_points(points)

    def take_points(self, points):
        self.score -= points
        print(f'{self.name} loses {points} points :(')
        
        if self.score < 0:
            self.score = 0
            self.active = False
            print(f'{self.name} has been eliminated!')
    def is_active(self):
        return self.active
    def show_stats(self):
        print(f'     :o        ')
        print(f'Name: {self.name}')
        print(f'Skill: {self.skill}')
        print(f'Speed: {self.speed}')
        print(f'Creativity: {self.creativity}')
        print(f'Score: {self.score}')
        print(f'Active: {self.active}')

class CookingContest:
    def __init__(self):
        self.chefs = []

    def add_chef(self, chef):
        self.chefs.append(chef)

    def get_active_chefs(self):
        active = []
        for chef in self.chefs:
            if chef.active:
                active.append(chef)
        return active
    
    def start_contest(self):
        print('Contest started!')
        active = self.get_active_chefs()

        while len(active) > 1:
            random.shuffle(active)

            c1 = active[0]
            c2 = active[1]

            print(f'\n{c1.name} vs {c2.name}')
            c1.compete(c2)
            
            if c2.is_active():
                c2.compete(c1)
                
            print('\nCurrent status:')
            
            for chef in self.chefs:
                chef.show_stats()
            
            active = self.get_active_chefs()


    def show_winner(self):
        winner = self.get_active_chefs()
        print(f'Winner: {winner[0].name}')

# main lol 
chef1 = Chef('Diana', 15, 7, 10)
chef2 = Chef('Aiken', 12, 2, 8)
chef3 = Chef('Aruka', 16, 9, 9)

contest = CookingContest()
contest.add_chef(chef1)
contest.add_chef(chef2)
contest.add_chef(chef3)


contest.start_contest()
contest.show_winner()
