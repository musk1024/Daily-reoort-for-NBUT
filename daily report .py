import json
import requests
import time

headers={'Host': 'form.nbut.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '871',
        'Access-Control-Allow-Origin': '*',
        'Accept': 'application/json, text/plain, */*',
        'Access-Control-Allow-Credentials': 'true',
        'Authentication': '！！！！！！！！！！！！！！！！！',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6304051b)',
        'Origin': 'https://form.nbut.edu.cn',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'JSESSIONID=BC15ED74EFE4EA3C2CA702F3C8350A53',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://form.nbut.edu.cn/&state=STATE',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}


text = repr({"formWid":"33cbf04e092b4d17aef3946f245d5cb4","userId":"AM@stamp522","dataMap":{"wid":"","INPUT_KWYMPWZO":"!!!Name!!!","INPUT_KWYMPWZP":"!!!学院!!!","INPUT_KWZRFKE3":"！！！专业！！！","INPUT_KWZ02SZK":"！！！寝室楼！！！","INPUT_KWZ02SZL":"！！！寝室号！！！","RADIO_KWYMPX0A":"是","RADIO_KX369F35":"风华校区","RADIO_KX1T8ENX":"否","RADIO_KX1T8ENY":"否","RADIO_KWYMPX04":"绿","RADIO_KWYMPX05":"绿","RADIO_KWYMPWZT":"是","RADIO_KWYMPWZU":"两针","RADIO_KWYMPWZV":"是","DATEPICKER_KWYW0UX4":"2021-12-12","RADIO_KWYMPWZX":"阴性","LOCATION_KX7NAIQR":"宁波市镇海区","INPUT_KX14LP0P":"宁波工程学院","RADIO_KWZ02SZM":"否","RADIO_KWZ02SZN":"","SELECT_KWZ02SZO":"","SELECT_KWZ02SZP":"","SELECT_KWZ02SZQ":"","INPUT_KX7NAIQS":"","INPUT_KX7NAIQT":"","INPUT_KWYMPWZR":"","RADIO_KWYMPX03":""},"commitDate":"date","commitMonth":"month","auditConfigWid":""})
data = eval(text.replace('stamp',str(int(time.time()))).replace('date',time.strftime("%Y-%m-%d", time.localtime())).replace('month',time.strftime("%Y-%m", time.localtime())))
datas=json.dumps(data)
r=requests.post("https://form.nbut.edu.cn/dfi/formData/saveFormSubmitData", data=datas, headers=headers)
print(r.text)
#print(json.loads(datas))
print(datas)
