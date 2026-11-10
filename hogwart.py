"""students = ["harry","ash","ron"]
for student in students:
   print(student)
print(len(students))"""


students = {
   "1.harry":"iceland",
   "2.ash":"india",
   "3.dreco":"austria"
}
address = {
   "iceland":"xyz",
   "india":"abc",
   "austria":"pqr"
}
students.update(address)
print(students)

