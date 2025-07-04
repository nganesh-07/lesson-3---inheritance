class bird:
    def __init__(self):
        print("Bird is ready.")

    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("Swim faster.")

    
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready.")
    
    def whoisthis(self):
        print("Penguin")

    def run(self):
        print("Run faster.")


pingu = penguin()
parent = bird()
parent.whoisthis()
pingu.whoisthis()
pingu.run()
pingu.swim()