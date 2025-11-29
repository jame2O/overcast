import sys
import os
import logging
import random
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

lib_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
asset_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'assets')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from lib.waveshare_epd import epd2in7_V2;

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Display Demo")
    epd = epd2in7_V2.EPD()
    
    logging.info("Init, Clear")
    epd.init_Fast()
    epd.Clear()
    
    # Create a blank canvas
    logging.info(f"Display Width: {epd.width}, Display Height: {epd.height}")
    canvas = Image.new('1', (epd.width, epd.height), 255) # 255 = White i.e clear the frame
    drawer = ImageDraw.Draw(canvas)
    
    while True:
        # draw random rect
        x1, x2, y1, y2 = 0,0,0,0
        x1 = random.randint(10, epd.width - 10)
        while (x2 < x1):
            x2 = random.randint(10, epd.width - 10)
        y1 = random.randint(10, epd.height - 10)
        while (y2 < y1):
            y2 = random.randint(10, epd.height - 10)
        drawer.rectangle((x1, y1, x2, y2), outline=0)
        
        #display the image
        epd.display_Fast(epd.getbuffer(canvas))
        
        # Hold the frame for 2 seconds
        time.sleep(1)

        

except IOError as e:
    logging.error(e)
    
except KeyboardInterrupt:
    exit()