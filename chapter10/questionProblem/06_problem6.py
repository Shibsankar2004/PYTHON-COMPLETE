from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    def book(shib,fro,to):
        print(f"Ticket is booked in train no:{shib.trainNo} from {fro} to {to}")
    def getstatus(shib):
        print(f"Train no: {shib.trainNo} is running on time")
    def getFare(shib,fro,to):
        print(f"Ticket fare in train no:{shib.trainNo} from {fro} to {to} is {randint(222,56767)}")

t=Train(12345)
t.book("Berhampore","sealdaha")
t.getstatus()
t.getFare("Berhampore","sealdaha")