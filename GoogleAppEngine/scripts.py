months=[ "January","February", "March", "May", "June", "July", "August", "September", "October", "November", "December"]
months_abbvs = dict( (m[:3].lower(), m) for m in months )
print months_abbvs


def valid_month(month):
	if month:
		short_month = month[:3].lower()
		return months_abbvs.get(short_month, None)

print valid_month('january')


def valid_day(day):
	ret = None
	if day.isdigit():
		int_day = int(day)
		if int_day in [x+1 for x in range(31)]:
			ret = int_day
	return ret

def valid_year(year):
	ret = None
	if year.isdigit():
		int_year = int(year)
		if int_year >= 1900 and int_year <=2020:
			ret = int_year
	return ret	

print valid_year('13')
print valid_year('43.5')
print valid_year('xoxo')
print valid_year('2000')
