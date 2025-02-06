import ujson
from MyDevices import Input,Print

class Fields:
    def __init__(self, name, row, col,no_plant, crop):
        self.name = name
        self.row  = row
        self.col  = col
        self.no_plant=no_plant
        self.crop=crop

def Write(objects):
    serialized_data = []
    for obj in objects:
        serialized_data.append(obj.__dict__)
    
    try:
        with open('myFeilds.json', "w") as file:
            ujson.dump(serialized_data, file)
    except :
        print("Error during serialization:")
        
def Read(object_class):
    try:
        with open('myFeilds.json', "r") as file:
            serialized_data = ujson.load(file)
            objects = [object_class(**data) for data in serialized_data]
            return objects
    except:
        print("Error during Deserialization:")

def Create_field():
    name=Input('Name of Field:')
    row =int(Input('Row'))
    col =int(Input('colume:'))
    n=row*col
    c=Input('crop name:')
    obj=Fields(name,row,col,n,c)
    fields.append(obj)
    Write(fields)
    print("Field created")
    Print('Field created sucessfully')
    
def Mode():
    global fields
    Print('--*Field Control Mode*--')
    while True:
        Print('       Menu')
        op=int(Input('1-> New Field\n2-> Field Details\n3-> Delete Field\n0-> Exit to main loop'))
        if op ==1:
            Create_field()
            
        elif op==2:
            i=0
            for f in fields:
                Print(f'{i}->{f.name}')
                i+=1
            f=fields[int(Input('Enter Field ID:'))]
            Print(f'Name         : {f.name}')
            Print(f'No of Plants : {f.no_plant}')
            Print(f'No of Rows   : {f.row}')
            Print(f'No of columns: {f.col}')
            Print(f'Crop         : {f.crop}\n')
            
        elif op==3:
            i=0
            for f in fields:
                Print(f'{i}->{f.name}')
                i+=1
            j=int(Input('Enter Field ID to Delete:'))
            f=fields[j]
            t=Input(f'Are you sure to delete {f.name} field [Y/N]')
            if t=='Y':
                fields.pop(j)
                Write(fields)
                Print('Field Deteled Sucessfully')
            
        elif op==0:
            return   
    
fields=Read(Fields)
