import numpy as np
print("Welcome to the Ultimate Constant Angular Acceleration")
print("What variable are you missing?")
print("1 for angular velocity (w), 2 for initial angular velocity (w0), ")
print("3 for angular acceleration (a), 4 for time (t), 5 for position (p)")
var = int(input("Missing: "))

w = w0 = a = t = p = None
#Calculating angular velocity
if var == 1:
  print("\nWhat are your known variables? ")
  print("Options are: 1 for w0 a t, 2 for w0 a p, 3 for p w0 t, 4 for p t a ")
  av = int(input("Available: "))
  
  if av == 1:
    w0 = float(input("\nAngular velocity (w0) in rad/s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: "))
    t = float(input("Time (t) in s: "))
    w = w0 + a*t
 
  elif av == 2:
    w0 = float(input("\nInitial angular velocity (w0) in rad/s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: "))
    p_deg = float(input("Position (p) in degrees: "))
    p = np.radians(p_deg)
    rz = (w0**2 + 2*a*p)
    if rz < 0:
      print("\nInvalid input")
    else:
      w = np.sqrt(rz)
  elif av == 3:
    p_deg = float(input("\nPosition (p) in degrees: "))
    w0 = float(input("Initial angular velocity (w0) in rad/s: "))
    t = float(input("Time (t) in s: "))
    p = np.radians(p_deg)
    if t == 0:
      print("\nInvalid input")
    else:
      w = 2*p/t - w0
 
  elif av == 4:
    p_deg = float(input("\nPosition (p) in degrees: "))
    a = float(input("Angular acceleration (a) in rad/s^2: "))
    t = float(input("time (t) in s: "))
    p = np.radians(p_deg)
    if t == 0:
      print("\nInvalid input")
    else:
      w = p/t + a*t*.5
 
  else:
      print("\nInvalid input")
  if w is not None:
    print(f"Angular velocity is {w} rad/s")

#Calculating initial angular velocity
elif var == 2:
  print("\nWhat are your known variables? ")
  print("Options are: 1 for w a t, 2 for w a p, 3 for p t a, 4 for p w t ")
  av = int(input("Available: "))

  if av == 1:
    w = float(input("\nAngular velocity (w) in rad/s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: "))
    t = float(input("Time (t) in s: "))
    w0 = w - a*t

  elif av ==2:
    w = float(input("\nAngular velocity (w) in rad/s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: "))
    p_deg = float(input("Position (p) in degrees: "))
    p = np.radians(p_deg)
    rz = (w**2 - 2*a*p)
    if rz < 0:
      print("\nInvalid input")
    else:
      w0 = np.sqrt(rz)
  elif av == 3:
    p_deg = float(input("\nPosition (p) in degrees: "))
    t = float(input("Time (t) in s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: "))
    p = np.radians(p_deg)
    if t == 0:
      print("\nInvalid input")
    else:
      w0 = p/t - a*t*.5

  elif av == 4:
    p_deg = float(input("\nPosition (p) in degrees: "))
    w = float(input("Angular velocity (w) in rad/s: "))
    t = float(input("Time (t) in s: "))
    p = np.radians(p_deg)
    if t == 0:
      print("\nInvalid input")
    else:
      w0 = 2*p/t - w

  else:
    print("\nInvalid input")
  if w0 is not None:
    print(f"Initial angular velocity is {w0} rad/s")

#Calculating angular acceleration
elif var == 3:
  print("\nWhat are your known variables? ")
  print("Options are: 1 for w0 w t, 2 for w0 w p, 3 for p w0 t, 4 for p w t ")
  av = int(input("Available: "))

  if av == 1:
    w0 = float(input("\nInitial angular velocity (w0) in rad/s: "))
    w = float(input("Angular velocity (w) in rad/s: "))
    t = float(input("Time (t) in s: "))
    if t == 0:
      print("\nInvalid input")
    else:
      a = (w - w0)/t

  elif av == 2:
    w0 = float(input("\nInitial angular velocity (w0) in rad/s: "))
    w = float(input("Angular velocity (w) in rad/s: "))
    p_deg = float(input("Position (p) in degrees: "))
    p = np.radians(p_deg)
    if p == 0:
      print("\nInvalid input")
    else:
      a = (w**2 - w0**2)/(2*p)

  elif av == 3:
    p_deg = float(input("\nPosition (p) in degrees: "))
    w0 = float(input("Initial angular velocity (w0) in rad/s: "))
    t = float(input("Time (t) in s: "))
    p = np.radians(p_deg)
    if t == 0:
      print("\nInvalid input")
    else:
      a = (2*(p-w0*t)/t**2)

  elif av == 4:
    p_deg = float(input("\nPosition (p) in degrees: "))
    w = float(input("Angular velocity (w) in rad/s: "))
    t = float(input("Time (t) in s: "))
    p = np.radians(p_deg)
    if t == 0:
      print("\nInvalid input")
    else:
      a = (2*(w*t-p))/t**2

  else:
    print("\nInvalid input")
  if a is not None:
    print(f"Angular acceleration is {a} rad/s^2")
  
