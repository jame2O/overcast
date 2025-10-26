import sys
import os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
assets_dir = os.path.join(ROOT_DIR, 'assets')
libdir = os.path.join(ROOT_DIR, 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7_V2  # type: ignore
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Initializing & Configuring Display...")
    epd = epd2in7_V2.EPD()
    epd.init()
    epd.Clear()
    
    logging.info("Loading Fonts...")
    font_12 = ImageFont.truetype(os.path.join(assets_dir, 'fonts/BigBlueTerm.ttf'), 12)
    font_16 = ImageFont.truetype(os.path.join(assets_dir, 'fonts/BigBlueTerm.ttf'), 16)
    font_20 = ImageFont.truetype(os.path.join(assets_dir, 'fonts/BigBlueTerm.ttf'), 20)
    
    logging.info("Starting Main Loop & Initializing Modules...")
    i = 0
    while (i < 10):
        base_img = Image.new('1', (epd.height, epd.width), 255)
        draw = ImageDraw.Draw(base_img)
        draw.text((10, 20), "Welcome to Overcast.", font = font_20, fill = 0)
        draw.text((10, 50), "The time is:", font = font_16, fill=16)
        draw.text((50, 50), time.strftime('%H:%M:%S'), font=font_16, fill=0)
        
        epd.display_Partial(epd.getbuffer(base_img), 110, epd.height - 120, 150, epd.height-10)
        i+=1
        
except KeyboardInterrupt:
    logging.info("Exiting.")
    epd2in7_V2.epdconfig.module_exit(cleanup=True)
    exit()