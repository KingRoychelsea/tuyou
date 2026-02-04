#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
攻略数据访问层
"""
from utils.db import db

class StrategyMapper:
    """攻略数据访问类"""
    
    def get_by_id(self, strategy_id):
        """根据ID获取攻略
        
        Args:
            strategy_id: 攻略ID
        
        Returns:
            dict: 攻略信息
        """
        cursor = db.get_cursor()
        try:
            sql = "SELECT * FROM travel_strategy WHERE id = %s AND del_flag = 0"
            cursor.execute(sql, (strategy_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
    
    def get_list(self, keyword=None, page=1, page_size=10):
        """获取攻略列表
        
        Args:
            keyword: 搜索关键词（标题/目的地）
            page: 页码
            page_size: 每页大小
        
        Returns:
            list: 攻略列表
        """
        cursor = db.get_cursor()
        try:
            offset = (page - 1) * page_size
            if keyword:
                sql = "SELECT * FROM travel_strategy WHERE (title LIKE %s OR destination LIKE %s) AND del_flag = 0 ORDER BY create_time DESC LIMIT %s OFFSET %s"
                cursor.execute(sql, (f"%{keyword}%", f"%{keyword}%", page_size, offset))
            else:
                sql = "SELECT * FROM travel_strategy WHERE del_flag = 0 ORDER BY create_time DESC LIMIT %s OFFSET %s"
                cursor.execute(sql, (page_size, offset))
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def create(self, title, destination, content, images, user_id):
        """创建攻略
        
        Args:
            title: 标题
            destination: 目的地
            content: 内容
            images: 图片路径（逗号分隔）
            user_id: 用户ID
        
        Returns:
            int: 新创建的攻略ID
        """
        cursor = db.get_cursor()
        try:
            sql = "INSERT INTO travel_strategy (title, destination, content, images, user_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (title, destination, content, images, user_id))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            raise e
        finally:
            cursor.close()
    
    def update(self, strategy_id, title, destination, content, images):
        """更新攻略
        
        Args:
            strategy_id: 攻略ID
            title: 标题
            destination: 目的地
            content: 内容
            images: 图片路径（逗号分隔）
        
        Returns:
            bool: 更新是否成功
        """
        cursor = db.get_cursor()
        try:
            sql = "UPDATE travel_strategy SET title = %s, destination = %s, content = %s, images = %s WHERE id = %s AND del_flag = 0"
            cursor.execute(sql, (title, destination, content, images, strategy_id))
            db.commit()
            return cursor.rowcount > 0
        except Exception as e:
            db.rollback()
            raise e
        finally:
            cursor.close()
    
    def delete(self, strategy_id):
        """删除攻略（逻辑删除）
        
        Args:
            strategy_id: 攻略ID
        
        Returns:
            bool: 删除是否成功
        """
        cursor = db.get_cursor()
        try:
            sql = "UPDATE travel_strategy SET del_flag = 1 WHERE id = %s"
            cursor.execute(sql, (strategy_id,))
            db.commit()
            return cursor.rowcount > 0
        except Exception as e:
            db.rollback()
            raise e
        finally:
            cursor.close()

# 攻略数据访问实例
strategy_mapper = StrategyMapper()
