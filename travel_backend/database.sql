-- 创建数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 使用数据库
USE travel_db;

-- 用户表
CREATE TABLE IF NOT EXISTS sys_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
    password VARCHAR(50) NOT NULL COMMENT '密码（明文存储）',
    phone VARCHAR(20) NOT NULL COMMENT '手机号',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    del_flag TINYINT DEFAULT 0 COMMENT '逻辑删除（0-未删/1-已删）'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

-- 攻略表
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

-- 评论表
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
-- 用户数据
INSERT INTO sys_user (username, password, phone) VALUES
('admin', '123456', '13800138001'),
('user', '123456', '13800138002');

-- 攻略数据
INSERT INTO travel_strategy (title, destination, content, images, user_id) VALUES
('北京三日游攻略', '北京', '第一天游览故宫，第二天爬长城，第三天逛胡同。', 'images/20240101_001.jpg,images/20240101_002.jpg', 1),
('上海迪士尼乐园游玩指南', '上海', '建议早上8点到达，先玩热门项目，晚上看烟花表演。', 'images/20240102_001.jpg', 2),
('成都美食之旅', '成都', '必吃火锅、串串、川菜，推荐去宽窄巷子和锦里。', 'images/20240103_001.jpg,images/20240103_002.jpg,images/20240103_003.jpg', 1);

-- 评论数据
INSERT INTO strategy_comment (strategy_id, user_id, content) VALUES
(1, 2, '很棒的攻略，我也想去北京！'),
(1, 1, '谢谢支持！'),
(2, 1, '迪士尼确实很好玩！'),
(3, 2, '成都美食太诱惑了！'),
(3, 1, '欢迎来成都！');