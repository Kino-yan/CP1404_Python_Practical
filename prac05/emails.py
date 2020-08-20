name_list=[]
email_list=[]
email=input("Please enter the email: ")
while email !="":
    name_email=email.split("@")
    if "." in name_email[0]:
        full_name = name_email[0]
        dis_full_name=name_email[0].split(".")
        option = input("Is your name {} {:2}? (Y/n)".format(dis_full_name[0], dis_full_name[1])).lower()
    else:
        full_name=name_email[0]
        option = input("Is your name {}? (Y/n)".format(full_name)).lower()

    if option=="y" or option=="yes":
        full_name=full_name
    elif option=="n" or option=="no":
        name_email=input("Name: ")
        full_name = name_email
    else:
        print("Invalid option.")
    name_list.append(full_name)
    email_list.append(email)
    email = input("Please enter the email: ")

for i in range(len(name_list)):
    print(name_list[i], end="")
    print("(", email_list[i], ")")


