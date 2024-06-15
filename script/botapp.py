import requests

TOKEN = '6584654808:AAFshuC0u-417ggR-7CKJg9N_GpJKBFcAXI'
DOMAIN_URL = '127.0.0.1'  # تغییر داده شده به localhost
WEBHOOK_URL = f'http://{DOMAIN_URL}/webhook/'  # استفاده از HTTP به جای HTTPS برای localhost

response = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}')
print(response.json())