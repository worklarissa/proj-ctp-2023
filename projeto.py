#Divisão de tarefas 
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
        print ("O evento foi criado com sucesso!\n")
        tarefa_finalizada = (input("Deseja fazer mais alguma coisa?")).lower #caso o usuario queria realizar mais alguma tarefa
    
        if tarefa_finalizada == "sim":
                    main()
        else:
            print ("Tudo bem! Volte sempre.")
        
    else:
        print('A data e o local coincidem com de outro evento! Por favor, crie um outro evento com outra data e local')


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
    """Exibe detalhes de um evento. Dados que deverá exibir: nome,
      data, localização, capacidade e vagas disponíveis. Retorna esses detalhes"""
    pass
                           
def salvar_dados ():
    """salva todos os dados do sistema (eventos, reservas e etc.) de um arquivo """
    pass
                            
def carregar_dados ():
    """carrega os dados do sistema a partir de um arquivo. Deve confirmar que os dados foram carregados, incluir erros para arquivo inexistente ou corrompido"""
    pass

                 

if __name__ == "__main__":
    menu()
        