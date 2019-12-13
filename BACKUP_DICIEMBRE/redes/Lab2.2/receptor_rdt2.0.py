from constantes import *
from paquete import *
from network import *

def create_socket():#(servidor)
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((RECEPTOR_IP, RECEPTOR_PORT)) #es para saber donde tiene que escuchar el ip y purta del archivo constantes
	return UDPsocket

def extract(packet):
    data=packet.get_data()
    return data

def deliver_data(message):
	print(message)

def rdt_rcv(red, datos):#recibe la data de la red, obtengo dato, descomprime data , obtiene el pkt y emisor
	datos=sock.recv(2048)
	emisor, paquete=loads(datos) #descomprimo con load
	'''print(paquete)'''
	return emisor, paquete

def make_pkt(datos):
    paquete = Paquete(receptor, emisor, datos, 0) #indicamos de dnd sale y a dond tiene q ir
    ckecksum = calcular_checksum(paquete)
    paquete.set_checksum(ckecksum)
    return paquete

def corrupto(paquete):
    if paquete.set_checksum()== 0:
        return True
    else:
        return False

def udp_send(paquete, emisor): #envia el paq
    datos = dumps(emisor, confirmacion) #comprime
    socket.sento(datos, (NETWORK_IP, NETWORK_PORT)) #ENVI datos a la red
    return datos

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

	# Iteramos indefinidamente
	while True:
                secuencia=0
                #num de id del paquete
                paquete=rdt_rcv(servidor,datos)
                #Recibimos un paquete de la red
                if recv_paquete and corrupto:
                    sndpkt=make_pkt("NAK")
                    paquete=rdt_rcv(servidor,datos)
                elif recv_paquete and not corrupto:
                    data=extract(paquete)
                    #Extraemos los datos
                    deliver_data(data)
                    #Entregamos los datos a la cap de aplicacion
                    paquete=make_pkt("ACK",get_checksum)
                    udt_send(paquete)
	close_socket()
