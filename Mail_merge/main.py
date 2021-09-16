#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


starting_letter = open("./Input/Letters/starting_letter.txt")
# x = "".join(f.readlines())
letter = starting_letter.read()
invited_names = open("./Input/Names/invited_names.txt")
names = "".join(invited_names.readlines())

for name in names.split():
    replaced_name = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(replaced_name)
