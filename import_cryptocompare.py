import cryptocompare #Import Crypto Database API
from pushover import init, Client #Import Mobile Push Service API
#Define User Parameters
clientChristian = Client("u7qr7w4m9x3jqxg1o1f9829seqokbo", api_token="as15vtro6wm8abbcsm9kf85kxphvwc") 
clientKyle = Client("undjhx9dacw4473ap9oovtka4zvykx", api_token="ahyqq71me344th3j8rvg2vi2nee84o")

from apscheduler.schedulers.blocking import BlockingScheduler



def push_notification_crypto():
    print(cryptocompare.get_price('BTC', currency='USD'))
    
    #Get Index Values for Bitcoin
    crypto = cryptocompare.get_price('BTC', currency='USD')
    #Get Overall Change of BTC over 24 Hours
    change = cryptocompare.get_avg('BTC' 'CHANGE24HOUR')

    crypto1 = (crypto['BTC'])
    crypto2 = (crypto1['USD'])

    print(crypto2)
    print(change)

    dogeValues = cryptocompare.get_price('DOGE', currency='USD')
    doge = (dogeValues['DOGE'])
    dogePrice = (doge['USD'])

    clientChristian.send_message(dogePrice, title="Current DogeCoin Price")

    clientKyle.send_message(dogePrice, title="Current DogeCoin Price")
    

scheduler = BlockingScheduler()
scheduler.add_job(push_notification_crypto, 'interval', hours=1)
scheduler.start()





