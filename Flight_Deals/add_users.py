from data_manager import DataManager


data_manager = DataManager()
print("Welcome to Karan's Flight Club.")
print("We find the best flight deals and email you.")
fname = input("What is your first name?\n")
lname = input("What is your last name?\n")
email = input("What is your email?\n")
cemail = input("Type your email again.\n")
if email == cemail:
    data_manager.put_data_users(fname, lname, email)
    print("Success! Your email has been added. Look forwards to mailing you.")
else:
    print("Email doesn't match.")