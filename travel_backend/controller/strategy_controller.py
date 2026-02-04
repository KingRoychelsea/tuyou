#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
攻略控制层
"""
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from service.strategy_service import strategy_service
from utils.response import success, error
from utils.upload import upload_multiple_files

class StrategyController:
    """攻略控制器类"""
    
    def get_strategy_list(self):
        """获取攻略列表
        
        Returns:
            json: 攻略列表
        """
        try:
            # 获取请求参数
            keyword = request.args.get('keyword')
            page = int(request.args.get('page', 1))
            page_size = int(request.args.get('page_size', 10))
            
            # 调用业务层获取攻略列表
            strategies = strategy_service.get_strategy_list(keyword, page, page_size)
            return jsonify(success(data=strategies))
        except Exception as e:
            return jsonify(error(msg=str(e)))
    
    def get_strategy(self, strategy_id):
        """获取攻略详情
        
        Args:
            strategy_id: 攻略ID
        
        Returns:
            json: 攻略详情
        """
        try:
            # 调用业务层获取攻略详情
            strategy = strategy_service.get_strategy(strategy_id)
            return jsonify(success(data=strategy))
        except Exception as e:
            return jsonify(error(msg=str(e)))
    
    @jwt_required()
    def create_strategy(self):
        """创建攻略
        
        Returns:
            json: 创建结果
        """
        try:
            # 获取当前用户ID
            user_id = get_jwt_identity()
            
            # 获取请求参数
            title = request.form.get('title')
            destination = request.form.get('destination')
            content = request.form.get('content')
            
            # 检查参数
            if not title or not destination or not content:
                return jsonify(error(msg="标题、目的地、内容不能为空"))
            
            # 处理文件上传
            files = request.files.getlist('images')
            images = upload_multiple_files(files)
            
            # 调用业务层创建攻略
            result = strategy_service.create_strategy(title, destination, content, images, user_id)
            return jsonify(success(data=result, msg="攻略发布成功"))
        except Exception as e:
            return jsonify(error(msg=str(e)))
    
    @jwt_required()
    def update_strategy(self, strategy_id):
        """更新攻略
        
        Args:
            strategy_id: 攻略ID
        
        Returns:
            json: 更新结果
        """
        try:
            # 获取当前用户ID
            user_id = get_jwt_identity()
            
            # 获取请求参数
            title = request.form.get('title')
            destination = request.form.get('destination')
            content = request.form.get('content')
            
            # 检查参数
            if not title or not destination or not content:
                return jsonify(error(msg="标题、目的地、内容不能为空"))
            
            # 处理文件上传
            files = request.files.getlist('images')
            images = upload_multiple_files(files)
            
            # 调用业务层更新攻略
            result = strategy_service.update_strategy(strategy_id, title, destination, content, images, user_id)
            return jsonify(success(data=result, msg="攻略更新成功"))
        except Exception as e:
            return jsonify(error(msg=str(e)))
    
    @jwt_required()
    def delete_strategy(self, strategy_id):
        """删除攻略
        
        Args:
            strategy_id: 攻略ID
        
        Returns:
            json: 删除结果
        """
        try:
            # 获取当前用户ID
            user_id = get_jwt_identity()
            
            # 调用业务层删除攻略
            deleted = strategy_service.delete_strategy(strategy_id, user_id)
            if deleted:
                return jsonify(success(msg="攻略删除成功"))
            else:
                return jsonify(error(msg="攻略删除失败"))
        except Exception as e:
            return jsonify(error(msg=str(e)))

# 攻略控制器实例
strategy_controller = StrategyController()
