import sys
import time
import hiwonder.Board as Board
import hiwonder.ActionGroupControl as AGC


AGC.runActionGroup('stand')
AGC.runActionGroup('right_move')
Board.setPWMServoPulse(1, 2000, 500)
time.sleep(0.5)
Board.setPWMServoPulse(1, 1500, 0)
time.sleep(1)
Board.setPWMServoPulse(2, 2000, 1000)
time.sleep(1)


if __name__ == '__main__':
    main()

