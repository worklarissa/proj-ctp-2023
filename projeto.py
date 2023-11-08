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
                 
    

def visualizar_detalhes_evento(eventos):
    """exibe os seguintes dados do evento: nome, data, localização, capacidade e vagas disponíveis"""
    agenda = dict(sorted(eventos.items()))
    print("DETALHE DOS EVENTOS")
    for nome, evento in agenda.items():
        print(f"\nNome: {nome}")
        for tipo, valor in evento.items():
            print(f"{tipo}: {valor}")

                           
def salvar_dados(eventos, arquivo):
    """Essa função salva os eventos em um arquivo .json"""
    try:
        with open('eventos.json', 'w') as a:
            json.dump(eventos, a)
        print(f"Os eventos foram salvos com sucesso em {arquivo}")
    except:
        print("Ocorreu um erro ao tentar salvar os eventos!")

                            
def carregar_dados(arquivo):
    """Essa função carrega os dados do sistema a partir de um arquivo .json. Confirma que os dados foram carregados com sucesso, informa erros para aquivos inexistentes ou corrompidos"""
    try:
        with open(arquivo,'r') as a:
            json.load(a)
        print(f"Os eventos foram carregados com sucesso a partir de {arquivo}!")
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado!")
    except:
        print("Ocorreu um erro ao tentar carregar os eventos")

def menu(): 
    while True:
        user_op = input("Escolha uma opção:")

        if user_op == "1":
            arquivo = input('Dê um nome para o arquivo em que os eventos serão salvos: ')
            salvar_dados(eventos,arquivo)

        elif user_op == "2":
            arquivo = input('Qual o nome do arquivo que você gostaria de importar? ')
            carregar_dados(arquivo)

        elif user_op == "3":
            visualizar_detalhes_evento(eventos)

        else:
            break

                             
if __name__ == "__main__":
    menu()
