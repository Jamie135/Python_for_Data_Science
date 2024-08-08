import inspect
from pprint import pprint
from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)
print("\n------------------\n")
pprint(inspect.getmembers(Student, inspect.isfunction))
print("\n------------------\n")
student = Student(name="Edward", surname="agle", id="toto")
print(student)
