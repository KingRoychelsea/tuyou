#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
攻略实体类
"""

class TravelStrategy:
    """攻略实体类"""
    
    def __init__(self, id=None, title=None, destination=None, content=None, images=None, user_id=None, create_time=None, update_time=None, del_flag=0):
        """初始化攻略对象
        
        Args:
            id: 攻略ID
            title: 标题
            destination: 目的地
            content: 内容
            images: 图片路径（多个用逗号分隔）
            user_id: 发布用户ID
            create_time: 创建时间
            update_time: 更新时间
            del_flag: 逻辑删除标志
        """
        self.id = id
        self.title = title
        self.destination = destination
        self.content = content
        self.images = images
        self.user_id = user_id
        self.create_time = create_time
        self.update_time = update_time
        self.del_flag = del_flag
    
    def to_dict(self):
        """转换为字典
        
        Returns:
            dict: 攻略信息字典
        """
        return {
            "id": self.id,
            "title": self.title,
            "destination": self.destination,
            "content": self.content,
            "images": self.images,
            "user_id": self.user_id,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "del_flag": self.del_flag
        }
