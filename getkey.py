from pynput import keyboard
import time
import sys
'''
class to manage keypress, returns keys that wr pressed on being continued to be pressed after last keypress read call. 
'''
class GetKey():
    def __init__(self):
        self.keyp=[]#
        self.keyr=[]
        
        # ...or, in a non-blocking fashion:
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()
    def stop(self):
        print('stopping listener')
        self.listener.stop()
    def on_press(self,key):
        try:
            if key.char not in self.keyp:
                self.keyp.append(key.char)
                #print(' {0} pressed'.format(self.keyp))
            
        except AttributeError:
            #self.keyp.append(key.char)
            print('special key {0} pressed'.format(key))
            if key == keyboard.Key.esc:
                # Stop listener
                print('esc pressed')

    def on_release(self,key):
        try:
            if key.char not in self.keyr:
                    self.keyr.append(key.char)
            #print('{0} released'.format(self.keyr))
        except AttributeError:
            print('special key {0} released'.format(key))
            
    def get_pressed_keys(self):
        #returns keys pressed 
        k=self.keyp
        #print(' {0} pressed2'.format(self.keyp))
        #print('{0} released2'.format(self.keyr))
        self.keyp=list(set(self.keyp)-set(self.keyr))
        self.keyr=[]
        return k
        
    def checkforkey(self,key):
        #checks if a key is pressed
        keys = self.get_pressed_keys()
        print('\rkeys pressed: ',keys, end='')
        #sys.stdout.flush()
        if key in keys:
            return True
        else:
            return False
            
if __name__ == '__main__':       
    kobj = GetKey()
    while 1:
        time.sleep(.5)
        
        keys = kobj.get_pressed_keys()
        print('Keys pressed: ',keys)
        
        '''
        kflag = kobj.checkforkey('r')
        print('kflag: ',kflag)
        '''
    

    
    





