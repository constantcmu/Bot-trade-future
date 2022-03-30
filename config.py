import os

BINANCE_API_KEY = "xxxxxxxxxxxxxxxx"
BINANCE_API_SECRET = "xxxxxxxxxxxxxxxx"

BINANCE_FUTURE_API_KEY = "RqIf63kEps5WPS0iqaNBW9dJkDPzfingNJqU6XopB1AHcoykeV90LKiAVcegg8YF"
BINANCE_FUTURE_API_SECRET = "xe10AjFBHVeaOTNa4By3TPr2Y8VkwI1THAG4qJWiCikzICaasxFiw41DJ3DiXoAz"
LINE_NOTIFY_TOKEN = "SUTUl3GEBKeM8hzeuCImz8vp0b8bQnxF8dDJV76UMhh"


# แก้ไขเวลา Deploy ขึ้น heroku ใช้ ENV variable เพื่อปกป้อง api key
# heroku config:set BINANCE_API_KEY=xxx
# heroku config:set BINANCE_API_SECRET=xxx
# heroku config:set LINE_NOTIFY_API=xxx
# heroku config:set BINANCE_FUTURE_API_KEY=xxx
# heroku config:set BINANCE_FUTURE_API_SECRET=xxx
# heroku config:set HTTP_PROXY=xxx
# heroku config:set HTTPS_PROXY=xxx

# git add .
# git commit -m "add"
# git push heroku master

# BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
# BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
# BINANCE_FUTURE_API_KEY = os.getenv("BINANCE_FUTURE_API_KEY")
# BINANCE_FUTURE_API_SECRET = os.getenv("BINANCE_FUTURE_API_SECRET")
# LINE_NOTIFY_API = os.getenv("LINE_NOTIFY_API")