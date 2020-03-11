import xmlrpc.client
from array import *

proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

if __name__ == "__main__":
    print("Connected to Server")
    saldoA = int(1000000)
    rekening = []
    time = []
    time2 = []
    Jtransfer = []
    penarikan = []
    saldo = []
    saldo2= []
    while(True):
        print ("\n")
        print("Please choose an operation")
        print("[1] Pull")
        print("[2] Mutation")
        print("[3] Transfer")
        print("[4] History")
        print("[5] Finish")
        pilihan = int(input("Choice   : "))
        if(pilihan == 1) :
            tarik = int(input("Masukkan jumlah penarikan     : "))
            if(saldoA>=tarik) :
                saldo,time,penarikan,saldoA = proxy.pull(saldoA,tarik,time,saldo,penarikan)
                print("Pull succesful!")
            else :
                print("Pull failed! Please check your balance before proceeding or contact us for more information!")
        elif(pilihan == 2):
            i = 0
            print ("\n")
            print("5 latest mutation :")
            if(len(penarikan) <= 5) :
                while(i<len(saldo)) :
                    print(i, ". Saldo keluar sebesar Rp.", penarikan[i], " pada ", time[i], ", sisa saldo : Rp.",saldo[i])
                    i = i + 1
            else :
                i = len(penarikan)-5
                while(i<len(penarikan)) :
                    print(i, ". Saldo keluar sebesar Rp.", penarikan[i], " pada ", time[i], ", sisa saldo : Rp.",saldo[i])
                    i = i + 1
        elif(pilihan == 3) :
            a = int(input("Masukkan nomor rekening      : "))
            b = int(input("Masukkan jumlah transfer     : "))
            print("Transfer ", b, " ke rekening ", a, "?")
            YTransfer = input("Y/T >")
            if (YTransfer == 'Y' and saldoA >= b) :
                rekening, Jtransfer, time2, saldoA, saldo2 = proxy.transfer(rekening,Jtransfer,saldo2,b,a,time2,saldoA)
                print("Transfer succesful!")
            else :
                print("Transfer failed! Please check your balance before proceeding or contact us for more information!")
        elif(pilihan == 4) :
            i = 0
            print ("\n")
            print("Transaction History :")
            while(i<len(rekening)) :
                print(i,". Transaksi transfer ke nomor rekening ", rekening[i], " pada ", time2[i], " dengan jumlah transfer sebesar Rp.", Jtransfer[i], ", sisa saldo : Rp.", saldo2[i])
                i = i + 1
        elif(pilihan == 5) :
            print("Thank you for banking with us!")
            exit()
