#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一响应结果工具类
"""

def success(data=None, msg="操作成功"):
    """成功响应
    
    Args:
        data: 响应数据
        msg: 响应消息
    
    Returns:
        dict: 统一响应格式
    """
    return {
        "code": 200,
        "msg": msg,
        "data": data
    }

def error(code=400, msg="操作失败"):
    """错误响应
    
    Args:
        code: 错误状态码
        msg: 错误消息
    
    Returns:
        dict: 统一响应格式
    """
    return {
        "code": code,
        "msg": msg,
        "data": None
    }

def unauth(msg="未登录"):
    """未授权响应
    
    Args:
        msg: 响应消息
    
    Returns:
        dict: 统一响应格式
    """
    return {
        "code": 401,
        "msg": msg,
        "data": None
    }
