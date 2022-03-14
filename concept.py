from telegram.ext import Updater, CommandHandler, RegexHandler, MessageHandler,Filters
from random import *
from telegram import ReplyKeyboardMarkup,Bot
import requests,json
import os

config = json.load(open('config.json','r'))

DEV = True
TOKEN = config['api_key']
admins = config['admins']
refr = config['ref']
dash_key = [['Referral Link','Referred'],['Balance']]
option_key = [['A', 'B'], ['C', 'D']]
admin_key = [['Users','Get List']]

webhook_url = 'Your Webook'
PORT = int(os.environ.get('PORT','8443'))

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
        name = str(update.message.chat.username)
        if user not in data['users']:
            data['users'].append(user)
            data['name'][user] = name
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
            update.message.reply_text('''\n↪️  Step-by-step guide:\n\nAnswer every question correctly to get 10 bitcoins. \n\n**Complete the captcha to get started👇🏻**''')
            update.message.reply_photo(verification())
        else:
            welcome_msg = "Already done!"
            reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
            update.message.reply_text(welcome_msg,reply_markup=reply_markup)
    else:
        msg = '{} \n. I don\'t reply in group, come in private'.format(config['intro'])
        update.message.reply_text(msg)

def extra(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)

        if data["process"][user] == 'verify':
            msg = '''Who is the founder of bitcoin?'''
            text = update.message.text.lower()
            if text == '2bg48':
                reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
                update.message.reply_text(msg, reply_markup=reply_markup)
                update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
                data['process'][user] = '1st question'
            elif text == '2fxgd':
                reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
                update.message.reply_text(msg, reply_markup=reply_markup)
                update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
                data['process'][user] = '1st question'
            elif text == '5n728':
                reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
                update.message.reply_text(msg, reply_markup=reply_markup)
                update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
                data['process'][user] = '1st question'
            elif text == 'ec6pm':
                reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
                update.message.reply_text(msg, reply_markup=reply_markup)
                update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
                data['process'][user] = '1st question'
            elif text == 'm457d':
                reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
                update.message.reply_text(msg, reply_markup=reply_markup)
                update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
                data['process'][user] = '1st question'
            elif text == 'w4x2m':
                reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
                update.message.reply_text(msg, reply_markup=reply_markup)
                update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
                data['process'][user] = '1st question'
            elif text == 'yew6p':
                reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
                update.message.reply_text(msg, reply_markup=reply_markup)
                update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
                data['process'][user] = '1st question'
            else:
                update.message.reply_text("err, try again")
        elif data["process"][user] == '1st question':
            answer = update.message.text
            data["correct_questions"][user] = 0
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = "What will be the price bitcoin"
            reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            update.message.reply_text('''\n A: 1 million\n B: 0.5 Billion\n C: 1000k\n D: 20k''')
            data['process'][user] = '2nd question'
            json.dump(data,open('users.json','w'))
        elif data["process"][user] == '2nd question':
            answer = update.message.text
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = "Who is the founder of solana"
            reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
            data['process'][user] = '3rd question'
            json.dump(data, open('users.json', 'w'))
        elif data["process"][user] == '3rd question':
            answer = update.message.text
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = "Who is the founder of coinmarketcap"
            reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
            data['process'][user] = '4th question'
            json.dump(data, open('users.json', 'w'))
        elif data["process"][user] == '4th question':
            answer = update.message.text
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = "Who is the founder of coinswitch"
            reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
            data['process'][user] = '5th question'
            json.dump(data, open('users.json', 'w'))
        elif data["process"][user] == '5th question':
            answer = update.message.text
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = "Who is the founder of cardano"
            reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
            data['process'][user] = '6th question'
            json.dump(data, open('users.json', 'w'))
        elif data["process"][user] == '6th question':
            answer = update.message.text
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = "Who is the founder of degenerates"
            reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
            data['process'][user] = '7th question'
            json.dump(data, open('users.json', 'w'))
        elif data["process"][user] == '7th question':
            answer = update.message.text
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = "Who is the founder of polkadot"
            reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
            data['process'][user] = '8th question'
            json.dump(data, open('users.json', 'w'))
        elif data["process"][user] == '8th question':
            answer = update.message.text
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = "Who is the founder of discord"
            reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
            data['process'][user] = '9th question'
            json.dump(data, open('users.json', 'w'))
        elif data["process"][user] == '9th question':
            answer = update.message.text
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = "Who is the founder of tesla"
            reply_markup = ReplyKeyboardMarkup(option_key, resize_keyboard=True, one_time_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            update.message.reply_text('''\n A: Someone\n B: No one\n C: Any one\n D: I don't Know''')
            data['process'][user] = '10th question'
            json.dump(data, open('users.json', 'w'))
        elif data["process"][user] == '10th question':
            answer = update.message.text
            if answer == 'A':
                data["correct_questions"][user] = data["correct_questions"][user] + 1
            msg = (f"Great, You have given {data['correct_questions'][user]} of the 10 questions correctly... You'll be getting 10 bitcoins for each correct answers. You can win more by reffering more people")
            update.message.reply_text(msg)
            update.message.reply_text('''Please enter your Bitcoin wallet address so that we can send you the prize.''')
            data['process'][user] = "bitcoin"
            json.dump(data, open('users.json', 'w'))
        elif data["process"][user] == 'bitcoin':
            wallet_address = update.message.text
            data['wallet_address'][user] = wallet_address
            msg = "Thank you"
            data['process'][user] = "Finished"
            reply_markup = ReplyKeyboardMarkup(dash_key, resize_keyboard=True)
            update.message.reply_text(msg, reply_markup=reply_markup)
            json.dump(data, open('users.json', 'w'))
        else:
            msg = "Invalid keystroke"
            reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
            update.message.reply_text(msg,reply_markup=reply_markup)

def admin(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        if user in admins:
            msg = "Welcome to Admin Dashboard"
            reply_markup = ReplyKeyboardMarkup(admin_key,resize_keyboard=True)
            update.message.reply_text(msg,reply_markup=reply_markup)

def link(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        msg = 'https://t.me/{}?start={}'.format(config['botname'],data['id'][user])
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

def bal(update, context):
    if update.message.chat.type == 'private':
        user = str(update.message.chat.id)
        i = str(data["id"][user])
        referred = 0
        if i in data['referred']:
            referred = data['referred'][i]
        answer = data["correct_questions"][user]
        bal = (answer * 10) + (refr * referred)
        msg = "You have {} Bitcoins".format(bal)
        reply_markup = ReplyKeyboardMarkup(dash_key,resize_keyboard=True)
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
            f.write("userid,username,wallet_address,balance,referred\n")
            for u in data['users']:
                if data['process'][u] == "finished":
                    i = str(data['id'][u])
                    refrrd = 0
                    answer = data["correct_questions"][user]
                    balance = (answer * 10) + (refr * refrrd)
                    if i in data['referred']:
                        refrrd = data['referred'][i]
                    d = "{},{},{},{},{}\n".format(
                         u,data['name'][u], data['wallet_address'][u], balance, refrrd)
                    f.write(d)
                if data['process'][u] == "bitcoin":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        u,data['name'][u], "", balance, "")
                    f.write(d)
                if data['process'][u] == "3rd question":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        u,data['name'][u], "", "", "")
                    f.write(d)
                if data['process'][u] == "2nd question":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        u,data['name'][u], "", "", "")
                    f.write(d)
                if data['process'][u] == "1st question":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        u,data['name'][u], "", "", "")
                    f.write(d)
                if data['process'][u] == "verify":
                    i = str(data['id'][u])
                    refrrd = 0
                    d = "{},{},{},{},{}\n".format(
                        u,data['name'][u], "", "", "")
                    f.write(d)
            f.close()
            bot = Bot(TOKEN)
            bot.send_document(chat_id=update.message.chat.id, document=open('users.csv','rb'))


if __name__ == '__main__':
    data = json.load(open('users.json','r'))
    updater = Updater(TOKEN,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("admin",admin))
    dp.add_handler(MessageHandler(Filters.regex('^Referral Link$'), link))
    dp.add_handler(MessageHandler(Filters.regex('^Referred$'), ref))
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