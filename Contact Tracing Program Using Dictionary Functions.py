# Programmed by Erika Jane T. Reyes
# Python program for contact tracing using dictionary functions

# Declare a variable that stores an empty dictionary
initial_dictionary = {
    "Reika Yamazaki": {
        "Full Name": "Reika Yamazaki",
        "Gender": "Female",
        "Sex": "Female",
        "Address": "Amaya, Tanza Cavite",
        "Email Address": "reiyamazakifg@gmail.com",
        "Phone Number": "09999999999",
        "Temperature": 36.5,
        "Vaccination Status": "2nd dose",
        "COVID Status": "Negative",
        "Comorbidities": "None"
    }
}

contacts_dictionary = {
    "Contact": {}
}

initial_dictionary.update(contacts_dictionary)

loop = True

# Display a menu of options
def print_menu():
    print("*" * 38)
    print("\tContact Tracing Program")
    print("\n" + "*"* 15 + "  MENU  " + "*" * 15)
    print("1 -> Add an item")
    print("2 -> Search")
    print("3 -> Exit program [Y/N]")

    # Allows user input to select item in the menu
while loop:
    print_menu()

    try:
        user_input = int(input("What do you want to do: "))

    except ValueError:
        print("Invalid choice.")
    else:
        if user_input == 1:
            print("Please complete this form to provide us with the esential information that will aid in contact tracing.")
            contacts_dictionary["Contact"]["Full Name"] = input("Full Name: ")
            contacts_dictionary["Contact"]["Gender"] = input("Gender [Male/Female/Other]: ")
            contacts_dictionary["Contact"]["Age"] = int(input("Age: "))
            contacts_dictionary["Contact"]["Address"] = input("Address: ")
            contacts_dictionary["Contact"]["Email Address"]= input("Email Address: ")
            contacts_dictionary["Contact"]["Phone Number"] = int(input("Phone Number: "))
            contacts_dictionary["Contact"]["Temperature"] = float(input("Temperature: "))
            contacts_dictionary["Contact"]["Vaccination Status"] = input("Vaccination Status [Not Yet/1st Dose/2nd Dose]: ")
            contacts_dictionary["Contact"]["COVID Status"] = input("COVID Status in the last 14 days: ")
            contacts_dictionary["Contact"]["Comorbidities"] = input("Existing comorbidities, or other health risks: ")

            for contact, information in contacts_dictionary["Contact"].items():
                print(f"{contact}: {information}")





            
