import random as r

legal = [0, 10]

class Turtle:
    def __init__(self):
        self.hp = 100                               #初始hp
        self.x = r.randint(legal[0], legal[1])
        self.y = r.randint(legal[0], legal[1])      #初始位置


    def move(self):
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])   #移动

        if new_x < legal[0]:
            self.x = 2 * legal[0] - new_x
        elif new_x > legal[1]:
            self.x = 2 * legal[1] - new_x
        else:
            self.x = new_x

        if new_y < legal[0]:
            self.y = 2 * legal[0] - new_y
        elif new_y > legal[1]:
            self.y = 2 * legal[1] - new_y
        else:
            self.y = new_y                          #出界防止


        self.hp -= 1                                #hp消耗

        return (self.x, self.y)                     #返回位置


    def eat(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100                           #回血



class Fish():
    def __init__(self):
        self.x = r.randint(legal[0], legal[1])
        self.y = r.randint(legal[0], legal[1])      #初始位置

    def move(self):
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])   #移动

        if new_x < legal[0]:
            self.x = 2 * legal[0] - new_x
        elif new_x > legal[1]:
            self.x = 2 * legal[1] - new_x
        else:
            self.x = new_x

        if new_y < legal[0]:
            self.y = 2 * legal[0] - new_y
        elif new_y > legal[1]:
            self.y = 2 * legal[1] - new_y
        else:
            self.y = new_y                          #出界防止

        return (self.x, self.y)                     #返回位置


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)




while True:
    if not len(fish):
        print('All fish eaten, You Win')
        break
    if not turtle.hp:
        print('Yuo die, GAME OVER')
        break


    pos = turtle.move()

    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()                            #eat
            fish.remove(each_fish)
            print('a fish has been eaten')
