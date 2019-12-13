from constantes import *
from paquete import *
from network import *
from paquete import *

def create_socket():#(servidor)
	UDPsocket=socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((RECEPTOR_IP, RECEPTOR_PORT)) #tiene que escuchar el ip y parta del archivo constantes
	return UDPsocket
    
def extract(packet): 
	data=packet.get_datos()
	return data
    
def rdt_send(message):	
    print(message)
    

def make_pkt(data):
	paquete = Paquete(EMISOR_PORT, RECEPTOR_PORT, data, 0)
	ckecksum=calcular_checksum(paquete)
	paquete.set_checksum(ckecksum)
	return paquete
    
def corrupto(paquete):
	if calcular_checksum(paquete) == 0:
		return False
	else:
		return True
        
	
def udp_send(socket, paquete, emisor): 
	data=dumps((emisor, paquete))
	socket.sendto(data, (NETWORK_IP,NETWORK_PORT))
	
def udp_recv(socket):
	datos, net=socket.recvfrom(2048) 
	emisor, paquete=loads(datos) 
	return emisor, paquete
    
def close_socket(socket, signal, frame):
	print ("\rCerrando socket")
	socket.close()
	exit(0)
    
    
if __name__ == "__main__":
	servidor=create_socket()
	# Creamos el socket "receiver"

	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, servidor))
	# Imprimimos el cartel "Listo para recibir mensajes..."
	
	print("Listo para recibir mensajes...")

	secuencia = 0
	
	while 1:
		emisor, paquete = udp_recv(servidor)
		mensaje = extract(paquete)
		
		if corrupto(paquete):
			paquete = make_pkt("NAK" )
			destinatario = (EMISOR_IP , EMISOR_PORT)
			udp_send(servidor, paquete, destinatario)
		else:
			mensaje = extract(paquete)
			rdt_send(mensaje)
			paquete = make_pkt("ACK")
			destinatario = (EMISOR_IP , EMISOR_PORT)
			udp_send(servidor, paquete, destinatario)

			
				
		  
	close_socket()
