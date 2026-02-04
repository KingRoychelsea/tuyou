#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户数据访问层
"""
from utils.db import db

class UserMapper:
    """用户数据访问类"""
    
    def get_by_id(self, user_id):
        """根据ID获取用户
        
        Args:
            user_id: 用户ID
        
        Returns:
            dict: 用户信息
        """
        cursor = db.get_cursor()
        try:
            sql = "SELECT * FROM sys_user WHERE id = %s AND del_flag = 0"
            cursor.execute(sql, (user_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
    
    def get_by_username(self, username):
        """根据用户名获取用户
        
        Args:
            username: 用户名
        
        Returns:
            dict: 用户信息
        """
        cursor = db.get_cursor()
        try:
            sql = "SELECT * FROM sys_user WHERE username = %s AND del_flag = 0"
            cursor.execute(sql, (username,))
            return cursor.fetchone()
        finally:
            cursor.close()
    
    def get_by_phone(self, phone):
        """根据手机号获取用户
        
        Args:
            phone: 手机号
        
        Returns:
            dict: 用户信息
        """
        cursor = db.get_cursor()
        try:
            sql = "SELECT * FROM sys_user WHERE phone = %s AND del_flag = 0"
            cursor.execute(sql, (phone,))
            return cursor.fetchone()
        finally:
            cursor.close()
    
    def get_by_account(self, account):
        """根据账号（用户名/手机号）获取用户
        
        Args:
            account: 账号
        
        Returns:
            dict: 用户信息
        """
        cursor = db.get_cursor()
        try:
            sql = "SELECT * FROM sys_user WHERE (username = %s OR phone = %s) AND del_flag = 0"
            cursor.execute(sql, (account, account))
            return cursor.fetchone()
        finally:
            cursor.close()
    
    def create(self, username, password, phone):
        """创建用户
        
        Args:
            username: 用户名
            password: 密码
            phone: 手机号
        
        Returns:
            int: 新创建的用户ID
        """
        cursor = db.get_cursor()
        try:
            sql = "INSERT INTO sys_user (username, password, phone) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, password, phone))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            raise e
        finally:
            cursor.close()

# 用户数据访问实例
user_mapper = UserMapper()
