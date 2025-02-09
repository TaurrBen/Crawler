# Crawler

## B站

### 参数

```
index_url = "https://www.bilibili.com"
user_agent = 随机得到一个
playwright_proxy_format = None
httpx_proxy_format = None
```

### 流程

#### 1.启动

- 配置代理池

- 获取浏览器上下文
  - 保存登录信息launch_persistent_context
  - 不保存launch
- 创建客户端
  - BilibiliClient
  - Pong
