# 途游攻略分享平台部署文档

## 项目概述

途游攻略分享平台是一个基于Python、Flask、Vue.js和MariaDB的全栈旅游攻略分享系统，用户可以注册登录、浏览攻略、发布自己的旅游攻略并进行评论互动。

## 系统要求

### 硬件要求
- CPU: 1核及以上
- 内存: 1GB及以上
- 存储空间: 10GB及以上

### 软件要求
- **操作系统**: Linux (CentOS 7/8, Ubuntu 18.04+)
- **Python**: 3.6+
- **MariaDB/MySQL**: 5.7+
- **网络**: 支持TCP/IP协议，开放5000端口

## 部署步骤

### 1. 准备数据库

#### 1.1 安装MariaDB/MySQL

**CentOS/RHEL**: 
```bash
sudo yum install -y mariadb-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo mysql_secure_installation
```

**Ubuntu/Debian**: 
```bash
sudo apt update
sudo apt install -y mysql-server
sudo mysql_secure_installation
```

#### 1.2 初始化数据库

1. **登录数据库**:
   ```bash
   mysql -u root -p
   ```

2. **执行初始化脚本**:
   ```sql
   -- 创建数据库
   CREATE DATABASE IF NOT EXISTS travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   
   -- 创建用户并授权
   CREATE USER IF NOT EXISTS 'travel_user'@'localhost' IDENTIFIED BY 'your_database_password';
   GRANT ALL PRIVILEGES ON travel_db.* TO 'travel_user'@'localhost';
   FLUSH PRIVILEGES;
   
   -- 使用数据库
   USE travel_db;
   
   -- 创建用户表
   CREATE TABLE IF NOT EXISTS sys_user (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
       password VARCHAR(50) NOT NULL COMMENT '密码（明文存储）',
       phone VARCHAR(20) NOT NULL COMMENT '手机号',
       create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
       update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
       del_flag TINYINT DEFAULT 0 COMMENT '逻辑删除（0-未删/1-已删）'
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
   
   -- 创建攻略表
   CREATE TABLE IF NOT EXISTS travel_strategy (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(100) NOT NULL COMMENT '攻略标题',
       destination VARCHAR(50) NOT NULL COMMENT '目的地',
       content TEXT NOT NULL COMMENT '攻略内容',
       images VARCHAR(1000) COMMENT '图片路径（多个图片用逗号分隔）',
       user_id INT NOT NULL COMMENT '发布用户ID',
       create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
       update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
       del_flag TINYINT DEFAULT 0 COMMENT '逻辑删除（0-未删/1-已删）',
       FOREIGN KEY (user_id) REFERENCES sys_user(id)
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='攻略表';
   
   -- 创建评论表
   CREATE TABLE IF NOT EXISTS strategy_comment (
       id INT AUTO_INCREMENT PRIMARY KEY,
       strategy_id INT NOT NULL COMMENT '攻略ID',
       user_id INT NOT NULL COMMENT '评论用户ID',
       content VARCHAR(500) NOT NULL COMMENT '评论内容',
       create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
       update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
       del_flag TINYINT DEFAULT 0 COMMENT '逻辑删除（0-未删/1-已删）',
       FOREIGN KEY (strategy_id) REFERENCES travel_strategy(id),
       FOREIGN KEY (user_id) REFERENCES sys_user(id)
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='评论表';
   
   -- 插入测试数据
   INSERT INTO sys_user (username, password, phone) VALUES
   ('admin', '123456', '13800138001'),
   ('user', '123456', '13800138002');
   
   INSERT INTO travel_strategy (title, destination, content, images, user_id) VALUES
   ('北京三日游攻略', '北京', '第一天游览故宫，第二天爬长城，第三天逛胡同。', 'images/20240101_001.jpg,images/20240101_002.jpg', 1),
   ('上海迪士尼乐园游玩指南', '上海', '建议早上8点到达，先玩热门项目，晚上看烟花表演。', 'images/20240102_001.jpg', 2),
   ('成都美食之旅', '成都', '必吃火锅、串串、川菜，推荐去宽窄巷子和锦里。', 'images/20240103_001.jpg,images/20240103_002.jpg,images/20240103_003.jpg', 1);
   
   INSERT INTO strategy_comment (strategy_id, user_id, content) VALUES
   (1, 2, '很棒的攻略，我也想去北京！'),
   (1, 1, '谢谢支持！'),
   (2, 1, '迪士尼确实很好玩！'),
   (3, 2, '成都美食太诱惑了！'),
   (3, 1, '欢迎来成都！');
   
   -- 退出
   quit;
   ```

   或者使用项目提供的数据库初始化脚本:
   ```bash
   mysql -u root -p < database_init.sql
   ```

