from constants import *
from network import *


def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	return UDPsocket


def rdt_send():
    data=input('ingrese mensaje') #recibe por teclado
    return data.encode('utf-8')
    

def make_pkt(data): #crea el paquete
    pkt = Packet(SENDER_PORT,RECEIVER_PORT, data) #le paso (p.origen,puerto destino,datos)
    return pkt


def udp_send(socket, receiver, packet): # envia paquete
    dato = dumps((receiver,packet)) #Comprimimos el packete
    socket.sendto(dato,(NETWORK_IP,NETWORK_PORT)) # envia dato por udt(no confiable) a la red
    

def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
	cliente=create_socket()
	
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, cliente))
	# Iteramos indefinidamente
	while True:
		data=rdt_send() # Leemos el mensaje desde teclado
		pkt= make_pkt(data) # crea el paquete
		receiver=(RECEIVER_IP,RECEIVER_PORT)
		udp_send(cliente,receiver,pkt) #enviamos el mensaje a la red
	close_socket(cliente)
		
