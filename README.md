# 途游攻略分享平台

## 项目介绍
途游攻略分享平台是一个基于Python、Flask、Vue.js和MariaDB的全栈旅游攻略分享系统，用户可以注册登录、浏览攻略、发布自己的旅游攻略并进行评论互动。

## 技术栈

### 后端
- Python 3.6+
- Flask 2.7.x
- JWT (JSON Web Token) 认证
- MariaDB/MySQL 数据库
- RESTful API 设计

### 前端
- HTML5/CSS3
- JavaScript (ES6+)
- Fetch API
- localStorage 存储
- 原生JavaScript实现的前端逻辑

### 数据库
- MariaDB/MySQL
- 三表结构设计（用户表、攻略表、评论表）

## 核心功能

1. **用户系统**
   - 注册/登录功能
   - JWT令牌认证
   - 用户信息管理

2. **攻略管理**
   - 攻略发布（支持多图片上传）
   - 攻略列表展示
   - 攻略详情查看
   - 攻略搜索功能

3. **评论系统**
   - 攻略评论功能
   - 评论列表展示

4. **图片上传**
   - 本地存储图片
   - 图片路径管理

## 项目结构

```
/project/tuyou/
├── travel_backend/          # 后端代码
│   ├── app.py               # Flask应用主文件
│   ├── routes.py            # API路由
│   ├── utils/               # 工具函数
│   │   └── db.py            # 数据库连接
│   ├── database.sql         # 数据库结构
│   └── uploads/             # 图片上传目录
├── travel_frontend/         # 前端代码
│   ├── index.html           # 首页
│   ├── login.html           # 登录页
│   ├── register.html        # 注册页
│   ├── detail.html          # 攻略详情页
│   ├── publish.html         # 发布攻略页
│   └── uploads/             # 前端图片目录
├── database_init.sql        # 数据库初始化脚本
└── README.md                # 项目文档
```

## 环境要求

- Python 3.6+
- MariaDB/MySQL 5.7+
- 浏览器（Chrome、Firefox、Edge等）

## 安装与部署

### 1. 克隆项目

```bash
git clone <项目地址>
cd /project/tuyou
```

### 2. 安装后端依赖

```bash
cd travel_backend
pip install flask flask-cors pyjwt pymysql
```

### 3. 配置数据库

#### 3.1 创建数据库用户

```sql
CREATE USER 'travel_user'@'localhost' IDENTIFIED BY '*******';
GRANT ALL PRIVILEGES ON travel_db.* TO 'travel_user'@'localhost';
FLUSH PRIVILEGES;
```

#### 3.2 初始化数据库

```bash
# 登录MySQL/MariaDB
mysql -u root -p

# 执行初始化脚本
source /project/tuyou/database_init.sql;

# 退出
quit;
```

### 4. 配置后端数据库连接

编辑 `travel_backend/utils/db.py` 文件，确保数据库连接配置正确：

```python
# 数据库连接配置
config = {
    'host': 'localhost',
    'user': 'travel_user',
    'password': '*******',
    'database': 'travel_db',
    'port': 3306,
    'charset': 'utf8mb4'
}
```

### 5. 启动服务

#### 5.1 启动后端服务

```bash
cd /project/tuyou/travel_backend
python app.py
```

后端服务将运行在 `http://localhost:5000`

#### 5.2 启动前端服务

```bash
cd /project/tuyou/travel_frontend
python3 -m http.server 8000
```

前端服务将运行在 `http://localhost:8000`

## 数据库结构

### 1. 用户表 (`sys_user`)

| 字段名 | 数据类型 | 约束 | 描述 |
|--------|----------|------|------|
| id | INT | AUTO_INCREMENT PRIMARY KEY | 用户ID |
| username | VARCHAR(50) | NOT NULL UNIQUE | 用户名 |
| password | VARCHAR(50) | NOT NULL | 密码（明文存储） |
| phone | VARCHAR(20) | NOT NULL | 手机号 |
| create_time | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| update_time | DATETIME | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 更新时间 |
| del_flag | TINYINT | DEFAULT 0 | 逻辑删除（0-未删/1-已删） |

