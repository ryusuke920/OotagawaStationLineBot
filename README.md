# OotagawaStationLineBot
LINE's automatic bot that tells you the departure time of the train from Ootagawa Station (my local station)

## Production period
2021/04/04(Sun) 〜 2021/04/05(Mon)

## Producer
[Ryusuke](https://github.com/ryusuke920)

## [Content](https://github.com/ryusuke920/OotagawaStationLineBot)
|derectoryName|Explanation|
|:-:|:-:|
|[img](https://github.com/ryusuke920/OotagawaStationLineBot/tree/main/img)|The image of Ootagawa Station, which is the icon of the line, is stored.|
|[line](https://github.com/ryusuke920/OotagawaStationLineBot/tree/main/line)|Contains the SDK that creates the outline of the automatic bot.|
|[app.py](https://github.com/ryusuke920/OotagawaStationLineBot/blob/main/app.py)|It is a Py code that describes the timetable of the main train and the sentences to be sent.|
|[station.py](https://github.com/ryusuke920/OotagawaStationLineBot/blob/main/station.py)|This is the Py code I wrote for debug. It doesn't matter if you don't have it.|

## One flow

### 1. Terminal operation
```git
git clone https://github.com/ryusuke920/OotagawaStationLineBot.git
```
Enter.

### 2. Launch ngrok
```
./ngrok http 5000
```
You can get the http and https URLs corresponding to localhost by typing.
![スクリーンショット 2021-04-05 19 15 18](https://user-images.githubusercontent.com/66785066/113563815-53553380-9643-11eb-8600-cdf52fb4c63c.png)

### 3. Settings in LINE Developers
Copy this URL into the Webhook URL in the LINE Developers Webhook settings.  
At this time, if you are not https, it will be invalidated, so be careful.
![スクリーンショット 2021-04-05 18 59 39](https://user-images.githubusercontent.com/66785066/113562481-20aa3b80-9641-11eb-8c79-e1e38416ae0e.png)

### 4. Launch Flask
At the terminal,
```
flask run
```
Enter to complete.  
If you go to the LINE Bot screen and send the station name and time, the time based on it will be returned automatically.

### Image diagram
<img src ="https://user-images.githubusercontent.com/66785066/113563957-8697c280-9643-11eb-8e27-691b580df8f8.jpg" width= "300" >
