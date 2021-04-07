import json
import logging

logging.basicConfig(level=logging.DEBUG)

# jsonファイルの読み込み
restaurants_dict = dict()
with open('./test/Roboter/store.json', mode='rt', encoding='utf-8') as file:
    restaurants_dict = json.load(file)
logging.debug('restaurants: %s',restaurants_dict)
logging.debug('restaurants type: %s',type(restaurants_dict))

print('こんにちは！私はRobokoです。あなたの名前はなんですか？')
user_name = input()

if restaurants_dict == None:
    print('{0}さん。どこのレストランが好きですか？'.format(user_name))
    restaurants_dict = input()
else:
    # ソート
    restaurants_dict = sorted(restaurants_dict.items(), key=lambda x:x[0])
    print("私のおすすめのレストランは、{0}です。\nこのレストランは好きですか？[Yes][No]".format(restaurants_dict[0][0]))
    like = input()
    if 'Y' in like or 'y' in like:
        restaurants_dict[0][1] += 1
    else:
        print('{0}さん。どこのレストランが好きですか？'.format(user_name))
        restaurant_name = input()

output_dict = dict(restaurants_dict)
print(output_dict)

print('{0}さん、ありがとうございました。\n良い1日を！さようなら。'.format(user_name))
# ソート
# 標準入出力
# 結果をjsonファイルに保存