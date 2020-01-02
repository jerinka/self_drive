import numpy as np
import cv2
from mss import mss
from PIL import Image
from getkey import GetKey
from getmouse import GetMouse 
from getscreen import GetScreen
import time
import os


if __name__ == '__main__': 

    dst = 'db'
    if not os.path.exists(dst):
        os.makedirs(dst) 
        
    scobj=GetScreen()
    kobj = GetKey()
    
    
    while True:
        im,t2 = scobj.getimg()
        cv2.imshow('screen', im)
        
        keys = kobj.get_pressed_keys()
        str1 = "" 
  
        # using join function join the list s by  
        # separating words by str1 
        str1 = str1.join(keys) 
        print('Keys pressed: ',str1)
        
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break
        nam = os.path.join(dst, str(int(t2* 10**7)) +'_'+ str1+'.jpg')
        #import pdb;pdb.set_trace()
        cv2.imwrite(nam,im)
        
        
        
        
        
        
