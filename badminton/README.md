# 用于中大体育馆预约

## 环境
`google chrome`, `selenium`, `ddddocr`

## 使用方法
修改`main.py`文件中以下代码
```
username.send_keys('username') #用户名
pwd.send_keys('password') # 密码
rangle = (1155, 850, 1333, 907) #验证码在网页中的位置
```

使用`crontab`定时启动程序
```
00 6 * * 2,6 python path/badminton/main.py >> path/badminton/log.txt 2>&1
```
每周二、周六早上六点执行程序预约体育馆
