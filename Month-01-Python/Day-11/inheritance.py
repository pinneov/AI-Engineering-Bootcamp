# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(f"Employee: {self.name}")


# class Developer(Employee):
#     def __init__(self, name, primary_language):
#         super().__init__(name)

#         self.primary_language = primary_language

# developer = Developer("Vincent")

# developer.display()

# print(isinstance(developer, Developer))
# print(isinstance(developer, Employee))

# print(issubclass(Developer, Employee))


class Employee:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"Employee: {self.name}")


class Developer(Employee):
    def __init__(self, name, primary_language):
        super().__init__(name)
        self.primary_language = primary_language

    def describe(self):
        super().describe()
        #print(f"Developer: {self.name}")
        print(f"Primary language: {self.primary_language}")

employee = Employee("Alice")
developer = Developer("Vincent", "C#")

employee.describe()
developer.describe()
