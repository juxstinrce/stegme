from PIL import Image
import random
import sys

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])


imageOriginale = Image.open('image.png')
pixelOriginal = imageOriginale.load()
longueur = imageOriginale.size[0]
largeur = imageOriginale.size[1]

imageStega = Image.open('image.png')
pixelStega = imageStega.load()

solved = False


flag = ''
flag2 = ''
flag3 = ''

key = ['2x0', '42x40', '28x40', '23x42', '30x15', '31x31', '42x42', '1x35', '49x25', '41x11', '3x24', '16x42', '9x19', '23x0', '41x16', '43x13', '25x31', '2x5', '35x0', '32x36', '31x6', '8x23', '17x21', '26x11', '16x6', '43x38', '7x29', '3x32', '36x21', '0x8', '16x43', '18x20', '26x3', '36x19', '2x13', '1x47', '0x40', '24x32', '20x47', '7x47', '22x0', '33x25', '22x15', '33x34', '0x20', '9x4', '7x39', '16x27', '17x36', '27x13', '11x30', '29x41', '43x49', '38x39', '24x13', '18x34', '20x45', '28x38', '0x45', '48x14', '15x41', '44x26', '49x42', '47x44', '43x42', '37x47', '11x9', '31x29', '12x26', '31x40', '23x23', '33x33', '26x17', '34x26', '42x2', '12x12', '12x0', '38x0', '34x23', '15x44']

for pixels in key:
	iLongueur = int(pixels.split("x")[0])
	iLargeur = int(pixels.split("x")[1])
	print("Reading pixel ", iLongueur, "x", iLargeur)
	if pixelOriginal[iLongueur, iLargeur] != pixelStega[iLongueur, iLargeur]:
		if pixelOriginal[iLongueur, iLargeur][0] != pixelStega[iLongueur, iLargeur][0]: # R
			print("R has been modified.")
			print("Original was : " + str(pixelOriginal[iLongueur, iLargeur][0]) + " modified is : " + str(pixelStega[iLongueur, iLargeur][0]) + "\n")
			if (pixelOriginal[iLongueur, iLargeur][0] - pixelStega[iLongueur, iLargeur][0]) == 1:
				flag+='0'
				flag2+='0'
				flag3+='0'
			elif (pixelOriginal[iLongueur, iLargeur][0] - pixelStega[iLongueur, iLargeur][0]) == -1:
				flag+='1'
				flag2+='1'
				flag3+='1'
		elif pixelOriginal[iLongueur, iLargeur][1] != pixelStega[iLongueur, iLargeur][1]: # G
			print("G has been modified.")
			print("Original was : " + str(pixelOriginal[iLongueur, iLargeur][1]) + " modified is : " + str(pixelStega[iLongueur, iLargeur][1]) + "\n")
			if (pixelOriginal[iLongueur, iLargeur][1] - pixelStega[iLongueur, iLargeur][1]) == 1:
				flag+='0'
				flag2+='0'
				flag3+='0'
			elif (pixelOriginal[iLongueur, iLargeur][1] - pixelStega[iLongueur, iLargeur][1]) == -1:
				flag+='1'
				flag2+='1'
				flag3+='1'
		elif pixelOriginal[iLongueur, iLargeur][2] != pixelStega[iLongueur, iLargeur][2]: # B
			print("B has been modified.")
			print("Original was : " + str(pixelOriginal[iLongueur, iLargeur][2]) + " modified is : " + str(pixelStega[iLongueur, iLargeur][2]) + "\n")
			if (pixelOriginal[iLongueur, iLargeur][2] - pixelStega[iLongueur, iLargeur][2]) == 1:
				flag+='0'
				flag2+='0'
				flag3+='0'
			elif (pixelOriginal[iLongueur, iLargeur][2] - pixelStega[iLongueur, iLargeur][2]) == -1:
				flag+='1'
				flag2+='1'
				flag3+='1'
		else:
			print("wtf")
			sys.exit(0)
	else:
		flag2+='1'
		flag3+='0'

print("There are 3 potentiel hidden datas : ")
print("[*] " + flag)
print("[*] " + flag2)
print("[*] " + flag3)