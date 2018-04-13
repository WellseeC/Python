from check2_helper import make_square
from PIL import Image
fn1 = 'ca.jpg'
fn2 = '2.jpg'
fn3 = '3.jpg'
fn4 = '4.jpg'
im1 = Image.open(fn1)
im2 = Image.open(fn2)
im3 = Image.open(fn3)
im4 = Image.open(fn4)
im1 = make_square(im1)
im2 = make_square(im2)
im3 = make_square(im3)
im4 = make_square(im4)
im1 = im1.resize((256,256))
im2 = im2.resize((256,256))
im3 = im3.resize((256,256))
im4 = im4.resize((256,256))
x = 512
im = Image.new('RGB',(x,x),'white')
im.paste(im1,(0,0))
im.paste(im2,(0,int(x/2)))
im.paste(im3,(int(x/2),0))
im.paste(im4,(int(x/2),int(x/2)))

im.show()