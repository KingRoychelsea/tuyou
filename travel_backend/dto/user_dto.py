#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户相关DTO
"""

class RegisterDTO:
    """注册请求DTO"""
    
    def __init__(self, username, password, phone):
        """初始化注册请求
        
        Args:
            username: 用户名
            password: 密码
            phone: 手机号
        """
        self.username = username
        self.password = password
        self.phone = phone

class LoginDTO:
    """登录请求DTO"""
    
    def __init__(self, account, password):
        """初始化登录请求
        
        Args:
            account: 账号（用户名/手机号）
            password: 密码
        """
        self.account = account
        self.password = password
