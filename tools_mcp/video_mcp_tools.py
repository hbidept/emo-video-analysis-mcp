import logging
from pydantic import Field
from mcp.server.fastmcp import FastMCP

# 依赖于项目中的其他模块
from extra_client import call_video_api
from utils import get_auth_keys
from auth import SignCache




def register_video_tools(mcp: FastMCP, sign_cache_instance: SignCache):
    """
    将所有视频处理相关的工具注册到 FastMCP 应用上。
    """
    async def base_video_tool(model_name, video_url: str, position_type: str,num_frames_per_second:int) -> dict:
        """
        基础视频处理工具函数，调用指定的视频API模型。
        """
        try:
            keys = get_auth_keys()
            sign = await sign_cache_instance.get_sign(keys["appKey"], keys["appSecret"])
            logging.info(f"成功获取 Sign: {sign[:4]}...{sign[-4:]}")
            
            result = await call_video_api(
                model_name=model_name,
                video_url=video_url,
                position_type=position_type,
                num_frames_per_second=num_frames_per_second,
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
    async def lianxin_video_api_EmotionRecognitionModel_front(
         video_url: str = Field(description="视频链接"),num_frames_per_second: int = (Field(default=1, description="每秒抽取的帧数"))
    ) -> dict:
        """
        名称: 对视频进行情绪分析
        描述: 使用连信情绪识别模型对视频进行情绪分析，适用于怼脸、平视 视角。
        Args:
            video_url (str):视频链接
            num_frames_per_second (int): 每秒抽取的帧数
        Returns:
            dict: 包含API响应的字典，包含状态码和数据。
        """
        return await base_video_tool(
            model_name="EmotionRecognitionModel",
            video_url=video_url,
            position_type="front_face",
            num_frames_per_second=num_frames_per_second
        )
    
    @mcp.tool()
    async def lianxin_video_api_PressureDetectionModel_front(
        video_url:str = (Field(description="视频链接")),num_frames_per_second: int = (Field(default=1, description="每秒抽取的帧数"))
    )-> dict:
        """
        Name: 对视频进行压力分析
        Desciption: 使用连信压力分析模型对视频检测并识别人的面部表情、肌肉紧张度、微动作等特征，评估个体可能正在承受的压力水平。适用于怼脸、平视 视角。
        Args:
        video_url (str):视频链接
        num_frames_per_second (int): 每秒抽取的帧数
        Returns:
            dict: 包含API响应的字典，包含状态码和数据

        """
        return await base_video_tool(
            model_name="PressureDetectionModel",
            video_url=video_url,
            position_type="front_face",
            num_frames_per_second=num_frames_per_second
        )
    
    @mcp.tool()
    async def lianxin_video_api_PadRecognitionModel_front(
        video_url:str = (Field(description="视频链接")),num_frames_per_second: int = (Field(default=5, description="每秒抽取的帧数"))
    )-> dict:
        """
        Name: 对视频进行情绪强度分析
        Desciption: 使用连信情绪强度模型对视频进行情绪强度分析，输出PAD（愉悦度、激活度、支配度）三维情绪空间的量化评估，提供更精细的情绪描述。适用于怼脸、平视 视角。
        Args:
            video_url (str):视频链接
            num_frames_per_second (int): 每秒抽取的帧数
        Returns:
            dict: 包含API响应的字典，包含状态码和数据

        """
        return await base_video_tool(
            model_name="PadRecognitionModel",
            video_url=video_url,
            position_type="front_face",
            num_frames_per_second=num_frames_per_second
        )

    @mcp.tool()
    async def lianxin_video_api_EmotionRecognitionModel_monitor(
         video_url: str = Field(description="视频链接"),num_frames_per_second: int = (Field(default=1, description="每秒抽取的帧数"))
    ) -> dict:
        """
        名称: 对视频进行情绪分析
        描述: 使用连信情绪识别模型对视频进行情绪分析，适用于高位、监控 视角。
        Args:
        video_url (str):视频链接
        num_frames_per_second (int): 每秒抽取的帧数
        Returns:
            dict: 包含API响应的字典，包含状态码和数据。
        """
        return await base_video_tool(
            model_name="EmotionRecognitionModel",
            video_url=video_url,
            position_type="monitor_face",
            num_frames_per_second=num_frames_per_second
        )
    
    @mcp.tool()
    async def lianxin_video_api_PressureDetectionModel_monitor(
        video_url:str = (Field(description="视频链接")),num_frames_per_second: int = (Field(default=1, description="每秒抽取的帧数"))
    )-> dict:
        """
        Name: 对视频进行压力分析
        Desciption: 使用连信压力分析模型对视频检测并识别人的面部表情、肌肉紧张度、微动作等特征，评估个体可能正在承受的压力水平。适用于高位、监控 视角。
        Args:
        video_url (str):视频链接
        num_frames_per_second (int): 每秒抽取的帧数
        Returns:
            dict: 包含API响应的字典，包含状态码和数据

        """
        return await base_video_tool(
            model_name="PressureDetectionModel",
            video_url=video_url,
            position_type="monitor_face",
            num_frames_per_second=num_frames_per_second
        )
    
    @mcp.tool()
    async def lianxin_video_api_PadRecognitionModel_monitor(
        video_url:str = (Field(description="视频链接")),num_frames_per_second: int = (Field(default=5, description="每秒抽取的帧数"))
    )-> dict:
        """
        Name: 对视频进行情绪强度分析
        Desciption: 使用连信情绪强度模型对视频进行情绪强度分析，输出PAD（愉悦度、激活度、支配度）三维情绪空间的量化评估，提供更精细的情绪描述。适用于高位、监控 视角。
        Args:
        video_url (str):视频链接
        num_frames_per_second (int): 每秒抽取的帧数
        Returns:
            dict: 包含API响应的字典，包含状态码和数据

        """
        return await base_video_tool(
            model_name="PadRecognitionModel",
            video_url=video_url,
            position_type="monitor_face",
            num_frames_per_second=num_frames_per_second
        )
    # 如果还有其他视频相关的工具，可以继续在这里定义和注册
    # @mcp.tool()
    # async def another_video_tool(...):
    #     ...
