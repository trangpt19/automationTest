from datetime import date, datetime, timedelta
import random
import HTMLParser

def Is_Leap_Year(year):
    """return True if leap year; else False"""
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
	    return True
    else:
        return False	
		
def ASCII_String_Decode(ascii_str):
    """return string contain ascii character"""
    h = HTMLParser.HTMLParser()
    return h.unescape(ascii_str)

def UTF8_String_Decode(str):
    return str.decode('UTF-8')
	
def Get_Random_Key_From_Dict(dict):
    """return a random key from given dictionary"""
    return ASCII_String_Decode(random.choice(dict.keys()))	
	
def Get_Random_Value_From_Dict(dict):
    """return a random value from given dictionary"""
    return ASCII_String_Decode(random.choice(dict.values()))
	
def Get_Random_Item_From_List(list):
    """return a random item from given list"""
    return random.choice(list)
	
def Get_Intended_Travel_Date(no_of_days):
    """return a date in future from current"""
    no_of_days=int(no_of_days)
    tmpdate = datetime.today() + timedelta(days=no_of_days)
    tmpdate=str(tmpdate)
    newdate=tmpdate[:10]
    newdate=newdate.split("-")
    intended_date=newdate[2]+'-'+newdate[1]+'-'+newdate[0]
    return str(intended_date)
	
def Get_Future_Date(no_of_days):
    """return a date in future from current
	Example current date: 2015-09-03
	on_of_days = 5
	return future date: 08/09/2015"""
    no_of_days=int(no_of_days)
    tmpdate = datetime.today() + timedelta(days=no_of_days)
    tmpdate=str(tmpdate)
    newdate=tmpdate[:10]
    newdate=newdate.split("-")
    intended_date=newdate[2]+'/'+newdate[1]+'/'+newdate[0]
    return str(intended_date)

def Is_One_Year_Passed(strdate):
    """return true if 1 year passed from the given date"""
    cdate = datetime.strptime(strdate, '%d-%m-%Y')
    tmpdate = cdate + timedelta(days=365)
    return datetime.today() > tmpdate