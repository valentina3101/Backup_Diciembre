from constants import *
from packet import *
from constants import *
from network import *

def create_socket(): #crea socket
	servidor = socket(AF_INET, SOCK_DGRAM)
	servidor.bind((RECEIVER_IP,RECEIVER_PORT))
	return servidor

def extract(packet): #extrae paquete
    data=packet.get_data()
    return data


def deliver_data(message): #envia los datos
	print(message)

def udp_send(socket, emisor, packet): # envia paquete
    dato = dumps((emisor,packet)) #Comprimimos el packete
    socket.sendto(dato,(NETWORK_IP,NETWORK_PORT)) # envia dato por udt(no confiable) a la red

def rdt_rcv(socket): #recive mensaje
    data=socket.recv(2048)
    paquete=loads(data)
    return paquete


def close_socket(socket, signal, frame): #cierra socket
	print ("\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
	servidor= create_socket()# Creamos el socket "receiver"
	
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, servidor))
	print ("listo para recibir mensajes..")# Imprimimos el cartel "Listo para recibir mensajes..."
	
	# Iteramos indefinidamente
	while True:
		packet=rdt_rcv(servidor)# Recibimos un paquete de la red
		data=extract(packet)# Extraemos los datos
		deliver_data(data)# Entregamos los datos a la capa de aplicacion
        
	close_socket(servidor)
		
