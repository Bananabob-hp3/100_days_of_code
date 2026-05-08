import random
letters = [chr(i) for i in range(97 , 123)] 
numbers = [chr(i) for i in range(49 , 58)]
symbols = [chr(i) for i in range(33 , 48)]
nr_letters = int(input("how many letters would you ike in your password?\n"))

#easy evel
#password = ""
# nr_letters = 4

#for char in range (0 , nr_letters):
    #random_char = random.choice(letters)
    #print(random_char)
    #password += random_char
    #print(password)
 #  password  += random.choice(letters)
 #  print(password)
#same for numbers

#numbers = [chr(i) for i in 
#range(49 , 58)]
#same for symbols

##symbols = [chr(i) for i in range(33 , 48)]
#print(password)symbols = [chr(i) for i in range(33 , 48)]






#hard level
#password = ""
password_list = []
password = ""
# nr_letters = 4
#password_list.append(random.choice(password_list))
for char in range(0 , nr_letters):
    #random_char = random.choice(letters)
    #print(random_char)
    #password += random_char
    #print(password)
    #password  += random.choice(letters)
    #print(password)
    password_list.append(random.choice(letters))
    #password_list.append(random.choice(password))    
random.shuffle(password)
for char in password_list:
    password += char
print(f"your password is:  {password}")
