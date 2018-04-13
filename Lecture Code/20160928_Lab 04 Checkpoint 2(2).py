from PIL import Image
def make_square (n):
    im = min(n.size[0],n.size[1])
    new = n.crop((0,0,im,im))
    return new