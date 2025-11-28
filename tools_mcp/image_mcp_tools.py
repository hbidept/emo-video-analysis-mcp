# tools/image_tools.py

import logging
from pydantic import Field
from mcp.server.fastmcp import FastMCP

# 依赖于项目中的其他模块
from extra_client import call_image_api
from utils import get_auth_keys
from auth import SignCache




def register_image_tools(mcp: FastMCP, sign_cache_instance: SignCache):
    """
    将所有图像处理相关的工具注册到 FastMCP 应用上。
    """
    async def base_image_tool(model_name, image_url: str, position_type: str,) -> dict:
        """
        基础图像处理工具函数，调用指定的图像API模型。
        """
        try:
            keys = get_auth_keys()
            sign = await sign_cache_instance.get_sign(keys["appKey"], keys["appSecret"])
            logging.info(f"成功获取 Sign: {sign[:4]}...{sign[-4:]}")
            
            result = await call_image_api(
                model_name=model_name,
                image_url=image_url,
                position_type=position_type,
                app_key=keys['appKey'],
                sign=sign
            )
            return result
            
        except ValueError as e:
            return {"code": 401, "data": f"认证失败: {str(e)}"}
        except Exception as e:
            logging.error(f"处理请求时发生严重错误: {str(e)}")
            return {"code": 500, "data": f"服务器内部错误: {str(e)}"}
    
    @mcp.tool()
    async def lianxin_image_api_EmotionRecognitionModel_front(
         image_url: str = Field(description="图像链接")
    ) -> dict:
        """
        名称: 对图像进行情绪分析
        描述: 使用连信情绪识别模型对图像进行情绪分析，适用于怼脸、平视 视角。
        Args:
            image_url (str): 要分析的公开可访问的图像 URL。
        Returns:
            dict: 包含API响应的字典，包含状态码和数据。
        """
        return await base_image_tool(
            model_name="EmotionRecognitionModel",
            image_url=image_url,
            position_type="front_face"
        )
    
    @mcp.tool()
    async def lianxin_image_api_PressureDetectionModel_front(
        image_url:str = (Field(description="图像链接"))
    )-> dict:
        """
        Name: 对图像进行压力分析
        Desciption: 使用连信压力分析模型对图像检测并识别人脸静态图片中的面部表情、肌肉紧张度、微动作等特征，评估个体可能正在承受的压力水平。适用于怼脸、平视 视角。
        Args:
            image_url (str): 图像链接
        Returns:
            dict: 包含API响应的字典，包含状态码和数据

        """
        return await base_image_tool(
            model_name="PressureDetectionModel",
            image_url=image_url,
            position_type="front_face"
        )  # image_api("PressureDetectionModel", image_url, "front_face")
    
    @mcp.tool()
    async def lianxin_image_api_PadRecognitionModel_front(
        image_url:str = (Field(description="图像链接"))
    )-> dict:
        """
        Name: 对图像进行情绪强度分析
        Desciption: 使用连信情绪强度模型对图像进行情绪强度分析，输出PAD（愉悦度、激活度、支配度）三维情绪空间的量化评估，提供更精细的情绪描述。适用于怼脸、平视 视角。
        Args:
            image_url (str): 图像链接
        Returns:
            dict: 包含API响应的字典，包含状态码和数据

        """
        return await base_image_tool(
            model_name="PadRecognitionModel",
            image_url=image_url,
            position_type="front_face"
        )  # image_api("PadRecognitionModel", image_url, "front_face")

    @mcp.tool()
    async def lianxin_image_api_EmotionRecognitionModel_monitor(
         image_url: str = Field(description="图像链接")
    ) -> dict:
        """
        名称: 对图像进行情绪分析
        描述: 使用连信情绪识别模型对图像进行情绪分析，适用于高位、监控 视角。
        Args:
            image_url (str): 要分析的公开可访问的图像 URL。
        Returns:
            dict: 包含API响应的字典，包含状态码和数据。
        """
        return await base_image_tool(
            model_name="EmotionRecognitionModel",
            image_url=image_url,
            position_type="monitor_face"
        )
    
    @mcp.tool()
    async def lianxin_image_api_PressureDetectionModel_monitor(
        image_url:str = (Field(description="图像链接"))
    )-> dict:
        """
        Name: 对图像进行压力分析
        Desciption: 使用连信压力分析模型对图像检测并识别人脸静态图片中的面部表情、肌肉紧张度、微动作等特征，评估个体可能正在承受的压力水平。适用于高位、监控 视角。
        Args:
            image_url (str): 图像链接
        Returns:
            dict: 包含API响应的字典，包含状态码和数据

        """
        return await base_image_tool(
            model_name="PressureDetectionModel",
            image_url=image_url,
            position_type="monitor_face"
        )  # image_api("PressureDetectionModel", image_url, "monitor_face")
    
    @mcp.tool()
    async def lianxin_image_api_PadRecognitionModel_monitor(
        image_url:str = (Field(description="图像链接"))
    )-> dict:
        """
        Name: 对图像进行情绪强度分析
        Desciption: 使用连信情绪强度模型对图像进行情绪强度分析，输出PAD（愉悦度、激活度、支配度）三维情绪空间的量化评估，提供更精细的情绪描述。适用于高位、监控 视角。
        Args:
            image_url (str): 图像链接
        Returns:
            dict: 包含API响应的字典，包含状态码和数据

        """
        return await base_image_tool(
            model_name="PadRecognitionModel",
            image_url=image_url,
            position_type="monitor_face"
        )  # image_api("PadRecognitionModel", image_url, "monitor_face")
    # 如果还有其他图像相关的工具，可以继续在这里定义和注册
    # @mcp.tool()
    # async def another_image_tool(...):
    #     ...
