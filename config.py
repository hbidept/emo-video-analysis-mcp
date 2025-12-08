'''
Date: 2025-11-25 15:28:48
LastEditors: sunkr1995 35027245+sunkr1995@users.noreply.github.com
LastEditTime: 2025-11-27 17:07:24
FilePath: \lianxin_mcp_stdio\config.py
Description: Do not edit
'''
# config.py
import os
# API 网关基础地址
API_BASE = "https://gateway.lianxinyun.com"

# 模型名称映射
MODEL_NAME_MAPPING = {
    "EmotionRecognitionModel": "emotionRecognitionModel",
    "PressureDetectionModel":"PressureDetectionModel",
    "PadRecognitionModel":"padRecognitionModel"
}

# 签名缓存的 TTL (Time-To-Live)，单位：秒
# 12 * 60 * 60 = 12 小时
SIGN_CACHE_TTL = 12 * 60 * 60

APP_KEY=os.getenv('APP_KEY',None)

APP_SECRET=os.getenv('APP_SECRET',None)

# 认证服务器地址
AUTH_SERVER_URL = "https://gateway.lianxinyun.com/access/token"

# --- 日志配置 ---
LOG_FILE_PATH = "app.log"  # 日志文件路径
LOG_LEVEL = "INFO"         # 日志级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# 日志轮转配置：当文件达到 5MB 时，创建一个新文件
LOG_MAX_BYTES = 1024 * 1024 * 5  # 5 MB
LOG_BACKUP_COUNT = 3             # 保留最近的 3 个日志文件
