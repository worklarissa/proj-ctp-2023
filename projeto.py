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

def criar_evento (): 
    """Criar_Evento, permite o usuário a criar um novo evento,
    fornecendo, nome,data, capacidade e localização 
    temos que criar um dicionário pra cada evento e armazenar no sistema. """
    nome_evento = input("Nome do evento: ")
    if nome_evento not in eventos:
        dt_evento = input ("Data do evento: ")
        cap_evento = int (input("Quantas pessoas podem participar? "))
    if cap_evento != int:
        print ('A quantidade de pessoas precisa ser um valor inteiro!')
    else:
        loc_evento = input("Local do evento: ")

    if dt_evento and loc_evento not in eventos:
        eventos[nome_evento] = {"Data":dt_evento,"Capacidade":cap_evento,"Localização":loc_evento}
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
    def menu(criar_evento, listar_eventos, reservar_vaga, cancelar_reserva, visualizar_detalhes_evento, salvar_dados, carregar_dados):
        print("Bem-vindo(a) ao sistema da LPEventos, escolha o que você quer fazer hoje:\n"
        "Para adicionar um evento - Digite 1\n" 
        "Para lista os eventos adicionados em nosso sistema - Digite 2\n"
        "Para comprar um ingresso - Digite 3\n"
        "Para cancelar a compra de um ingresso - Digite 4\n"
        "Para visualizar detalhes de um evento - Digite 5\n"
        "Para salvar dados do sistema em um arquivo - Digite 6\n"
        "Para carregar um arquivo no sistema  - Digite 7\n")
    entrada =  input("Digite um número de 1 a 7 de acordo com o menu: ")

    if entrada == "1":
        return criar_evento
    elif entrada == "2":
        return listar_eventos
    elif entrada == "3":
        return reservar_vaga
    elif entrada == "4":
        return cancelar_reserva
    elif entrada == "5":
        return visualizar_detalhes_evento
    elif entrada == "6":
        return salvar_dados
    elif entrada == "7":
        return carregar_dados
    else:
        print('Opção inválida!')
    return menu
