# Author Name: Deziallia Morris
# Purpose: To implement the Flu vs. Allergies vs. COVID-19 Diagnostic Test

# Message variables for final results to make code easier to read
welcomeMessage = "\nHello! Welcome to the Flu vs. Allergies vs. COVID-19 Diagnostic Test!\n"

covid_message = "\nYou MAY have COVID-19\n"\
                "\nOther symptoms include:\n"\
                "Cough\nFatigue\nWeakness\nExhaustion"

flu_message = "\nYou MAY have the flu\n"\
              "\nOther symptoms include:\n"\
              "Cough\nFatigue\nWeakness\nExhaustion"

cold_message = "\nYou MAY have the common cold\n"\
               "\nOther symptoms include:\n"\
               "Sneezing\nRunny Nose\nMild chest discomfort"

allergies_message = "\nYou MAY have allergies\n"\
                    "\nOther symptoms include:\n"\
                    "Sneezing\nRunny Nose"

error_message = "\nInvalid input entered, program ended."


# A simple welcome message to welcome the user
print(welcomeMessage)

# Prompts and gathers user input and converts it to lower case
userInput = input("Do you have a fever?\n>> ").lower()

# Compares user's input to determine which statement to take
if userInput == 'yes':

    # Prompts and gathers user input and converts it to lower case
    userInput = input("Are you experiencing shortness of breath?\n>> ").lower()

    # Depending on the user input, this displays the final output
    if userInput == 'yes':
        print(covid_message)

    # Depending on the user input, this displays the final output
    elif userInput == 'no':
        print(flu_message)

    # If invalid input is detected, the program displays a message and ends
    else:
        print(error_message)

# Compares user's input to determine which statement to take
elif userInput == 'no':

    # Prompts and gathers user input and converts it to lower case
    userInput = input("Do you have itchy eyes?\n>> ").lower()

    # Depending on the user input, this displays the final output
    if userInput == 'yes':
        print(allergies_message)

    # Depending on the user input, this displays the final output
    elif userInput == 'no':
        print(cold_message)

    # If invalid input is detected, the program displays a message and ends
    else:
        print(error_message)

# If invalid input is detected, the program displays a message and ends
else:
    print(error_message)