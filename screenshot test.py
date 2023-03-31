from PIL import ImageGrab
import time
from screeninfo import get_monitors
#time.sleep(5)
#image = ImageGrab.grab(bbox=(0,0,1920,1080))
#image.save('sc.png')
for i in get_monitors():
    print(str(i))