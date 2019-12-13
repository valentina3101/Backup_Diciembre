from socket import *
from pickle import *
from paquete import *
from constantes import *

def create_socket(address, port):
	servidor = socket(AF_INET, SOCK_DGRAM)
	servidor.bind((address, port))
	return servidor

def print_message(message):
    print (message)

def rdt_recv(socket): #recibe paquete del emisor rdt=tranferencia confiable
    datos = socket.recv(2048) #permite recibir una cantidad de datos que va a esperar
    packet=loads(datos) # toma los datos recibidos por medio del socket, y los vuelve a convertir en un paquete. 
    return packet

def extract(packet): # estrae el encabezado del paquete, para solo quedarse con los datos
    data=packet.get_data()	
    return data


def deliver_data(data): #envia los datos a la capa de aplicacion
    print (data)

def close_socket(socket):
    socket.close()

if __name__ == "__main__":
    servidor= create_socket(RECEIVER_IP, RECEIVER_PORT)
    print_message("servidor corriendo")
    while True :
        packet=rdt_recv(servidor) #recibe paquete del emisor
        data=extract(packet) # estrae el encabezado del paquete, para solo quedarse con los datos
        deliver_data(data) #envia los datos a la capa de aplicacion
        
    close_socket(servidor)

