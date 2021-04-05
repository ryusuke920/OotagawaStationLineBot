from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('HICNdxCb3wcKouZZ8KqSWqUsvRrNjS3EvkXwVzamAMkgeTSVdjHRmlEiFRHkKYCWqebxtcu1jiV7pLak7TKhfy662Va/5H2FKj/FWP+u4cesLHagVg/CzejRcMmOExitC97iU1VfPfIYwh/3xPhfwgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7484a3f13168906a0a6fb03d4b1a3ed5')

# ngrok動いてるかの確認用
"""
@app.route("/")
def test():
    return "OK"
"""


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 自分の通い駅
home_station = ["太田川"]

# 河和線の駅名
kouwasenn_home = ["高横須賀", "南加木屋", "八幡新田", "巽ヶ丘", "白沢", "坂部",
                    "阿久比", "植大", "半田口", "住吉町", "知多半田", "成岩",
                    "青山", "上ゲ", "知多武豊", "富貴", "河和口", "河和"]

# 知多新線の駅名
titasinnsenn_home = ["上野間", "美浜緑苑", "知多奥田", "野間", "内海"]

# 常滑線の駅名
tokonamesenn_home = ["尾張横須賀", "寺本", "朝倉", "古見", "長浦", "日長", "新舞子",
                    "大野町", "西ノ口", "蒲池", "榎戸", "多屋", "常滑", "りんくう常滑", "中部国際空港", "セントレア"]

# 築港線の駅名
tikkousenn_home = ["新日鉄前", "聚楽園", "名和", "柴田", "大同町", "大江", "道徳", "豊田本町", "神宮前"]

# 知多半島内全ての駅名
station = home_station + kouwasenn_home + titasinnsenn_home + tokonamesenn_home + tikkousenn_home

# 太田川 -> 河和線行きのダイヤ
ootagawa_station_kouwasenn_time = [
                                    "05:47", "05:56",
                                    "06:21", "06:36", "06:46",
                                    "07:04", "07:15", "07:28", "07:38", "07:58",
                                    "08:04", "08:15", "08:28", "08:38", "08:58",
                                    "09:04", "09:15", "09:28", "09:38", "09:58",
                                    "10:04", "10:15", "10:28", "10:38", "10:58",
                                    "11:08", "11:14", "11:58",
                                    "12:08", "12:14", "12:58",
                                    "13:08", "13:14", "13:58",
                                    "14:08", "14:14", "14:58",
                                    "15:08", "15:14", "15:58",
                                    "16:08", "16:14", "16:58",
                                    "17:08", "17:14", "17:58",
                                    "18:08", "18:14", "18:58",
                                    "19:08", "19:14", "19:58",
                                    "20:08", "20:14", "20:58",
                                    "21:08", "21:14", "21:58",
                                    "22:08", "22:14", "22:58",
                                    "23:04", "23:47", "23:51",
                                    "00:16"
                                    ]

# 太田川 -> 知多新線行きのダイヤ
ootagawa_station_titasinnsenn_time = [
                                    "05:47", "05:56",
                                    "06:21", "06:36", "06:46",
                                    "07:20", "07:44", "07:50",
                                    "08:20", "08:44", "08:50",
                                    "09:20", "09:44", "09:50",
                                    "10:20", "10:44", "10:50",
                                    "11:28", "11:38", "11:44",
                                    "12:28", "12:38", "12:44",
                                    "13:28", "13:38", "13:44",
                                    "14:28", "14:38", "14:44",
                                    "15:28", "15:38", "15:44",
                                    "16:28", "16:38", "16:44",
                                    "17:28", "17:38", "17:44",
                                    "18:28", "18:38", "18:44",
                                    "19:28", "19:38", "19:44",
                                    "20:28", "20:38", "20:44",
                                    "21:28", "21:38", "21:44",
                                    "22:28", "22:38", "22:44",
                                    "23:15"
                                    ]

