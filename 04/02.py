import random
class Warrior:
    life = 100
    name = "Warrior"
    def attack(self):
        hit = random.choice(range(20))
        print("Воин",self.name,"атаковал на",hit)
        return hit

    def defence(self, hit):
        self.life -= hit
        print("Атаковали",self.name,"на",hit)
        if self.life <= 0:
            print("Воин",self.name,"умер.")
        return (self.life <= 0)
war1 = Warrior()
war1.name = "Первый"
war2 = Warrior()
war2.name = "Второй"
end = False
while end == False:
    print(war1.name, ":", war1.life)
    print(war2.name, ":", war2.life)
    end = end or war2.defence(war1.attack())
    end = end or war1.defence(war2.attack())
