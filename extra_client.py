'''
Date: 2025-11-25 15:30:15
LastEditors: sunkr 522697475@qq.com
LastEditTime: 2025-11-25 16:57:17
FilePath: /lianxin_mcp_stream/extra_client.py
Description: Do not edit
'''
# client.py

import httpx
import logging
import time
import random
from config import API_BASE, MODEL_NAME_MAPPING

async def call_image_api(model_name: str, image_url: str, position_type: str, app_key: str, sign: str) -> dict:
    """
    调用连信的图像处理 API。
    
    Args:
        model_name (str): 模型名称。
        image_url (str): 图像链接。
        position_type (str): 位置类型 (如 'front_face')。
        app_key (str): 应用的 Key。
        sign (str): 认证签名。

    Returns:
        dict: API 的响应结果。
    """
    url = API_BASE + '/algorithm/fast/image/' + MODEL_NAME_MAPPING[model_name]
    
    try:
        logging.info(f"正在处理图像API请求: {image_url}")
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={
                    "model_name": model_name,
                    "param": {
                        "url": image_url,
                        "position_type": position_type
                    }
                },
                headers={
                    'sign': sign,
                    'appKey': app_key,
                    'timestamp': str(int(time.time())),
                    'nonce': str(random.randrange(100, 1000)),
                    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'Host': 'gateway.biyouxinli.com',
                    'Connection': 'keep-alive'
                },
                timeout=30
            )
            response.raise_for_status()  # 如果状态码是 4xx 或 5xx，则抛出 HTTPError

        res = response.json()
        logging.info(f"API 响应: {res}")
        return {'code': res.get('code'), 'data': res.get('data')}

    except httpx.HTTPStatusError as e:
        logging.error(f"API 请求失败 (HTTP Status): {e.response.status_code} - {e.response.text}")
        raise Exception(f"API 请求失败: HTTP {e.response.status_code}") from e
    except Exception as e:
        logging.error(f"调用 API 时发生未知错误: {str(e)}")
        raise Exception(f"API 调用失败: {str(e)}") from e
    

async def call_video_api(model_name: str, video_url: str, position_type: str,num_frames_per_second: int, app_key: str, sign: str) -> dict:
    """
    调用连信的图像处理 API。
    
    Args:
        model_name (str): 模型名称。
        video_url (str): 视频链接。
        position_type (str): 位置类型 (如 'front_face')。
        app_key (str): 应用的 Key。
        sign (str): 认证签名。

    Returns:
        dict: API 的响应结果。
    """
    url = API_BASE + '/algorithm/fast/video/' + MODEL_NAME_MAPPING[model_name]
    
    try:
        logging.info(f"正在处理图像API请求: {video_url}")
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={
                    "model_name": model_name,
                    "param": {
                        "url": video_url,
                        "position_type": position_type,
                        "num_frames_per_second": num_frames_per_second 
                    }
                },
                headers={
                    'sign': sign,
                    'appKey': app_key,
                    'timestamp': str(int(time.time())),
                    'nonce': str(random.randrange(100, 1000)),
                    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'Host': 'gateway.biyouxinli.com',
                    'Connection': 'keep-alive'
                },
                timeout=30
            )
            response.raise_for_status()  # 如果状态码是 4xx 或 5xx，则抛出 HTTPError

        res = response.json()
        logging.info(f"API 响应: {res}")
        return {'code': res.get('code'), 'data': res.get('data')}

    except httpx.HTTPStatusError as e:
        logging.error(f"API 请求失败 (HTTP Status): {e.response.status_code} - {e.response.text}")
        raise Exception(f"API 请求失败: HTTP {e.response.status_code}") from e
    except Exception as e:
        logging.error(f"调用 API 时发生未知错误: {str(e)}")
        raise Exception(f"API 调用失败: {str(e)}") from e

