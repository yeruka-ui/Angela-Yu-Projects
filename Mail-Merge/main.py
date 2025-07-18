#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as guests:
    guest_list = [name.strip() for name in guests.readlines()]

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    invitation_lines = letter.readlines()
    invitation = "".join(invitation_lines) #Returns List as String

for name in guest_list:
    """Loop to create an individual letter per person. Also replaces the name for each letter to the respective person"""
    individual_letters = invitation.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(individual_letters)

