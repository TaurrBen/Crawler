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
  - Pong测试

#### 2.按照关键词搜索

- search_video_by_keyword
  - 筛选时间提高爬虫
- 并发获取视频信息
- 聚集信息并处理
  - 解析并存储视频信息
  - 解析并存储up主信息
  - 获取视频
- 并发获取评论

#### 3.获取特定视频

#### 4.获取创造者主页

### 重要uri

```
/x/web-interface/nav:个人登录信息
/x/web-interface/wbi/search/type:关键词搜素获取信息
/x/web-interface/view/detail:获取视频信息
/x/player/wbi/playurl:获取视频
```

## 小红书

### 参数

### 流程

#### 1.
