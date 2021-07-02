
#from Bot import wiki
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import wikipedia
import requests
import sqlite3
wikipedia.set_lang('RU')

status_list = ['Нуб', 'Обычный','Абьюзер','Губернатор','Король','император']



action_dict = {}




class user_lol:
    def __init__(self,status,exp,id,Name):
        self.status = status
        self.exp = exp
        self.id = id
        self.Name = None

    def get_exp(self):
        return(self.exp)

    def get_info(self):
        return (self.status,self.exp,self.id) 

    def get_status(self):
        return self.status

    def get_id(self):
        return(self.id)

    def farm_exp(self):
        self.exp +=1

    def change_status(self,status):
        self.status = status



def replace_text(text):
    text = text.replace(',','')
    text = text.replace('.','')
    text = text.replace('!','')
    text = text.replace('?','')
    text = text.replace('[','')
    text = text.replace(']','')
    return text

def read_dict():
    action_dict = {}
    f = open('actions.txt','r')
    a = f.read()
    if a == '':
        return {}
    a = a.split(';')
    for stroka in a:
        if stroka !='':
            key_value = stroka.split(':')
            print(stroka.split(':'))
            action_dict.update({key_value[0]:key_value[1]})
    return action_dict


def rewrite_dict(new_action):
    f = open('actions.txt','a')
    new_action = new_action.lower()
    new_action = new_action + ';'
    f.write(new_action)
    f.close
    return True
    
def chek_phrase(stroka1,stroka2,bot_api):
    for key,value in read_dict().items():
        if key == stroka1 or value == stroka2:
            bot_api.messages.send(
                                            random_id   =   random.getrandbits(32),
                                            chat_id     =   event.chat_id,
                                            message     =  '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", действие уже имеется!"
                                            )
            return False
    return True

def chek_bot(event):
    if event.message['reply_message']['from_id'] < 0:
        return False
    return True

def chek_new_users(list1,list2):
    for user1 in list1:
        flag = True
        for user2 in list2:
            if user1.get_id() == user2.get_id():
                flag = False
    return flag

def get_old_users(list1,list2):
    old_users = []
    for user1 in list1:
        flag = False
        for user2 in list2:
            if user1.get_id() == user2.get_id():
                flag = True
        if flag:
            old_users.append(user1)
        
    return old_users

def get_new_users(list1,list2):
    new_users = []
    for user1 in list1:
        flag = True
        for user2 in list2:
            if user1.get_id() == user2.get_id():
                flag = False
        if flag:
            new_users.append(user1)
        
    return new_users
    
def chek_exp(bot_api,user,event,cursor):
    if user.get_exp()>10 and user.get_status()!=status_list[0] and user.get_exp()<101 :
        cursor.execute('update users_game set status = ? where userid = ?',(status_list[0],user.get_id()))
        bot_api.messages.send(
            random_id   =   random.getrandbits(32),
            chat_id     =   event.chat_id,
            message     =   '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", Поздравляю, теперь ты "+status_list[0]+'!'
            )
    if user.get_exp()>100 and user.get_status()!=status_list[1] and user.get_exp()<501:
        cursor.execute('update users_game set status = ? where userid = ?',(status_list[1],user.get_id()))
        bot_api.messages.send(
            random_id   =   random.getrandbits(32),
            chat_id     =   event.chat_id,
            message     =   '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", Поздравляю, теперь ты "+status_list[1]+'!'
            )
    if user.get_exp()>500 and user.get_status()!=status_list[2] and user.get_exp()<1001:
        cursor.execute('update users_game set status = ? where userid = ?',(status_list[2],user.get_id()))
        bot_api.messages.send(
            random_id   =   random.getrandbits(32),
            chat_id     =   event.chat_id,
            message     =   '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", Поздравляю, теперь ты "+status_list[2]+'!'
            )
    if user.get_exp()>1000 and user.get_status()!=status_list[3] and user.get_exp()<5001:
        cursor.execute('update users_game set status = ? where userid = ?',(status_list[3],user.get_id()))
        bot_api.messages.send(
            random_id   =   random.getrandbits(32),
            chat_id     =   event.chat_id,
            message     =   '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", Поздравляю, теперь ты "+status_list[3]+'!'
            )
    if user.get_exp()>5000 and user.get_status()!=status_list[4] and user.get_exp()<10001:
        cursor.execute('update users_game set status = ? where userid = ?',(status_list[4],user.get_id()))
        bot_api.messages.send(
            random_id   =   random.getrandbits(32),
            chat_id     =   event.chat_id,
            message     =   '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", Поздравляю, теперь ты "+status_list[4]+'!'
            )
    if user.get_exp()>10000 and user.get_status()!=status_list[5]:
        cursor.execute('update users_game set status = ? where userid = ?',(status_list[5],user.get_id()))
        bot_api.messages.send(
            random_id   =   random.getrandbits(32),
            chat_id     =   event.chat_id,
            message     =   '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", Поздравляю, теперь ты "+status_list[5]+'!'
            )
    return user

