from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time)

msg = input('Enter message: ')
typ =  input('Type of message: ')
class log(object):

    def __init__(self, msg, typ):
        fh = open('log.txt','a+')
        #ans = input('Make log? y or n :')
        ans = 'y'
        while ans is 'y' :
            current_time = now.strftime("%H:%M:%S")
            fh.write('Time: ' + str(current_time) + '\n' + 'Type: ' + typ + '\n' + 'Message: ' + msg + '\n\n\n')
            ans = input('Make log? y or n :')
            if ans is 'y' : 
                msg = input('Enter message: ')
                typ =  input('Type of message: ') 
                current_time = now.strftime("%H:%M:%S")
            else : break
        fh.close()

fh = open('log.txt','r')
print(fh)

l = log(msg, typ)

