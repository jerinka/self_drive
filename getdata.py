import numpy as np
import cv2
from mss import mss
from PIL import Image
from getkey import GetKey
from getmouse import GetMouse 
from getscreen import GetScreen
import time
import os
import sys

def compare_imgs(im1,im2):
    if (im1 is None) or (im2 is None) :
        return False
    else:
        difference = cv2.subtract(im1, im2)    
        result = not np.any(difference)
        return result


if __name__ == '__main__': 

    dst = 'db'
    if not os.path.exists(dst):
        os.makedirs(dst) 
        
    scobj=GetScreen()
    kobj = GetKey()
    cv2.namedWindow('crop', cv2.WINDOW_NORMAL)
    im1=None
    while True:
        im,t2 = scobj.getimg()
        keys = kobj.get_pressed_keys()
        
        
        
        #import pdb;pdb.set_trace()
        if (not compare_imgs(im1,im)) or keys :
            
            im1=im
            cv2.imshow('crop', im)

            str1 = ''
            keys2=[]

            if keys:
                keys2.append('_')
                for key in keys:
                    keys2.append(key)
                    keys2.append('_')
                str1 = str1.join(keys2)
                print('Keys pressed: ',str1)
                #import pdb;pdb.set_trace()
                
            
            if cv2.waitKey(50) == 27:
                cv2.destroyAllWindows()
                break
            nam = os.path.join(dst, str(int(t2* 10**7)) +str1+'.jpg')
            cv2.imwrite(nam,im)
        if keys:
            if keys[-1]=='esc':
                break
        
    
    sys.stdout.flush()
    print('getdata end')
            
        
        
        
