
from datetime import date

def date_separate(msg):
    msg_list = msg.split(" ")
    today_time = date.today()
    year,month,day = today_time.year,today_time.month, today_time.day
    for msg_elem in msg_list:
        
