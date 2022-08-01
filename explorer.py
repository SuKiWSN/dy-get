import requests


class request:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Cookie': 'home_can_add_dy_2_desktop=%220%22; ttwid=1%7CmE8mr7e9Bdc_o3iZIralxpWvnv04p0JP0p4DO54jnSE%7C1657789373%7Ccee2f805dda444b69836ca18413f5b6b420fd80319e1ba8feeb722bc98591776; tt_scid=UPNBfTvCA3YEili2.B0K3boBhz7rTdn-a5Nnl8QLiZV.uTHOGbBrbLbRc1DC4fph46d4; msToken=9mUht47p1aSAhetCa5JV9101rGTO16tCcPyGeoKviAY3rDMSZTiWDX05ufuTU4HKhTPqZthFx7bWkvuEXfg7yAo_Y_mzVDaDErYn1cOCrpuR0YyCOJvb9A==; download_guide=%223%2F20220715%22; msToken=OVNSjBeIVoN2rSXUqL2JlsTm5BrF1ECdMh13_QIZtOqg3H8NXPXDRsf5BQ9UCizspGeUgIEuW-hpF7lm19q-Oq1CGmKwKIZSm5HzNTKwJaMXrUBQu-j17w==; __ac_nonce=062d0d88c0023c2b68e78; __ac_signature=_02B4Z6wo00f01f7ieRgAAIDAQa3Wwg06PDH-wn2AAB1qpStbZcAtvUn3F6TFnTC4wYuiUDDThWJ2xyKbAfeu8O7YXYQqd8ZltV9TIr.GhcwJ4ODrHTMOBd2J6gIx6Qs0wdKBOAoIh3falFeYeb; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAhuSvi8L6t_esxlz778m8SlTnAMB2BSoyIqvzfQxhzyMetfyGe3rczmumcNk25S4w%2F1657900800000%2F0%2F1657842653934%2F0%22; strategyABtestKey=1657842653.495; douyin.com=; odin_tt=03772b5f97ccffb6094b3d7b3757c338e1d28fe016d4186fc143383f446c3b5dcd2e281cc361209bbcd2b4964b2102c60c612b9ddad19ca6808d6d87f132c1ef; sessionid=a89214612abe7dcecfa8f9c2afad8252; sessionid_ss=a89214612abe7dcecfa8f9c2afad8252; sid_guard=a89214612abe7dcecfa8f9c2afad8252%7C1657790675%7C5184000%7CMon%2C+12-Sep-2022+09%3A24%3A35+GMT; sid_tt=a89214612abe7dcecfa8f9c2afad8252; sid_ucp_v1=1.0.0-KDEwYzhiM2ZiMTZmNTk2NGM5MzkzYWM4YTljOTI0ZmFkYTIzYjM5ZjAKHwiz0oDC4vSWBxDTwb-WBhjvMSAMMPeJiusFOAZA9AcaAmxmIiBhODkyMTQ2MTJhYmU3ZGNlY2ZhOGY5YzJhZmFkODI1Mg; ssid_ucp_v1=1.0.0-KDEwYzhiM2ZiMTZmNTk2NGM5MzkzYWM4YTljOTI0ZmFkYTIzYjM5ZjAKHwiz0oDC4vSWBxDTwb-WBhjvMSAMMPeJiusFOAZA9AcaAmxmIiBhODkyMTQ2MTJhYmU3ZGNlY2ZhOGY5YzJhZmFkODI1Mg; uid_tt=92828592d959896b9534d0921ff1d847; uid_tt_ss=92828592d959896b9534d0921ff1d847; n_mh=fG0FGo-Hca8NjusEARb83152h-IlDFj6XkluDwjPU3g; sid_ucp_sso_v1=1.0.0-KDk1YWE3NzZhMmJmYTI1YTc2MmI1NjlkZWQ5ZjZkYjk2OTZmNGJiODEKHwiz0oDC4vSWBxDSwb-WBhjvMSAMMPeJiusFOAZA9AcaAmxxIiBhODkyMTQ2MTJhYmU3ZGNlY2ZhOGY5YzJhZmFkODI1Mg; ssid_ucp_sso_v1=1.0.0-KDk1YWE3NzZhMmJmYTI1YTc2MmI1NjlkZWQ5ZjZkYjk2OTZmNGJiODEKHwiz0oDC4vSWBxDSwb-WBhjvMSAMMPeJiusFOAZA9AcaAmxxIiBhODkyMTQ2MTJhYmU3ZGNlY2ZhOGY5YzJhZmFkODI1Mg; sso_uid_tt=92828592d959896b9534d0921ff1d847; sso_uid_tt_ss=92828592d959896b9534d0921ff1d847; toutiao_sso_user=a89214612abe7dcecfa8f9c2afad8252; toutiao_sso_user_ss=a89214612abe7dcecfa8f9c2afad8252; pwa_guide_count=%223%22; IS_HIDE_THEME_CHANGE=%221%22; THEME_STAY_TIME=%22299605%22; ttcid=5ff792cf75b04f96a4f978140255fe8418; AB_LOGIN_GUIDE_TIMESTAMP=%221657789375246%22; passport_csrf_token=cc15af798ac7d3f9d96cbb5cc63b4291; passport_csrf_token_default=cc15af798ac7d3f9d96cbb5cc63b4291; s_v_web_id=verify_l5kszp8t_wxJALWDP_Cfm5_4CMH_BhlK_6u5gqERXH5go',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
            'Referer': 'https://www.douyin.com/video/6994999052655938831',
            'Cache-Control': 'no-cache',
            'Host': 'www.douyin.com',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Accept': 'application/json, text/plain, */*',
        }
    def get(self):
        res = requests.get(self.url, headers=self.headers)
        return res