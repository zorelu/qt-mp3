import time
import pygame
import os,sys
import time
import pygame
import os,sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from MP3UI import Ui_Dialog

#获取当前文件夹所有文件
filenum= (os.listdir('./music'))
# print (len(filenum))
#获取放置音乐的文件夹
file = (os.listdir('./music'))
lu = os.path.abspath('./music')

num = 0

#音乐播放代码
class play:
	def player(num):
		playfile = lu + "\\" + file[num]
		pygame.mixer.init()
		pygame.mixer.music.load(playfile)
		pygame.mixer.music.play()
		#只播放3秒
		time.sleep(3)
		pygame.mixer.music.stop()
# play.player(num=1)
#定义按钮功能代码
class MainWindow(QMainWindow ):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
#播放按钮
	def Playmu(self):
		global num
		play.player(num)


#上一首按钮
	def Umu(self):
		global num
		num -= 1
		while num > 0:
			play.player(num)
			print("now play")
			break
		else:
			num =0
			print("first music")
			play.player(num)

#下一首按钮
	def Dmu(self):
		global num
		num += 1
		while num > len(filenum) - 1:
			num = len(filenum) - 1
			play.player(num)
			print("now play")
			break
		else:
			print(num)
			play.player(num)



if __name__=="__main__":
	app = QApplication(sys.argv)  
	win = MainWindow()  
	win.show()  
	sys.exit(app.exec_())  
