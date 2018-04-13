from PIL import Image
fn1 = 'ca.jpg'
fn2 = 'im.jpg'
fn3 = 'hk.jpg'
fn4 = 'bw.jpg'
im1 = Image.open(fn1)
im2 = Image.open(fn2)
im3 = Image.open(fn3)
im4 = Image.open(fn4)
x = 512
im = Image.new('RGB',(x,x),'white')
im1 = im1.resize((int(x/2),int(x/2)))
im2 = im2.resize((int(x/2),int(x/2)))
im3 = im3.resize((int(x/2),int(x/2)))
im4 = im4.resize((int(x/2),int(x/2)))
im.paste(im1,(0,0))
im.paste(im2,(0,int(x/2)))
im.paste(im3,(int(x/2),0))
im.paste(im4,(int(x/2),int(x/2)))
im.show()