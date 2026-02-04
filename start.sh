#!/bin/bash

# 启动脚本 - 途游攻略分享平台

echo "========================================"
echo "途游攻略分享平台启动脚本"
echo "========================================"

# 进入项目目录
cd "$(dirname "$0")/travel_backend" || {
    echo "错误：无法进入travel_backend目录"
    exit 1
}

# 检查并创建环境变量文件
if [ ! -f ".env" ]; then
    echo "未找到.env文件，从.env.example创建..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "已创建.env文件，请根据实际情况修改配置"
    else
        echo "错误：.env.example文件不存在"
        exit 1
    fi
fi

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误：Python 3 未安装"
    exit 1
fi

# 检查pip是否安装
if ! command -v pip3 &> /dev/null; then
    echo "错误：pip3 未安装"
    exit 1
fi

# 安装依赖
echo "安装依赖包..."
pip3 install -r requirements.txt || {
    echo "错误：依赖安装失败"
    exit 1
}

echo "依赖安装成功"

# 启动应用
echo "========================================"
echo "启动途游攻略分享平台..."
echo "访问地址: http://localhost:5000"
echo "========================================"

python3 app.py
