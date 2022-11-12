# Programmed by Erika Jane T. Reyes
# Python program for contact tracing using dictionary functions

# Display a menu of options
def print_menu():
    print("*" * 38)
    print("\tContact Tracing Program")
    print("\n" + "*"* 15 + "  MENU  " + "*" * 15)
    print("1 -> Add an item")
    print("2 -> Search")
    print("3 -> Exit program [Y/N]")

print_menu()
# Allows user input to select item in the menu
try:
    user_input = int(input("What do you want to do: "))
# Perform the selected option
except ValueError:
    print("Invalid choice.")
else:
    if user_input == 1:
        full_name = input("Full name: ")
        gender = input("Gender [Male/Female/Other]: ")
        age = int(input("Age: "))
        address = input("Address: ")
        email_address = input("Email Address: ")
        phone_number = int(input("Phone number: "))
        vaccination_status = input("Vaccination Status [Not Yet/1st Dose/2nd Dose]: ")
        covid_status = input("Positive for COVID in the last 14 days [Y/N]: ")



