from socket import *
from pickle import *
from paquete import *
from constantes import *

def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	return UDPsocket	

def rdt_send(): #manda datos desde la capa de aplicacion rdt=tranferencia confiable
    data=input('ingrese mensaje') #recibe por teclado
    return data.encode('utf-8')


def make_pkt(data):# crea el paquete
    pkt = Packet(SOURCE_PORT,RECEIVER_PORT, data) #le paso (p.origen,puerto destino,datos)
    return pkt


def udp_send(socket,pkt): # envia paquete por udp al servidor
    dato = dumps(pkt) #Comprimimos genera los datos que se pueden enviar a través del socket, a partir de un paquete
    socket.sendto(dato,(RECEIVER_IP, RECEIVER_PORT)) # (datos,ip,puerto)

def close_socket(socket): # cierra el 
    socket.close()
    
    
if __name__ == "__main__":
    cliente=create_socket()

    while True:
        data=rdt_send() #manda segmentos desde el emisor rdt=tranferencia confiable
        pkt= make_pkt(data) # crea el paquete
        udp_send(cliente,pkt) # envia paquete por medio no confiable
    close_socket(cliente)

