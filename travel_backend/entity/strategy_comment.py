#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
评论实体类
"""

class StrategyComment:
    """评论实体类"""
    
    def __init__(self, id=None, strategy_id=None, user_id=None, content=None, create_time=None, update_time=None, del_flag=0):
        """初始化评论对象
        
        Args:
            id: 评论ID
            strategy_id: 攻略ID
            user_id: 评论用户ID
            content: 评论内容
            create_time: 创建时间
            update_time: 更新时间
            del_flag: 逻辑删除标志
        """
        self.id = id
        self.strategy_id = strategy_id
        self.user_id = user_id
        self.content = content
        self.create_time = create_time
        self.update_time = update_time
        self.del_flag = del_flag
    
    def to_dict(self):
        """转换为字典
        
        Returns:
            dict: 评论信息字典
        """
        return {
            "id": self.id,
            "strategy_id": self.strategy_id,
            "user_id": self.user_id,
            "content": self.content,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "del_flag": self.del_flag
        }
