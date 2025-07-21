from DEVICES import *
from time import sleep

class Spray:

    def __init__(self,Field,spray_flag=True):
        self.F_row,self.F_col = Field
        self.Spray_flag  =   spray_flag
        self.F_Matrix    =   [[False for i in range(self.F_row)] for j in range(self.F_col)]
        print(self.F_Matrix)
        self.F_total_plants = self.F_row * self.F_col
        self.F_sprayed = 0
        self.F_plant_skipped = 0
        self.F_completed = 0

    def Start (self):
        RightLeft_flag = True #{True -> next turn Right side False -> next turn Left}
        
        Print("Spray Task Starting....")
        for j in range(self.F_col):
            Print(f"Column: {j} started")
            for i in range(self.F_row):
                if ('Q' in User.raw_read()):
                    Print("Task Quited by User")
                    return ''

                Print(f"Row: {i} Checking....")
                result = DD.Detect()
                self.F_Matrix[j][i] = result
                self.F_completed += 1
                if result == 'Quit':
                    Print("Task Quited by User")
                    return''
                elif result == True:
                    Print("Disease Detected!")
                    if self.Spray_flag == True:
                        F_module.Fert_spray()
                        self.F_sprayed += 1
                        Print("\t Fertilizer Sprayed!")
                    else:
                        self.F_plant_skipped += 1
                        Print("\t Not Sprayed")
                
                elif result == False:
                    Print("Disease not Detected!")
                    self.F_plant_skipped += 1
                    Print("\t Not Sprayed")
                else:
                    Print(f"Invalid result ({result})")
                    self.F_plant_skipped += 1
                    Print("\t Skipped...")

                Automation.MoveNext()
                
            if RightLeft_flag:
                Automation.MoveRight()
            else:
                Automation.MoveLeft()    
            
            RightLeft_flag = not RightLeft_flag

        Print('Task Completed Sucessfuly')
 

    def Result (self):
        pass