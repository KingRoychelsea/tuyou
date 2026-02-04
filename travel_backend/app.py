#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flask主应用文件
"""
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

# 创建Flask应用实例
app = Flask(__name__)

# 配置
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key-change-in-production'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1小时过期

# 跨域配置
CORS(app, resources={r"/*": {"origins": "*"}})

# JWT配置
jwt = JWTManager(app)

# 文件上传配置
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 确保上传目录存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
# 静态文件配置
app.static_folder = 'static'
app.static_url_path = '/static'

# 导入路由和异常处理器
from routes import *
from exception.global_exception_handler import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
