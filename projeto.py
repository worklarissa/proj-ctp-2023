#Divisão de tarefas 
import json

eventos = {
    "Rock in Rio": {
            "Data":"12/12/2023",
            "Capacidade":"10,000",
            "Localização":"Neo Química Arena",
            "Ingressos":500
    },
    "Lolapalooza": {
            "Data":"15/01/2024",
            "Capacidade":"15,000",
            "Localização": "Maracanã",
            "Ingressos":0
    }

}

def menu():
    def menu():
        while True:
            print("Bem-vindo(a) ao sistema da LPEventos, escolha o que você quer fazer hoje:\n"
            "Para adicionar um evento - Digite 1\n" 
            "Para lista os eventos adicionados em nosso sistema - Digite 2\n"
            "Para comprar um ingresso - Digite 3\n"
            "Para cancelar a compra de um ingresso - Digite 4\n"
            "Para visualizar detalhes de um evento - Digite 5\n"
            "Para salvar dados do sistema em um arquivo - Digite 6\n"
            "Para carregar um arquivo no sistema  - Digite 7\n"
            "Para sair do sistema  - Digite 8")
            entrada =  input("Digite um número de 1 a 8 de acordo com o menu: ")

            if entrada == "1":
                criar_evento()
            elif entrada == "2":
                listar_eventos()
            elif entrada == "3":
                reservar_vaga ()
            elif entrada == "4":
                cancelar_reserva()
            elif entrada == "5":
                visualizar_detalhes_evento()
            elif entrada == "6":
                salvar_dados()
            elif entrada == "7":
                carregar_dados()
            elif entrada == "8":
                print ("Você está saindo do sistema!")
                break
            else:
                print('Opção inválida!')

def criar_evento (): 
    """permite o usuário a criar um novo evento,fornecendo, nome,data, 
    capacidade e localização temos que criar um dicionário pra cada 
    evento e armazenar no sistema."""
    nome_evento = input("Nome do evento: ") #pede o nome do evento
    if nome_evento not in eventos: #if e else para a validação do nome, se já existir um evento com esse nome não é possivel criar outro
        dt_evento = input ("Data do evento: ")
        cap_evento = int(input("Quantas pessoas podem participar? "))
        if cap_evento >= 1 or cap_evento <= 1000000000: #validação para que a capacidade seja um número inteiro
                loc_evento = input("Local do evento: ")    
        else:
             print ('A quantidade de pessoas precisa ser um valor inteiro')
    else: 
        print ('Já existe um evento cadastrado com esse nome!') 
        return criar_evento()

    if dt_evento and loc_evento not in eventos: #validar se um evento não coincide com outro 
        eventos[nome_evento] = {"Data":dt_evento,"Capacidade":cap_evento,"Localização":loc_evento}
        print ("O evento foi criado com sucesso!\n\n")

    else:
        print('A data e o local coincidem com de outro evento! Por favor, crie um outro evento com outra data e local')
    



    

# def  listar_eventos ():
"""  Exibe uma lista de todos os eventos dísponives 
    com todas as informações básicas.Apenas exibir lista de 
    eventos formatada com detalhes."""    
    


       

def reservar_vaga(eventos):
    ingresso=""
    resposta= "sim"
    reservas=[]
    while resposta =="sim":
        ingresso = input("Digite o nome do evento: ")
        if ingresso in eventos:
            if eventos[ingresso]["Ingressos"]>0:
                reservas.append(ingresso)
                print(f"Você selecionou o o ingresso para o {ingresso}")
                eventos[ingresso]["Ingressos"]-=1
                print(f"Você concluiu a reserva com sucesso o número de reserva é  {eventos[ingresso]['Ingressos']}")
                resposta= input("Você deseja continuar comprando?: (sim/não)")
            elif eventos[ingresso]["Ingressos"]<=0:
                print("Sem ingressos!")

        else:
            print("Opção inválida!")
    
    return reservas

print(eventos)
reserva=reservar_vaga(eventos)                      
print(reserva)                      
def cancelar_reserva (reserva): 
    resposta="sim"
    cancelar=""
    print(f"Você tem reservas para o {reserva}")
    while resposta =="sim":
        cancelar=input("Qual reserva você deseja cancelar?: ")
        if cancelar in reserva:
            reserva.remove(cancelar)
            eventos[cancelar]["Ingressos"]+=1
            print("Você cancelou com sucesso!")
            perguntar_continuar= input("Você deseja cancelar mais alguma reserva?:(sim/não)")
        else:
            print("Você não tem nenhuma reserva deste evento!")
    return reserva
 
cancelar_reserva(reserva)
        
   


    
                 
    

def visualizar_detalhes_evento(eventos):
    """exibe os seguintes dados do evento: nome, data, localização, capacidade e vagas disponíveis"""
    agenda = dict(sorted(eventos.items()))
    print("DETALHE DOS EVENTOS")
    for nome, evento in agenda.items():
        print(f"\nNome: {nome}")
        for tipo, valor in evento.items():
            print(f"{tipo}: {valor}")
                           
def salvar_dados(eventos):
    """Essa função salva os eventos em um arquivo .json"""
    arquivo = input('Dê um nome para o arquivo em que os eventos serão salvos: ')
    try:
        with open(arquivo, 'w') as a:
            json.dump(eventos, a)
        print(f"Os eventos foram salvos com sucesso em {arquivo}")
    except:
        print("Ocorreu um erro ao tentar salvar os eventos!")
                            
def carregar_dados():
    """Essa função carrega os dados do sistema a partir de um arquivo .json. Confirma que os dados foram carregados com sucesso, informa erros para aquivos inexistentes ou corrompidos"""
    arquivo = input('Qual o nome do arquivo que você gostaria de importar? ')
    try:
        with open(arquivo,'r') as a:
            json.load(a)
        print(f"Os eventos foram carregados com sucesso a partir de {arquivo}!")
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado!")
    except:
        print("Ocorreu um erro ao tentar carregar os eventos")

                             
if __name__ == "__main__":
    menu()

