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
    """Menu inicial de input, vai receber um int para selecionar 
    um dos serviços que vamos ter"""
    pass

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
