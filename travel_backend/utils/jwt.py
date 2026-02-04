#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JWT工具类
"""
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


def generate_token(user_id):
    """生成JWT token
    
    Args:
        user_id: 用户ID
    
    Returns:
        str: JWT token
    """
    return create_access_token(identity=user_id)


def get_current_user_id():
    """获取当前登录用户ID
    
    Returns:
        int: 用户ID
    """
    return get_jwt_identity()


def jwt_required_decorator():
    """JWT认证装饰器
    
    Returns:
        function: 装饰器函数
    """
    return jwt_required()
