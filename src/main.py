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
    
    epd.init_Fast()
    Limage = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(Limage)
    draw.text((2, 0), 'Hello James :)', font = font_20, fill = 0)
    time.sleep(5)
        
except KeyboardInterrupt:
    logging.info("Exiting.")
    epd2in7_V2.epdconfig.module_exit(cleanup=True)
    exit()