# -*- coding: UTF-8 -*-

from fbchat import log, Client
from fbchat.models import *
import random
import sqlite3

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        #check if have react
        conn = sqlite3.connect('bot.db')
        c = conn.cursor()
        d = c.execute("SELECT * FROM test WHERE name = ?", (message_object.text,))
        print type(d)
        if 'react' in d:
           client.send(Message(text=d['react']), thread_id=thread_id, thread_type=thread_type)
        conn.close()
        if author_id != self.uid and message_object.text == '/test':
            client.send(Message(text='test successs'), thread_id=thread_id, thread_type=thread_type)
        elif message_object.text == '/bye' and thread_type == ThreadType.GROUP:
            log.info('{} will be removed from {}'.format(author_id, thread_id))
            self.removeUserFromGroup(self.uid, thread_id=thread_id)
        elif message_object.text.find('/text_test') > -1:
            client.send(Message(text='text_test successs'), thread_id=thread_id, thread_type=thread_type)
        elif message_object.text.find(u'運勢') > -1:
            a = random.randrange(1, 5)
            b = random.randrange(1, 3)
            if a==1:
	       if b==1:
                 c = '美好的一天從幹你娘開始'
               elif b==2:
                 c = '子瑜睡你身邊'

               client.send(Message(text='大吉'+' '+c), thread_id=thread_id, thread_type=thread_type)
            elif a==2:
                if b==1:
                  c = '掰'
                elif b==2:
                  c = '極好吉滿'

                client.send(Message(text='小吉'+' '+c), thread_id=thread_id, thread_type=thread_type)
            elif a==3:
                if b==1:
                  c = '出門會被車撞死'
                elif b==2:
                  c = '還是回家打手槍還比較安全'

                client.send(Message(text='凶'+' '+c), thread_id=thread_id, thread_type=thread_type)
            elif a==4:
                if b==1:
                  c = '吞口水都會被噎死'
                elif b==2:
                  c = '看a片看到習近平'

                client.send(Message(text='大凶'+' '+c), thread_id=thread_id, thread_type=thread_type)
        elif message_object.text.find('/add') > -1:
            name  = message_object.text.split('_')[1]
            react = message_object.text.split('_')[2]
            params = (name, react)
            conn = sqlite3.connect('bot.db')
            c = conn.cursor()
            c.execute("INSERT INTO test VALUES (?, ?)", params)
            conn.commit()
            conn.close()
            client.send(Message(text='add key successful'), thread_id=thread_id, thread_type=thread_type)
            client.send(Message(text='name: '+name), thread_id=thread_id, thread_type=thread_type)
            client.send(Message(text='react: '+react), thread_id=thread_id, thread_type=thread_type)

client = EchoBot("noname08010828@gmail.com", "e27676271")
client.listen()
