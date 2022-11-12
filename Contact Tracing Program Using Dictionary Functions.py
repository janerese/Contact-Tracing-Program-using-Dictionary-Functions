# Programmed by Erika Jane T. Reyes
# Python program for contact tracing using dictionary functions

# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

initial_dictionary = {
    "Reika Yamazaki": {
        "Full Name": "Reika Yamazaki",
        "Gender": "Female",
        "Age": 19,
        "Sex": "Female",
        "Address": "Amaya, Tanza Cavite",
        "Email Address": "reiyamazakifg@gmail.com",
        "Phone Number": "09999999999",
        "Temperature": 36.5,
        "COVID-19 Vaccination Status": "2nd dose",
        "COVID-19 Status": "Negative",
        "Comorbidities": "None"
    }
}
# Declare a variable that stores an empty dictionary
contacts_dictionary = {
}

# Append initial dictionary to empty dictionary
contacts_dictionary.update(initial_dictionary)

# Display a menu of options
def print_menu():
    print("*" * 68)
    print("\n\t\t         CONTACT TRACING PROGRAM")
    print("\n" + "*"*30 + "  MENU  " + "*" * 30)
    print("\n\t\t\t1 -> Add an item")
    print("\t\t\t2 -> Search")
    print("\t\t\t3 -> Exit program [Y/N]\n")
    print("*" * 68)

while True:
    print_menu()

    try:
        # Allows user input to select item in the menu
        user_input = int(input("\n\t\tWhat do you want to do [1 / 2 / 3]: "))
        print()
        print("*" * 68)

    except ValueError:
        print("\n\t\t\tInvalid choice.\n")
    else:
        # Allows the user to add item to contacts dictionary
        if user_input == 1:
            contact_key = input("\n      Please enter your full name to be used as data file name: \n\t\t\t")
            print("\n\t    Please complete this form to provide us with the\n\tesential information that will aid in contact tracing.\n")
            print("*" * 68)
            full_name = input("\nFull Name: ")
            gender = input("Gender [Male/Female/Other]: ")
            age = int(input("Age: "))
            address = input("Address: ")
            email = input("Email Address: ")
            phone_number = int(input("Phone Number: "))
            temperature = float(input("Temperature: "))
            vax_status = input("COVID-19 Vaccination Status [Not Yet/1st Dose/2nd Dose]: ")
            covid_status = input("COVID-19 Status in the last 14 days [Positive/Negative]: ")
            comorbidities = input("Existing comorbidities, or other health risks: ")
            print()
            print("*" * 68)

            # Storing user input in the contacts dictionary
            contacts_dictionary[contact_key] = {
                "Full Name": full_name,
                "Gender": gender,
                "Age": age,
                "Address": address,
                "Email Address": email,
                "Phone Number": phone_number,
                "Temperature": temperature,
                "COVID-19 Vaccination Status": vax_status,
                "COVID-19 Status": covid_status,
                "Comorbidities": comorbidities
            }

            print(f"\n    {contact_key}'s contact tracing information has been saved.\n\t\tThank you for completing the form.\n")

        # Allows the user to search for item in the contacts dictionary
        elif user_input == 2:
            contact_name = input("\n\t\t    Enter the Contact's data file name: \n\t\t\t")
            print()
            print("*" * 68)
            print()
            print(f"\n{contact_name}'s contact tracing information has been found.")
            print()
            print("*" * 68)
            print()
            print("Full name:" , contacts_dictionary[contact_name]["Full Name"])
            print("Gender:" , contacts_dictionary[contact_name]["Gender"])
            print("Age:" , contacts_dictionary[contact_name]["Age"])
            print("Address:" , contacts_dictionary[contact_name]["Address"])
            print("Email Address:" , contacts_dictionary[contact_name]["Email Address"])
            print("Phone Number:" , contacts_dictionary[contact_name]["Phone Number"])
            print("Temperature:" , contacts_dictionary[contact_name]["Temperature"])
            print("COVID-19 Vaccination Status:" , contacts_dictionary[contact_name]["COVID-19 Vaccination Status"])
            print("COVID-19 Status:" , contacts_dictionary[contact_name]["COVID-19 Status"])
            print("Comorbidities:" , contacts_dictionary[contact_name]["Comorbidities"])
            print()

        # Allows the user to exit the program
        elif user_input == 3:
            exit_program = input("\n\t\t      Exit the program [Y/N]? ").lower()
            if exit_program == "y":
                print("\n\t\t     CLOSING PROGRAM...THANK YOU!")
                break
            elif exit_program == "n":
                print("\n\t\t\tPROGRAM WILL CONTINUE...\n")
                continue
            else:
                print("\n\t\t\tInvalid choice.\n")
                continue

# Prints contacts dictionary
print("\n\nCONTACTS DICTIONARY:\n")
print(*[str(key) + ':' + str(values) for key,values in contacts_dictionary.items()], sep='\n\n')
print("\n")
