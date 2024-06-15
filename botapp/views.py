from django.shortcuts import render
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from .handlers import start, handle_coin
import logging


# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.DEBUG)

TOKEN = '6584654808:AAFshuC0u-417ggR-7CKJg9N_GpJKBFcAXI'
bot = Bot(token=TOKEN)

@csrf_exempt
def webhook(request):
    logging.debug("Webhook called")
    if request.method == 'POST':
        logging.debug("Webhook POST request received")
        update = Update.de_json(request.body, bot)
        dispatcher = Dispatcher(bot, None, workers=0)
        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_coin))
        dispatcher.process_update(update)
        logging.debug("Update processed")
        return JsonResponse({'status': 'ok'})
    logging.debug("Invalid request method")
    return JsonResponse({'status': 'bad request'}, status=400)


def index(request):
    telegram_id = 'test_user'  # برای تست، از یک شناسه ثابت استفاده می‌کنیم
    user, created = User.objects.get_or_create(telegram_id=telegram_id, defaults={'username': 'TestUser'})
    context = {
        'username': user.username,
        'coins': user.coins
    }
    return render(request, 'botapp/index.html', context)

@csrf_exempt
def collect_coin(request):
    if request.method == 'POST':
        telegram_id = 'test_user'  # برای تست، از یک شناسه ثابت استفاده می‌کنیم
        user, created = User.objects.get_or_create(telegram_id=telegram_id, defaults={'username': 'TestUser'})
        user.coins += 10
        user.save()
        return JsonResponse({'coins': user.coins})
    return JsonResponse({'error': 'Invalid request method'}, status=400)