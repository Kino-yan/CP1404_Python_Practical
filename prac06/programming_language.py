class ProgrammingLanguage:
    def __init__(self, name, Typing, Reflection, year):
        self.name = name
        self.typing = Typing
        self.reflection = Reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        return  self.typing == "Dynamic"


