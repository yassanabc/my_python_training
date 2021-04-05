import json
import logging

logging.basicConfig(level=logging.DEBUG)

# jsonファイルの読み込み
restaurants_dict = dict()
with open('./test/Roboter/store.json', mode='rt', encoding='utf-8') as file:
    restaurants_dict = json.load(file)
logging.debug('restaurants: %s',restaurants_dict)

print('こんにちは！私はRobokoです。あなたの名前はなんですか？')
name = input()

if restaurants_dict == None:
    print('%sさん。どこのレストランが好きですか？')
    restaurants_dict = input()
else:
    pass

# ソート
# 標準入出力
# 結果をjsonファイルに保存