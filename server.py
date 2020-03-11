from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import array as arr
import datetime

waktu = datetime.datetime.now()

def pull(saldoA,tarik,time,saldo,penarikan):
    print("Client requested a pull : The amount => ", tarik)
    saldo.append(saldoA-tarik)
    penarikan.append(tarik)
    time.append(waktu)
    print("Operation succesful!")
    print ("\n")
    return saldo, time, penarikan, saldoA-tarik

def transfer(rekening,Jtransfer,saldo2,b,a,time2,saldoA):
    print("Client requested a transfer to ", a ," : The amount => ", b)
    rekening.append(a)
    Jtransfer.append(b)
    time2.append(waktu)
    saldo2.append(saldoA-b)
    print("Operation succesful!")
    print ("\n")
    return rekening, Jtransfer, time2, saldoA-b, saldo2

# def history():
#     return "Thank you, I'm... speechless"

server = SimpleXMLRPCServer(("localhost",9000))
print("Server is listening on port 9000...")
server.register_function(pull,"pull")
server.register_function(transfer,"transfer")
# server.register_function(history,"history")
server.serve_forever()