#Divisão de tarefas 
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
 


# def menu():
"""Menu inicial de input, vai receber um int para selecionar 
    um dos serviços que vamos ter"""
    

#  def criar_evento (): 
"""Criar_Evento, permite o usuário a criar um novo evento,
 fornecendo, nome,data, capacidade e localização 
 temos que criar um dicionário pra cada evento e armazenar no sistema. """

    

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
        ingresso.rstrip()
        if ingresso in eventos:
            if eventos[ingresso]["Ingressos"]>0:
                reservas.append(ingresso)
                print(f"Você selecionou o o ingresso para o {ingresso}")
                eventos[ingresso]["Ingressos"]-=1
                print(f"Você concluiu a reserva com sucesso o número de reserva é  {eventos[ingresso]['Ingressos']}")
                resposta= input("Você deseja continuar comprando? (sim/não): ")
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
            resposta= input("Você deseja cancelar mais alguma reserva?:(sim/não)")
        else:
            print("Você não tem nenhuma reserva deste evento!")
    return reserva
 
cancelar_reserva(reserva)
        
   


    
                 
    

# def visualizar_detalhes_evento ():
""" Exibe detalhes de um evento. Dados que deverá exibir: nome,
      data, localização, capacidade e vagas disponíveis. Retorna esses detalhes"""
    
                           
#  salvar_dados ():
""" salva todos os dados do sistema (eventos, reservas e etc.) de um arquivo """
    
                            
# def carregar_dados ():
""" carrega os dados do sistema a partir de um arquivo. Deve confirmar que os dados foram carregados, incluir erros para arquivo inexistente ou corrompido"""
    
#def menu():
"reservar_vaga()"

                             
#if __name__ == "__main__":
"menu()"

