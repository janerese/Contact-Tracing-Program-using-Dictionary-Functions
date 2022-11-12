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
    print("*" * 38)
    print("\tContact Tracing Program")
    print("\n" + "*"* 15 + "  MENU  " + "*" * 15)
    print("1 -> Add an item")
    print("2 -> Search")
    print("3 -> Exit program [Y/N]")


# Allows user input to select item in the menu

while True:
    print_menu()

    try:
        user_input = int(input("What do you want to do: "))
    except ValueError:
        print("Invalid choice.")
    else:
        if user_input == 1:
            contact_key = input("Please enter your full name to be used as data file name: ")
            print("Please complete this form to provide us with the esential information that will aid in contact tracing.")
            full_name = input("Full Name: ")
            gender = input("Gender [Male/Female/Other]: ")
            age = int(input("Age: "))
            address = input("Address: ")
            email = input("Email Address: ")
            phone_number = int(input("Phone Number: "))
            temperature = float(input("Temperature: "))
            vax_status = input("COVID-19 Vaccination Status [Not Yet/1st Dose/2nd Dose]: ")
            covid_status = input("COVID-19 Status in the last 14 days[Positive/Negative]: ")
            comorbidities = input("Existing comorbidities, or other health risks: ")

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

            print(f"{contact_key}'s contact tracing information has been saved. Thank you for completing the form.")

        elif user_input == 2:
            contact_name = input("Enter the Contact's full name: ")
            
            print(f"{contact_name}'s contact tracing information has been accessed.")
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


        elif user_input == 3:
            exit_program = input("Exit the program [Y/N]: ").lower()
            if exit_program == "y":
                print("Thank you for using this Contact-Tracing Program! ")
                break
            elif exit_program == "n":
                print("Program will continue")
                continue
            else:
                print("Invalid choice.")
                continue

            