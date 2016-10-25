import os
import datetime

EXEC_IPLAYER = './get_iplayer-2.97/get_iplayer'

BBC_NEWS_AT_6_WEEKDAY_PID = 'b07z8429'
BBC_NEWS_AT_10_WEEKEND_PID = 'b009m51q'

RECORDING_DESTINATION = '/home/pi/Downloads/news'
RECORDINGS_SINCE_LAST_X_HOURS = '22'



'''
Get date in the format YYYYmmdd
E.g. 20161025
'''
dateToday = datetime.date.today().strftime("%Y%m%d")

'''
Get day of the week.
where 0 is Sunday and 6 is Saturday
'''
weekday = int(datetime.date.today().strftime("%w"))


command_base = EXEC_IPLAYER+' --file-prefix '+dateToday+' --available-since '+RECORDINGS_SINCE_LAST_X_HOURS+' --modes=hlsvhigh --force -o '+RECORDING_DESTINATION

if(weekday in range(1,5)):
	print 'Recording weekday 6pm evening news.'
	command = command_base + ' --pid='+BBC_NEWS_AT_6_WEEKDAY_PID
	print command
	os.system(command+">"+RECORDING_DESTINATION+"/log/"+dateToday+".log")
else:
	print 'Recording weekend 10pm evening news.'
	command = command_base + ' --pid='+BBC_NEWS_AT_10_WEEKEND_PID
	print command
	os.system(command+">"+RECORDING_DESTINATION+"/log/"+dateToday+".log")


