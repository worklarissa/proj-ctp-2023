#Divisão de tarefas 
import json

eventos = {
    "Rock in Rio": {
            "Data":"12/12/2023",
            "Capacidade":"10,000",
            "Localização":"Neo Química Arena"
    },
    "Lolapalooza": {
            "Data":"15/01/2024",
            "Capacidade":"15,000",
            "Localização": "Maracanã"
    },

}

def criar_evento (): 
    """Criar_Evento, permite o usuário a criar um novo evento,
    fornecendo, nome,data, capacidade e localização 
    temos que criar um dicionário pra cada evento e armazenar no sistema. """

    pass

def  listar_eventos ():
    """Exibe uma lista de todos os eventos dísponives 
    com todas as informações básicas.Apenas exibir lista de 
    eventos formatada com detalhes."""    
    pass
    
             

def reservar_vaga (): 
    """reservar_vaga permite o usuário reservar uma vaga em um 
    evento em especifico, é necessário dados do evento e confirmação
    da reserva"""
    pass
                         
                        
def cancelar_reserva (): 
    """Permite o usuário remover uma reserva. Necessário dados 
     do evento e confirmação do cancelamento"""
    pass
                 
    

def visualizar_detalhes_evento ():
    """exibe os seguintes dados do evento: nome, data, localização, capacidade e vagas disponíveis"""
    pass
                           
def salvar_dados(agenda, arquivo):
    """Essa função salva a agenda em um arquivo .json"""
    try:
        with open('agenda.json', 'w') as a:
            json.dump(agenda, a)
        print(f"A agenda de eventos foi salva com sucesso em {arquivo}")
    except:
        print("Ocorreu um erro ao tentar salvar a agenda!")

                            
def carregar_dados(arquivo):
    """Essa função carrega os dados do sistema a partir de um arquivo .json. Confirma que os dados foram carregados com sucesso, informa erros para aquivos inexistentes ou corrompidos"""
    try:
        with open('agenda.json','r') as a:
            json.load(a)
        print(f"A agenda foi carregada com sucesso a partir de {arquivo}!")
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não foi encontrado!")
    except:
        print("Ocorreu um erro ao tentar carregar a agenda")

def menu(): 
    """Menu inicial de input, vai receber um int para selecionar 
    um dos serviços que vamos ter"""
    pass

                             
if __name__ == "__main__":
    menu()
