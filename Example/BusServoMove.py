import time
import hiwonder.Board as Board

# print('''
# **********************************************************
# ********功能:幻尔科技TonyPi扩展板，串口舵机控制例程*******
# **********************************************************
# ----------------------------------------------------------
# Official website:http://www.hiwonder.com
# Online mall:https://huaner.tmall.com/
# ----------------------------------------------------------
# 以下指令均需在LX终端使用，LX终端可通过ctrl+alt+t打开，或点
# 击上栏的黑色LX终端图标。
# ----------------------------------------------------------
# Usage:
#     python3 BusServoMove.py
# ----------------------------------------------------------
# Version: --V1.2  2021/07/03
# ----------------------------------------------------------
# Tips:
#  * 按下Ctrl+C可关闭此次程序运行，若失败请多次尝试！
# ----------------------------------------------------------
# ''')

# while True:
#     # 参数：参数1：舵机id; 参数2：位置; 参数3：运行时间
#     Board.setBusServoPulse(8, 500, 500) # 8号舵机转到500位置，用时500ms
#     time.sleep(0.5) # 延时时间和运行时间相同
    
#     Board.setBusServoPulse(8, 200, 500) #舵机的转动范围0-240度，对应的脉宽为0-1000,即参数2的范围为0-1000
#     time.sleep(0.5)
    
#     Board.setBusServoPulse(8, 500, 200)
#     time.sleep(0.2)
    
#     Board.setBusServoPulse(8, 200, 500)  
#     Board.setBusServoPulse(16, 200, 500)
#     time.sleep(0.5)
    
#     Board.setBusServoPulse(8, 500, 500)  
#     Board.setBusServoPulse(16, 500, 500)
#     time.sleep(0.5)    

# servo_id = Board.getBusServoID()
# print('id:',servo_id)
Board.setBusServoPulse(19, 800, 500)

# Board.setBusServoID(18, 19)

# print('''
# **********************************************************
# *****功能:幻尔科技树莓派扩展板，串口舵机读取状态例程******
# **********************************************************
# ----------------------------------------------------------
# Official website:http://www.lobot-robot.com/pc/index/index
# Online mall:https://lobot-zone.taobao.com/
# ----------------------------------------------------------

# ----------------------------------------------------------
# Usage:
#     sudo python3 set_BusServo_status.py
# ----------------------------------------------------------
# Version: --V1.0  2021/08/16
# ----------------------------------------------------------
# Tips:
#  * 按下Ctrl+C可关闭此次程序运行，若失败请多次尝试！
# ----------------------------------------------------------
# ''')

# def get_status():
#     servo_id = Board.getBusServoID()
#     dev = Board.getBusServoDeviation(servo_id)
#     if dev > 125:
#         dev = -(0xff - (dev - 1))
#     angle_range = Board.getBusServoAngleLimit(servo_id)
#     vin_range = Board.getBusServoVin(servo_id)
#     temperature_warn = Board.getBusServoTempLimit(servo_id)
#     load_state = Board.getBusServoLoadStatus(servo_id)
#     print('*******current status**********')
#     print('id:%s'%(str(servo_id).ljust(3)))
#     print('dev:%s'%(str(dev).ljust(4)))
#     print('angle_range:%s'%(str(angle_range).ljust(4)))
#     print('voltage_range:%s'%(str(vin_range).ljust(5)))
#     print('temperature_warn:%s'%(str(temperature_warn).ljust(4)))
#     print('lock:%s'%(str(load_state).ljust(4)))
#     print('*******************************')

# print('''
# --------------------------               
# 1 id                
# 2 dev               
# 3 save_dev          
# 4 help      
# 5 voltage_range   
# 6 temperature_warn
# 7 lock              
# 8 exit
# --------------------------''')
# # 4 angle_range 
# while True:
#     try:
#         get_status()
#         mode = int(input('input mode:'))
#         if mode == 1:
#             oldid = int(input('current id:'))
#             newid = int(input('new id(0-253):'))
#             Board.setBusServoID(oldid, newid)
#         elif mode == 2:
#             servo_id = int(input('servo id:'))
#             dev = int(input('deviation(-125~125):'))
#             if dev < 0:
#                 dev = 0xff + dev + 1
#             Board.setBusServoDeviation(servo_id, dev)
#         elif mode == 3:
#             servo_id = int(input('servo id:'))
#             Board.saveBusServoDeviation(servo_id)
#         # elif mode == 4:
#         #     servo_id = int(input('servo id:'))
#         #     min_pos = int(input('min pos(0-1000):'))
#         #     max_pos = int(input('max pos(0-1000):'))
#         #     Board.setBusServoAngleLimit(servo_id, min_pos, max_pos)        
#         elif mode == 5:
#             servo_id = int(input('servo id:'))
#             min_vin = int(input('min vin(4500-14000):'))
#             max_vin = int(input('max vin(4500-14000):'))
#             Board.setBusServoVinLimit(servo_id, min_vin, max_vin)  
#         elif mode == 6:
#             servo_id = int(input('servo id:'))
#             max_temp = int(input('temperature(0-85):'))
#             Board.setBusServoMaxTemp(servo_id, max_temp)  
#         elif mode == 7:
#             servo_id = int(input('servo id:'))
#             status = int(input('status 0 or 1:'))
#             Board.unloadBusServo(servo_id, status) 
#         elif mode == 4:
#             print('''
# --------------------------
# 1 id                
# 2 dev               
# 3 save_dev          
# 4 help      
# 5 voltage_range   
# 6 temperature_warn
# 7 lock              
# 8 exit
# --------------------------''')
#         elif mode == 8:
#             break
#         else:
#             print('error mode')
#     except KeyboardInterrupt:
#         break