def create_user_class(event):
    cursor.execute('select status from users_game where userid = ?',(event.message['from_id'],))
    user_status = cursor.fetchone()[0]
    cursor.execute('select exp from users_game where userid = ?',(event.message['from_id'],))
    user_exp = cursor.fetchone()[0]
    user_id = event.message['from_id']
    user = user_lol(user_status,user_exp,user_id,None) 
    return user

def dict_in_list(dict):
    list_of_dict = []
    for key in dict.keys():
        list_of_dict.append(key)

    return list_of_dict


def chek_userid_reply(cursor,event):
    cursor.execute('select userid from users_game')
    ids = cursor.fetchall()
    for i in ids:
        if i == event.message['from_id']:
            return True
    return False

def chek_userid(cursor,event):
    cursor.execute('select userid from users_game')
    ids = cursor.fetchall()
    for i in ids:
        if i == event.message['action']['member_id']:
            return True
    return False

def spam_attack(bot_api,event):
    i = 0
    for i in range(9):
        bot_api.messages.send(
            random_id   =   random.getrandbits(32),
            user_id     =   event.message['reply_message']['from_id'],
            message     =   'Хдыщ!'
        )

def role_play():
    pass 

def grammatika():
    url = 'https://www.google.com/search?q='
    request_google = 'гараж'

    text = requests.get(url+request_google).text
    return print(text)


 
