list_student = [19,27,62,24,21,2,51]
print("Insertion sort")

for i in range(len(list_student)):
    
    value = list_student[i]
    
    j = i-1
    
    while j >= 0 and value < list_student[j]:
        
        list_student[j+1] = list_student[j]
        j -= 1
        
    list_student[j+1] = value

print(list_student)

print("\n\nSelection sort")

for i in range(len(list_student)):
    min_val_index = i
    for j in range(i+1,len(list_student)):
        if list_student[min_val_index] > list_student[j]:
            min_val_index = j
            
    list_student[i], list_student[min_val_index] = list_student[min_val_index],list_student[i]
    
print(list_student)


print("\n\nBubble sort")

list_of_number = [19,26,44,58,10,60,58,98,87]

def bubbleSort(list_of_number):
    
    for i in range(len(list_of_number) - 1):
        
        for j in range(0, len(list_of_number)-i-1):
            
            if list_of_number[j] > list_of_number[j+1]:
                list_of_number[j], list_of_number[j+1] = list_of_number[j+1], list_of_number[j]
                
bubbleSort(list_of_number)
print(list_of_number)
