from pynput import mouse
import time

class GetMouse():
    def __init__(self):
        self.pos = []
        self.pts=[]
        # ...or, in a non-blocking fashion:
        self.listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)
        self.listener.start()
        
        
        
    def stop(self):
        self.listener.stop()
        
    def on_move(self,x, y):
        #print('Pointer moved to {0}'.format((x, y)))
        self.pos=[x,y]

    def on_click(self,x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        
        if pressed:
            self.pts.append([x,y])
            # Stop listener
            #return False

    def on_scroll(self,x, y, dx, dy):
        pass
        #print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
    def getpts(self):
        #get clicked points
        return self.pts
    def clear(self):
        mobj.pts=[]


   
if __name__ == '__main__':       
    mobj = GetMouse()
    while 1:
        time.sleep(.5)
        pts = mobj.getpts()
        if pts:
            print('mobj: ',pts[-1])
        print('current pos: ',mobj.pos)
        
        


