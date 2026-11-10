"""names = []

for _ in range(3):

   name = input("what's ur name?")
   names.append(name)
for name in sorted(names):
   print(f"hello, {name}")"""

"""name = input("what's ur name?")
with open("name.txt","a") as file:
   file.write(f"{name}\n")"""

"""with open("name.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

#2nd method
with open("name.txt","r") as file:
    for line in file:
        print("hello,", line.rstrip())"""

names = []

with open("name.txt","r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")