import telepot
from telepot.loop import MessageLoop

TOKEN="6864572073:AAExyBw0PJzALi1NLP0ekPoZXHCCp8uUr88"
USER="49317077"

class TelegramBot:
    def __init__(self):
        self.bot = None
        self.user_id = None
        self.registered_users = {}

    def handle_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        name = msg["from"]["id"]
        print(name)

        if content_type == 'text':
            text = msg['text']
            user_id = msg['from']['id']
            username = msg['from']['username']


            if text.lower() == '/start':
                self.registered_users[user_id] = username
                self.bot.sendMessage(chat_id, "Comunica con la Savana")
                self.bot.sendMessage(chat_id, "Dicci qualcosa che non sappiamo")


            else:
                if self.user_id is not None:
                    recipient_username = self.registered_users.get(self.user_id, 'Utente Sconosciuto')
                    self.bot.sendMessage(self.user_id, f"(@{username})//{user_id}//> {text}")

        elif content_type == 'photo':
            user_id = msg['from']['id']
            username = msg['from']['username']

            if self.user_id is not None:
                recipient_username = self.registered_users.get(self.user_id, 'Utente Sconosciuto')
                self.bot.sendPhoto(self.user_id, msg['photo'][-1]['file_id'], caption=f"(@{username}) //{user_id}//>")


    def run(self, token, user_id):
        self.bot = telepot.Bot(token)
        self.user_id = user_id
        MessageLoop(self.bot, self.handle_message).run_as_thread()
        print("Bot in ascolto...")

        while True:
            pass

if __name__ == '__main__':
    bot_token = TOKEN
    user_id =USER

    telegram_bot = TelegramBot()
    telegram_bot.run(bot_token, user_id)
