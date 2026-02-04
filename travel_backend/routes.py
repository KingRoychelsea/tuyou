#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
路由配置文件
"""
from app import app
from flask_jwt_extended import jwt_required
from controller.user_controller import user_controller
from controller.strategy_controller import strategy_controller
from controller.comment_controller import comment_controller

# 用户相关路由
@app.route('/api/user/register', methods=['POST'])
def register():
    """用户注册"""
    return user_controller.register()

@app.route('/api/user/login', methods=['POST'])
def login():
    """用户登录"""
    return user_controller.login()

@app.route('/api/user/info', methods=['GET'])
@jwt_required()
def get_user_info():
    """获取当前用户信息"""
    return user_controller.get_user_info()

# 攻略相关路由
@app.route('/api/strategy/list', methods=['GET'])
def get_strategy_list():
    """获取攻略列表"""
    return strategy_controller.get_strategy_list()

@app.route('/api/strategy/<int:strategy_id>', methods=['GET'])
def get_strategy(strategy_id):
    """获取攻略详情"""
    return strategy_controller.get_strategy(strategy_id)

@app.route('/api/strategy', methods=['POST'])
def create_strategy():
    """创建攻略"""
    return strategy_controller.create_strategy()

@app.route('/api/strategy/<int:strategy_id>', methods=['PUT'])
def update_strategy(strategy_id):
    """更新攻略"""
    return strategy_controller.update_strategy(strategy_id)

@app.route('/api/strategy/<int:strategy_id>', methods=['DELETE'])
def delete_strategy(strategy_id):
    """删除攻略"""
    return strategy_controller.delete_strategy(strategy_id)

# 评论相关路由
@app.route('/api/comment/list/<int:strategy_id>', methods=['GET'])
def get_comment_list(strategy_id):
    """获取评论列表"""
    return comment_controller.get_comment_list(strategy_id)

@app.route('/api/comment', methods=['POST'])
def create_comment():
    """创建评论"""
    return comment_controller.create_comment()

@app.route('/api/comment/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    """删除评论"""
    return comment_controller.delete_comment(comment_id)

# 健康检查路由
@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查"""
    return {"status": "ok"}
