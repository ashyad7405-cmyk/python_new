try:
  x = int(input("what's x"))

  print(f"x is {x}")

except ValueError:
  print("invalid entry")

#anthor way

try:
  x = int(input("what's x"))

except ValueError:
  print("x is not an integer")

else:
  print(f"x is {x}")
  

