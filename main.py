from telegram.ext import Updater, CommandHandler, RegexHandler, MessageHandler,Filters
from random import *
from telegram import ReplyKeyboardMarkup,Bot
import requests,json
import os

config = json.load(open('config.json','r'))

TOKEN = config['api_key']
DEV = True
signup = config['signup']
refr = config['ref']
admins = config['admins']
data = []
dash_key = [['Twitter','Gmail'],['Referral Link','Referred'],['Balance']]
admin_key = [['Users','Get List']]

webhook_url = 'Your Webook'
PORT = int(os.environ.get('PORT','8449'))

def verification():
    random_number = randint(1, 7)
    if random_number == 1:
        captcha1 = "https://i.postimg.cc/TwjQ9mfd/2bg48.png"
        return captcha1
    elif random_number == 2:
        captcha2 = "https://i.postimg.cc/wM62bvjh/2fxgd.png"
        return captcha2
    elif random_number == 3:
        captcha3 = "https://i.postimg.cc/hvpsFBXN/5n728.png"
        return captcha3
    elif random_number == 4:
        captcha4 = "https://i.postimg.cc/7PVmJgKX/ec6pm.png"
        return captcha4
    elif random_number == 5:
        captcha5 = "https://i.postimg.cc/Pr5KWPcH/m457d.png"
        return captcha5
    elif random_number == 6:
        captcha6 = "https://i.postimg.cc/hPZspKWd/w4x2m.png"
        return captcha6
    elif random_number == 7:
        captcha7 = "https://i.postimg.cc/52H3rDbk/yew6p.png"
        return captcha7

