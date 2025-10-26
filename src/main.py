import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7_V2 
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Initializing")
    epd = epd2in7_V2.EPD()
    
    logging.info
except KeyboardInterrupt:
    logging.info("Exiting.")
    epd2in7_V2.epdconfig.module_exit(cleanup=True)
    exit()