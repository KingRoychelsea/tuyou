# 途游攻略分享平台部署说明

## 环境要求

### 后端环境
- Python 3.6+
- Flask 2.0+
- Flask-CORS
- Flask-JWT-Extended
- PyMySQL
- python-dotenv

### 数据库
- MariaDB 10.3+
- 数据库连接信息：
  - 主机：127.0.0.1
  - 端口：3306
  - 用户名：root
  - 密码：612345
  - 数据库名：travel_db

### 前端环境
- 现代浏览器（支持HTML5、CSS3、JavaScript ES6+）

## 部署步骤

### 1. 数据库初始化

1. 确保MariaDB服务已启动
2. 执行数据库初始化脚本：

```bash
mysql -h 127.0.0.1 -u root -p612345 < travel_backend/database.sql
```

### 2. 启动后端服务

1. 进入后端项目目录：

```bash
cd travel_backend
```

2. 安装依赖（如果未安装）：

```bash
pip3 install flask flask-cors flask-jwt-extended pymysql python-dotenv
```

3. 启动Flask服务：

```bash
python3 app.py
```

服务将运行在 `http://localhost:5000/`

### 3. 访问前端页面

直接在浏览器中打开前端HTML文件：

- 首页：`travel_frontend/index.html`
- 登录页：`travel_frontend/login.html`
- 注册页：`travel_frontend/register.html`
- 发布攻略页：`travel_frontend/publish.html`
- 编辑攻略页：`travel_frontend/edit.html`
- 攻略详情页：`travel_frontend/detail.html?id=1`（需替换为实际攻略ID）

## 测试账号

### 已初始化的测试账号
- 账号1：
  - 用户名：admin
  - 密码：123456
  - 手机号：13800138001

- 账号2：
  - 用户名：user
  - 密码：123456
  - 手机号：13800138002

## 核心功能测试

### 1. 登录注册功能
- 打开 `login.html` 页面，使用测试账号登录
- 打开 `register.html` 页面，注册新用户

### 2. 首页展示与搜索功能
- 打开 `index.html` 页面，查看攻略列表
- 在搜索框中输入关键词，测试搜索功能

### 3. 攻略发布与编辑功能
- 登录后，点击导航栏的"发布攻略"按钮
- 填写攻略信息并上传图片，测试发布功能
- 在攻略详情页，点击"编辑攻略"按钮，测试编辑功能

### 4. 评论功能
- 登录后，在攻略详情页下方的评论区发布评论
- 测试删除自己发布的评论

## 项目结构说明

### 后端结构
```
travel_backend/
├── app.py                # Flask主应用文件
├── routes.py             # 路由配置文件
├── database.sql          # 数据库初始化脚本
├── config/               # 核心配置类
├── controller/           # 控制层
├── service/              # 业务层
├── mapper/               # 数据访问层
├── entity/               # 实体类
├── dto/                  # 数据传输对象
├── utils/                # 工具类
├── exception/            # 全局异常处理器
└── static/images/        # 图片存储目录
```

### 前端结构
```
travel_frontend/
├── index.html            # 首页
├── login.html            # 登录页
├── register.html         # 注册页
├── publish.html          # 发布攻略页
├── edit.html             # 编辑攻略页
└── detail.html           # 攻略详情页
```

## API接口说明

### 用户相关接口
- `POST /api/user/register` - 用户注册
- `POST /api/user/login` - 用户登录
- `GET /api/user/info` - 获取当前用户信息（需JWT认证）

### 攻略相关接口
- `GET /api/strategy/list` - 获取攻略列表（支持关键词搜索）
- `GET /api/strategy/{id}` - 获取攻略详情
- `POST /api/strategy` - 创建攻略（需JWT认证）
- `PUT /api/strategy/{id}` - 更新攻略（需JWT认证）
- `DELETE /api/strategy/{id}` - 删除攻略（需JWT认证）

### 评论相关接口
- `GET /api/comment/list/{strategy_id}` - 获取攻略评论列表
- `POST /api/comment` - 发布评论（需JWT认证）
- `DELETE /api/comment/{id}` - 删除评论（需JWT认证）

## 注意事项

1. **图片存储**：攻略图片存储在 `travel_backend/static/images/` 目录下
2. **JWT认证**：登录成功后，前端会将token存储在localStorage中，后续请求会在请求头中携带token
3. **权限控制**：只有攻略发布者可以编辑/删除自己的攻略，只有评论发布者可以删除自己的评论
4. **安全提示**：本项目为教学示例，密码采用明文存储，实际生产环境中应使用密码哈希
5. **跨域处理**：后端已配置CORS，支持前端跨域请求

## 教学重点

1. **后端核心知识点**：
   - Flask框架基础使用
   - JWT无状态认证
   - 数据库CRUD操作
   - 文件上传处理
   - 分层架构设计

2. **前端核心知识点**：
   - HTML5+CSS3基础
   - JavaScript异步编程（fetch API）
   - 前端本地存储（localStorage）
   - 动态DOM操作
   - 表单验证

3. **全栈整合**：
   - RESTful API设计
   - 前后端数据交互
   - 认证机制实现
   - 完整业务流程

---

**项目状态**：已完成核心功能开发，可直接用于教学演示和学习参考。