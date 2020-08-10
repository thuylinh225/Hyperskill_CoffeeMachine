class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + birth_year

name_input = str(input())
last_name_input = str(input())
birth_year_input = str(input())

newid = Student(name_input, last_name_input, birth_year_input)
print(newid.id)
