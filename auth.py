'''
Date: 2025-11-25 15:29:14
LastEditors: sunkr 522697475@qq.com
LastEditTime: 2025-11-25 15:29:15
FilePath: /ChatPPT-MCP/python/sse/auth.py
Description: Do not edit
'''
# auth.py

import httpx
import asyncio
import hashlib
import time
from config import SIGN_CACHE_TTL, AUTH_SERVER_URL

class SignCache:
    """
    管理和缓存用于API认证的 sign。
    """
    def __init__(self):
        # 缓存结构：{key: (value, expire_time)}
        self._cache = {}
        self._ttl = SIGN_CACHE_TTL

    def _make_auth_cache_key(self, user_key: str, user_secret: str) -> str:
        """根据 appKey 和 appSecret 生成唯一的缓存键"""
        raw = f"{user_key}:{user_secret}"
        return hashlib.md5(raw.encode()).hexdigest()

    async def _fetch_sign_from_server(self, user_key: str, user_secret: str) -> str:
        """从认证服务器获取新的 sign"""
        params = {
            "appKey": user_key,
            "appSecret": user_secret
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(AUTH_SERVER_URL, params=params)
            data = response.json()
            if response.status_code != 200 or data.get("code") != 200:
                raise Exception(f"获取 sign 失败: {data.get('message', '未知错误')}")
            return data["data"]
    
    async def get_sign(self, app_key: str, app_secret: str) -> str:
        """
        获取 sign，优先从缓存中读取。
        如果缓存不存在或已过期，则从服务器重新获取并更新缓存。
        """
        key = self._make_auth_cache_key(app_key, app_secret)
        item = self._cache.get(key)
        now = time.time()

        if item:
            sign, expire_time = item
            if now < expire_time:
                return sign
        
        # 缓存未命中或已过期，重新获取
        print("缓存未命中或已过期，正在从认证服务器获取新的 sign...")
        new_sign = await self._fetch_sign_from_server(app_key, app_secret)
        expire_time = now + self._ttl
        self._cache[key] = (new_sign, expire_time)
        return new_sign

