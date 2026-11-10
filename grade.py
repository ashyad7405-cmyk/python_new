score = int(input("score:"))

if score>=90 and score<=100:
    print("grade: A")
elif score>=80 and score<90:
    print("grade:"" C")
elif score>=60 and score<70:
    print("grade: D")
elif score>=50 and score<60:
    print("grade: E")
else:
    print("grade: F")
