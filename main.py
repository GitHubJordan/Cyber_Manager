import PySimpleGUI as sg
import os
from time import sleep as slp
from time import localtime
import time
from pygame import mixer

import pygame

from os.path import dirname, realpath, join
from login.utils.lib import JsonManager
from getpass import getpass


#definindo o tema do programa
#command for view color themes "sg.list_of_look_and_feel_values()"

Themes = [
sg.theme("DarkBlue"),
sg.theme("DarkBlue1"),
sg.theme("DarkBlue2"),
sg.theme("DarkBlue3"),
sg.theme("LightBlue"),
sg.theme("LightBlue1"),
sg.theme("LightBlue2"),
sg.theme("DarkGrey")
]
sg.theme(Themes[7])


#Definindo o caminho dos comandos
vBloquearPC = "rundll32.exe user32.dll,LockWorkStation"
vAtivarInternet = "wmic path win32_networkadapter where index=1 call enable"
vBloquearInternet = "wmic path win32_networkadapter where index=1 call disable"
vDesligarPC = "shutdown /s /t 10"

intro_demo = "img\\CyberManager-intro_demo.gif"

#função principal do programa
class  TelaCM:
    def __init__(self):

        #Layout
        menu_def = [
            ['&File', ['&Conta', ['!A&lterar dados do usuário', '&Terminar sessão'], '&Ativar Internet', 'E&xit', ]],
            ['&Help', 'A&bout...']
        ]

        layout = [
            [
                [sg.Menu(menu_def)]
            ],
            [
                [sg.Text("CYBER MANAGER", size=(22,0), justification='center', font=('Helvetica', 14), relief=sg.RELIEF_RIDGE)],
                [sg.Text("==============================")]
            ],
            [
                [sg.Text("Tempo de uso da máquina"), sg.Input(key='tUMaquina', size=(7, 1))],
                [sg.Text("Tempo Inicial", size=(19,1)), sg.Text("00:00:00", key='tInicial',size=(7,1))],
                [sg.Text("Tempo Final", size=(19,1)), sg.Text("00:00:00", key='tFinal',size=(7,1))]
            ],
            [
                [sg.Text("Comando/Operacão", size=(19,1))],
                [
                    sg.Checkbox("Bloquear O PC", key='bloquearPC'),
                    sg.Checkbox("Desligar Internet", key='desligarInternet')
                 ],
                [sg.Checkbox("Desligar O PC", key='desligarPC')]
            ],
            [
                [sg.Cancel("Sair",size=(7,1), button_color = "red", key='btnSair'),
                 sg.Text(size=(10,1)), sg.Button("Start", size=(7,0), key='btnStart')]
            ]
        ]

        #Windows
        self.telas = sg.Window("Cyber Manager", icon='img\\6103903.ico').layout(layout)



        layout2 = [
            [sg.Text("A Internet foi desliga, introdusa o código de segurança para a tivar e ter o acesso a internet novamente", size=(27,3), key='co')],
            [
                [sg.Input(key='senhaAtivaInternet', size=(27,0), password_char='*')],
                [sg.Text(size=(7,0)), sg.Button("Ativar", size=(7,0), key='btn_Ativar')]
            ]
        ]

        self.telas2 = sg.Window("Ativar Internet", icon='img\\Cyber-Security.ico').layout(layout2)

    def Iniciar(self):
        self.tmp = time.localtime()
        #Extraindo os dados da Tela
        while True:
            self.eventos, self.value = self.telas.read(timeout=100)

            if self.eventos == sg.WINDOW_CLOSED or self.eventos == 'Exit' or self.eventos == 'Terminar sessão' or self.eventos == 'btnSair':
                break

            if self.eventos == 'Alterar dados do usuário':

                pass

            if self.eventos == 'About...':
                sg.PopupQuickMessage("CyberManager\nVersion: 0.1\nBy: Jordan Adelino\nJAMy COMPANY©", auto_close_duration=5, background_color='dark blue')

            if self.eventos == 'Ativar Internet':
                self.telas.Hide()
                self.eventos2, self.valores2 = self.telas2.read()
                if self.eventos2 == sg.WINDOW_CLOSED:
                    if self.telas.UnHide() == False:
                        self.telas.UnHide()
                        return True

                self.telas2.UnHide()
                if self.telas2.UnHide() == True:

                    self.telas2.UnHide()

                    if self.eventos2 == 'btn_Ativar':
                        if self.valores2['senhaAtivaInternet'] == 'admin_2':
                            os.system(vAtivarInternet)
                            sg.PopupQuickMessage("A Internet foi restablecida", background_color='blue')
                            slp(2)
                            self.telas2.Hide()
                            if self.telas.UnHide() == False:
                                self.telas.UnHide()
                                return True

                            else:
                                sg.PopupQuickMessage("A senha de segurança inválida", background_color='red')
                                slp(2)
                                self.telas2.UnHide()

                if self.telas.UnHide() == False:
                    self.telas.UnHide()
                    return True


            if self.eventos == 'btnStart':

                self.telas['tInicial'].update(time.strftime('%H:%M:%S'))

                self.telas.Hide()

                tinicial = int(self.value['tUMaquina'])

                M = tinicial

                x = time.localtime()
                tempo = x[4]
                afterTime = tempo + M

                while 1:
                    #print(afterTime)
                    #print(localtime().tm_min)
                    if int(afterTime) > 59:
                        afterTime = 0 + afterTime % 60
                    if localtime().tm_min == int(afterTime):
                        mixer.init()
                        mixer.music.load("utils/som_tempo.mp3")
                        mixer.music.play()
                        slp(5)
                        break

                if self.value['bloquearPC'] == True:
                    os.system(vBloquearPC)
                #    print("Bloquear o PC")

                if self.value['desligarInternet'] == True:
                    os.system(vBloquearInternet)
                #    print("Desligar Internet")

                if self.value['desligarPC'] == True:
                    os.system(vDesligarPC)
                #    print("Desligar o PC")

                if self.value['desligarInternet'] == True:

                    self.eventos2, self.valores2 = self.telas2.read()
                    if self.eventos2 == sg.WINDOW_CLOSED:
                        if self.telas.UnHide() == False:
                            self.telas.UnHide()
                            return True

                    if self.eventos2 == 'btn_Ativar':
                        if self.valores2['senhaAtivaInternet'] == 'admin_2':
                            os.system(vAtivarInternet)
                            self.telas2.Hide()
                            slp(1)
                            sg.PopupQuickMessage("A Internet foi restablecida", background_color='blue')
                            slp(2)
                            if self.telas.UnHide() == False:
                                self.telas.UnHide()
                                return True
                        else:
                            sg.PopupQuickMessage("A senha de segurança inválida", background_color='red')
                            #self.telas2.UnHide()
                            slp(2)
                            os.system(vBloquearPC)
                            break
                else:
                    if self.telas.UnHide() == False:
                        self.telas.UnHide()
                        return True
                                
                self.telas['tFinal'].update(time.strftime('%H:%M:%S'))