#Calculating time
elif var == 4:
  print("\nWhat are your known variables? ")
  print("Options are: 1 for w a w0, 2 for w p w0, 3 for w0 a p, 4 for w a p ")
  av = int(input("Available: "))

  if av == 1:
    w = float(input("\nAngular velocity (w) in rad/s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: "))
    w0 = float(input("Initial angular velocity (w0) in rad/s: "))
    if a == 0:
      print("\nInvalid input")
    else:
      t = (w - w0)/a
  
  elif av == 2:
    w = float(input("\nAngular velocity (w) in rad/s: "))
    p_deg = float(input("Position (p) in degrees: "))
    w0 = float(input("Initial angular velocity (w0) in rad/s: "))
    div = w + w0
    if div == 0:
      print("\nInvalid input")
    else:
      p = np.radians(p_deg)
      t = 2*p/(w0+w)
  
  elif av == 3:
    w0 = float(input("\nInitial angular velocity (w0) in rad/s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: "))
    p_deg = float(input("Position (p) in degrees: ")) 
    p = np.radians(p_deg)
    if a == 0:
      print("\nInvalid input")
    else:
      rz = (w0**2 + 2*a*p)
      if rz < 0:
        print("\nInvalid input")
      else:
        t1 = (-w0+np.sqrt(rz))/a
        t2 = (-w0-np.sqrt(rz))/a
        if t1 > 0:
          t = t1
        elif t2 > 0:
          t = t2
        else:
          print("\nInvalid input (Time is in the past)")
  
  elif av == 4:
    w = float(input("\nAngular velocity (w) in rad/s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: "))
    p_deg = float(input("Position (p) in degrees: ")) 
    p = np.radians(p_deg)
    if a == 0:
      print("\nInvalid input")
    else:
      rz = (w**2 - 2*a*p)
      if rz < 0:
        print("\nInvalid input")
      else:
        t1 = (w+np.sqrt(rz))/a
        t2 = (w-np.sqrt(rz))/a
        if t1 > 0:
          t = t1
        elif t2 > 0:
          t = t2
        else:
          print("\nInvalid input (Time is in the past)")
  
  if t is not None:
    print(f"Time is {t} s")
  else:
    print("\nInvalid input")

#Calculating position
elif var == 5:
  print("\nWhat are your known variables? ")
  print("Options are: 1 for w t a, 2 for w w0 a, 3 for w0 w t, 4 for w0 t a ")
  av = int(input("Available: "))
  
  if av == 1:
    w = float(input("\nAngular velocity (w) in rad/s: "))
    t = float(input("Time (t) in s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: ")) 
    p = w*t - .5*a*t**2
 
  elif av == 2:
    w = float(input("\nAngular velocity (w) in rad/s: "))
    w0 = float(input("Initial angular velocity (w0) in rad/s: "))
    a = float(input("Angular acceleration (a) in rad/s^2: ")) 
    if a == 0:
      print("Invalid input")
    else:
      p = (w**2 - w0**2)/(2*a)
 
  elif av == 3:
    w0 = float(input("\nInitial angular velocity (w0) in rad/s: "))
    w = float(input("Angular velocity (w) in rad/s: "))
    t = float(input("Time (t) in s: "))
    p = (w0 + w)*t/2
 
  elif av == 4:
    w0 = float(input("\nInitial angular velocity (w0) in rads: "))
    t = float(input("Time (t) in s: "))
    a = float(input("Angular acceleration (a) in rad/s^2"))
    p = w0*t + .5*a*t**2
 
  if p is not None:
    p_deg = np.degrees(p)  
    print(f"Position is {p_deg}°")
  else:
    print("\nInvalid input")
