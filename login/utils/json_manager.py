from os.path import dirname, realpath, join
from os import system
from utils.lib import JsonManager
from getpass import getpass
from time import sleep as slp


class Login(JsonManager):

    def __init__(self):
        self.root= dirname(realpath(__file__))
        self.path_data = join(self.root, '../data/data.json')

    def home(self, data):

        opc = '0'

        slp(5)

        while opc != '2':
            system('cls')
            print("==================MENU==================")
            print("    1 - Alterar Login       2 - Sair    ")
            opc = input(">_ ")

            if opc == '1':
                self.update_login(data)
            elif opc == '2':
                break
            else:
                print("Option invalid!")

            slp(5)

    def sign_in(self):
        #data = JsonManager().read_json(realpath(__file__))
        print("######### Sign In #########")
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")
        password_verify = getpass("Repeat your password")

        while password != password_verify:
            print("Password do no match!")
            password_verify = getpass("Repeat your password")

        JsonManager().create_json(self.path_data, username, password_verify)
        print("Registration done!")

    def loggin_in(self, data):
        print("######### Loggin In #########")
        username = input("Enter your username: ")

        while username != data['username']:
            print("Username invalid!")
            username = input("Enter your username: ")

        password = getpass("Enter your password: ")

        if password != data['password']:
            print("Password invalid!")
        else:
            print("Login success")
            self.home(data)

    def update_login(self, data):
        print("######### Loggin In #########")
        username = input("Enter new your username: ")
        password_old = getpass("Enter your old password: ")

        while password_old != data['password']:
            print("Old password invalid!")
            password_old = getpass("Enter your old password: ")

        password_new = getpass("Enter  your new password: ")
        password_ner_verify = getpass("Repeat new password: ")

        while password_new != password_ner_verify:
            print("New password do not match.")
            password_ner_verify = getpass("Repeat new password: ")

        data['username'] = username
        data['password'] = password_ner_verify

        JsonManager().update_json(self.path_data, data)
        print("Updata success!")

    def main(self):
        data = JsonManager().read_json(self.path_data)
        if data:
            self.loggin_in(data)
        else:
            self.sign_in()

if __name__ == '__main__':
    lgn = Login()
    lgn.main()