### 2. 攻略表 (`travel_strategy`)

| 字段名 | 数据类型 | 约束 | 描述 |
|--------|----------|------|------|
| id | INT | AUTO_INCREMENT PRIMARY KEY | 攻略ID |
| title | VARCHAR(100) | NOT NULL | 攻略标题 |
| destination | VARCHAR(50) | NOT NULL | 目的地 |
| content | TEXT | NOT NULL | 攻略内容 |
| images | VARCHAR(1000) | | 图片路径（多个图片用逗号分隔） |
| user_id | INT | NOT NULL, FOREIGN KEY | 发布用户ID |
| create_time | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| update_time | DATETIME | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 更新时间 |
| del_flag | TINYINT | DEFAULT 0 | 逻辑删除（0-未删/1-已删） |

### 3. 评论表 (`strategy_comment`)

| 字段名 | 数据类型 | 约束 | 描述 |
|--------|----------|------|------|
| id | INT | AUTO_INCREMENT PRIMARY KEY | 评论ID |
| strategy_id | INT | NOT NULL, FOREIGN KEY | 攻略ID |
| user_id | INT | NOT NULL, FOREIGN KEY | 评论用户ID |
| content | VARCHAR(500) | NOT NULL | 评论内容 |
| create_time | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| update_time | DATETIME | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 更新时间 |
| del_flag | TINYINT | DEFAULT 0 | 逻辑删除（0-未删/1-已删） |

## API 接口

### 用户相关
- `POST /api/auth/register` - 用户注册
- `POST /api/auth/login` - 用户登录

### 攻略相关
- `GET /api/strategy/list` - 获取攻略列表（支持关键词搜索）
- `GET /api/strategy/detail` - 获取攻略详情
- `POST /api/strategy` - 发布攻略

### 评论相关
- `GET /api/comment/list` - 获取评论列表
- `POST /api/comment` - 发布评论

## 测试账号

| 用户名 | 密码 | 角色 |
|--------|------|------|
| admin | 123456 | 管理员 |
| user | 123456 | 普通用户 |

## 使用说明

1. **访问系统**
   - 打开浏览器，访问 `http://localhost:8000`
   - 点击登录按钮，使用测试账号登录

2. **浏览攻略**
   - 登录后，首页会显示攻略列表
   - 可以使用搜索框搜索攻略
   - 点击攻略标题查看详情

3. **发布攻略**
   - 点击导航栏的"发布攻略"按钮
   - 填写标题、目的地、内容
   - 选择图片（最多5张）
   - 点击"发布攻略"按钮

4. **评论攻略**
   - 在攻略详情页底部填写评论内容
   - 点击"发表评论"按钮

## 注意事项

1. **密码安全**
   - 本项目使用明文存储密码，仅用于学习目的
   - 生产环境应使用密码哈希（如bcrypt）

2. **图片存储**
   - 图片存储在本地服务器
   - 生产环境应考虑使用CDN或对象存储服务

3. **安全性**
   - 本项目仅用于学习目的
   - 生产环境应添加更多安全措施，如HTTPS、CORS配置、输入验证等

4. **性能优化**
   - 数据库连接使用了简单的连接池
   - 生产环境应考虑使用更完善的连接池和缓存机制

## 故障排除

### 常见问题

1. **数据库连接失败**
   - 检查数据库服务是否运行
   - 检查数据库连接配置是否正确
   - 检查数据库用户权限是否正确

2. **图片上传失败**
   - 检查 `uploads` 目录权限
   - 检查图片大小是否超过限制

3. **API请求失败**
   - 检查后端服务是否运行
   - 检查前端请求URL是否正确
   - 检查JWT令牌是否有效

### 日志查看

- 后端日志：查看Flask控制台输出
- 前端日志：使用浏览器开发者工具查看控制台

## 许可证

本项目仅用于学习目的，不用于商业用途。

## 联系方式

如有问题，请联系项目维护者。
