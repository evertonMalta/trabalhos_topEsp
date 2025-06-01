# -*- coding: utf-8 -*-
from tabulate import tabulate
from utils import *
from getpass import getpass

class General:
    def Login():
        print("---Login---")
        user_name = input("Usuario: ")
        password =  getpass("Senha: ")
        return user_name, password
    
    def About():
        print("Tópicos Especiais em Informática")
        print("---Projeto Prático B2---")
        print("Tema escolhido - Gerenciador de estacionamento")
        print("Aluno: Everton Malta Gouveia de Queiroz RA: 2840482223040")

        input("\n\nAperte Enter para voltar!")





class Menu:    

    def Main_menu():
        print("---Menu---")
        print("1 - Registrar entrada de Veiculo")
        print("2 - Registrar Saida do carro")
        print("3 - Conferir estacionamento")
        print("4 - Fechar caixa")
        print("5 - Sobre")
        print("0 - Finalizar seção")

        opc = TryParseOpcInput(input("Escolha a opção: "))
        return opc
    
    def Register_Entry_Menu():
        print("---Registrar Entrada---")
        plate = input("Digite Placa do veiculo: ")        
        car_id = input("Digite id do veiculo: ")
        color_id = input("Digite id cor: ")

        return plate, car_id, color_id
    
    def Register_Departure_Menu():
        print("---Registrar Saida---")
        id = input("Digite o Id de entrada: ")

        return id

    def Check_parking(parking):
        print("---Conferir estacionamento---")
        print(tabulate(parking, headers="keys",tablefmt='orgtbl'))
        input("\nAperte Enter para sair!")



class Menu_Admin:

    def Main_menu():
        print("---Menu Adminstrativo---")
        print("1 - Usuarios")
        print("2 - Carros")
        print("3 - Cores")
        print("4 - Exportar Json")
        print("5 - Importar Json")
        print("6 - Sobre")
        print("0 - Finalizar seção")

        opc = TryParseOpcInput(input("Escolha a opção: "))
        return opc
    

    # ----------------------------
    # User Interface
    # ----------------------------
    
    def User_menu():
        print("---Menu Usuarios---")
        print("1 - Criar")
        print("2 - Editar")
        print("3 - Listar")
        print("4 - Deletar")
        print("0 - Sair")

        opc = TryParseOpcInput(input("Escolha a opção: "))
        return opc
    
    def Create_user_menu():        
        print("---Criando usario---")
        name = input("Nome: ")
        user_name = input("Nome do usario: ")
        password = input("Senha: ")
        return name, user_name, password


    def Edit_user_menu(step):
        print("---Editar usario---")
        if step == 1:
            id = input("Digite o ID: ")
            return id
        

    
    def List_user_menu(user):                
        print("---Lista usario---")
        print(tabulate(user, headers="keys",tablefmt='orgtbl'))
        input("\nAperte Enter para sair!")

    
    def Delete_user_menu():
        print("---Deletar usario---")
        id = TryParseOpcInput(input("Digite o ID: "))
        return id
    
    # ----------------------------
    # Car Interface
    # ----------------------------

    def Car_menu():
        print("---Menu Carros---")
        print("1 - Criar")
        print("2 - Editar")
        print("3 - Listar")
        print("4 - Deletar")
        print("0 - Sair")
        opc = TryParseOpcInput(input("Escolha a opção: "))
        return opc
    
    def Create_car_menu():
        print("---Criando Carro---")
        name = input("Nome: ")
        manufacturer = input("Montadora: ")
        price_per_hour = float(input("Preço por hora: "))
        return name,manufacturer,price_per_hour

    def Edit_car_menu():
        print("em progresso")


    def List_car_menu(car):        
        print("---Lista de Carros---")                
        print(tabulate(car,headers="keys",tablefmt='orgtbl'))        
        input("\nAperte Enter para sair!")
    
    def Delete_car_menu():
        print("---Deletar Carro---")
        id = input("Digite o ID: ")
        return id
    
    # ----------------------------
    # Color Interface
    # ----------------------------
    def Color_menu():
        print("---Menu Cores---")
        print("1 - Criar")
        print("2 - Editar")
        print("3 - Listar")
        print("4 - Deletar")
        print("0 - Sair")
        opc = TryParseOpcInput(input("Escolha a opção: "))
        return opc
    
    def Create_color_menu():
        print("---Criando Cor---")
        name = input("Nome: ")
        hex = input("hexadecimal: ")
        return name,hex


    def Edit_color_menu():
        print("em progresso")
    
    def List_color_menu(color):
        print("---Lista de Cores---")       
        print(tabulate(color, headers="keys",tablefmt='orgtbl'))               
        input("\nAperte Enter para sair!")
    
    def Delete_color_menu():
        print("---Deletar Cor---")
        id = input("Digite o ID: ")
        return id
    
    def Import():
        print("---Menu Importar---")
        print("1 - Arquivo")
        print("2 - Online")
        print("0 - Sair")
        opc = TryParseOpcInput(input("Escolha a opção: "))
        return opc
