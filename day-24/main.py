

# READ #with open("my_file.txt", mode="r" #reading is default) as file:
 #   contents = file.read()
  #  print(contents)

#WRITE 
with open("second_file.txt", mode="w") as file:
    file.write("mustache")

#a is like list.append()
#w mode actually creates a separate text file from scratch
# with "with" as variable  no need of closing the file like file.close() for file = open("my_file.txt")
# with will do that automatically


