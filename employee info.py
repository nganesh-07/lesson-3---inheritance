class person(object):

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

class employee(person):
    def __init__(self, name, id, salary, pos):
        self.salary = salary
        self.pos = pos

        person.__init__(self, name, id)

n = employee("rahul", 209175, 150000, "manager")

n.display()
