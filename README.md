# ALL PYTHON STUFF
***
使用python 2.7
***

## [zhouzhouliArray.py](zhouzhouliArray.py)
腾讯游戏，天涯明月刀的领奖程序，
### 需要安装splinter
pip install splinter -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
### 下载chrome驱动
http://chromedriver.storage.googleapis.com/index.html?path=2.20/
### 改用户名密码 sleep时间
然后修改下代码里的循环条件。增加自己的用户名密码，网络慢建议增加sleep时间
### 最后运行程序
多个用户会一个接一个的去领奖，适合号多的人。
***
## [wechatAddGroup.py](wechatAddGroup.py)
腾讯微信自定义加组的功能。
因为有需要不定期拉不同的人进新组的需求，所以搞了这套。
### 第一步需要把好友都添加备注
因为昵称里带各种符号，基本没法用来判断
### 第二步需要建立list.txt文件
在py文件相同目录下用gbk编码建立list.txt文件，每行一个人名（备注）
### 第三步执行py程序。
所有列表中的好友都会被拉进群。进群后会说一句话“欢迎进群”
### 感谢
感谢各种做轮子的大神
[Urinx/WeixinBot](https://github.com/Urinx/WeixinBot/)
[0x5e/wechat-deleted-friends](https://github.com/0x5e/wechat-deleted-friends/)
