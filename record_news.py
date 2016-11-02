import os, sys, datetime, ConfigParser

EXEC_IPLAYER = './get_iplayer-2.97/get_iplayer'

BBC_NEWS_AT_6_WEEKDAY_KEYWORD = 'BBC News at Six'
BBC_NEWS_AT_10_WEEKEND_KEYWORD = 'BBC Weekend News'

RECORDINGS_SINCE_LAST_X_HOURS = '22'

#Get directory from config
config = ConfigParser.ConfigParser()
config.read('config')
RECORDING_DESTINATION = config.get('Directory', 'RECORDING_DIR')
if not os.path.isdir(RECORDING_DESTINATION):   #Create directory if directory don't exist
	os.makedirs(RECORDING_DESTINATION)

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

command_arguments = ' --file-prefix '+dateToday+' --available-since '+RECORDINGS_SINCE_LAST_X_HOURS+' --modes=hlsvhigh --force -o '+RECORDING_DESTINATION+' --get'

if(!internet()):
    sys.exist()


if(weekday in range(1,5)):
	print 'Recording weekday 6pm evening news.'
	command = EXEC_IPLAYER+' \"'+BBC_NEWS_AT_6_WEEKDAY_KEYWORD+'\" '+ command_arguments
	print command
	os.system(command+">"+RECORDING_DESTINATION+"/log/"+dateToday+".log")
else:
	print 'Recording weekend 10pm evening news.'
	command = EXEC_IPLAYER+' \"'+BBC_NEWS_AT_10_WEEKEND_KEYWORD+'\" '+ command_arguments
	print command
	os.system(command+">"+RECORDING_DESTINATION+"/log/"+dateToday+".log")


