data={0:{'name':'status'}}
def menu():
    s=int(input("Enter:\n1 - Adding tasks\n2 - Updating tasks\n3 - Deleting Tasks\n4 - Listing All Tasks\n5 - Searching Tasks\n6 - Listing Tasks by Last Letter\n0 - exit\n"))
    match(s):
        case 1:
            Id=int(input('enter id : '))
            name=input("enter name : ")
            status=input("enter status : ")
            add(name,Id,status)
            menu()
            print("TASK ADDED")
        case 2:
            Id=int(input('enter id for which data to be updated: '))
            name=input("enter name : ")
            status=input("enter status : ")
            add(name,Id,status)
            print("UPDATED")
            menu()
        case 3:
            name=input("enter name to be deleted: ")
            delete(name)
            print("DELETED")
            menu()
        case 4:
            display()
            menu()
        case 5:
            Id=int(input('enter id : '))
            search(Id)
            menu()
        case 6:
            lastletter=input("enter last letter : ")
            print_bylast(lastletter)
            menu()
            
            
        
def add(name,Id,status):
    data[Id]=[name,status]
    
def delete(name):
    pass

def display():
    for key in data:
        print(key,' : ',data[key])
        
def search(Id):
    for key in data:
        if(Id==key):
            for subkey in data[key]:
                print(f"Id : {key}\nname : {subkey}\nstatus : {data[key][subkey]}")

def print_bylast(lastletter):
    pass
    
menu()
print(data)
