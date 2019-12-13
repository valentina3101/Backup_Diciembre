from constantes import *
from socket import *
from paquete import *
import signal
import sys


def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((EMISOR_IP, EMISOR_PORT))   
	return UDPsocket

def rdt_recv():
	data = input('Ingrese mensaje: ')
	return (data.encode('utf-8'))



def udt_send(socket, receiver, packet):
	dato = dumps((receiver, packet)) 
	socket.sendto(dato, (NETWORK_IP, NETWORK_PORT))


def make_pkt(data):
	pkt = Paquete(EMISOR_PORT, RECEPTOR_PORT, data, 0)
	cksum = calcular_checksum(pkt)
	pkt.set_checksum(cksum)
	return pkt

def rdt_rcv(sock):
	data=sock.recv(2048) 
	emisor, paquete=loads(data) # decodifica 
	return emisor, paquete

def extract(packet):
	data = paquete.get_datos() 
	return data

def rdt_send(mensaje):
	print(mensaje)

def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
	# Creamos el socket
	cliente = create_socket()

	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, cliente))

	secuencia = 0
	# Iteramos indefinidamente
	while True:
		flag = True
		# Leemos el mensaje desde teclado
		data = rdt_recv()
		# Hacemos el paquete
		pkt = make_pkt(data)
		# Establecemos el destinatario
		receiver = (RECEPTOR_IP, RECEPTOR_PORT)
		# Enviamos el mensaje
		udt_send(cliente,receiver, pkt)
		# recibo pquete
		receptor, paquete = rdt_rcv(cliente)
		data = extract(paquete)		
		rdt_send(data)
		while(flag):
			if data == 'ACK':
				secuencia = (secuencia +1)%2
				flag = False
			else:
				udt_send(cliente,receiver, pkt)
				receptor, paquete = rdt_rcv(cliente)
				data = extract(paquete)
		# Extraemos los datos
		print (secuencia)
		
	close_socket(cliente)
