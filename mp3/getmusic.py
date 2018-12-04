2# -*- coding: utf-8 -*-
import time
import pygame
import os,sys



print (os.path.abspath('./music'))

file= (os.listdir('./music'))
# b = len(a)
# print (type(b))
# for c in file:
#     print("序号：%s   值：%s" % (list.index(c) + 1, c))
#
lu = os.path.abspath('./music')
###加r换成普通的字符串
num =0
playfile = lu + "\\" + file[num]
print (playfile)
pygame.mixer.init()
print("播放音乐1")
pygame.mixer.music.load(playfile)
pygame.mixer.music.play()
time.sleep(6)
num =1
playfile = lu + "\\" + file[num]
pygame.mixer.music.load(playfile)
pygame.mixer.music.play()
time.sleep(44)
