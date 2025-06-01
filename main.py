# -*- coding: utf-8 -*-
from tabulate import tabulate
from utils import *
from model import Create_tables
from view import General, Menu, Menu_Admin

from controller import Controller



def Main():
    current_user = Login()

    Clear()

    if(current_user.is_admin):
        Menu_Admin_Controller()
    else:
        Menu_Controller(current_user)



def Menu_Controller(current_user):
    opc  = -1
    subOpc = -1
    while(opc != 0):
        Clear()
        opc =  Menu.Main_menu()
        if(opc == 1):
            Clear()
            plate, car_id, color_id = Menu.Register_Entry_Menu()

            result = Controller.Register_parking(plate, car_id, color_id, current_user.id)
            
            print("Veiculo Registrado" if result == 1 else "Erro ao Registrar!")   


        elif(opc == 2):
            Clear()
            id = Menu.Register_Departure_Menu()

            result, final_price,time_of_parking = Controller.Finish_parking(id,current_user.id)
            
            print(f"Saida Realiza!\n\nValor a Receber: R${round(final_price,2)}\nTempo de estacionamento: {time_of_parking} " if result == True else "Erro ao dar Baixa!")  
            input("Aperte Enter Confirmar!")

        elif(opc == 3):
            Clear()
            Menu.Check_parking(Controller.Get_parkings_cars())

        elif(opc == 4):
            Clear()
        elif(opc == 5):
            Clear()
            General.About()
        elif(opc == 0):
            Clear()                    
            print("Saindo")
        else:
            Error()



   
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
                    Controller.Create_user(name, user_name, password )

                elif(subOpc == 2):
                    Clear()
                    #editar

                elif(subOpc == 3):
                    #listar
                    Clear()
                    Menu_Admin.List_user_menu(Controller.Get_all_users())

                elif(subOpc == 4):
                    #deletar
                    Clear()
                    id = Menu_Admin.Delete_user_menu()
                    result = Controller.Delete_user(id)
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
                    Controller.Create_car(name, manufacturer, price_per_hour )

                elif(subOpc == 2):
                    Clear()
                    #editar
                    
                elif(subOpc == 3):
                    #listar
                    Clear()
                    Menu_Admin.List_car_menu(Controller.Get_all_cars())

                elif(subOpc == 4):
                    #deletar
                    Clear()
                    id = Menu_Admin.Delete_car_menu()
                    result = Controller.Delete_car(id)
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
                    Controller.Create_color(name, hex)

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
                    result = Controller.Delete_color(id)
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
            Controller.Export_to_json()
            input("\nAperte Enter para sair!")

        elif(opc == 5):
            
            #Import
            while subOpc !=0:
                Clear()
                subOpc = Menu_Admin.Import()

                if(subOpc == 1):                  
                    Clear()
                    print("---Importar arquivo---")
                    path = input("Digite o caminho do arquivo: ")
                    Controller.Import_from_json(path)
                    input("\nAperte Enter para sair!")

                elif(subOpc == 2):
                    Clear()
                    print("---Importar URL---")
                    url = input("Digite o URL: ")
                    Controller.Import_from_url(url)
                    input("\nAperte Enter para sair!")
                    

                elif(subOpc == 0):
                    Clear()                    
                    print("Saindo")
                else:
                    Error()
        elif(opc == 6):
            Clear()
            General.About()
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

        user = Controller.Login_user(user_name,password)
       

        if user == None:
            input("Senha ou Login Invalido!")
        else:
            isLoginValid = True
        

    return user
        






    


 






if __name__ == "__main__":
   Main()