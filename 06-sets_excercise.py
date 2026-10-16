python_curse = {"Ana", "Luis", "Maria", "Pedro"}
java_curse = {"Pepito", "Pedro", "Carlos", "Ricardo"}

two_courses = python_curse.intersection(java_curse)
print(two_courses)

only_python = python_curse.difference(java_curse)
print(only_python)

only_java = java_curse.difference(python_curse)
print(only_java)

all_students = python_curse.union(java_curse)
print(all_students)
