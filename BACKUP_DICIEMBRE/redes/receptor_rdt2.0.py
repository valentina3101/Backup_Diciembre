from constantes import *
from pickle import *
from socket import *
from paquete import *


def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((RECEPTOR_IP, RECEPTOR_PORT))
	return UDPsocket

def extract(packet):
	data = paquete.get_datos() # habia puesto Packet.get_data por eso no andaba
	return data

def deliver_data(data):
	print(data)

def rdt_rcv(sock):
	data =sock.recv(2048) #luego de esta linea estaba printeando
	emisor, paquete=loads(data) # decodifica 
	return emisor, paquete

def corrupto(paquete):
	if calcular_checksum(paquete) == 0:
		return True
	else:
		return False


def make_pckt(dato):
	pkt = Paquete(RECEPTOR_PORT, EMISOR_PORT, dato, 0)
	checksum = calcular_checksum(paquete)
	paquete.set_checksum(dato)
	return pkt


def udp_send(socket, receptor, paquete):
	dato = dumps((receptor, paquete)) 
	socket.sendto(dato, (NETWORK_IP, NETWORK_PORT))

def close_socket(socket, signal, frame):
	print ("\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
	# Creamos el socket "receiver"
	receptor = create_socket()
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, receptor))
	# Imprimimos el cartel "Listo para recibir mensajes..."
	print('recibiendo mensaje: ')

	secuencia = 0
	# Iteramos indefinidamente
	while True:
		# Recibimos un paquete de la red
		emisor, paquete = rdt_rcv(receptor)
		if corrupto(paquete) == 0:
			emisor = (EMISOR_IP, EMISOR_PORT)
			pkt = make_pckt("NAK")
			udp_send(receptor, emisor, pkt)
		else:
			emisor = (EMISOR_IP, EMISOR_PORT)
			pkt1 = make_pckt("ACK")
			udp_send(receptor, emisor, pkt1)	
		# Extraemos los datos
		data = extract(paquete) #aca pedia un paquete no definido antes. ahora anda
		#print(data.get_data)
		# Entregamos los datos a la capa de aplicacion
		deliver_data(data)
		#pkt = make_pckt(data)
		# Establecemos el destinatario
		
		# Enviamos el mensaje
		
	close_socket(receptor)
