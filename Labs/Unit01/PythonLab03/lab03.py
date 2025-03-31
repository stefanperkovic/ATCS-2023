def to_celsius(temps):
    return list(map(lambda x: (x - 32) * 5/9, temps))


def remove_email_domains(emails):
    return list(map(lambda s: s[0: s.find("@")], emails))

def get_students(school, students):
    return list(filter(lambda s:  s["school"] in school, students))
    
from functools import reduce
def average_math_scores(students):
    lst = []
    for student in students:
        is_in_math = list(filter(lambda s: s == "math", student.keys()))
        if len(is_in_math) > 0:
            lst.append(student)
    lst = list(map(lambda s: s["math"], lst))
    return reduce(lambda x, y: x + y, lst) / len(lst)
       # lst = list(filter(lambda s: s["math"], students))




# emails = ["user1@example.com", "user2@example.com",
# "user3@gmail.com", "user4@example.com"]
# result = remove_email_domains(emails)
# print(result)
# schools = ['Menlo', 'Sacred Heart']
# students = [{'name': 'Alice', 'grade': 9, 'school': 'Menlo'},
# {'name': 'Bob', 'grade': 10, 'school': 'Sacred Heart'},
# {'name': 'Charlie', 'grade': 9, 'school': 'Menlo'},
# {'name': 'Delta', 'grade': 9, 'school': 'Sacred Heart'},
# {'name': 'Epsilon', 'grade': 9, 'school': 'Nueva'}]
# print(get_students(schools, students))

# students = [{'name': 'Alice', 'math': 85, 'science': 92},
# {'name': 'Bob', 'science': 88},
# {'name': 'Charlie', 'math': 90, 'science': 78},
# {'name': 'Delta', 'math': 94, 'science': 78}]
# print(average_math_scores(students))