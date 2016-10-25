import glob, os

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

os.system(command)


