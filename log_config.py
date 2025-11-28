'''
Date: 2025-11-25 16:08:52
LastEditors: sunkr 522697475@qq.com
LastEditTime: 2025-11-25 16:08:53
FilePath: /lianxin_mcp_stream/log_config.py
Description: Do not edit
'''
# log_config.py

import logging
import sys
from logging.handlers import RotatingFileHandler
from config import LOG_FILE_PATH, LOG_LEVEL, LOG_MAX_BYTES, LOG_BACKUP_COUNT

def setup_logging():
    """
    配置日志系统，使其同时输出到控制台和文件。
    """
    # 1. 创建一个通用的日志格式
    log_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 2. 获取根日志记录器 (root logger)
    #    所有通过 `logging.getLogger()` 创建的 logger 都会继承它的设置
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)

    # 3. 配置日志轮转文件处理器 (File Handler)
    #    - RotatingFileHandler 可以根据文件大小自动分割日志文件
    #    - 这可以防止日志文件无限增长，耗尽磁盘空间
    file_handler = RotatingFileHandler(
        LOG_FILE_PATH,
        maxBytes=LOG_MAX_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding='utf-8'
    )
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    # 4. 配置控制台处理器 (Console/Stream Handler)
    #    - 这会将日志输出到标准输出（你的终端）
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    logging.info("日志系统配置完成，将同时输出到控制台和文件。")