replies = [ "Да", "Нет" ]
bot_session = vk_api.VkApi(token="0d0a7bd3bd782d92f0ee1482801dfa9e210bebe5a7a5d0695dfecdeb1981ec13ae7b87d101f86c6584ed2")
bot_api = bot_session.get_api()
longpoll = VkBotLongPoll(bot_session, "204973482")
while True:
    try:
        for event in longpoll.listen():
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            print(event)
            print("got event")
            if  event.type == VkBotEventType.MESSAGE_NEW and event.message.get('action') is not None:
                print("im in")
                if event.message['action']['type'] == 'chat_invite_user':
                    if chek_userid_reply(cursor,event):
                        cursor.execute('insert into users_game (status,exp,userid) values (?,?,?)',(None,0,event.message['action']['member_id']))
                        bot_api.messages.send(
                                random_id   =   random.getrandbits(32),
                                chat_id     =   event.chat_id,
                                message     =   '[id'+str(event.message['action']['member_id'])+'|'+bot_api.users.get(user_ids = event.message['action']['member_id'])[0]['first_name'] +']'+ ", Добро пожаловать!"
                                )
                elif event.message['action']['type'] == 'chat_invite_user_by_link':
                    if chek_userid(cursor,event):
                        cursor.execute('insert into users_game (status,exp,userid) values (?,?,?)',(None,0,event.message['from_id']))
                        bot_api.messages.send(
                                random_id   =   random.getrandbits(32),
                                chat_id     =   event.chat_id,
                                message     =   '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", Добро пожаловать!"
                                )
            if event.type == VkBotEventType.MESSAGE_NEW and event.message['text'] != '':
                user = create_user_class(event)
                cursor.execute('select exp from users_game where userid = ?',(event.message['from_id'],))
                exp = cursor.fetchone()
                exp = exp[0]+1
                cursor.execute('update users_game set exp = ? where userid = ?',(exp,event.message['from_id']))
                chek_exp(bot_api,user,event,cursor)
                user_message = event.message['text'].lower()
                if user_message == 'да или нет':
                    bot_api.messages.send(
                        random_id   =   random.getrandbits(32),
                        chat_id     =   event.chat_id,
                        message     =   random.choice(replies) 
                        )
                if read_dict().get(user_message) is not None and  event.message.get('reply_message') is not None and chek_bot(event):
                            bot_api.messages.send(
                                                random_id   =   random.getrandbits(32),
                                                chat_id     =   event.chat_id,
                                                message     =  '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +'] '+ read_dict().get(user_message) +' [id'+str(event.message['reply_message']['from_id'])+'|'+bot_api.users.get(user_ids = event.message['reply_message']['from_id'])[0]['first_name'] +']'
                                                )
                if user_message.find('бот',0,3) != -1:
                    print(user_message)
                    if user_message.find('википедия') !=-1:
                        user_message = user_message[user_message.find('википедия')+9:]
                        print(user_message)
                        try:
                            bot_api.messages.send(
                            random_id   =   random.getrandbits(32),
                            chat_id     =   event.chat_id,
                            message     =   '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']' +',\n'+str(wikipedia.summary(replace_text(user_message)))
                            )
                        except wikipedia.exceptions.WikipediaException:
                            bot_api.messages.send(
                            random_id   =   random.getrandbits(32),
                            chat_id     =   event.chat_id,
                            message     =  '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", не получилася"
                            )
                            
                            continue
                    if user_message.find('добавь действие') != -1:
                        user = create_user_class(event)
                        for status in range(len(status_list)-1):
                            if user.get_status() == status_list[status]:
                                if status > 1:
                                    if user_message.find(':') !=-1 and user_message[user_message.find(':')+1::].find(':') == -1:
                                        stroka = user_message[user_message.find('добавь действие')+16::].split(':')
                                        
                                        print(stroka)
                                        if chek_phrase(stroka[-2],stroka[-1],bot_api):
                                            rewrite_dict(stroka[-2]+':'+stroka[-1])
                                            bot_api.messages.send(
                                                random_id   =   random.getrandbits(32),
                                                chat_id     =   event.chat_id,
                                                message     =  '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", действие добавлено!"
                                                )
                                            break
                                    else:
                                        bot_api.messages.send(
                                            random_id   =   random.getrandbits(32),
                                            chat_id     =   event.chat_id,
                                            message     =  '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", ошибка!"
                                            )
                                        break
                                else:
                                    bot_api.messages.send(
                                        random_id   =   random.getrandbits(32),
                                        chat_id     =   event.chat_id,
                                        message     =  '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", у вас низкий статус!"
                                        )
                    if user_message.find('список действий') != -1:      
                        text = replace_text(str(dict_in_list(read_dict())))        
                        bot_api.messages.send(
                            random_id   =   random.getrandbits(32),
                            chat_id     =   event.chat_id,
                            message     =  '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ', список действий: '+text
                            )

                    if user_message.find('инфо') != -1:
                        user = create_user_class(event)
                        bot_api.messages.send(
                            random_id   =   random.getrandbits(32),
                            chat_id     =   event.chat_id,
                            message     =  '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ", ваш статус: "+user.get_status()+', кол-во опыта: '+str(user.get_exp())
                            )
                    if user_message.find('фас') !=-1:
                        if  event.message['reply_message']['from_id']:
                            user = create_user_class(event)
                            for status in range(len(status_list)-1):
                                if user.get_status() == status_list[status]:
                                    if status > 1:
                                        spam_attack(bot_api,event)
                                    else:
                                        bot_api.messages.send(
                            random_id   =   random.getrandbits(32),
                            chat_id     =   event.chat_id,
                            message     =  '[id'+str(event.message['from_id'])+'|'+bot_api.users.get(user_ids = event.message['from_id'])[0]['first_name'] +']'+ ', слишком низкий статус!'
                            )
                    if user_message.find('грамматика') !=-1:
                        grammatika()


            conn.commit()
            cursor.close()
            conn.close()
    except requests.exceptions.ReadTimeout:
        continue