# 太田川 -> セントレア（中部国際空港）・常滑行きのダイヤ
ootagawa_station_senntorea_time = [
                                    "05:29", "05:41", "05:52", "05:55",
                                    "06:04", "06:06", "06:25", "06:34", "06:37", "06:51",
                                    "07:00", "07:10", "07:18", "07:22", "07:37", "07:47", "07:53",
                                    "08:07", "08:17", "08:23", "08:37", "08:47", "08:53",
                                    "09:07", "09:17", "09:23", "09:37", "09:47", "09:53",
                                    "10:07", "10:17", "10:23", "10:37", "10:47", "10:53",
                                    "11:07", "11:17", "11:23", "11:37", "11:47", "11:53",
                                    "12:07", "12:17", "12:21", "12:37", "12:47", "12:51",
                                    "13:07", "13:17", "13:21", "13:37", "13:47", "13:51",
                                    "14:07", "14:17", "14:21", "14:37", "14:47", "14:51",
                                    "15:07", "15:17", "15:21", "15:37", "15:47", "15:51",
                                    "16:07", "16:17", "16:21", "16:37", "16:47", "16:51",
                                    "17:07", "17:17", "17:21", "17:37", "17:47", "17:51",
                                    "18:07", "18:17", "18:21", "18:37", "18:47", "18:51",
                                    "19:07", "19:17", "19:21", "19:37", "19:47", "19:51",
                                    "20:07", "20:17", "20:21", "20:37", "20:47", "20:51",
                                    "21:07", "21:17", "21:21", "21:37", "21:47", "21:53",
                                    "22:08", "22:17", "22:23", "22:36", "22:50",
                                    "23:03", "23:17", "23:33", "23:48"
                                    ]

# 太田川 -> 築港線（金山・名鉄名古屋）行きのダイヤ
ootagawa_station_tikkousenn_time = [
                                    "06:31", "06:48", "06:51", "06:06", "06:17", "06:19", "06:22", "06:30", "06:32", "06:40", "06:45", "06:48",
                                    "07:01", "07:03", "07:06", "07:13", "07:15", "07:19", "07:23", "07:29", "07:33", "07:36", "07:39", "07:46", "07:49", "07:52", "07:57",
                                    "08:00", "08:04", "08:07", "08:10", "08:16", "08:19", "08:22", "08:26", "08:34", "08:37", "08:40", "08:46", "08:49", "08:52", "08:56",
                                    "09:04", "09:07", "09:10", "09:17", "09:22", "09:26", "09:34", "09:37", "09:40", "09:47", "09:52", "09:56",
                                    "10:04", "10:07", "10:10", "10:17", "10:22", "10:26", "10:34", "10:37", "10:40", "10:47", "10:52", "10:56",
                                    "11:04", "11:07", "11:10", "11:17", "11:22", "11:26", "11:34", "11:37", "11:40", "11:47", "11:52", "11:56",
                                    "12:04", "12:07", "12:10", "12:17", "12:22", "12:26", "12:34", "12:37", "12:40", "12:47", "12:52", "12:56",
                                    "13:04", "13:07", "13:10", "13:17", "13:22", "13:26", "13:34", "13:37", "13:40", "13:47", "13:52", "13:56",
                                    "14:04", "14:07", "14:10", "14:17", "14:22", "14:26", "14:34", "14:37", "14:40", "14:47", "14:52", "14:56",
                                    "15:04", "15:07", "15:10", "15:17", "15:22", "15:26", "15:34", "15:37", "15:40", "15:47", "15:52", "15:56",
                                    "16:04", "16:07", "16:10", "16:17", "16:22", "16:26", "16:34", "16:37", "16:40", "16:47", "16:52", "16:56",
                                    "17:04", "17:07", "17:10", "17:17", "17:22", "17:26", "17:34", "17:37", "17:40", "17:47", "17:52", "17:56",
                                    "18:04", "18:07", "18:10", "18:17", "18:22", "18:26", "18:34", "18:37", "18:40", "18:47", "18:52", "18:56",
                                    "19:04", "19:07", "19:10", "19:17", "19:22", "19:26", "19:34", "19:37", "19:40", "19:47", "19:52", "19:56",
                                    "20:04", "20:07", "20:10", "20:17", "20:22", "20:26", "20:34", "20:37", "20:40", "20:47", "20:52", "20:56",
                                    "21:04", "21:07", "21:10", "21:17", "21:22", "21:26", "21:34", "21:37", "21:40", "21:47", "21:52", "21:56",
                                    "22:04", "22:07", "22:10", "22:17", "22:22", "22:26", "22:34", "22:37", "22:46", "22:51",
                                    "23:00", "23:07", "23:10", "23:21", "23:24", "23:38", "23:50"
                                    ]

