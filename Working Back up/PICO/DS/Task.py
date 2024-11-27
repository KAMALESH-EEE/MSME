from Feild import fields
from MyDevices import DS,SM,RV,HC,Input,Print,com
from time import sleep

class Fert_Spray:

    def __init__(self,Qunt,F):
        self.Qunt=Qunt
        self.Num=F.no_plant
        self.F_Sprayed=0
        self.F_skiped=0
        self.f=F

    def __str__(self):

        return f'Fertilizer Sprayer->completed {self.F_Sprayed + self.F_skiped}/{self.Num}'
    
    def Spray(self):
        HC.write('Robot is ready to do task\n')
        #HC.write('Waiting for your command:\n')
        T,h=SM.DHT()
        d=f'Tem: {T}, Hum: {h}'
        Print(d)
        Print('Waiting for remote command\n do-> start the task \n exit -> end the task')
        while True:
            if HC.any():
                t=str(HC.read()).split("'")
                n=t[1]
                if n=='do':
                    break
                elif n=='exit':
                    return 0
            sleep(0.5)
            
        p=True
        for j in range(self.f.row):
            print('Next Rows')
            for i in range(self.f.col):
                if HC.any():
                    n=Input('')
                    if n=='exit':
                        return (self.F_Sprayed)
                print("DS>MOVE")
                sleep(2)
                DS.forward()
                Print("running")
                sleep(5)
                DS.stop()
                of=True
#                 while True:
#                     dis=int(SM.dis())
#                     if dis<=25:
#                         DS.stop()
#                         Print('Obstracal Detected')
#                         while True:
#                             try:
#                                 dis=int(SM.dis())
#                             except:
#                                 dis = 5
#                             if dis>35:
#                                 break
#                             sleep(1)
                pf=RV.detect()
                if HC.any():
                    n=Input('')
                    if n=='sk':
                        n='S'
                        
                    if n=='sp':
                        n='D'
                        
                    if n=='exit':
                        return (self.F_Sprayed)
        
                else:
                    n='S'

                    if pf:
                        n='D'
    
                    else:
                        n='S'
        
                
                
                if n=='D':
                    print("FS>SPRAR")
                    Print("Dis detected and Fert is Sparying")
                    SM.Spray()
                    self.F_Sprayed+=1
                else:
                    Print('No Disease deteced')
                    self.F_skiped+=1
#             print('DS>turn')
#             Print('Turnning')
                    
        return (self.F_Sprayed)
            

task =[Fert_Spray]

def create_task():
    global task,fields
    i=0
    f=fields[0]
    #try:
    for f in fields:
        Print(f'{i}->{f.name}')
        i+=1
    f=fields[int(Input('Enter Field ID:'))]
    ch=int(Input('\tTask\n1->Fertilizer Spray\n2->Seeding\nEnter choice no:'))
#     except:
#         
#         Print('Error')
#         return
    if ch==1:
        ts = Fert_Spray(0.5,f)
        Print(f'Task Created in {f.name} Field')
        ts.Spray()
        S=str(ts)
        print(S)
        Print(S+"\n")
        S=(f'Sprayed: {ts.F_Sprayed} Skipped: {ts.F_skiped}')
        print(S)
        Print(S+"\n")

#create_task()
        
def preTask():
    t=int(Input('Enter No.of.Plant:'))
    
    for i in range(t):
        DS.forward()
        Print("Moving")
        time.sleep(5)
        
        
    