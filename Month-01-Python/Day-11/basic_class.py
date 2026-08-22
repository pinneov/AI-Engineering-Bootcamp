#class Developer:
#    pass

#print(developer)
#print(type(developer))

class Developer:
    def __init__(self, name):
        self.name = name

developer = Developer("Vincent")

print(developer.name)