### 2. 部署应用

#### 2.1 方法一：使用打包好的压缩包

1. **上传压缩包到服务器**:
   ```bash
   scp tuyou_*.tar.gz user@server_ip:/path/to/destination
   ```

2. **解压压缩包**:
   ```bash
   tar -xzf tuyou_*.tar.gz
   cd travel_package
   ```

#### 2.2 方法二：从源码部署

1. **克隆或上传项目代码**:
   ```bash
   git clone <项目地址>
   cd tuyou
   ```

### 3. 配置应用

1. **进入后端目录**:
   ```bash
   cd travel_backend
   ```

2. **创建并配置环境变量文件**:
   ```bash
   cp .env.example .env
   ```

3. **编辑.env文件**:
   ```bash
   vi .env
   ```

   修改以下配置:
   ```
   # 数据库配置
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_USER=travel_user
   DB_PASSWORD=your_database_password  # 替换为实际的数据库密码
   DB_NAME=travel_db

   # Flask配置
   FLASK_SECRET_KEY=your_secret_key_change_in_production
   FLASK_JWT_SECRET_KEY=your_jwt_secret_key_change_in_production
   ```

### 4. 启动服务

#### 4.1 使用启动脚本

1. **返回项目根目录**:
   ```bash
   cd ..
   ```

2. **执行启动脚本**:
   ```bash
   ./start.sh
   ```

   脚本会自动:
   - 检查环境变量文件
   - 安装Python依赖
   - 启动Flask应用

#### 4.2 手动启动

1. **安装依赖**:
   ```bash
   cd travel_backend
   pip3 install -r requirements.txt
   ```

2. **启动应用**:
   ```bash
   python3 app.py
   ```

### 5. 访问应用

服务启动后，可以通过以下地址访问:
- **首页**: `http://服务器IP:5000/`
- **登录页**: `http://服务器IP:5000/login.html`
- **注册页**: `http://服务器IP:5000/register.html`
- **发布攻略**: `http://服务器IP:5000/publish.html`

### 6. 停止服务

- **Ctrl+C**: 在启动服务的终端中按Ctrl+C停止
- **Kill进程**: 
  ```bash
  ps aux | grep python3
  kill <进程ID>
  ```

## 配置说明

### 1. 数据库配置

在`.env`文件中配置数据库连接信息:

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| DB_HOST | 数据库主机地址 | 127.0.0.1 |
| DB_PORT | 数据库端口 | 3306 |
| DB_USER | 数据库用户名 | travel_user |
| DB_PASSWORD | 数据库密码 | your_database_password |
| DB_NAME | 数据库名称 | travel_db |

### 2. Flask配置

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| FLASK_SECRET_KEY | Flask应用密钥 | your-secret-key-change-in-production |
| FLASK_JWT_SECRET_KEY | JWT令牌密钥 | your-jwt-secret-key-change-in-production |

### 3. 文件上传配置

- **上传目录**: `travel_backend/static/images`
- **支持的图片格式**: jpg, jpeg, png
- **最大文件大小**: 16MB

## 测试账号

| 用户名 | 密码 | 角色 |
|--------|------|------|
| admin | 123456 | 管理员 |
| user | 123456 | 普通用户 |

## 功能测试

### 1. 登录测试
1. 访问 `http://服务器IP:5000/login.html`
2. 使用测试账号登录
3. 登录成功后应跳转到首页

### 2. 浏览攻略
1. 在首页查看攻略列表
2. 使用搜索框搜索攻略
3. 点击攻略标题查看详情

