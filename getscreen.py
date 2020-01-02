import numpy as np
import cv2
from mss import mss
from PIL import Image
from getkey import GetKey
from getmouse import GetMouse 
import time
import os

class GetScreen():
    def __init__(self):
        self.sct = mss()
    
        
            
        kobj = GetKey()
        print('Press r and select roi using mouse leftbutton diagonal clicks ')
        while True:
            time.sleep(.5)
            kflag = kobj.checkforkey('r')
            
            if kflag:
                print('\rkey pressed: ',kflag)
                kobj.stop()
                break
            
        mobj = GetMouse()
        pt1=[]
        pt2=[]
        while True:
            time.sleep(.5)
            pts = mobj.getpts()
            pos = mobj.pos
            if len(pts)==1:
                if not pt1:
                    pt1 = pts[0]
                    print('pt1: ',pt1)
                    
                elif not pt2:
                    pt2 = pos
            elif len(pts)==2:
                break
                           
        print('box pts: ',pt1,pt2)
        self.bounding_box = {'top': pt1[1], 'left': pt1[0], 'width': pt2[0]-pt1[0], 'height': pt2[1]-pt1[1]}
        self.t1 = time.time()
        
    def getimg(self):
        t2 = time.time()
        sct_img = np.array(self.sct.grab(self.bounding_box))
        im = cv2.cvtColor(sct_img, cv2.COLOR_BGR2RGB)
        
        print('FPS: {} ',format(1/(t2-self.t1)))
        self.t1=t2
        return im,t2
        
if __name__ == '__main__': 

    dst = 'db'
    if not os.path.exists(dst):
        os.makedirs(dst) 
        
    scobj=GetScreen()
    
    
    while True:
        im,t2 = scobj.getimg()
        cv2.imshow('screen', im)
        
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break
        nam = os.path.join(dst, str(int(t2* 10**7))+'.jpg')
        #import pdb;pdb.set_trace()
        cv2.imwrite(nam,im)
        
        
        
        
        
        