from time import time # corrent_timeを取得
import datetime

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    sender_message = event.message.text.split() # [駅名, 時刻]
    print(sender_message,"です。")

    INF = 10 ** 9 + 7 # 初期値

    # メッセージを送信した時刻
    now_time = datetime.datetime.utcnow()
    now_time = str(now_time)
    now = list(now_time.split())
    year = int(now[0][0 : 4]) # 年
    month = int(now[0][5 : 7]) # 月
    date = int(now[0][8 : 10]) # 日
    time = [int(now[1][0 : 2]) + 9, int(now[1][3 : 5])] # 時間・分

    # 指定した時刻
    if len(sender_message) >= 2 and len(sender_message[1]) >= 5 and sender_message[1][2] == ":":
        sender_time = [int(sender_message[1][0 : 2]), int(sender_message[1][3 : 5])] # 時間・分
    else:
        sender_time = [99, 99] # 検索に引っかからないようにする

    # 24:00を超えていたら１日分ずらす
    if time[0] >= 24:
        time[0] -= 24
        date += 1

    # 時刻を2桁表示
    if len(str(time[0])) == 1:
        time[0] = "0" + str(time[0])

    # print(year, month, date, time) # 時刻のdebug用

    # 現在の時刻の数の大きさ -> int
    corrent_time = time[0] * 100 + time[1]

    # 指定した時刻の数の大きさ -> int
    if len(sender_message) >= 2 and len(sender_message[1]) >= 5 and sender_message[1][2] == ":":
        sender_specification_time = sender_time[0] * 100 + sender_time[1]
    else:
        sender_specification_time = INF # 検索に引っかからないようにする
    
    print(sender_message,sender_time,sender_specification_time,"aaaaa")
    show_time = [] # 現時刻の送信する時刻を保管する場所
    show_time_stock = 0 # 何個分まで見せてるか
    specification_time = [] # 指定した時刻を保管する場所
    specification_time_stock = 0 # 指定した時刻の何個分まで見せてるか

    station_Bool = False # 入力した駅名が存在したかの判定

    for i in range(len(station)):
        if sender_message[0] in station:
            station_distance = i + 1 # 目的地の駅までのホーム数
            destination_station = station[i] # 目的地の駅名
            station_Bool = True

            # "太田川" の文字列が含まれている場合の処理
            if sender_message[0] in home_station:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text = f"ここはあなたのホーム駅です。 \n 移動する必要はありません！"))
                station_Bool = True

            # "河和線" の駅名が含まれている場合の処理（現在の時刻版）
            if sender_message[0] in kouwasenn_home:
                for j in range(len(ootagawa_station_kouwasenn_time)):
                    if show_time_stock == 3:
                        break
                    if int(ootagawa_station_kouwasenn_time[j][0 : 2] + ootagawa_station_kouwasenn_time[j][3 : 5]) >= corrent_time:
                        show_time_stock += 1
                        show_time.append(ootagawa_station_kouwasenn_time[j])
                station_Bool = True

            # "河和線" の駅名が含まれている場合の処理（指定した時刻版）
            if sender_message[0] in kouwasenn_home:
                for j in range(len(ootagawa_station_kouwasenn_time)):
                    if specification_time_stock == 3:
                        break
                    if int(ootagawa_station_kouwasenn_time[j][0 : 2] + ootagawa_station_kouwasenn_time[j][3 : 5]) >= sender_specification_time:
                        specification_time_stock += 1
                        specification_time.append(ootagawa_station_kouwasenn_time[j])

            # "知多新線" の駅名が含まれている場合の処理（現在の時刻版）
            if sender_message[0] in titasinnsenn_home:
                for j in range(len(ootagawa_station_titasinnsenn_time)):
                    if show_time_stock == 3:
                        break
                    if int(ootagawa_station_titasinnsenn_time[j][0 : 2] + ootagawa_station_titasinnsenn_time[j][3 : 5]) >= corrent_time:
                        show_time_stock += 1
                        show_time.append(ootagawa_station_titasinnsenn_time[j])
                station_Bool = True

            # "知多新線" の駅名が含まれている場合の処理（指定した時刻版）
            if sender_message[0] in titasinnsenn_home:
                for j in range(len(ootagawa_station_titasinnsenn_time)):
                    if specification_time_stock == 3:
                        break
                    if int(ootagawa_station_titasinnsenn_time[j][0 : 2] + ootagawa_station_titasinnsenn_time[j][3 : 5]) >= sender_specification_time:
                        specification_time_stock += 1
                        specification_time.append(ootagawa_station_titasinnsenn_time[j])

            # "常滑線" の駅名が含まれている場合の処理（現在の時刻版）
            if sender_message[0] in tokonamesenn_home:
                for j in range(len(ootagawa_station_senntorea_time)):
                    if show_time_stock == 3:
                        break
                    if int(ootagawa_station_senntorea_time[j][0 : 2] + ootagawa_station_senntorea_time[j][3 : 5]) >= corrent_time:
                        show_time_stock += 1
                        show_time.append(ootagawa_station_senntorea_time[j])
                station_Bool = True

            # "常滑線" の駅名が含まれている場合の処理（指定した時刻版）
            if sender_message[0] in tokonamesenn_home:
                for j in range(len(ootagawa_station_senntorea_time)):
                    if specification_time_stock == 3:
                        break
                    if int(ootagawa_station_senntorea_time[j][0 : 2] + ootagawa_station_senntorea_time[j][3 : 5]) >= sender_specification_time:
                        specification_time_stock += 1
                        specification_time.append(ootagawa_station_senntorea_time[j])

            # "築港線" の駅名が含まれている場合の処理（現在の時刻版）
            if sender_message[0] in tikkousenn_home:
                for j in range(len(ootagawa_station_tikkousenn_time)):
                    if show_time_stock == 3:
                        break
                    if int(ootagawa_station_tikkousenn_time[j][0 : 2] + ootagawa_station_tikkousenn_time[j][3 : 5]) >= corrent_time:
                        show_time_stock += 1
                        show_time.append(ootagawa_station_tikkousenn_time[j])
                station_Bool = True

            # "築港線" の駅名が含まれている場合の処理（指定した時刻版）
            if sender_message[0] in tikkousenn_home:
                for j in range(len(ootagawa_station_tikkousenn_time)):
                    if specification_time_stock == 3:
                        break
                    if int(ootagawa_station_tikkousenn_time[j][0 : 2] + ootagawa_station_tikkousenn_time[j][3 : 5]) >= sender_specification_time:
                        specification_time_stock += 1
                        specification_time.append(ootagawa_station_tikkousenn_time[j])


    # 駅名を改行表示させるための操作（現在の時刻版）
    show_time = list(set(show_time)) # 重複をなくす
    show_time.sort()
    show_time_stock = len(show_time)
    station_time_array = "\n".join(show_time)

    # 駅名を改行表示させるための操作（指定した時刻版）
    specification_time = list(set(specification_time))
    specification_time.sort()
    specification_time_stock = len(specification_time)
    specification_station_time_array = "\n".join(specification_time)

    # 存在しない駅名を入力した際の処理
    if not station_Bool:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"あなたの入力した駅名は存在しないか、範囲外の駅です。 \nもう一度ご確認の上、入力して下さい。"))        
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"現在は{year}年{month}月{date}日{time[0]}:{time[1]}です。 \n\n直近の{sender_message[0]}行きの{show_time_stock}つの電車の時間は以下の通りです。 \n{station_time_array}\n\nまた{sender_message[0]}行きであなたが指定した時刻の直近の{specification_time_stock}つの電車は以下の通りです。\n{specification_station_time_array}"))

# debug確認用
"""
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
"""

if __name__ == "__main__":
    app.run()