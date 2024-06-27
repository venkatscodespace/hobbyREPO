from datetime import datetime
from webbrowser import open_new
from datetime import datetime
import time
def get_current_time_hh_mm():
    now = datetime.now()
    return now.strftime("%H:%M")
target_time = '09:56'
opened = False
while not opened:
    current_time = get_current_time_hh_mm()
    if current_time == target_time:
        open_new('https://netacad.webex.com/netacad/j.php?MTID=mfa0f4792b3511fc25bc0ff4d98403231')
        opened = True
    time.sleep(30)  # Check every 30 seconds
