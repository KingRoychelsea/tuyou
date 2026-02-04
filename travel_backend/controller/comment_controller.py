#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
评论控制层
"""
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from service.comment_service import comment_service
from utils.response import success, error

class CommentController:
    """评论控制器类"""
    
    def get_comment_list(self, strategy_id):
        """获取评论列表
        
        Args:
            strategy_id: 攻略ID
        
        Returns:
            json: 评论列表
        """
        try:
            # 调用业务层获取评论列表
            comments = comment_service.get_comment_list(strategy_id)
            return jsonify(success(data=comments))
        except Exception as e:
            return jsonify(error(msg=str(e)))
    
    @jwt_required()
    def create_comment(self):
        """创建评论
        
        Returns:
            json: 创建结果
        """
        try:
            # 获取当前用户ID
            user_id = get_jwt_identity()
            
            # 获取请求参数
            data = request.get_json()
            if not data:
                return jsonify(error(msg="请求参数不能为空"))
            
            strategy_id = data.get('strategy_id')
            content = data.get('content')
            
            # 检查参数
            if not strategy_id or not content:
                return jsonify(error(msg="攻略ID和评论内容不能为空"))
            
            # 调用业务层创建评论
            result = comment_service.create_comment(strategy_id, user_id, content)
            return jsonify(success(data=result, msg="评论发布成功"))
        except Exception as e:
            return jsonify(error(msg=str(e)))
    
    @jwt_required()
    def delete_comment(self, comment_id):
        """删除评论
        
        Args:
            comment_id: 评论ID
        
        Returns:
            json: 删除结果
        """
        try:
            # 获取当前用户ID
            user_id = get_jwt_identity()
            
            # 调用业务层删除评论
            deleted = comment_service.delete_comment(comment_id, user_id)
            if deleted:
                return jsonify(success(msg="评论删除成功"))
            else:
                return jsonify(error(msg="评论删除失败"))
        except Exception as e:
            return jsonify(error(msg=str(e)))

# 评论控制器实例
comment_controller = CommentController()
