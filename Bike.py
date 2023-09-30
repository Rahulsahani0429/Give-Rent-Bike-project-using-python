class Bikerate:
    def __init__(self,stoke):
        self.stoke=stoke
    def displayBike(self):
        print("total bike",self.stoke)
    def ranteforBike(self,q):
        if q<=0:
            print("enter the postive number or greater than zero")
        elif q>self.stoke:
            print("enter the valied value (less the stoke(q))")
        else:
            self.stoke=self.stoke-q
            print("total prices",q*100)
            print("total bike",self.stoke)


while True:
    ojb=Bikerate(100)
    jan=int(input('''
1 Display stocks
2 Rent a Bike
3 Exit
                  
'''))
    if jan==1:
        ojb.displayBike()
    elif jan==2:
        n=int(input('enter the Qty:---'))
        ojb.ranteforBike(n)
    else:
        break




    