:from webbrowser import open_new
from datetime import datetime
def get_current_time_hh_mm():
    now = datetime.now()
    return now.strftime("%H:%M")
time=get_current_time_hh_mm()
while time=='09:28':
    open_new('https://netacad.webex.com/netacad/j.php?MTID=mfa0f4792b3511fc25bc0ff4d98403231')
    time=get_current_time_hh_mm()