# Programmed by Erika Jane T. Reyes
# Python program for contact tracing using dictionary functions

# Declare a variable that stores an empty dictionary
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

contacts_dictionary = {
}

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

# Allows user input to select item in the menu
while True:
    print_menu()

    try:
        user_input = int(input("\n\t\t\tWhat do you want to do: "))
        print()
        print("*" * 68)

    except ValueError:
        print("\n\t\t\tInvalid choice.\n")
    else:
        # Allows the user to add item to  contacts dictionary
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
            covid_status = input("COVID-19 Status in the last 14 days[Positive/Negative]: ")
            comorbidities = input("Existing comorbidities, or other health risks: ")
            print()
            print("*" * 68)


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

print("\n\nCONTACTS DICTIONARY:\n")
print(*[str(key) + ':' + str(values) for key,values in contacts_dictionary.items()], sep='\n\n')
print("\n")
