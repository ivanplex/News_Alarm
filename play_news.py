import glob, os, time_reader, crontab_manager


FILE_DIR = "/home/pi/Downloads/news"

os.chdir(FILE_DIR)

'''
Sort and import all news into a list
'''
news_list = []
for news_file in sorted(glob.glob("*.ts")):
    news_list.append(news_file)

'Remove news older than 3 days'
while (len(news_list) > 3):
	oldest_news = news_list.pop(0)
	os.system("rm "+oldest_news)

lastest_news = news_list[-1]

command = "totem --fullscreen "+FILE_DIR+"/"+lastest_news

#os.system(command)

'''
Get time from time.txt
'''
with open("time.txt", 'r') as timefile:
    time = timefile.read().splitlines()[0]
timefile.close()


#print time
formatted_time = time_reader.simple_string_to_time(time)
hour = formatted_time[0]
minute = formatted_time[1]

cron = minute+" "+hour+ " * * 1-5 "+command
print cron
crontab_manager.add_crontab(cron)

