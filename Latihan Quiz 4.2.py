import random

file = open('coffee.txt','w+')
file.close()

isicof = []

def addco():
    while True:
        cname = input('Input Coffee Name : ')
        if cname.istitle():
            break
        else:
            print('Please Capitalize First Letter of Every Word')
    
    while True:
        try:
            cpric = int(input('Please Input Coffee Price : '))
            cpric = float(cpric)
            break
        except ValueError:
            print('Must be a Number!')

    while True:
        ctype = input('Input Coffee Bean Type [Arabica | Robusta] (Case Sensitive) : ')
        if ctype in ['Arabica','Robusta']:
            break
        else:
            print('Coffee Must Be Arabica or Robusta')

    while True:
        try: 
            cquan = int(input('Input Coffee Quantity : '))
            if cquan >=0:
                break
            else:
                print('Must be a Number Higher or Equal to 0')

        except ValueError:
            print('Must be a Number Higher or Equal to 0')

    cfid = f'CF{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
    
    isoi = [cfid,cname,cpric,ctype,cquan]
    isicof.append(isoi)

    file = open('coffee.txt','w+')
    for a in isicof:
        file.write(f'{a[0]}#{a[1]}#{a[2]}#{a[3]}#{a[4]}\n')
    file.close()


    print('\n')
    print('='*10,'Coffee Details','='*10)
    print(f'{cfid}|{cname}|${cpric}|{ctype}|{cquan}')

    print('Coffee Added Sucessfully!')
    input('Press Enter To Continue....')

def vcof():
    if isicof == []:
        print('='*100)
        print('No Coffe Available, Please Add Coffe First'.center(100))
        print('='*100)
        
        
    else:
        print('='*100)
        print('View All Coffee'.center(100))
        print('='*100)
        print(f'| {'No':<3}| {'ID':<6}| {'Name':<25}| {'Price':<20}| {'Type':<10}| {'Quantity':<10}|')
        print('='*100)
        k = 1 
        for i in isicof:
            print(f'| {k:<3}| {i[0]:<6}| {i[1]:<25}| {i[2]:<20}| {i[3]:<10}| {i[4]:<10}|')
            k+=1
        print('='*100)
        input('Press Enter to Continue....')
        
def pcof():
    if isicof == []:
        print('='*100)
        print('No Coffe Available, Please Add Coffe First'.center(100))
        print('='*100)
    else:
        print('='*100)
        print('Produce Coffee'.center(100))
        print('='*100)
        print(f'| {'No':<3}| {'ID':<6}| {'Name':<25}| {'Price':<20}| {'Type':<10}| {'Quantity':<10}|')
        print('='*100)
        k = 1 
        for i in isicof:
            print(f'| {k:<3}| {i[0]:<6}| {i[1]:<25}| {i[2]:<20}| {i[3]:<10}| {i[4]:<10}|')
            k+=1
        print('='*100)
        while True: 
            try: 
                pcois = int(input(f'Input Coffee Index to be Produced (1-{len(isicof)}): '))
                
                if 1<= pcois <= len(isicof) :
                    pcois -=1
                    
                    while True:
                        try:
                            tamb = int(input('Input Produced Quantity : '))
                            isicof[pcois][4] = isicof[pcois][4] + tamb
                            print(f'Coffe Data : {isicof[pcois][4]}')
                            file = open('coffee.txt','w+')
                            for a in isicof:
                                file.write(f'{a[0]}#{a[1]}#{a[2]}#{a[3]}#{a[4]}\n')
                            file.close()
                            break
                        
                        except ValueError:
                            print('Salah Input')
                    break   
                else:
                    print('Invalid Data')   
            except ValueError:
                print('Invalid Input')
                        
             










while True:
    print('\nMenu')
    print('1. Add New Coffee')
    print('2. View All Coffee')
    print('3. Produce Coffee')
    print('4. Exit')

    try:
        pilih = int(input('>> '))
        if pilih == 1:
            addco()

        if pilih == 2:
            vcof()

        if pilih == 3:
            pcof()

        if pilih == 4:
            print('Exiting....')
            break
    except ValueError:
        print('Must be A Number')