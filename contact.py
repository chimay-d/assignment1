class Contact(object):
    
    def edit_cont(self) :
        name = input('Enter name: ')
        fh = open('contact.txt')
        for line in fh :
            line = line.rstrip()
            if line.startswith('Name: ') : 
                nm = line[0] + line[1]
            if nm == ('Name: ') + name  :
                name = input('Name exists, try something unique: ')
        no = input('Enter contact number: ')
        mail = input('Enter email: ')
        while not '@' in mail and '.com' in mail :
            mail = input('Enter correct email: ')
        add = input('Enter address: ')

        fh = open('contact.txt', 'a+')
        fh.write('Name: ' + name + '\t' + 'Number: ' + no + '\t' + 'E-mail: ' + mail + '\t' + 'Address: ' + add + '\n')
        fh.close()

    def srch_cont(self) :
        fh = open('contact.txt', 'r')
        info = input('Enter name/number/mail/address: ')
        f = 0
        for line in fh : 
            line = line.rstrip()
            if info in line :
                print(line) 
                f = 1
        if f == 0 :
            print('No records')
            

def main() :
    print('1. Enter contact')
    print('2. Search contact')
    print('3. Exit')
    ch = input('Enter your choice: ')
    ch = int(ch)
    c = Contact()
    while ch != 3 :
        if ch == 1 :
            c.edit_cont()
            
        else : 
            c.srch_cont()
        
        ch = input('Enter your choice: ')
        ch = int(ch)
    
if __name__ == "__main__":
    main()