#PRACTICING ERRORS AND CATCHING THE EXCEPTIONS

#try:
#   file = open("a_file.txt")
#except:
#   file = open("a_file.txt", "w")
#    file.write("Something")

try:
    file = open("a new_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["tutyt"])
except FileNotFoundError:
    file = open("a new_file.txt", "w")
    file.write("Something New")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    contents = file.read()
    print(contents)
#finally:
#    file.close()
#    print("File was closed")
finally:
    raise TypeError("This is an error i made up")

