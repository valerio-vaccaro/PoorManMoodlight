from pyfirmata import Arduino, util
import ImageGrab
import Image
import time

board = Arduino('COM3')

blue = board.get_pin('d:9:p')
green = board.get_pin('d:10:p')
red = board.get_pin('d:11:p')
while (True):
	im = ImageGrab.grab()
	im.resize((5,5), Image.NEAREST)
	pix = im.load()
	(r,g,b) = pix[2,2]

	red.write(r/255.0)
	green.write(g/255.0)
	blue.write(b/255.0)
	time.sleep(1)

