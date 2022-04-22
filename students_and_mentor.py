#  Отдельно выводим в новый класс статический метод расчета среднего
class Math:
    @staticmethod
    def average(dict):
            if len(dict) >= 1:
                summ_values = 0
                len_values = 0

                for key, values in dict.items():
                    len_values = len_values + len(values)
                    for value in values:
                        summ_values = summ_values + value
                average = summ_values / len_values
            else:
                average = 'Not grades'
            return average

# Класс студенты-------------------------------------------------------
class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Выставляем оценки читаюшим
    def rate_hw(self, lecturer, course, grade):
        # если читающий принадлежит лекторам, курс есть у Читающего и курс есть у студента
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] +=[grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        res = f'''
        Student
        Name: {self.name}
        Surname: {self.surname}
        Average grade for homework: {Math.average(self.grades)}
        Courses in progress: {", ".join(i for i in self.courses_in_progress)} 
        Completed courses: {", ".join(i for i in self.finished_courses)} 
        '''
        return res

    def __lt__(self, other):
        
        if Math.average(self.grades) == 'Not grades' or Math.average(other.grades) == 'Not grades' or not isinstance(other, Student):
            return print('Not grades')
        else:
            return Math.average(self.grades) < Math.average(other.grades)
    
        
# Класс Менторы----------------------------------------------------------
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
# Класс Читающих лекции------------------------------------------------------
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

     

    def __str__(self):
        res = f'''
        LECTURER
        Name: {self.name}
        Surname: {self.surname}
        Average grade for lectures: {Math.average(self.grades)}
        '''
        return res
    
    def __lt__(self, other):

        if Math.average(self.grades) == 'Not grades' or Math.average(other.grades) == 'Not grades' or not isinstance(other, Lecturer):
            return print('Not grades')
        else:
            return Math.average(self.grades) < Math.average(other.grades)


# Класс Проверяющих-------------------------------------------------------------
class Reviewer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    # Расставляем оценки ученикам 
    def rate_hw(self, student, course, grade):
        # если студент принадлежит студентам, курс есть у Ревьювера и курс есть у студента
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] +=[grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'
        
    def __str__(self):
        res = f'''
        REVIEWER
        Name: {self.name}
        Surname: {self.surname}
        '''
        return res

        
        
# Вводим персонажей---------------------------------------------------------------------
student1 = Student('Valera', 'Chashkin', 'men')
student1.courses_in_progress += ['Python', 'GIT', 'Photoshop']
student1.finished_courses += ['ArchiCad', 'MS Offise', 'Git', '3D MAX']

student2 = Student('Sema', 'Zaytzhev', 'men')
student2.courses_in_progress += ['Java']

student3 = Student('Gosha', 'Tetradkin', 'men')
student3.courses_in_progress += ['Python', 'Java', ]
student3.finished_courses += ['ArcGis', 'Mapinfo', 'Git', 'Photoshop']

student4 = Student('Lilya', 'Pustishkina', 'women')
student4.courses_in_progress += ['Python']


# Вводим Проверяющих-----------------------------------------------------------------------

reviewer1 = Reviewer('Prosya', 'Doyarkina')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Zina', 'Rezina')
reviewer2.courses_attached += ['Python', 'Java']

# Вводим читающий лекции----------------------------------------------------------------

lecturer1 = Lecturer('Boris', 'Ochkov')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Yana', 'Korito-Krito')
lecturer2.courses_attached += ['Java']

# Проставляем оценки ученикам и просматриваем результат------------------------------
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Java', 5)   # Проверка на ошибку
reviewer2.rate_hw(student3, 'Python',6)
reviewer2.rate_hw(student4, 'Python', 8)

# print(student1.grades)
# print(student2.grades)
# print(student3.grades)
# print(student4.grades)

# Расставляем оценки лекторам-------------------------------------------

student1.rate_hw(lecturer1, 'Python', 10)
student2.rate_hw(lecturer2, 'Java', 8)
student3.rate_hw(lecturer1, 'Python', 10)
student4.rate_hw(lecturer2, 'Python', 9)

# print(lecturer1.grades)
# print(lecturer2.grades)

# Вывод описания------------------------

# print(student2)
print(lecturer2)
# print(reviewer1)
#  Проверяем на Больше-Меньше---------------------------------------


print(student1 > student2)
print(lecturer2 > lecturer1)