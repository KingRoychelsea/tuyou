#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户控制层
"""
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from service.user_service import user_service
from utils.response import success, error, unauth
from dto.user_dto import RegisterDTO, LoginDTO

class UserController:
    """用户控制器类"""
    
    def register(self):
        """用户注册
        
        Returns:
            json: 注册结果
        """
        try:
            # 获取请求参数
            data = request.get_json()
            if not data:
                return jsonify(error(msg="请求参数不能为空"))
            
            # 验证参数
            username = data.get('username')
            password = data.get('password')
            phone = data.get('phone')
            
            if not username or not password or not phone:
                return jsonify(error(msg="用户名、密码、手机号不能为空"))
            
            # 调用业务层注册
            result = user_service.register(username, password, phone)
            return jsonify(success(data=result, msg="注册成功"))
        except Exception as e:
            return jsonify(error(msg=str(e)))
    
    def login(self):
        """用户登录
        
        Returns:
            json: 登录结果
        """
        try:
            # 获取请求参数
            data = request.get_json()
            if not data:
                return jsonify(error(msg="请求参数不能为空"))
            
            # 验证参数
            account = data.get('account')
            password = data.get('password')
            
            if not account or not password:
                return jsonify(error(msg="账号和密码不能为空"))
            
            # 调用业务层登录
            result = user_service.login(account, password)
            return jsonify(success(data=result, msg="登录成功"))
        except Exception as e:
            return jsonify(error(msg=str(e)))
    
    def get_user_info(self):
        """获取当前用户信息
        
        Returns:
            json: 用户信息
        """
        try:
            # 获取当前用户ID
            user_id = get_jwt_identity()
            
            # 调用业务层获取用户信息
            user_info = user_service.get_user_info(user_id)
            return jsonify(success(data=user_info))
        except Exception as e:
            return jsonify(error(msg=str(e)))

# 用户控制器实例
user_controller = UserController()
