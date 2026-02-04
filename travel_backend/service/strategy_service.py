#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
攻略业务层
"""
from mapper.strategy_mapper import strategy_mapper
from mapper.user_mapper import user_mapper

class StrategyService:
    """攻略业务服务类"""
    
    def get_strategy(self, strategy_id):
        """获取攻略详情
        
        Args:
            strategy_id: 攻略ID
        
        Returns:
            dict: 攻略详情，包含发布者信息
        """
        # 获取攻略
        strategy = strategy_mapper.get_by_id(strategy_id)
        if not strategy:
            raise Exception("攻略不存在")
        
        # 获取发布者信息
        user = user_mapper.get_by_id(strategy['user_id'])
        if user:
            strategy['publisher'] = user['username']
        
        return strategy
    
    def get_strategy_list(self, keyword=None, page=1, page_size=10):
        """获取攻略列表
        
        Args:
            keyword: 搜索关键词
            page: 页码
            page_size: 每页大小
        
        Returns:
            list: 攻略列表，每条包含发布者信息
        """
        # 获取攻略列表
        strategies = strategy_mapper.get_list(keyword, page, page_size)
        
        # 为每条攻略添加发布者信息
        for strategy in strategies:
            user = user_mapper.get_by_id(strategy['user_id'])
            if user:
                strategy['publisher'] = user['username']
        
        return strategies
    
    def create_strategy(self, title, destination, content, images, user_id):
        """创建攻略
        
        Args:
            title: 标题
            destination: 目的地
            content: 内容
            images: 图片路径列表
            user_id: 用户ID
        
        Returns:
            dict: 创建结果
        """
        # 检查标题
        if not title or len(title.strip()) == 0:
            raise Exception("标题不能为空")
        
        # 检查内容长度
        if len(content) < 10:
            raise Exception("攻略内容至少10个字")
        
        # 检查图片数量
        if len(images) > 5:
            raise Exception("最多上传5张图片")
        
        # 格式化图片路径
        images_str = ','.join(images) if images else None
        
        # 创建攻略
        strategy_id = strategy_mapper.create(title, destination, content, images_str, user_id)
        return {"strategy_id": strategy_id, "title": title}
    
    def update_strategy(self, strategy_id, title, destination, content, images, user_id):
        """更新攻略
        
        Args:
            strategy_id: 攻略ID
            title: 标题
            destination: 目的地
            content: 内容
            images: 图片路径列表
            user_id: 用户ID
        
        Returns:
            dict: 更新结果
        """
        # 获取攻略
        strategy = strategy_mapper.get_by_id(strategy_id)
        if not strategy:
            raise Exception("攻略不存在")
        
        # 检查权限
        if strategy['user_id'] != user_id:
            raise Exception("无权限修改此攻略")
        
        # 检查标题
        if not title or len(title.strip()) == 0:
            raise Exception("标题不能为空")
        
        # 检查内容长度
        if len(content) < 10:
            raise Exception("攻略内容至少10个字")
        
        # 检查图片数量
        if len(images) > 5:
            raise Exception("最多上传5张图片")
        
        # 格式化图片路径
        images_str = ','.join(images) if images else None
        
        # 更新攻略
        updated = strategy_mapper.update(strategy_id, title, destination, content, images_str)
        if not updated:
            raise Exception("更新失败")
        
        return {"strategy_id": strategy_id, "title": title}
    
    def delete_strategy(self, strategy_id, user_id):
        """删除攻略
        
        Args:
            strategy_id: 攻略ID
            user_id: 用户ID
        
        Returns:
            bool: 删除是否成功
        """
        # 获取攻略
        strategy = strategy_mapper.get_by_id(strategy_id)
        if not strategy:
            raise Exception("攻略不存在")
        
        # 检查权限
        if strategy['user_id'] != user_id:
            raise Exception("无权限删除此攻略")
        
        # 删除攻略
        deleted = strategy_mapper.delete(strategy_id)
        return deleted

# 攻略业务服务实例
strategy_service = StrategyService()
