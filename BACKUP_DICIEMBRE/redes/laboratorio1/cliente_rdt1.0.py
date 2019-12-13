from socket import *

def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	return UDPsocket	

def rdt_send(): #manda segmentos desde el emisor rdt=tranferencia confiable
    data=input('ingrese mensaje') #recibe por teclado
    return data.encode('utf-8')


def make_pkt(data):
    return data


def udp_send(socket,data): # envia paquete por udp al servidor
    socket.sendto(data,('localhost',20000))

def close_socket(socket): # cierra el 
    socket.close()
    
    
if __name__ == "__main__":
    cliente=create_socket()

    while True:
        data=rdt_send() #manda segmentos desde el emisor rdt=tranferencia confiable
        pkt= make_pkt(data) # crea el paquete
        udp_send(cliente,packet) # envia paquete por medio no confiable
    close_socket(cliente)

