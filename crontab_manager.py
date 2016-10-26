import os

'''
Add crontab job

cron: full cron command
     E.g.: 00 09 * * 1-5 echo hello
'''
def add_crontab(cron):
    os.system("crontab -l > mycron.temp")
    os.system("echo '"+cron+"' >> mycron.temp")
    os.system("crontab mycron.temp")
    os.system("rm mycron.temp")
    return True

