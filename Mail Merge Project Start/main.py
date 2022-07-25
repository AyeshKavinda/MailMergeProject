#Day-24 #100DaysOfCode Python Task:
# Our Teacher: @Yu_Angela
# Completed by @ProgrammerEsh

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

NAME_HOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_text:
    name_list = names_text.readlines()

    # print(name_list)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_in = letter_file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_in.replace(NAME_HOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as output_letter:
            output_letter.write(new_letter)

        #When you run It will create whole bunch of text files with each name inside each letter.





