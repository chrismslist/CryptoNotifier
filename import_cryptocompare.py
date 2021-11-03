import os #Import OS Package
import cryptocompare #Import Crypto Database API to get Crypto Prices
from pushover import init, Client #Import Mobile Push Service API 
import schedule #Import Scheduling Service for Repeating Functions
import time #Import Time Package to get Current Time
from datetime import datetime #Import DateTime Package to get Date and Time
from colored import fg, bg, attr #Import Colored Package to Color Text

#Define Colors for Colored Text
color = bg('blue') + fg('white')
color2 = bg(0) + fg('green')
reset = attr('reset')


#Define User Parameters
clientChristian = Client("u7qr7w4m9x3jqxg1o1f9829seqokbo", api_token="as15vtro6wm8abbcsm9kf85kxphvwc") 
clientKyle = Client("undjhx9dacw4473ap9oovtka4zvykx", api_token="ahyqq71me344th3j8rvg2vi2nee84o")

#Function w Parameters to Easily Send a Phone Notification
def sendNotification(message, header):
   clientChristian.send_message(str(message), title=str(header))
   clientKyle.send_message(str(message), title=str(header))


#Define Scheduled Job to be Performed, In this Case -> Send Crypto Prices to Phone
def scheduleNotifier():

   #Get Overall Change of DOGE over 24 Hours
   changeOverDay = cryptocompare.get_avg('DOGE', currency='USD', exchange='Kraken')

   #Get Dictionary Values for DOGE Change Over Day
   dogeDictChange = (changeOverDay['CHANGEPCT24HOUR']) #Get Doge 24HR Percent Change from API
   dogeDictChange = ((int)(dogeDictChange * 100 + .5) / 100.0) #Round up Float Value

   #Get Dictionary Values for DOGE
   dogeValues = cryptocompare.get_price('DOGE', currency='USD')

   #Define Dictionary DOGE Values
   doge = (dogeValues['DOGE'])
   dogePrice = (doge['USD'])

   #Send Notifiers Via PushOver
   clientChristian.send_message(str(dogePrice)+ " / "+str(dogeDictChange), title="DogeCoin Price / 24HR Percent Change")
   clientKyle.send_message(str(dogePrice) + " / "+str(dogeDictChange), title="DogeCoin Price / 24HR Percent Change")     

   #Update Time Variables
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S")

   #Print to Console Time and Job Status
   print(str(current_time)+color2+' > Job Completed'+reset)

#Set Interval for Schedule and Run that Schedule
#schedule.every().seconds.do(scheduleNotifier)
schedule.every(1).minutes.do(scheduleNotifier)
#schedule.every().hour.do(scheduleNotifier)
#schedule.every().day.at("10:30").do(scheduleNotifier)

#Clear Console Screen
os.system('cls')

#Get Current Time and Save to Variable
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

sendNotification("Schedule has been Set","--Program Initiated--") #Send Out Push Notification that Program has Started
print(color+'--Schedule Started at '+current_time+"--"+reset) #Push message to Console that Program has Started

#Hold Python Console while Timer is Running
while 1:
   schedule.run_pending()
   time.sleep(1)










