from datetime import datetime
import os
import pytz

tz = pytz.timezone(os.getenv('TZ', 'Europe/London'))

current_day = datetime.now(tz).strftime('%A')

if current_day == 'Thursday':
    print('Almost')
elif current_day == 'Friday':
    print('Yep')
else:
    print('Nope')
