#Calculator
print("Welcome, please enter the values of your two vectors ")
i1 = float(input("Value for i1: "))
j1 = float(input("Value for j1: "))
k1 = float(input("Value for k1: "))
i2 = float(input("Value for i2: "))
j2 = float(input("Value for j2: "))
k2 = float(input("Value for k2: "))
act = int(input("What do you want to do? (1 for sum, 2 for sub, 3 for mult, 4 for cross): "))
A = np.array([i1, j1, k1])
B = np.array([i2, j2, k2])
if act == 1:
  C = A + B
elif act == 2:
  C = A - B
elif act == 3:
  C = np.dot(A, B)
elif act == 4:
  C = np.cross(A, B)
else:
  print("Invalid input")
if act in [1, 2, 4]:
  print("Resultant vector = ", C)
  print("resultant magnitude = ", np.linalg.norm(C))
elif act == 3:
  print("Resultant scalar = ", C)
