#packs
import time
import datetime
#Functions

#Main
acionamento = 1
while acionamento != 0:
    # Obtenha a data e hora atual
    hora_atual = datetime.datetime.now()

    # Formate a hora para exibi-la
    hora_formatada = hora_atual.strftime("%H:%M:%S")

    # Imprima a hora formatada
    print("A hora atual é:{}".format(hora_formatada))
    time.sleep(1)