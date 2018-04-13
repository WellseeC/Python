from PIL import Image
fn1 = '1.jpg'
fn2 = '2.jpg'
fn3 = '3.jpg'
fn4 = '4.jpg'
fn5 = '5.jpg'
fn6 = '6.jpg'
im1 = Image.open(fn1)
im2 = Image.open(fn2)
im3 = Image.open(fn3)
im4 = Image.open(fn4)
im5 = Image.open(fn5)
im6 = Image.open(fn6)
im1 = im1.resize((148,256))
im2 = im2.resize((148,256))
im3 = im3.resize((148,256))
im4 = im4.resize((148,256))
im5 = im5.resize((148,256))
im6 = im6.resize((148,256))
im = Image.new('RGB',(1000,360),'white')
im.paste(im1,(31,20))
im.paste(im2,(189,60))
im.paste(im3,(347,20))
im.paste(im4,(505,60))
im.paste(im5,(663,20))
im.paste(im6,(821,60))
im.show()