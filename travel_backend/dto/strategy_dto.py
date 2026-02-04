#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
攻略相关DTO
"""

class StrategyDTO:
    """攻略发布/编辑请求DTO"""
    
    def __init__(self, title, destination, content):
        """初始化攻略请求
        
        Args:
            title: 攻略标题
            destination: 目的地
            content: 攻略内容
        """
        self.title = title
        self.destination = destination
        self.content = content

class CommentDTO:
    """评论请求DTO"""
    
    def __init__(self, strategy_id, content):
        """初始化评论请求
        
        Args:
            strategy_id: 攻略ID
            content: 评论内容
        """
        self.strategy_id = strategy_id
        self.content = content
