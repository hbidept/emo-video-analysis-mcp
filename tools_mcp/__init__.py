'''
Date: 2025-11-25 16:01:15
LastEditors: sunkr1995 35027245+sunkr1995@users.noreply.github.com
LastEditTime: 2025-11-27 17:09:17
FilePath: \lianxin_mcp_stdio\tools_mcp\__init__.py
Description: Do not edit
'''
# tools/__init__.py

from mcp.server.fastmcp import FastMCP
from auth import SignCache

# 从当前目录下的模块中导入各自的注册函数
from .image_mcp_tools import register_image_tools
from .video_mcp_tools import register_video_tools
# from .text_tools import register_text_tools # 未来可以添加

def register_all_tools(mcp: FastMCP, sign_cache_instance: SignCache):
    """
    调用所有工具模块的注册函数，将所有工具注册到 app 上。
    """
    register_image_tools(mcp, sign_cache_instance)
    register_video_tools(mcp, sign_cache_instance)
    # register_video_tools(mcp, sign_cache_instance) # 未来可以添加
    
    print("所有工具已成功注册！")