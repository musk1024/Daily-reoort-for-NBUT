import os

least = "2022-12-01" #最近一次核酸检测时间
Authentication = os.environ.get("AUTHENTICATION", "") # 必填 认证信息
TEXT = os.environ.get("TEXT", "") # 必填 填报的内容
SERVERPUSHKEY = os.environ.get("SERVERPUSHKEY", "")  # Server酱推送
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")  # Telegram推送服务Token
TG_USER_ID = os.environ.get("TG_USER_ID", "")  # Telegram推送服务UserId
BARK = os.environ.get("BARK", "")  # bark消息推送服务,自行搜索; secrets可填;形如jfjqxDx3xxxxxxxxSaK的字符串
PUSHPLUS = os.environ.get("PUSHPLUS", "")  # PUSHPLUS消息推送Token
PUSHDEERKEY = os.environ.get("PUSHDEERKEY", "") # PUSHDEER消息推送KEY
ACCESSTOKEN = os.environ.get("ACCESSTOKEN", "")  # 企业微信access_token     获取地址:https://work.weixin.qq.com/api/doc/90000/90135/91039
CORPID = os.environ.get("CORPID", "")  # 企业ID  （如果已经填写ACCESSTOKEN  则无需填写这个）
CORPSECRET = os.environ.get("CORPSECRET", "")  # 应用的凭证密钥  （如果已经填写ACCESSTOKEN  则无需填写这个）
TOUSER = os.environ.get("TOUSER", "@all")  # touser指定接收消息的成员  默认为全部
AGENTID = os.environ.get("AGENTID", "")  # agentid企业应用的id
THUMB_MEDIA_ID = os.environ.get("THUMB_MEDIA_ID", "") #企业微信素材库图片id
AUTHOR = os.environ.get("AUTHOR", "") #企业微信文章作者