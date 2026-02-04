#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全局异常处理器
"""
from flask import jsonify
from app import app
from utils.response import error

# 全局异常处理器
@app.errorhandler(Exception)
def handle_exception(e):
    """处理所有未捕获的异常
    
    Args:
        e: 异常对象
    
    Returns:
        json: 错误响应
    """
    return jsonify(error(msg=str(e)))

# 404错误处理器
@app.errorhandler(404)
def handle_404(e):
    """处理404错误
    
    Args:
        e: 异常对象
    
    Returns:
        json: 错误响应
    """
    return jsonify(error(code=404, msg="请求的资源不存在"))

# 405错误处理器
@app.errorhandler(405)
def handle_405(e):
    """处理405错误
    
    Args:
        e: 异常对象
    
    Returns:
        json: 错误响应
    """
    return jsonify(error(code=405, msg="请求方法不允许"))
