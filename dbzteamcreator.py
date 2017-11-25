import sys
from wand.image import Image
from wand.display import display
from urllib2 import urlopen

def resizeImgToHeight(image, height):
  scale = float(height) / float(image.height)
  image.resize(int(float(image.width) * float(scale)), height)

name_array = ["goku-SS", "vegeta-SS", "trunks", "gohan-y", "freeza", "majinBoo-z", "cell", "kuririn", "piccolo", "no16", "no18", "goku-SSGSS", "vegeta-SSGSS", "yamcha", "tenshinhan", "nappa", "ginyu", "gotenks", "gohan", "majinBoo"]        
input_char_left = 1
input_char_mid = 1
input_char_right = 1

input_char_left = int(sys.argv[1])
input_char_mid = int(sys.argv[2])
input_char_right = int(sys.argv[3])

leftchar = name_array[input_char_left]
midchar = name_array[input_char_mid]
rightchar = name_array[input_char_right]

bg_url = "http://dba.bn-ent.net/mode/images/bg_modeTtl.jpg"
left_url = "http://dba.bn-ent.net/character/images/" + leftchar + "/portrait.png"
mid_url = "http://dba.bn-ent.net/character/images/" + midchar + "/portrait.png"
right_url = "http://dba.bn-ent.net/character/images/" + rightchar + "/portrait.png"

character_distance_multiplier = 0.5
character_height_multiplier = 3

character_distance_multiplier = float(sys.argv[4])
character_height_multiplier = float(sys.argv[5])

left_char_bigger = 0
mid_char_bigger = 0
right_char_bigger = 0


mid_char_bigger = int(float(sys.argv[6]))


with Image(filename=bg_url) as img:
    character_height = int(img.height * character_height_multiplier)
    with Image(filename=mid_url) as mid:
        if mid_char_bigger == 1:
          resizeImgToHeight(mid, int(character_height * 1.2))
        else:
          resizeImgToHeight(mid, character_height)
        with Image(filename=left_url) as left:
            resizeImgToHeight(left, character_height)
            with Image(filename=right_url) as right:
                resizeImgToHeight(right, character_height)
                with Image(filename="http://i.imgur.com/QvZ9Ce0.png") as watermark:

                    #print(img.size)
                    #print(left.size)
    
                    leftpos = int(img.width/2 - mid.width/2 - left.width * character_distance_multiplier)
                    rightpos = int(img.width/2 + mid.width/2 - right.width * (1-character_distance_multiplier))
                    midpos = int(img.width/2 - mid.width/2)
    
                    img.gaussian_blur(4, 4)
    
                    img.composite(left, left=leftpos, top=0)
                    img.composite(right, left=rightpos, top=0)
                    if mid_char_bigger:
                      img.composite(mid, left=midpos, top=0)
                    else:
                      img.composite(mid, left=midpos, top=0)

                    targetWidth = 1500
    
                    img.crop(img.width/2 - targetWidth/2, 0, width=targetWidth, height=img.height)
                    #img.crop(leftpos, 0, width=rightpos + right.width/2 - (leftpos - left.width/2), height=img.height)
                    #resizeImgToHeight(watermark, 3)
                    img.composite(watermark, left = img.width - watermark.width - 10, top = img.height - watermark.height)
                    
                    print(img.size)
                    img.save(filename="./output/request-" + leftchar + "-" + midchar + "-" + rightchar + ".png")
                    #display(img)
