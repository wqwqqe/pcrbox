# 从零开始构建pcrbox

项目连接：

第一版先将信息以文件形式存储，后续接入数据库

## 数据获取

利用python爬虫从https://pcredivewiki.tw/获取数据

### 装备信息

利用selenium+python获取装备的图片，名字，保存到本地

见get_equipment.py

### 角色信息获取

见get_character.py