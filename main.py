import re
import time
import random
import plyer

f = open ('log.txt', 'r', encoding='utf-8')
    
text = f.readlines()


while True:
    random_line = random.randint(0,98)
    res = re.sub(r'\s+', ' ', text[random_line])

    print(type(res))
    print(res)

    plyer.notification.notify( title = "Learn New English Words", message=res, app_name = 'Reminder App Made By Jainesh',timeout=5)

    time.sleep(60*60)

f.close()