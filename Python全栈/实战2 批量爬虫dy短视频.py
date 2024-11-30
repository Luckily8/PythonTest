# 爬虫抓取视频资源
# 1. 通过requests获取网页源代码
# 2. 通过正则表达式匹配视频链接
# 3. 下载视频
# 4. 保存视频
import requests as r
import re

# 清理文件名函数
def clean_filename(filename):
    # 去除无效字符
    return re.sub(r'[\/:*?"<>|]', '', filename)

url = "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAArEAnx0OwOfG-EK8NQggTn5LATAIWWXiAAChtiomD5vI&max_cursor=1724662447000&locate_item_id=7414412100379905292&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=128.0.0.0&browser_online=true&engine_name=Blink&engine_version=128.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=150&webid=7411122591035196969&msToken=CdbxV9GUFxUAn83AMtUYMDulPyhh8ueHAS7PHiK5jUZxbXTV15rNp8oq7_XbJuTED--QRilqO9V2X9Eb5eamqAyZZCE2NhjO18NVNmbMxutfQhO4UE_CoP8vm8capT-ATiBGHwefGGx-YlU8xV2jTiV4_QAzvLzATBOz_4RxhoFdHtw0u8kfcjs%3D&a_bogus=YJ4RgetJDqWccpMbuOJxtG1U-ZjlrBuykMT%2FRwrPtNzcYhFO8mPgoaCzjxoAsKIJSbp0wq1HCEMMYxxcMGXwZ9nkzmkDSFkjcT25I68o8qwVbMiDgqmTC0gzLwBKUOiNe%2F9Si1mRUs0x2ndRVNVEAQZGH5z9QRjgbqBVp2GyJDSU3TLTIx2lecEWvwj%3D&verifyFp=verify_lzf90ovv_6NcE3oRP_5DNC_4k61_8raI_zBwk7QhGUigZ&fp=verify_lzf90ovv_6NcE3oRP_5DNC_4k61_8raI_zBwk7QhGUigZ"