### 3. 发布攻略
1. 登录后点击"发布攻略"按钮
2. 填写标题、目的地、内容
3. 选择图片（最多5张）
4. 点击"发布攻略"按钮
5. 发布成功后应跳转到首页并显示新发布的攻略

### 4. 评论测试
1. 在攻略详情页底部填写评论内容
2. 点击"发表评论"按钮
3. 评论应显示在评论列表中

## 常见问题排查

### 1. 数据库连接失败

**症状**:
- 应用启动时显示数据库连接错误
- 无法登录或访问攻略

**解决方案**:
- 检查数据库服务是否运行: `systemctl status mariadb` 或 `systemctl status mysql`
- 检查数据库配置是否正确: 确认.env文件中的数据库配置
- 检查数据库用户权限: 确认用户有访问travel_db的权限
- 检查网络连接: 确保数据库服务器可访问

### 2. 依赖安装失败

**症状**:
- 启动脚本执行时显示依赖安装错误

**解决方案**:
- 检查pip是否安装: `pip3 --version`
- 检查Python版本: `python3 --version` (需要3.6+)
- 检查网络连接: 确保可以访问PyPI
- 手动安装依赖: `pip3 install -r requirements.txt`

### 3. 应用启动失败

**症状**:
- 启动脚本执行后应用无法正常启动
- 访问应用时显示500错误

**解决方案**:
- 检查端口是否被占用: `netstat -tuln | grep 5000`
- 检查应用日志: 查看启动脚本的输出
- 检查环境变量: 确认.env文件配置正确
- 检查文件权限: 确保应用有读写权限

### 4. 图片上传失败

**症状**:
- 发布攻略时图片上传失败
- 攻略详情页图片无法显示

**解决方案**:
- 检查上传目录权限: `chmod 755 -R static/images`
- 检查图片大小: 确保不超过16MB
- 检查图片格式: 只支持jpg、jpeg、png格式

### 5. 跨域错误

**症状**:
- 浏览器控制台显示跨域错误
- API请求失败

**解决方案**:
- 应用已配置CORS，确保.env文件中的配置正确
- 检查浏览器是否阻止了跨域请求

## 性能优化

### 1. 生产环境建议

1. **使用WSGI服务器**:
   ```bash
   pip3 install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **配置反向代理**:
   - 使用Nginx作为反向代理
   - 配置HTTPS

3. **启用缓存**:
   - 使用Redis缓存热点数据
   - 配置浏览器缓存

4. **数据库优化**:
   - 添加索引
   - 优化查询语句
   - 考虑使用数据库连接池

### 2. 安全建议

1. **密码安全**:
   - 生产环境应使用密码哈希（如bcrypt）
   - 定期更新密码

2. **API安全**:
   - 实现请求频率限制
   - 添加CSRF保护

3. **文件上传安全**:
   - 验证文件类型和大小
   - 防止路径遍历攻击

4. **环境变量**:
   - 不要将.env文件提交到版本控制系统
   - 定期更新密钥

## 维护指南

### 1. 日志管理

- **应用日志**: 查看Flask应用的控制台输出
- **数据库日志**: 查看MySQL/MariaDB的错误日志

### 2. 备份与恢复

- **数据库备份**:
  ```bash
  mysqldump -u root -p travel_db > backup_$(date +%Y%m%d).sql
  ```

- **数据库恢复**:
  ```bash
  mysql -u root -p travel_db < backup_*.sql
  ```

- **文件备份**:
  ```bash
  tar -czf backup_$(date +%Y%m%d).tar.gz travel_backend/static/images
  ```

### 3. 更新应用

1. **停止服务**
2. **备份数据**
3. **上传新的代码或压缩包**
4. **更新配置**
5. **启动服务**
6. **测试功能**

## 技术支持

如果遇到问题，请检查以下资源:

1. **项目文档**: README.md 和本部署文档
2. **错误日志**: 应用和数据库的错误日志
3. **常见问题**: 本文档的"常见问题排查"部分

## 版本信息

- **应用版本**: 1.0.0
- **最后更新**: $(date +%Y-%m-%d)

---

**部署完成后，您的途游攻略分享平台应该已经可以正常使用了！**
