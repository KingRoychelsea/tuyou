#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户业务层
"""
from mapper.user_mapper import user_mapper
from utils.jwt import generate_token

class UserService:
    """用户业务服务类"""
    
    def register(self, username, password, phone):
        """用户注册
        
        Args:
            username: 用户名
            password: 密码
            phone: 手机号
        
        Returns:
            dict: 注册结果
        """
        # 检查用户名是否已存在
        existing_user = user_mapper.get_by_username(username)
        if existing_user:
            raise Exception("用户名已存在")
        
        # 检查密码长度
        if len(password) < 6:
            raise Exception("密码长度至少6位")
        
        # 创建用户
        user_id = user_mapper.create(username, password, phone)
        return {"user_id": user_id, "username": username}
    
    def login(self, account, password):
        """用户登录
        
        Args:
            account: 账号（用户名/手机号）
            password: 密码
        
        Returns:
            dict: 登录结果，包含token和用户信息
        """
        # 根据账号获取用户
        user = user_mapper.get_by_account(account)
        if not user:
            raise Exception("账号或密码错误")
        
        # 验证密码
        if user['password'] != password:
            raise Exception("账号或密码错误")
        
        # 生成token
        token = generate_token(user['id'])
        
        return {
            "token": token,
            "user": {
                "id": user['id'],
                "username": user['username'],
                "phone": user['phone']
            }
        }
    
    def get_user_info(self, user_id):
        """获取用户信息
        
        Args:
            user_id: 用户ID
        
        Returns:
            dict: 用户信息
        """
        user = user_mapper.get_by_id(user_id)
        if not user:
            raise Exception("用户不存在")
        
        return {
            "id": user['id'],
            "username": user['username'],
            "phone": user['phone']
        }

# 用户业务服务实例
user_service = UserService()
