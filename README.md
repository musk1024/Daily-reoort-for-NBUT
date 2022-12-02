# 宁波工程学院每日健康填报

> 2022-12-3 支持Github Action自动运行，极大程度降低了脚本的运行门槛，同时支持多种推送协议

1. 修改主体正文部分

```python
{"formWid":"33cbf04e092b4d17aef3946f245d5cb4","userId":"AM@stamp522","dataMap":{"wid":"","INPUT_KWYMPWZO":"!!NAME!!","INPUT_KWYMPWZP":"!!学院!!","INPUT_KWZRFKE3":"!!CLASS!!","INPUT_KWZ02SZK":"","INPUT_KWZ02SZL":"","RADIO_KWYMPX0A":"是","RADIO_KX369F35":"杭州湾校区","RADIO_KX1T8ENX":"否","RADIO_KX1T8ENY":"否","RADIO_KWYMPX04":"绿","RADIO_KWYMPWZT":"是","RADIO_KWYMPWZU":"两针","RADIO_KWYMPWZV":"否","DATEPICKER_KWYW0UX4":"last","RADIO_KWYMPWZX":"阴性","LOCATION_KX7NAIQR":"浙江省宁波市慈溪市","INPUT_KX14LP0P":"杭州湾汽车学院","RADIO_L0IZ3481":"无","INPUT_KX7NAIQS":"","INPUT_KX7NAIQT":"","INPUT_KWYMPWZR":"","RADIO_KWYMPX03":""},"commitDate":"date","commitMonth":"month","auditConfigWid":""}
```

对以上的正文进行修改

2. 安装fiddler，选择tools-option-HTTPS，按照以下的进行设置

![屏幕截图 2021-12-18 170745](https://user-images.githubusercontent.com/83929038/146635843-59715d80-e369-47c8-af8b-747da6562708.png)

3. 电脑端打开我的填报，同时查看fiddler，一次查看左边的抓包情况，选择host为form.nbut.edu.cn，查看右边Authentication，复制值

![屏幕截图 2021-12-18 171301](https://user-images.githubusercontent.com/83929038/146636136-4073163e-1fbc-4db4-88d1-8fbc01f3b6f5.png)

4. fork我的项目，在Setting中的Secret-Action中添加环境变量

   1. TEXT 填写修改的正文

   1. AUTHENTICATION 填写抓取的Authentication

   ![image-20221203010411048](https://www.apple1024.top:1888/images/2022/12/02/202212030104155.png)

5. **进阶：支持将结果推送至 APP** 

   现在支持一下几个软件以及对应的环境变量：

   - SERVERPUSHKEY Server酱推送
   - TG_BOT_TOKEN && TG_USER_ID Telegram推送服务
   - BARK bark消息推送服务
   - PUSHPLUS PUSHPLUS消息推送
   - PUSHDEERKEY PUSHDEER消息推送KEY
   - ACCESSTOKEN 企业微信access_token 或 CORPID && CORPSECRET && TOUSER && AGENTID

   ![image-20221203010610387](https://www.apple1024.top:1888/images/2022/12/02/202212030106524.png)

   详情见 *GlobalVariable.py* 有所有适用的环境变量

