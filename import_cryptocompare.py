import os
import cryptocompare #Import Crypto Database API
from pushover import init, Client #Import Mobile Push Service API
import schedule
import time

#Define User Parameters
clientChristian = Client("u7qr7w4m9x3jqxg1o1f9829seqokbo", api_token="as15vtro6wm8abbcsm9kf85kxphvwc") 
clientKyle = Client("undjhx9dacw4473ap9oovtka4zvykx", api_token="ahyqq71me344th3j8rvg2vi2nee84o")

#Define Scheduled Job to be Performed, In this Case -> Send Crypto Prices to Phone
def scheduleNotifier():
   #Print Current DOGE Dictionary Value to Console
   print(cryptocompare.get_price('DOGE', currency='USD'))

   #Get Overall Change of DOGE over 24 Hours
   changeOverDay = cryptocompare.get_avg('DOGE', currency='USD', exchange='Kraken')

   #Get Dictionary Values for DOGE Change Over Day
   dogeDictChange = (changeOverDay['CHANGEPCT24HOUR']) #Get Doge 24HR Percent Change from API
   dogeDictChange = ((int)(dogeDictChange * 100 + .5) / 100.0) #Round up Float Value

   #Print Change over Day Values for DOGE
   print(changeOverDay)

   #Get Dictionary Values for DOGE
   dogeValues = cryptocompare.get_price('DOGE', currency='USD')

   #Define Dictionary DOGE Values
   doge = (dogeValues['DOGE'])
   dogePrice = (doge['USD'])

   #Send Notifiers Via PushOver
   clientChristian.send_message(str(dogePrice) + " / "+str(dogeDictChange), title="DogeCoin Price / 24HR Percent Change")
   clientKyle.send_message(str(dogePrice) + " / "+str(dogeDictChange), title="DogeCoin Price / 24HR Percent Change")     

#Set Interval for Schedule and Run that Schedule
#schedule.every().seconds.do(scheduleNotifier)
schedule.every(1).minutes.do(scheduleNotifier)
#schedule.every().hour.do(scheduleNotifier)
#schedule.every().day.at("10:30").do(scheduleNotifier)

os.system('cls')
print('--Schedule/s Started--')

while 1:
   schedule.run_pending()
   time.sleep(1)










