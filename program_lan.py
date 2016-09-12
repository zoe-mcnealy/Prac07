
class ProgramLanguage:
    def __init__(self,typing,reflection,year):
        """create the fields and set them to parameters passed in"""
        self.name = str(self)
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """which returns True/False if the programming language is dynamically typed or not"""
        if self.typing ='Static':
            print("{}, Dynamic Typing,")

