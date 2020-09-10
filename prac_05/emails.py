def main():
    email_and_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm = input("Is your name {}? (Y/n) ".format(name))
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_and_name[email] = name
        email = input("Email: ")
    for email, name in email_and_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    email_start = email.split('@')[0]
    email_start_split = email_start.split('.')
    name = " ".join(email_start_split).title()
    return name


main()
