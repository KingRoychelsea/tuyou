#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件上传工具类
"""
import os
import uuid
from flask import request, current_app
from werkzeug.utils import secure_filename


def allowed_file(filename):
    """检查文件是否允许上传
    
    Args:
        filename: 文件名
    
    Returns:
        bool: 是否允许上传
    """
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(file):
    """上传文件
    
    Args:
        file: 文件对象
    
    Returns:
        str: 文件保存路径
    """
    if file and allowed_file(file.filename):
        # 生成唯一文件名
        filename = secure_filename(file.filename)
        ext = filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}.{ext}"
        # 保存文件
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        # 返回相对路径
        return f"images/{unique_filename}"
    return None


def upload_multiple_files(files):
    """上传多个文件
    
    Args:
        files: 文件列表
    
    Returns:
        list: 文件保存路径列表
    """
    file_paths = []
    for file in files:
        if file:
            path = upload_file(file)
            if path:
                file_paths.append(path)
    return file_paths
