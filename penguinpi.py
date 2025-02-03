import sys
sys.path.append("/root/mindplus/.lib/thirdExtension/liliang-gravityvoicerecognition-thirdex")
import time
from unihiker import GUI
from pinpong.board import Board,Pin
from pinpong.extension.unihiker import *
from pinpong.libs.dfrobot_speech_synthesis import DFRobot_SpeechSynthesis_I2C
from pinpong.libs.dfrobot_asr import DFRobot_ASR
from DFRobot_DF2301Q import *




#语音识别模块初始化
DF2301Q = DFRobot_DF2301Q_I2C()
DF2301Q.set_wake_time(60)
DF2301Q.set_volume(5)
DF2301Q.set_mute_mode(1)

#距离传感器计算距离函数
def get_IR(value):
    if value < 16:
        value = 16
    return 4800 / (value - 20)

#距离格式转换
def number_map(x, in_min, in_max, out_min, out_max):
    return(x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#界面初始化
p = gui.draw_image(image = "PeaceScene1.png", x = 0, y = -400)
p.config(h = 320)
school = gui.draw_image(image = "SchoolScene.png", x = 0, y = -400)
school.config(h = 320)
travel = gui.draw_image(image = "TravelScene.png", x = 0, y = -400)
travel.config(h = 320)
ec = gui.draw_image(image = "ECScene.png", x = 0, y = -400)
ec.config(h = 320)
s = gui.draw_image(image = "SleepScene1.png", x = 0, y = 0)
s.config(h = 320)
#dis = gui.draw_text(text = 'xxx', x = 0, y = 0, color="#0000FF")

abc = gui.draw_emoji(emoji = "Sleep", x = 0, y = -90, duration = 0.3)
sleep = True
is_playing = False

#初始化识别id的值
var = 0

while True:
    if is_playing:
        continue
        
    #获取语音输入
    var = DF2301Q.get_CMDID() 
    time.sleep(0.05)
    
    #获取距离
    #rd = p_p21_analog.read_analog()
    #value = number_map(rd, 0, 4095, 255, 0)
    #distance = int(get_IR(value))
    #dis.config(text = str(int(value)))   
    
    if ( var == 1 and sleep == True) :
        abc.config(emoji="Peace")
        s.config(y = -400)
        p.config(y = 0)
        voice.speak("主人我在，请选择出门情景")
        sleep = False
        is_playing = False

    elif sleep==False:
        if var == 5:
            is_playing = True
            p.config(y = -400)
            ec.config(y = -400)
            travel.config(y = -400)
            abc.config(y = -400)
            school.config(y = 0)
            voice.speak("主人，您去上学时需要带好")
            voice.speak("明天所有课所需要的书")
            voice.speak("笔袋、作业、电脑、水壶")
            voice.speak("以及正确的校服 ")
            voice.speak("最后提醒主人")
            voice.speak("检查一下作业是否带齐")
            voice.speak("并记得在正装日穿黑皮鞋")
            is_playing = False
        if var == 6:
            is_playing = True
            p.config(y = -400)
            school.config(y = -400)
            travel.config(y = -400)
            abc.config(y = -400)
            ec.config(y = 0)
            voice.speak("主人，上课外课时要带好")
            voice.speak("课上要求带的书或其他物品")
            voice.speak("笔袋、笔记本、水壶、手机")
            voice.speak("如需要的话，还要带上电脑")
            is_playing = False
        if var == 7:
            is_playing = True
            p.config(y = -400)
            school.config(y = -400)
            ec.config(y = -400)
            abc.config(y = -400)
            travel.config(y = 0)
            voice.speak("主人，您去旅游时要带好")
            voice.speak("每天的衣服")
            voice.speak("防晒和防雨外套")
            voice.speak("防晒霜、防蚊水")
            voice.speak("洗漱用品、OK镜")
            voice.speak("所需电子产品、作业")
            voice.speak("一些小零食、以及水壶")
            voice.speak("提醒主人")
            voice.speak("还要准备几套备用衣服")
            is_playing = False
        if var == 8:
            is_playing = True
            voice.speak("关闭中")
            p.config(y = -400)
            school.config(y = -400)
            travel.config(y = -400)
            ec.config(y = -400)
            abc.config(emoji="Sleep")
            abc.config(y = -95)
            s.config(y = 0)
            voice.speak("主人再见")
            sleep = True
            is_playing = False
        var = 0
        time.sleep(0.05)
