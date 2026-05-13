with open("./Input/Names/invited_names.txt", mode="r") as names:
    invited_names = names.readlines()
for each_name in invited_names:
    each_name = each_name.strip()
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        new_letter = letter.read()
        new_letter = new_letter.replace("[name]" , each_name)
    with open(f"./Output/ReadyToSend/{each_name}.txt", mode="w") as txt:
        txt.write(new_letter)

















#TODO: Create a letter using starting_letter
#with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
  # new_letter = letter.readlines()
#txt.replace([name], "new_name")

#new_letter.replace([name], "new_name")
#with open("./Input/Names/invited_names.txt", mode="r") as names:
 #   invited_names = names.readlines()

#txt = invited_names.replace([name], each_name)

#for each_name in invited_names:
#    each_name.txt
#for new_name in invited_names:
 #   txt.replace("[name]", "new_name")


# with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
 #       invited_names.new_name

#with open(f"./Output/ReadyToSend/{each_name}.txt", mode="w") as txt:
#    txt.write(new_letter)


#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
