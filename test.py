import sys
import time
import hiwonder.Board as Board
import hiwonder.ActionGroupControl as AGC


AGC.runActionGroup('stand')
AGC.runActionGroup('right_move')
Board.setPWMServoPulse(1, 1100, 100)
Board.setPWMServoPulse(2, 1100, 100)
Board.setBusServoPulse(3, 500, 200)


