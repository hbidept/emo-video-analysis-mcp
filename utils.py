# utils.py
from config import APP_KEY, APP_SECRET

def get_auth_keys() -> dict:
    app_key = APP_KEY
    app_secret = APP_SECRET
    
    if app_key and app_secret:
        return {
            "appKey": app_key,
            "appSecret": app_secret
        }
    
    raise ValueError("请求头中缺少 'appKey' 或 'appSecret'")

