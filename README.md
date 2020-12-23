# Dionaea
### web_dionaea

更新了Dockerfile

更新企业微信推送, 把tail.py放在/opt目录下

其中tail.py中的key需要配置 企业ID.Secret.AgentId 不了解的建议百度

原版请关注 [atiger77/Dionaea](https://github.com/atiger77/Dionaea)


#### 部署方式
1. 自定义蜜罐名称；修改/web_dionaea/templates/index.html中的对应title。
2. 制作蜜罐镜像；#docker build -t "web_dionaea" .
3. 创建蜜罐容器；#docker run -d -p 80:80 -v /opt:/tmp --restart=always web_dionaea

