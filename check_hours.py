from datetime import datetime, timezone, timedelta

def check():
	tz = timezone(timedelta(hours=-7))
	now = datetime.now(tz)
	td = now - datetime(2020, 9, 19, tzinfo = tz)
	weeks = td.days//7
	if now > datetime(2020,12,19, tzinfo = tz):
		vac = now - datetime(2020,12,19, tzinfo = tz)
		weeks -= min(vac.days,21)//7
	hours = weeks * 26
	if now > datetime(2020, 12, 19, tzinfo = tz) and now < datetime(2021, 1, 7, tzinfo = tz):
		pass
	elif now > datetime(2021, 1, 7, tzinfo = tz) and now < datetime(2021, 1, 9, tzinfo = tz):
		if now.weekday() == 3 and now.hour >= 10:
			hours += min(now.hour - 9, 4) 
		elif now.weekday() == 4:
			hours += 4
			if now.hour >= 8:
				if now.hour < 15:
					hours += min(now.hour - 7, 6) 
				else:
					hours += min(now.hour - 14, 2) + 6
	else:
		if now > datetime(2021,1,9, tzinfo = tz):
			hours += 12
		if now.weekday() == 0 and now.hour >= 13:
			if now.hour < 16:
				hours += 1
			else:
				hours += 2
		elif now.weekday() in [1,3]:
			hours += 2 + (now.weekday()//3)*12
			if now.hour >= 10:
				hours += min(now.hour - 9, 4) 
		elif now.weekday() in [2,4]:
			hours += 6 + (now.weekday()//4)*12
			if now.hour >= 8:
				if now.hour < 15:
					hours += min(now.hour - 7, 6) 
				else:
					hours += min(now.hour - 14, 2) + 6
	return hours