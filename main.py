# -*- coding: utf-8 -*-
from tabulate import tabulate
from utils import *
from model import create_tables
from view import General, Menu, Menu_Admin

from controller import Controller



def Main():
    current_user = Login()

    Clear()

    if(current_user.is_admin):
        Menu_Admin_Controller()
    else:
        Menu_Controller()



def Menu_Controller():
    opc  = -1
    subOpc = -1
    while(opc != 0):
        Clear()
        opc =  Menu.Main_menu()


   
def Menu_Admin_Controller():

    opc  = -1
    subOpc = -1
    while(opc != 0):
        Clear()
        opc = Menu_Admin.Main_menu()
        

        if(opc == 1):
            
            while subOpc !=0:
                Clear()
                subOpc = Menu_Admin.User_menu()
                if(subOpc ==1):
                   #crir
                    Clear()
                    name, user_name, password = Menu_Admin.Create_user_menu()
                    Controller.create_user(name, user_name, password )

                elif(subOpc == 2):
                    Clear()
                    #editar

                elif(subOpc == 3):
                    #listar
                    Clear()
                    Menu_Admin.List_user_menu(Controller.get_all_users())

                elif(subOpc == 4):
                    #deletar
                    Clear()
                    id = Menu_Admin.Delete_user_menu()
                    result = Controller.delete_user(id)
                    print("Usuario deletado" if result == 1 else "Erro ao deletar!")                   
                    input("\nAperte Enter para sair!")
                    
                elif(subOpc == 0):
                    Clear()                    
                    print("Saindo")
                else:
                    Error()



        elif (opc == 2):
            
            while subOpc !=0:
                Clear()
                subOpc = Menu_Admin.Car_menu()
                if(subOpc ==1):
                   #crir
                    Clear()
                    name, manufacturer, price_per_hour = Menu_Admin.Create_car_menu()
                    Controller.create_car(name, manufacturer, price_per_hour )

                elif(subOpc == 2):
                    Clear()
                    #editar
                    
                elif(subOpc == 3):
                    #listar
                    Clear()
                    Menu_Admin.List_car_menu(Controller.get_all_cars())

                elif(subOpc == 4):
                    #deletar
                    Clear()
                    id = Menu_Admin.Delete_car_menu()
                    result = Controller.delete_car(id)
                    print("Carro deletado" if result == 1 else "Erro ao deletar!")                   
                    input("\nAperte Enter para sair!")
                    
                elif(subOpc == 0):
                    Clear()                    
                    print("Saindo")
                else:
                    Error()
        elif(opc == 3):
            
            while subOpc !=0:
                Clear()
                subOpc = Menu_Admin.Color_menu_menu()
                if(subOpc ==1):
                   #crir
                    Clear()
                    name,hex  = Menu_Admin.Create_color_menu()
                    Controller.create_color(name, hex)

                elif(subOpc == 2):
                    Clear()
                    #editar
                    
                elif(subOpc == 3):
                    #listar
                    Clear()
                    Menu_Admin.List_color_menu(Controller.get_all_colors())

                elif(subOpc == 4):
                    #deletar
                    Clear()
                    id = Menu_Admin.Delete_color_menu()
                    result = Controller.delete_color(id)
                    print("Cor deletado" if result == 1 else "Erro ao deletar!")                   
                    input("\nAperte Enter para sair!")
                    
                elif(subOpc == 0):
                    Clear()                    
                    print("Saindo")
                else:
                    Error()
        elif(opc == 4):
            Clear()
            #Export
            Controller.export_to_json()
        elif(opc == 5):
            Clear()
            #Import
            while subOpc !=0:
                subOpc = Menu_Admin.Import()

                if(subOpc == 1):                  
                    Clear()
                    print("---Importar arquivo---")
                    path = input("Digite o caminho do arquivo: ")
                    Controller.import_from_json(path)

                elif(subOpc == 2):
                    Clear()
                    print("---Importar URL---")
                    url = input("Digite o URL: ")
                    Controller.import_from_url(url)

                elif(subOpc == 0):
                    Clear()                    
                    print("Saindo")
                else:
                    Error()

        elif(opc == 0):
            Clear()
            print("Saindo")

        else:
            Error()



    

def Login():
    isLoginValid = False


    while isLoginValid == False:
        Clear()
        user_name, password = General.Login()

        user = Controller.login_user(user_name,password)
       

        if user == None:
            input("Senha ou Login Invalido!")
        else:
            isLoginValid = True
        

    return user
        






    


 






if __name__ == "__main__":
   ## Main()
   Controller.import_from_json()