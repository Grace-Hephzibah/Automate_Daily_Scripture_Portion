import time
from year import year

import pywhatkit as wk


def text_required():
    month = time.gmtime().tm_mon - 1
    day = time.gmtime().tm_mday - 1

    today_text = f'Today\'s Bible Portion : {year[month][day]}'
    return today_text

