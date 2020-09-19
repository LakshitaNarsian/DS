def Tower_of_Hanoi(disk , src, dest, auxiliary): 
    if disk==1: 
        print("Transfer disk 1 to destination ",dest," from source ",src) 
        return
        Tower_of_Hanoi(disk-1, src, auxiliary, dest) 
    print("Transfer disk",disk,"to destination",dest,"from source",src) 
    Tower_of_Hanoi(disk-1, auxiliary, dest, src) 
          
disk = int(input("How many rings you want to search.?"))
Tower_of_Hanoi(disk,'L','A','K')
