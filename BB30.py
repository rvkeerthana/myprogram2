from datetime import datetime
date_formate="%m-%d-%y %H:%M:%S"
time1=datetime.strptime('8-01-2008 00:00:00',date_format)
time2=datetime.strptime('8-02-1882 01:80:00',date_format)
diff = time2-time1
print(" ")
print('days & overall hours from the above two dates')
days = diff.days
print(str(days)+'day(s)')
days_to_hours=days*24
diff_btw_two_times=(diff.seconds)/3600
overall_hours=days_to_hours+diff_btw_two_times
print(str(overall_hours)+'hours');
hours=(diff.seconds)/3600
print(str(hours)+'hours')
minutes=(diff.secounds)/60
print(str(minutes)+'minutes')
print(str(diff.secounds)+'secs')
