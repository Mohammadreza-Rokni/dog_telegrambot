# from telegram import Update
# from telegram.ext import CallbackContext
# from .models import User, Hamster

# def start(update: Update, context: CallbackContext):
#     telegram_id = update.message.from_user.id
#     username = update.message.from_user.username
#     user, created = User.objects.get_or_create(telegram_id=telegram_id, defaults={'username': username})
#     update.message.reply_text(f'Welcome {username}! Let\'s start the game.')

# def handle_message(update: Update, context: CallbackContext):
#     update.message.reply_text('This is a generic message handler.')
from telegram import Update
from telegram.ext import CallbackContext
from .models import User

def start(update: Update, context: CallbackContext):
    telegram_id = update.message.from_user.id
    username = update.message.from_user.username
    user, created = User.objects.get_or_create(telegram_id=telegram_id, defaults={'username': username})
    if created:
        update.message.reply_text(f'Welcome {username}! You have started the game. Tap on the coin to collect coins.')
    else:
        update.message.reply_text(f'Welcome back {username}! You have {user.coins} coins. Tap on the coin to collect more.')

def handle_coin(update: Update, context: CallbackContext):
    telegram_id = update.message.from_user.id
    user = User.objects.get(telegram_id=telegram_id)
    user.coins += 10
    user.save()
    update.message.reply_text(f'You have collected a coin! Total coins: {user.coins}')
