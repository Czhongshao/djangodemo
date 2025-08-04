# 🔧 Steam 数据可视化分析后端管理 · DjangoDemo

> 一个基于 **Django + MySQL** 的 Steam 游戏数据分析平台后端管理系统，提供高效的数据处理与 API 支持。

![License](https://img.shields.io/badge/license-MIT-green)
![Django](https://img.shields.io/badge/django-4.x-green)
![MySQL](https://img.shields.io/badge/mysql-8.x-blue)

---

## 📦 项目地址

GitHub: [https://github.com/Czhongshao/djangodemo.git](https://github.com/Czhongshao/djangodemo.git)

---

## 🧠 项目简介

本项目是 Steam 游戏数据可视化分析系统的后端服务，提供数据读取、处理、分析与 RESTful API 接口支持。支持数据模型的自动管理与接口权限控制，便于前后端分离开发。

---

## ⚙️ 技术栈

| 技术     | 用途           |
|----------|----------------|
| Django   | Web 后端框架   |
| Django REST Framework | API 开发 |
| MySQL    | 数据存储       |
| pymysql  | 数据库驱动     |
| corsheaders | 跨域支持    |

---

## 🔍 核心功能

- ✅ 支持 Steam 游戏数据的模型管理与数据库存储
- ✅ 提供 RESTful API 接口供前端调用
- ✅ 支持跨域访问、分页、过滤、排序
- ✅ 自定义管理后台用于数据维护

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/Czhongshao/djangodemo.git
cd djangodemo
```

### 2. 安装依赖

建议使用虚拟环境：

```bash
pip install -r requirements.txt
```

### 3. 配置数据库

在 `settings.py` 中配置你的 MySQL 数据库连接：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'steamdb',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. 初始化数据库

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 创建超级用户

```bash
python manage.py createsuperuser
```

### 6. 启动项目

```bash
python manage.py runserver
```

访问地址：[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🗂️ 目录结构

```bash
djangodemo/
├── steamapp/             # 核心应用
│   ├── models.py         # 数据模型
│   ├── views.py          # 视图处理
│   ├── serializers.py    # 序列化器
│   ├── urls.py           # 路由配置
├── djangodemo/           # 项目配置
│   └── settings.py       # 配置文件
├── requirements.txt      # 依赖文件
├── manage.py             # 管理脚本
└── README.md
```

---

## 📌 接口说明示例

- `GET /api/games/`：获取所有游戏信息
- `GET /api/games/?genre=Action`：按类型筛选
- `POST /api/games/`：添加新游戏（需登录）

更多接口文档见 Swagger 或 DRF 自动文档页面（若配置）。

---

## 💡 TODO

- [ ] 接入第三方 Steam 数据源自动更新
- [ ] 提供用户管理与鉴权
- [ ] 完善 API 文档页面
- [ ] 增加 Celery 异步处理能力

---

## 🤝 贡献指南

欢迎提交 PR 或 Issue！

---

## 📄 License

本项目采用 [MIT License](./LICENSE)。

---

## 📬 联系方式

- GitHub: [@Czhongshao](https://github.com/Czhongshao)
- Email: [3067982179@qq.com](mailto:3067982179@qq.com)
