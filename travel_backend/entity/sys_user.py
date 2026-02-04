#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户实体类
"""

class SysUser:
    """用户实体类"""
    
    def __init__(self, id=None, username=None, password=None, phone=None, create_time=None, update_time=None, del_flag=0):
        """初始化用户对象
        
        Args:
            id: 用户ID
            username: 用户名
            password: 密码
            phone: 手机号
            create_time: 创建时间
            update_time: 更新时间
            del_flag: 逻辑删除标志
        """
        self.id = id
        self.username = username
        self.password = password
        self.phone = phone
        self.create_time = create_time
        self.update_time = update_time
        self.del_flag = del_flag
    
    def to_dict(self):
        """转换为字典
        
        Returns:
            dict: 用户信息字典
        """
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "phone": self.phone,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "del_flag": self.del_flag
        }
