#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
评论数据访问层
"""
from utils.db import db

class CommentMapper:
    """评论数据访问类"""
    
    def get_by_id(self, comment_id):
        """根据ID获取评论
        
        Args:
            comment_id: 评论ID
        
        Returns:
            dict: 评论信息
        """
        cursor = db.get_cursor()
        try:
            sql = "SELECT * FROM strategy_comment WHERE id = %s AND del_flag = 0"
            cursor.execute(sql, (comment_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
    
    def get_by_strategy_id(self, strategy_id):
        """根据攻略ID获取评论列表
        
        Args:
            strategy_id: 攻略ID
        
        Returns:
            list: 评论列表
        """
        cursor = db.get_cursor()
        try:
            sql = "SELECT * FROM strategy_comment WHERE strategy_id = %s AND del_flag = 0 ORDER BY create_time DESC"
            cursor.execute(sql, (strategy_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def create(self, strategy_id, user_id, content):
        """创建评论
        
        Args:
            strategy_id: 攻略ID
            user_id: 用户ID
            content: 评论内容
        
        Returns:
            int: 新创建的评论ID
        """
        cursor = db.get_cursor()
        try:
            sql = "INSERT INTO strategy_comment (strategy_id, user_id, content) VALUES (%s, %s, %s)"
            cursor.execute(sql, (strategy_id, user_id, content))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            raise e
        finally:
            cursor.close()
    
    def delete(self, comment_id):
        """删除评论（逻辑删除）
        
        Args:
            comment_id: 评论ID
        
        Returns:
            bool: 删除是否成功
        """
        cursor = db.get_cursor()
        try:
            sql = "UPDATE strategy_comment SET del_flag = 1 WHERE id = %s"
            cursor.execute(sql, (comment_id,))
            db.commit()
            return cursor.rowcount > 0
        except Exception as e:
            db.rollback()
            raise e
        finally:
            cursor.close()

# 评论数据访问实例
comment_mapper = CommentMapper()
