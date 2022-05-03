# 宁波工程学院每日健康填报
1、首先在text处将姓名、学院、专业、寝室楼、寝室号进行修改，已经添加了“！！！”以防找不到

![屏幕截图 2021-12-18 172550](https://user-images.githubusercontent.com/83929038/146636302-d60097e2-0f97-4238-91aa-eb670ada744e.png)

2、安装fiddler，选择tools-option-HTTPS，按照以下的进行设置

![屏幕截图 2021-12-18 170745](https://user-images.githubusercontent.com/83929038/146635843-59715d80-e369-47c8-af8b-747da6562708.png)

3、电脑端打开我的填报，同时查看fiddler，一次查看左边的抓包情况，选择host为form.nbut.edu.cn，查看右边Authentication，复制值

![屏幕截图 2021-12-18 171301](https://user-images.githubusercontent.com/83929038/146636136-4073163e-1fbc-4db4-88d1-8fbc01f3b6f5.png)

4、返回python程序，将Authentication值！！！改成复制值

![屏幕截图 2021-12-18 172424](https://user-images.githubusercontent.com/83929038/146636259-eff33cd6-50b9-446f-b283-ce3ae2bc1b80.png)

Enjoy it
![屏幕截图 2021-12-18 173137](https://user-images.githubusercontent.com/83929038/146636435-96879a79-65b3-4458-a875-dc51b3c70c54.png)