myheader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.douyin.com/user/MS4wLjABAAAAAY-C0O4ybubfJ7dokO0ZdmzDpolyhfbeQ_BG4hKJRJ6NrnP7nC5s1qRmGh9NhZgt?from_tab_name=main',
    'cookie': 'store-region=cn-sn; store-region-src=uid; xgplayer_user_id=659439091375; live_use_vvc=%22false%22; my_rd=2; xgplayer_device_id=20404490263; bd_ticket_guard_client_web_domain=2; SEARCH_RESULT_LIST_TYPE=%22single%22; UIFID_TEMP=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e38528051aebb4ec8a476b99e05f786d7d80e5fffcfab8e12300b5c608713ef1be1ebb7f1eabd268e1020d34e169a415e8db45a; fpk1=U2FsdGVkX1+qT7yzLHwBuwiGinib0W27ywrcwzHeguyibW1HZ0NkDC65qo+c6aNhBL7MRlkShYNXtsekpTwVkA==; fpk2=5f4591689f71924dbd1e95e47aec4ed7; d_ticket=ede503b482b7698331839f5552b34030978dc; passport_assist_user=CkCX03RzhmZubCilVW92mgeeG0lEBod51jxHPy5kbcFk8d4YRGrXUFRiPzb49LZkSxYBFKSuAe6e9RtZzga37iteGkoKPDyDjn2IUpeIWoz7hECSprP3GxVF0IiuEjNy3teiJuiWuZtKnGhbQQ5Vf92ReMoqyNMk-0mFM5IG7WmvoBD_-9QNGImv1lQgASIBA8kQcqw%3D; n_mh=uN1BbQIFMe9Z1yH0ul9todRBwtoKfME0EqocxmKoP3s; uid_tt=54ad5ae26c1eff738b06d6f94cedc943; uid_tt_ss=54ad5ae26c1eff738b06d6f94cedc943; sid_tt=da8affcba26a7a17389e2073147f0362; sessionid=da8affcba26a7a17389e2073147f0362; sessionid_ss=da8affcba26a7a17389e2073147f0362; UIFID=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e3852806f6099c27c763197e9cf58997ba92b7051666a54e8265c33a34821233498c6692647b6a927d85209fad0c107dec7c384200831a1f74da51d348cfc5ee421468df99613489fb5b33edd30115074a5abcb6a7a0693a9c966c278038774f4c68628b14f727af5ff9cb6cf74c778068c3a5e522f01ec73e1436af853b86d384d4ca8; s_v_web_id=verify_lzf90ovv_6NcE3oRP_5DNC_4k61_8raI_zBwk7QhGUigZ; dy_swidth=1536; dy_sheight=864; passport_csrf_token=db41a50a61c6f0b0c25d594fa5abd733; passport_csrf_token_default=db41a50a61c6f0b0c25d594fa5abd733; SelfTabRedDotControl=%5B%5D; sid_guard=da8affcba26a7a17389e2073147f0362%7C1725108950%7C5184000%7CWed%2C+30-Oct-2024+12%3A55%3A50+GMT; is_staff_user=false; sid_ucp_v1=1.0.0-KDU3YWQ2NGRiMzNjY2UzZTFkNTg5ZjRjOTExNTg4NDRkYzI5N2M2NGQKGwitg6Co6oyoARDWpcy2BhjvMSAMOAZA9AdIBBoCbGYiIGRhOGFmZmNiYTI2YTdhMTczODllMjA3MzE0N2YwMzYy; ssid_ucp_v1=1.0.0-KDU3YWQ2NGRiMzNjY2UzZTFkNTg5ZjRjOTExNTg4NDRkYzI5N2M2NGQKGwitg6Co6oyoARDWpcy2BhjvMSAMOAZA9AdIBBoCbGYiIGRhOGFmZmNiYTI2YTdhMTczODllMjA3MzE0N2YwMzYy; pwa2=%220%7C0%7C3%7C0%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A1%7D; ttwid=1%7CgRdGqDPFK8gDSaWF8COziP7sT7MEuryFT2mYfKnLvco%7C1725536465%7C92abd9d4792c3a4288aa97ebab626b8bfcb75824d3f6571fd9ca7c39e4a49a03; publish_badge_show_info=%220%2C0%2C0%2C1725536469540%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __live_version__=%221.1.2.3340%22; live_can_add_dy_2_desktop=%220%22; douyin.com; xg_device_score=7.716500300874227; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; strategyABtestKey=%221725588960.398%22; csrf_session_id=e681dd281bd7d5503fcae73f638419e2; biz_trace_id=c70437df; download_guide=%223%2F20240906%2F0%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAALoeoG0UTWQTsYOJu9DuJyKpPCTeewHC6RKgJ5YAAXtw%2F1725638400000%2F0%2F0%2F1725590856796%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; WallpaperGuide=%7B%22showTime%22%3A1725590322183%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A21%2C%22cursor2%22%3A2%2C%22hoverTime%22%3A1725590621167%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQ2c4SVluU3FTSG14RGlHVVA1dGd3YnBCeU1rWjhHTDFJNGhNYWpFMDVzNnJoWjlqK0RWRDJycTBUak5hQTBPeUcwenkrZnordlUxRVdFNElmeFZHY1E9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; odin_tt=4fcd33c3b805d46c5a79a5f9dba3bfb8345b854d55f863c9372fb64323c1f910fd396dcc4a6454358ac99ceb20a0a939; passport_fe_beating_status=false; __ac_nonce=066da70fc0057a725bb9d; __ac_signature=_02B4Z6wo00f01xyrypQAAIDDJLj6EY-1Pxsci84AAKH6T3aCANhzTmm1yJzhXGLRY0BRNav..tOG4E0dVNtnbZ8yCTvzSM8GsiGj1yraTqRGBAaq-c0qu0NbRDT7jqK8rn3oELGY33FIgxSoe2; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22'

}

res = r.get(url, headers=myheader)
# print(res.text)
# 提取有效字段
aweme_list = res.json()['aweme_list']

for i in aweme_list:
    desc = i['desc']
    url = i['video']['play_addr']['url_list'][0]
    print(desc)
    res = r.get(url, headers=myheader)

# 清理文件名
clean_desc = clean_filename(desc)

with open(clean_desc + '.mp4', 'wb') as f:
    f.write(res.content)