def start(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        name = str(update.message.chat.first_name)
        if user not in data['users']:
            data['users'].append(user)
            data['name'].append(name)
            if user not in data['twitter']:
                data['twitter'][user] = ""
            if user not in data['eth']:
                data['eth'][user] = ""
            ref_id = update.message.text.split()
            if len(ref_id) > 1:
                data['ref'][user] = ref_id[1]
                if str(ref_id[1]) not in data['referred']:
                    data['referred'][str(ref_id[1])] = 1
                else:
                    data['referred'][str(ref_id[1])] += 1
            else:
                data['ref'][user] = 0
            data['total'] += 1
            data['id'][user] = data['total']
            data['process'][user] = "verify"
            json.dump(data,open('users.json','w'))
            msg = config['intro']
            update.message.reply_text(msg)
            update.message.reply_text('''\n↪️  Step-by-step guide:\n\nFollow steps of AirDrop_1 @ Metal\n\n1. Follow us on Twitter ( https://twitter.com/0xIconic ) \n2. Like and Retweet our Pinned post \n3. Share your Twitter handle and gmail id with us \n( for verification and distribution of token and incentives ) \n4. Join our Telegram Community ( https://t.me/OxIconic ) \n\nDownload and signup with your Gmail id ( provided here ) and you will receive the airdrop \nLink:-https://play.google.com/store/apps/details?id=one.metal\n\n**You can do these steps later before the airdrop. \n***There are great incentives for our early community members, so feel free to join the community.",
                                         \n\n**Complete the captcha to get started👇🏻**''')
            update.message.reply_photo(verification())
        else:
            welcome_msg = "Already done!"
            reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
            update.message.reply_text(welcome_msg,reply_markup=reply_markup)
    else:
        msg = '{} \n. I don\'t reply in group, come in private'.format(config['intro'])
        update.message.reply_text(msg)

def twitter(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        twtr_user = data['twitter'][user]
        msg = 'Your twitter username is {}'.format(twtr_user)
        reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
        update.message.reply_text(msg,reply_markup=reply_markup)

def mail(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        mail = data['email'][user]
        msg = 'Your mail address is {}'.format(mail)
        reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
        update.message.reply_text(msg,reply_markup=reply_markup)

def link(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        msg = 'https://t.me/{}?start={}'.format(config['botname'],data['id'][user])
        reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
        update.message.reply_text(msg,reply_markup=reply_markup)


def extra(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)

        if data["process"][user] == 'verify':
            started_msg = '''Our Twitter Id :  https://twitter.com/0xIconic \n\nPlease follow us, like, and retweet our pinned post.\n\n https://twitter.com/0xIconic/status/1483789918363332613 \n\n**Enter your Twitter Handle/ id Link down below👇🏻**'''
            text = update.message.text.lower()
            if text == '2bg48':
                data['process'][user] = 'twitter'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == '2fxgd':
                data['process'][user] = 'twitter'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == '5n728':
                data['process'][user] = 'twitter'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'ec6pm':
                data['process'][user] = 'twitter'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'm457d':
                data['process'][user] = 'twitter'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'w4x2m':
                data['process'][user] = 'twitter'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            elif text == 'yew6p':
                data['process'][user] = 'twitter'
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text(started_msg)
            else:
                update.message.reply_text("err, try again")
        elif data["process"][user] == 'twitter':
            data['twitter'][user] = update.message.text
            data['process'][user] = 'telegram group'
            json.dump(data,open('users.json','w'))
            update.message.reply_text('''https://t.me/OxIconic \nJoin our community to receive airdrop and stay updated about the project.\n\n**Type DONE once joined!**''')
        elif data["process"][user] == 'telegram group':
            confirmation_text = update.message.text.lower()
            if confirmation_text == "done":
                data['process'][user] = "email"
                json.dump(data, open('users.json', 'w'))
                update.message.reply_text("Please share your Gmail address.")
            else:
                update.message.reply_text("Type DONE once joined!")
        elif data["process"][user] == 'email':
            data['email'][user] = update.message.text
            data['process'][user] = "finished"
            json.dump(data, open('users.json', 'w'))
            msg = "Thanks for participating.\n\n We have recieved your request.\n\nPlease download the app : https://play.google.com/store/apps/details?id=one.metal\n\nWe will whitelist you and your token will be Added to your wallet.\n\nThe app is on Play Store only for now. Soon it will be rolled out for iOS users too.\n\n Stay updated by being active the telegram channel"
            reply_markup = ReplyKeyboardMarkup(dash_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
        else:
            msg = "Invalid keystroke"
            reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
            update.message.reply_text(msg,reply_markup=reply_markup)

def ref(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        i = str(data["id"][user])
        referred = 0
        if i in data['referred']:
            referred = data['referred'][i]
        msg = "You have referred {} people".format(referred)
        reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
        update.message.reply_text(msg,reply_markup=reply_markup)

def admin(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        if user in admins:
            msg = "Welcome to Admin Dashboard"
            reply_markup = ReplyKeyboardMarkup(admin_key,resize_keyboard=True)
            update.message.reply_text(msg,reply_markup=reply_markup)

def users(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        if user in admins:
            msg = "A total of {} have joined this program".format(data['total'])
            reply_markup = ReplyKeyboardMarkup(admin_key,resize_keyboard=True)
            update.message.reply_text(msg,reply_markup=reply_markup)

def get_file(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        if user in admins:

            f = open('users.csv','w')
            f.write("no.,userid,email,twitter username,referred\n")
            for u in data['users']:
                if data['process'][u] == "finished":
                    i = str(data['id'][u])
                    refrrd = 0
                    if i in data['referred']:
                        refrrd = data['referred'][i]
                    d = "{},{},{},{},{}\n".format(
                        i, u, data['email'][u], data['twitter'][u], refrrd)
                    f.write(d)
                if data['process'][u] == "verify":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        i, u, "", "", refrrd)
                    f.write(d)
                if data['process'][u] == "twitter":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        i, u, "", "", refrrd)
                    f.write(d)
                if data['process'][u] == "telegram group":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        i, u, "", data['twitter'][u], refrrd)
                    f.write(d)
                if data['process'][u] == "email":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        i, u, "", data['twitter'][u], refrrd)
                    f.write(d)
            f.close()
            bot = Bot(TOKEN)
            bot.send_document(chat_id=update.message.chat.id, document=open('users.csv','rb'))

def bal(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        i = str(data["id"][user])
        referred = 0
        if i in data['referred']:
            referred = data['referred'][i]
        bal = signup + refr * referred
        msg = "You have {} tokens".format(bal)
        reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
        update.message.reply_text(msg,reply_markup=reply_markup)

if __name__ == '__main__':
    data = json.load(open('users.json','r'))
    updater = Updater(TOKEN,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("admin",admin))
    dp.add_handler(MessageHandler(Filters.regex('^Twitter$'), twitter))
    # dp.add_handler(MessageHandler(Filters.regex('^Wallet address$'), eth))
    dp.add_handler(MessageHandler(Filters.regex('^Referral Link$'), link))
    dp.add_handler(MessageHandler(Filters.regex('^Referred$'), ref))
    dp.add_handler(MessageHandler(Filters.regex('Gmail$'), mail))
    dp.add_handler(MessageHandler(Filters.regex('^Users$'), users))
    dp.add_handler(MessageHandler(Filters.regex('^Get List$'), get_file))
    dp.add_handler(MessageHandler(Filters.regex('^Balance$'), bal))
    dp.add_handler(MessageHandler(Filters.text,extra))
    if DEV is not True:
        updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN)
        updater.bot.set_webhook(webhook_url + TOKEN)
    else:
        updater.start_polling()
    print("Bot Started")
    updater.idle()
