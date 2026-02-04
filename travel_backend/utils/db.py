#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据库连接工具类
"""
import pymysql
from pymysql.cursors import DictCursor

class Database:
    """数据库操作类"""
    
    def __init__(self):
        """初始化数据库连接"""
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.password = '612345'
        self.database = 'travel_db'
        self.charset = 'utf8mb4'
        self.cursorclass = DictCursor
        self.conn = None
        self._connect()
    
    def _connect(self):
        """建立数据库连接"""
        if self.conn is None or not self.conn.open:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                charset=self.charset,
                cursorclass=self.cursorclass
            )
    
    def get_cursor(self):
        """获取游标"""
        self._connect()
        return self.conn.cursor()
    
    def commit(self):
        """提交事务"""
        if self.conn and self.conn.open:
            self.conn.commit()
    
    def rollback(self):
        """回滚事务"""
        if self.conn and self.conn.open:
            self.conn.rollback()
    
    def close(self):
        """关闭连接"""
        if self.conn and self.conn.open:
            self.conn.close()

# 数据库连接实例
db = Database()
