Host Controller
SYS ID: 00



LIB function:

Write(#address_of_Slave_Reg,#data)
    ->Data encoded with datatype
    ->Send() invoked (Read flag as false) 
            ->Chip Select IO HIGH
            ->Data sent through UART channel
            ->Chip Select IO LOW

Read(#address_of_Slave_Reg)
    ->Send() invoked (Read flag as true) 
            ->Chip Select IO HIGH
            ->Data sent through UART channel
            ->Waiting for response from Slave (Max 10 sec)
            ->Chip Select IO LOW
            ->return Data



Task Function:

preTask() #You can directly create task without feild (For Demo)
    -> get No.of.Plants
    -> Move forward untill reaches No.of.Plants


