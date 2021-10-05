from sys import argv
from json import loads
from os.path import split
from datetime import datetime
import os


def convert(FILE_NAME, single_str, count):
    content_str = single_str['content']
    from_str = single_str['from']
    to_str = single_str['to']
    # 写入srt文件
    with open(SRT_DIR + FILE_NAME.strip('.json') + '.srt', 'a+', encoding='utf-8') as srt_file:
        srt_file.write(str(count) + '\n')
        srt_file.write(get_timestrip(from_str, to_str) + '\n')
        srt_file.write(content_str + '\n')
        srt_file.write('\n')
    srt_file.close()


def get_timestrip(from_str, to_str):
    # 00:00:00,760 --> 00:00:02,440
    # 0.76 2.44
    date_time_1 = datetime.utcfromtimestamp(float(from_str))
    timestrip_1 = date_time_1.strftime("%H:%M:%S,%f")[:-3]
    date_time_2 = datetime.utcfromtimestamp(float(to_str))
    timestrip_2 = date_time_2.strftime("%H:%M:%S,%f")[:-3]
    timestrip = timestrip_1 + ' --> ' + timestrip_2
    # test
    # print(timestrip)
    return timestrip


# 创建文件夹保存srt
SRT_DIR = os.getcwd() + '\\srt\\'
if os.path.exists(SRT_DIR):
    print("srt_path exists")
else:
    os.mkdir(SRT_DIR)

# 处理多个文件
FILES_PATH = argv[1:]
for FILE_PATH in FILES_PATH:
    # 单个文件
    FILE_DIR, FILE_NAME = split(FILE_PATH)
    count = 0
    # 读取文件 && 解析json
    with open(FILE_PATH, 'r', encoding='utf-8') as json_file:
        JSON_FILE_CONTENT = json_file.read()
        JSON_DATA = loads(JSON_FILE_CONTENT)
        # test
        # print(JSON_DATA['body'][0]['content'])
        for single_str in JSON_DATA['body']:
            convert(FILE_NAME, single_str, count)
            count = count + 1
