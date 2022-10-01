def main():
    full_name = get_full_name()
    password = get_password()
    email_address = get_valid_email_address()
    phone_number = get_valid_phone_number()
    print()
    first_name = get_first_name(full_name)
    print("Hi " + first_name + ", thanks for creating account.")

def get_full_name():
    while True:
        name = input("Enter full name:      ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")

def get_password():
    while True:
        password = input("Enter password:       ").strip()
        digit = False
        cap_letter = False
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
            "with at least one digit and one uppercase letter.")
        else:
            return password

def get_valid_email_address():
    while True:
        email = input("Enter email address:         ").strip()
        at_index = email.find("@")
        dot_index = email.find(".", at_index)
        if at_index == -1 or dot_index == -1:
            print("Please enter a valid email address.")
        else:
            return email

def get_valid_phone_number():
    while True:
        phone = input("Enter phone number:      ").strip()
        for char in " -().":
            phone = phone.replace(char, "")
        if len(phone) != 10 or phone.isdigit() == False:
            print("Please enter 10-digit phone number.")
        else:
            return phone

def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

if __name__ == "__main__":
    main()