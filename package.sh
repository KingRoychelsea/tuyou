#!/bin/bash

# 打包脚本 - 途游攻略分享平台

echo "========================================"
echo "途游攻略分享平台打包脚本"
echo "========================================"

# 进入项目根目录
cd "$(dirname "$0")" || {
    echo "错误：无法进入项目根目录"
    exit 1
}

# 定义打包目录
PACKAGE_DIR="travel_package"
VERSION="$(date +%Y%m%d_%H%M%S)"
FINAL_PACKAGE="tuyou_${VERSION}.tar.gz"

echo "创建打包目录..."
# 清理旧的打包目录
rm -rf "${PACKAGE_DIR}"
rm -f "tuyou_*.tar.gz"

# 创建新的打包目录
mkdir -p "${PACKAGE_DIR}"

# 复制后端文件
echo "复制后端文件..."
mkdir -p "${PACKAGE_DIR}/travel_backend"
mkdir -p "${PACKAGE_DIR}/travel_backend/templates"
mkdir -p "${PACKAGE_DIR}/travel_backend/static/images"
mkdir -p "${PACKAGE_DIR}/travel_backend/controller"
mkdir -p "${PACKAGE_DIR}/travel_backend/service"
mkdir -p "${PACKAGE_DIR}/travel_backend/mapper"
mkdir -p "${PACKAGE_DIR}/travel_backend/entity"
mkdir -p "${PACKAGE_DIR}/travel_backend/dto"
mkdir -p "${PACKAGE_DIR}/travel_backend/exception"
mkdir -p "${PACKAGE_DIR}/travel_backend/utils"

# 复制核心文件
cp -r travel_backend/*.py "${PACKAGE_DIR}/travel_backend/"
cp -r travel_backend/controller/*.py "${PACKAGE_DIR}/travel_backend/controller/"
cp -r travel_backend/service/*.py "${PACKAGE_DIR}/travel_backend/service/"
cp -r travel_backend/mapper/*.py "${PACKAGE_DIR}/travel_backend/mapper/"
cp -r travel_backend/entity/*.py "${PACKAGE_DIR}/travel_backend/entity/"
cp -r travel_backend/dto/*.py "${PACKAGE_DIR}/travel_backend/dto/"
cp -r travel_backend/exception/*.py "${PACKAGE_DIR}/travel_backend/exception/"
cp -r travel_backend/utils/*.py "${PACKAGE_DIR}/travel_backend/utils/"
cp -r travel_backend/templates/*.html "${PACKAGE_DIR}/travel_backend/templates/"
cp travel_backend/requirements.txt "${PACKAGE_DIR}/travel_backend/"
cp travel_backend/.env.example "${PACKAGE_DIR}/travel_backend/"

# 复制根目录文件
echo "复制根目录文件..."
cp start.sh "${PACKAGE_DIR}/"
cp README.md "${PACKAGE_DIR}/"
cp database_init.sql "${PACKAGE_DIR}/"

# 清理不必要的文件
echo "清理不必要的文件..."
find "${PACKAGE_DIR}" -name "__pycache__" -type d -exec rm -rf {} \; 2>/dev/null
find "${PACKAGE_DIR}" -name "*.pyc" -delete 2>/dev/null

# 创建压缩包
echo "创建压缩包..."
tar -czf "${FINAL_PACKAGE}" "${PACKAGE_DIR}"

# 清理打包目录
rm -rf "${PACKAGE_DIR}"

echo "========================================"
echo "打包完成！"
echo "生成的包文件：${FINAL_PACKAGE}"
echo "========================================"
echo ""
echo "部署步骤："
echo "1. 将 ${FINAL_PACKAGE} 上传到目标服务器"
echo "2. 解压：tar -xzf ${FINAL_PACKAGE}"
echo "3. 进入目录：cd travel_package"
echo "4. 修改配置：编辑 travel_backend/.env 文件"
echo "5. 启动服务：./start.sh"
echo ""
echo "访问地址：http://服务器IP:5000"
