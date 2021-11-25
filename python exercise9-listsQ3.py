defaultList=['a','b','c','d','c']


while True:
    print('''
    1.Append an element
    2.Insert an element
    3.Append a list to the given list
    4.Modify an existing element
    5.Delete an existing element from its position
    6.Delete an existing element with a given value
    7.Sort the list in the ascending order
    8.Sort the list in descending order
    9.Display the list.
    ''')
      
    order=input('Please enter your choice(1-9): ')
    
    if order=='0':
        print('Good luck')
        break
    
    if order=="1":
        while True:
            print('''***************************
Option 1: Append an element
***************************''')
            element=input('Enter the element to be appended: ')
              #if element=='0':
                  #break
            print('List before operation: ',defaultList)
            defaultList.append(element)
            print('List after operation: ',defaultList)
            repeat=input("\nHit Enter to append another element or 0 to return to menu: ")
            if repeat=="0":
                break
        
    elif order=="2":
        while True:
            print('''***************************
Option 2: Insert an element
***************************''')
            element=input('Enter the element to be inserted: ')
            position=int(input('Enter the position: '))
            print('List before operation: ',defaultList)
            defaultList.insert(position,element)
            print('List after operation: ',defaultList)
            repeat=input("\nHit Enter to insert another element or 0 to return to menu: ")
            if repeat=="0":
                break

    elif order=="3":
        while True:
            print('''***************************
Option 3: Append a list to the given list
***************************''')        
            element=input('Enter the list to append: ')
            print('List before operation: ',defaultList)
            count=0
            pos=0        
            while count<len(element):                  
                if element[count]==',':
                    defaultList.append(element[pos:count])
                    pos=count+1
                count=count+1
                if count==len(element):
                    defaultList.append(element[pos:count])        
                    print('List after operation: ',defaultList)
                   
            repeat=input("\nHit Enter to append another list or 0 to return to menu:")
            if repeat=="0":
                break                
                
    if order=="4":
        while True:
            print('''***************************
Option 4: Modify an existing element
***************************''')
            position=int(input('Enter the position of the element to be modified: '))
            element=input('Enter the new value for the element: ')
            print('List before operation: ',defaultList)
            defaultList[position]=element
            print('List after operation: ',defaultList)
            repeat=input("\nHit Enter to modify another element or 0 to return to menu: ")
            if repeat=="0":
                break

    if order=="5":
        while True:
            print('''***************************
Option 5: Delete an existing element from its position
***************************''')
            pos=int(input('Enter the position of the element to delete: '))
            if pos>len(defaultList)-1:
                print('\nInvalid position!!!!\n')
            else:
                print('List before operation: ',defaultList)
                defaultList.pop(pos)
                print('List after operation: ',defaultList)
            repeat=input("\nHit Enter to delete another element or 0 to return to menu: ")
            if repeat=="0":
                break

    if order=="6":
        while True:
            print('''***************************
Option 6: Delete an existing element with a given value
***************************''')
            value=input('Enter the value of the element to delete : ')
            numOfTimes=defaultList.count(value)
            print('List before operation: ',defaultList)
            for i in range (numOfTimes):
                defaultList.remove(value)
            print('List after operation: ',defaultList)
            repeat=input("\nHit Enter to delete another element or 0 to return to menu: ")
            if repeat=="0":
                break

    if order=="7":
        while True:
            print('''***************************
Option 7: Sort the list in ascending order
***************************''')
            print('List before operation: ',defaultList)
            defaultList.sort()
            print('List after operation: ',defaultList)
            repeat=input("\nHit Enter to sort again or 0 to return to menu: ")
            if repeat=="0":
                break

    if order=="8":
        while True:
            print('''***************************
Option 8: Sort the list in descending order
***************************''')
            print('List before operation: ',defaultList)
            defaultList.sort(reverse=True)
            print('List after operation: ',defaultList)
            repeat=input("\nHit Enter to sort again or 0 to return to menu: ")
            if repeat=="0":
                break
                
    if order=="9":
        while True:
            print('''***************************
Option 9: Display the list
***************************''')
            print('List is: ',defaultList)
            repeat=input("\nHit Enter to display again or 0 to return to menu: ")
            if repeat=="0":
                break
