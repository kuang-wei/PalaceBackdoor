import requests
import webbrowser
import datetime as dt
from bs4 import BeautifulSoup
from time import sleep
from random import uniform

def Scheduler(second, testbool=False):
	if testbool:
		today = (dt.datetime.today() + 
				 dt.timedelta(0,2)).strftime('%Y-%m-%d-%H-%M-%S').split('-')
		TriggerTime = dt.datetime(int(today[0]), int(today[1]),
								  int(today[2]), int(today[3]), int(today[4]), 
								  int(today[5]))
	else:
		today = dt.datetime.today().strftime('%Y-%m-%d-%H-%M-%S').split('-')
		TriggerTime = dt.datetime(int(today[0]), int(today[1]),
								  int(today[2]), 9, 59, 
								  int(second))

	print '\nBot scheduled at', TriggerTime.strftime('%H:%M:%S')
	print 'Current time:   ', dt.datetime.now().strftime('%H:%M:%S')
	sleep((TriggerTime-dt.datetime.now()).total_seconds())
	return None

def GetFirstNew():
	newurl = 'https://shop-usa.palaceskateboards.com/collections/new'
	r = requests.get(newurl)
	soup = BeautifulSoup(r.content, "lxml")
	newitemfound = False
	while not newitemfound:
		try:
			newitem = soup.find("div", {"class": "product-grid-item clearfix"})
			newitemfound = True
		except:
			newitem = ''
			delaytime = uniform(0.5, 2.0)
			print "Can't fetch the first new item, delay for %.2f s"%delaytime
			sleep(delaytime)
	return str(newitem)

def ChangeDetection(OldItem):
	NewItem = GetFirstNew()
	while NewItem==OldItem:
		delaytime = uniform(0.5, 2.0)
		print 'Found the same first new item, delay for %.2f s'%delaytime
		sleep(delaytime)
		NewItem = GetFirstNew()
	print '\nNew drop detected at', dt.datetime.now().strftime('%H:%M:%S')
	return None

def BackdoorOpen(keyword, targetsize):
	carturl = 'https://shop-usa.palaceskateboards.com/cart/'
	itemurl = ('https://shop-usa.palaceskateboards.com/products/'+keyword)
	now = dt.datetime.now
	ritem = requests.get(itemurl+'.xml')
	itemsoup = BeautifulSoup(ritem.content, "lxml")
	itemsxml = itemsoup.find_all("variant")
	for item in itemsxml:
		if item.find("title").text.lower() == targetsize:
			targetid = item.find("id").text
			print "Size matched at", now().strftime('%H:%M:%S')

	print "\nOpening backdoor link at", now().strftime('%H:%M:%S')
	print 'Backdoor link:', (carturl+targetid+":1")
	webbrowser.open(carturl+targetid+":1")
	print "Succesfully opened link at", now().strftime('%H:%M:%S')
	return (carturl+targetid+":1")

def main():
	newurl = 'https://shop-usa.palaceskateboards.com/collections/new'
	olditem = GetFirstNew()
	keyword = raw_input('Target keyword (i.e. block-hood-black)? ')
	targetsize = raw_input('Target size (i.e. medium)? ')
	test = input('Test run (True/False)? ')

	if not test:
		startsecond = input('Start bot at 09:59:x (x from 0 to 59)? ')
		Scheduler(startsecond, test)
		print 'Bot starting at', dt.datetime.now().strftime('%H:%M:%S'), '\n'
		ChangeDetection(olditem)
	else:
		_ = raw_input('Start now (hit ENTER)? ')
		startsecond = 0
		Scheduler(startsecond, test)
		print '\nBot starting at', dt.datetime.now().strftime('%H:%M:%S'), '\n'

	BackdoorOpen(keyword, targetsize)
	return None

if __name__ == '__main__':
	main()