'''
Date: 2025-11-27 15:42:40
LastEditors: sunkr1995 35027245+sunkr1995@users.noreply.github.com
LastEditTime: 2025-11-27 17:09:32
FilePath: \lianxin_mcp_stdio\main.py
Description: Do not edit
'''
"""
FastMCP quickstart example.

Run from the repository root:
    uv run examples/snippets/servers/fastmcp_quickstart.py
"""
import os
from mcp.server.fastmcp import FastMCP
from auth import SignCache
import logging
from tools_mcp import register_all_tools # 导入总的注册函数

from log_config import setup_logging # 导入日志配置函数

setup_logging() 
logging.info("应用程序启动中...")


# Create an MCP server
mcp = FastMCP("Demo")
sign_cache_instance = SignCache()
# --- 注册所有工具 ---
# 将 mcp 实例和依赖的 sign_cache_instance 传递给注册函数
logging.info("正在注册所有工具...")
register_all_tools(mcp, sign_cache_instance)
logging.info("所有工具注册完成。")

# Run with stdio transport
if __name__ == "__main__":
    print("Starting FastMCP server...")
    mcp.run(transport="stdio")