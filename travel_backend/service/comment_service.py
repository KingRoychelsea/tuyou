#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
评论业务层
"""
from mapper.comment_mapper import comment_mapper
from mapper.user_mapper import user_mapper
from mapper.strategy_mapper import strategy_mapper

class CommentService:
    """评论业务服务类"""
    
    def get_comment_list(self, strategy_id):
        """获取评论列表
        
        Args:
            strategy_id: 攻略ID
        
        Returns:
            list: 评论列表，每条包含评论者信息
        """
        # 检查攻略是否存在
        strategy = strategy_mapper.get_by_id(strategy_id)
        if not strategy:
            raise Exception("攻略不存在")
        
        # 获取评论列表
        comments = comment_mapper.get_by_strategy_id(strategy_id)
        
        # 为每条评论添加评论者信息
        for comment in comments:
            user = user_mapper.get_by_id(comment['user_id'])
            if user:
                comment['commenter'] = user['username']
        
        return comments
    
    def create_comment(self, strategy_id, user_id, content):
        """创建评论
        
        Args:
            strategy_id: 攻略ID
            user_id: 用户ID
            content: 评论内容
        
        Returns:
            dict: 创建结果
        """
        # 检查攻略是否存在
        strategy = strategy_mapper.get_by_id(strategy_id)
        if not strategy:
            raise Exception("攻略不存在")
        
        # 检查评论内容
        if not content or len(content.strip()) == 0:
            raise Exception("评论内容不能为空")
        
        # 创建评论
        comment_id = comment_mapper.create(strategy_id, user_id, content)
        return {"comment_id": comment_id, "content": content}
    
    def delete_comment(self, comment_id, user_id):
        """删除评论
        
        Args:
            comment_id: 评论ID
            user_id: 用户ID
        
        Returns:
            bool: 删除是否成功
        """
        # 获取评论
        comment = comment_mapper.get_by_id(comment_id)
        if not comment:
            raise Exception("评论不存在")
        
        # 检查权限
        if comment['user_id'] != user_id:
            raise Exception("无权限删除此评论")
        
        # 删除评论
        deleted = comment_mapper.delete(comment_id)
        return deleted

# 评论业务服务实例
comment_service = CommentService()
