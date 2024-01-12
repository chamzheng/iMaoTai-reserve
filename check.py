import datetime
import logging
import sys

import config
import login
import process
import privateCrypt

DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
TODAY = datetime.date.today().strftime("%Y%m%d")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
                    stream=sys.stdout,
                    datefmt=DATE_FORMAT)

print(r'''
**************************************
    欢迎使用i茅台自动预约工具
    作者GitHub：https://github.com/3 9 7 1 7 9 4 5 9
    vx：L 3 9 7 1 7 9 4 5 9 加好友注明来意
**************************************
''')

process.get_current_session_id()

# 校验配置文件是否存在
configs = login.config
if len(configs.sections()) == 0:
    logging.error("配置文件未找到配置")
    sys.exit(1)

aes_key = privateCrypt.get_aes_key()

s_title = '茅台申购结果'
s_content = ""

for section in configs.sections():
    if (configs.get(section, 'enddate') != 9) and (TODAY > configs.get(section, 'enddate')):
        continue
    mobile = privateCrypt.decrypt_aes_ecb(section, aes_key)
    province = configs.get(section, 'province')
    city = configs.get(section, 'city')
    token = configs.get(section, 'token')
    userId = privateCrypt.decrypt_aes_ecb(configs.get(section, 'userid'), aes_key)
    lat = configs.get(section, 'lat')
    lng = configs.get(section, 'lng')

    p_c_map, source_data = process.get_map(lat=lat, lng=lng)

    process.UserId = userId
    process.TOKEN = token
    process.init_headers(user_id=userId, token=token, lng=lng, lat=lat)
    
    # 根据配置中，要预约的商品ID，城市 进行自动预约
    try:
        s_content += process.get_result(mobile)

    except BaseException as e:
        print(e)
        logging.error(e)

# 推送消息
process.send_msg(s_title, s_content)
