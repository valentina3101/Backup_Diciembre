from constantes import *
from socket import *
from paquete import *

def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM) # creo el socket protocolo de red IP, protocolo transporte UDP
	UDPsocket.bind((EMISOR_IP, EMISOR_PORT))
	return UDPsocket


def rdt_recv():
    data=input('ingrese un mensaje:  ')
    return(data.encode('utf-8'))
    
def rdt_send(message):	
    print(message)

def make_pkt(data):
    pkt = Paquete(EMISOR_PORT, RECEPTOR_PORT, data, 0)
    cksum = calcular_checksum(pkt)
    pkt.set_checksum(cksum)
    return pkt  


def udp_send(socket, mensaje, receiver): #data y reciber
	data=dumps((receiver, mensaje))
	socket.sendto(data, (NETWORK_IP,NETWORK_PORT))
	
def udp_recv(socket):
	datos, net = socket.recvfrom(2048) 
	emisor, paquete = loads(datos) 
	return emisor, paquete

def extract(packet): 
	data=packet.get_datos()
	return data
    
def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)

if __name__ == "__main__":

	cliente=create_socket() # Creamos el socket
	
	signal.signal(signal.SIGINT, partial(close_socket, cliente))#esta funcion toma el socketal final
    
	secuencia = 0
    
	while True: # Iteramos indefinidamente
	
		flag = True
		
		data=rdt_recv() # Leemos el mensaje desde teclado
		paquete=make_pkt(data) # Hacemos el paquete
		destinatario = (RECEPTOR_IP, RECEPTOR_PORT) # Establecemos el destinatario
		udp_send(cliente, paquete, destinatario) # Enviamos el mensaje
		
		emisor, paquete = udp_recv(cliente)
		mensaje = extract(paquete)

		while flag:
		
			if mensaje == "ACK":
				secuencia = (secuencia+1)%2
				flag= False
			else: 
				udp_send(cliente, paquete, destinatario) # Enviamos el mensaje
				emisor, paquete = udp_recv(cliente)
				mensaje = extract(paquete)		
				
		print(secuencia)
				
							

	signal.signal(signal.SIGINT, partial(close_socket, servidor))
	close_socket(cliente)  
		