class Login(JsonManager):

    def __init__(self):
        self.root = dirname(realpath(__file__))
        self.path_data = join(self.root, 'login/data/data.json')

        layout = [
            [
                [sg.Text("Username", size=(10, 0)), sg.Input(key='username', size=(12, 2))],
                [sg.Text("Password", size=(10, 0)), sg.Input(key='password', password_char='*', size=(12, 2))]
            ],
            [
                sg.Text("", size=(15, 1)),
                sg.Button("Login", key='btn_Login')
            ]
        ]

        self.telaLogin = sg.Window("Login", icon='img\\cyber-security-icon1.ico').layout(layout)

        layout2 = [
            [
                [sg.Text("Username"), sg.Input(key='username', size=(12, 2))],
                [sg.Text("Password"), sg.Input(key='password', password_char='*', size=(12, 2))],
                [sg.Text("Password verify"), sg.Input(key='password_verify', password_char='*', size=(12, 2))]

            ],
            [
                sg.Text("", size=(15, 1)),
                sg.Button("Sign In", key='btn_Sign')
            ]
        ]

        self.telaSign = sg.Window("Sign In", icon='img\\cyber-security-2303512-1951575.ico').layout(layout2)

        layout3 = [
            [
                [sg.Text("Enter your new username"), sg.Input(key='new_username', size=(10,1))],
                [sg.Text("Enetr your old password"), sg.Input(key='old_password', password_char='*', size=(10,1))],
                [sg.Text("Enter your new password"), sg.Input(key='new_password', password_char='*', size=(10,1))],
                [sg.Text("Repeat new password"), sg.Input(key='new_password_verify', password_char='*', size=(10,1))]
            ],
            [
                [sg.Button("Cancel", key='btn_cancel'), sg.Button("Confirm", key='btn_confirm')]
            ]
        ]

        self.telaUpdata = sg.Window("Updata", icon='img\\cyber-security-2303512-1951575.ico').layout(layout3)

    def home(self):
        self.tela = TelaCM()
        self.tela.Iniciar()


    def sign_in(self):
        # data = JsonManager().read_json(realpath(__file__))

        while True:

            self.eventos, self.valores = self.telaSign.read() 

            if self.eventos == sg.WINDOW_CLOSED:
                break

            if self.eventos == 'btn_Sign':

                if self.valores['password'] != self.valores['password_verify']:
                    sg.PopupQuickMessage("Password do not match!", background_color='red')

                else:
                    JsonManager().create_json(self.path_data, self.valores['username'], self.valores['password_verify'], "offline", "off")
                    sg.PopupQuickMessage("Registration done!", background_color='green')
                    self.telaSign.Hide()
                    self.main()
                    break

    def loggin_in(self, data):

        while True:
            if data['start'] == 'off':
                os.system(intro_demo)
            else:
                data['start'] == 'on'
                JsonManager().update_json(self.path_data, data)

            if data['status'] == 'offline':
                self.eventos, self.valores = self.telaLogin.read()

                if self.eventos == sg.WINDOW_CLOSED:
                    break

                if self.eventos == 'btn_Login':

                    if self.valores['username'] != data['username']:
                        sg.PopupQuickMessage("Username invalid!", background_color='red')

                    else:
                        if self.valores['password'] != data['password']:
                            sg.PopupQuickMessage("Password invalid!", background_color='red')
                        else:
                            data['status'] = 'online'
                            data['start'] = 'on'
                            JsonManager().update_json(self.path_data, data)
                            self.telaLogin.Hide()
                            self.home()
                            break
            else:
                data['status'] = 'online'
                JsonManager().update_json(self.path_data, data)
                self.home()
                break

    def login_off(self, data):
        if sg.PopupYesNo("Desejas Terminar a Sessão?", icon="img\\6103903.ico") == 'Yes':
            data['status'] = 'offline'
            JsonManager().update_json(self.path_data, data)

    def update_login(self, data):
        while True:
            self.eventos, self.valores = self.telaUpdata.read()

            if self.eventos == sg.WINDOW_CLOSED or self.eventos == 'btn_cancel':
                break

            if self.valores['old_password'] != data['password']:
                sg.PopupQuickMessage("Old password invalid!", background_color='red')
                password_old = self.valores['old_password']

            else:
                if self.valores['new_password'] != self.valores['new_password_verify']:
                    sg.PopupQuickMessage("New password do not match.", background_color='red')
                    password_ner_verify = self.valores['new_password_verify']

                else:

                    data['username'] = self.valores['username']
                    data['password'] = password_ner_verify

                    JsonManager().update_json(self.path_data, data)
                    sg.PopupQuickMessage("Updata success!", background_color='green')
                    slp(3)
                    break


    def main(self):
        data = JsonManager().read_json(self.path_data)
        if data:
            self.loggin_in(data)
            if data['status'] == 'online':
                self.login_off(data)
        else:
            self.sign_in()

#chamando as funçõe principais
lgn = Login()
lgn.main()
