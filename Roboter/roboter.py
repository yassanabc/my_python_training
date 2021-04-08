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

output_dict = {}
if restaurants_dict == None:
    print('{0}さん。どこのレストランが好きですか？'.format(user_name))
    output_dict = ({input(), 1})
else:
    # ソート
    restaurants_list = sorted(restaurants_dict.items(), reverse=False)
    print("私のおすすめのレストランは、{0}です。\nこのレストランは好きですか？[Yes][No]".format(restaurants_list[0][0]))
    like = input()
    if 'Y' in like or 'y' in like:
        restaurants_dict[restaurants_list[0][0]] += 1
        output_dict = restaurants_dict
    else:
        print('{0}さん。どこのレストランが好きですか？'.format(user_name))
        restaurant_name = input()
        if restaurant_name in restaurants_list:
            restaurants_dict[restaurant_name] += 1
            output_dict = restaurants_dict
        else:
            restaurants_dict[restaurant_name] = 1
            output_dict = restaurants_dict

with open('./test/Roboter/store.json', mode='wt', encoding='utf-8') as file:
    json.dump(output_dict, file)

print('{0}さん、ありがとうございました。\n良い1日を！さようなら。'.format(user_name))