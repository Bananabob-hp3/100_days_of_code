height = float(input("Height: "))
weight = float(input("Weight: "))

bmi = weight / height ** height
print(bmi)

if height > 3:
    raise ValueError("Humans are not above 3 meters")



#Traceback (most recent call last):
 # File "/home/tarun/mycode/day-30/practice2.py", line 8, in <module>
 #   raise ValueError("Humans are not above 3 meters")
#ValueError: Humans are not above 3 meters
#tarun@tarun:~/mycode/day-30

