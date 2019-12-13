from socket import *

def create_socket(address, port):
	servidor = socket(AF_INET, SOCK_DGRAM)
	servidor.bind((address, port))
	return servidor

def print_message(message):
    print (message)

def rdt_recv(socket): #recibe paquete del emisor rdt=tranferencia confiable
    packet= socket.recv(2048) #recibe datos con el buffer asignado 
    return packet

def extract(packet): # estrae el encabezado del paquete, para solo quedarse con los datos
	return packet


def deliver_data(data): #envia los datos a la capa de aplicacion
    print (data)

def close_socket(socket):
    socket.close()

if __name__ == "__main__":
    servidor= create_socket('localhost', 20000)
    print_message("servidor corriendo")
    while True :
        packet=rdt_recv(servidor) #recibe paquete del emisor rdt=tranferencia confiable
        data=extract(packet) # estrae el encabezado del paquete, para solo quedarse con los datos
        deliver_data(data) #envia los datos a la capa de aplicacion
    close_socket(servidor)

