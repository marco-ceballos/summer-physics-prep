import numpy as np

print("Welcome, what do you want to do? (1 for sum, 2 for sub, 3 for dot, " )
act=int(input("4 for cross, 5 for unit vector, direction cosine and angles: ")) 

if act in [1, 2, 3, 4]:
  print("Please enter the values of both vectors \n")
  i1 = float(input("Value for i1: "))
  j1 = float(input("Value for j1: "))
  k1 = float(input("Value for k1: "))
  i2 = float(input("Value for i2: "))
  j2 = float(input("Value for j2: "))
  k2 = float(input("Value for k2: "))
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

elif act == 5:
  print("Please enter the values of your vector \n")
  i1 = float(input("Value for i1: "))
  j1 = float(input("Value for j1: "))
  k1 = float(input("Value for k1: "))
  A = np.array([i1, j1, k1])

else:
  print("Invalid input")

if act in [1, 2, 4]:
  print("\nResultant vector = ", C)
  print("resultant magnitude = ", np.linalg.norm(C))
elif act == 3:
  print("\nResultant scalar = ", C)
elif act == 5:
  magnitude = np.linalg.norm(A)
  unit_vector = A / magnitude
  print("\nUnit vector = ", unit_vector)
  
  print("\nDirection cosines:")
  print("cos(alpha) = ", unit_vector[0])
  print("cos(beta)  = ", unit_vector[1])
  print("cos(gamma) = ", unit_vector[2])
  
  angles_rad = np.arccos(unit_vector)
  angles_deg = np.degrees(angles_rad)
  
  print("\nDirection angles (in degrees):")
  print(f"  alpha = {angles_deg[0]}°")
  print(f"  beta  = {angles_deg[1]}°")
  print(f"  gamma = {angles_deg[2]}°")
