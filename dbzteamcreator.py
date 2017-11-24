from wand.image import Image
from wand.display import display
from urllib2 import urlopen

def resizeImgToHeight(image, height):
  scale = float(height) / float(image.height)
  print(scale)
  print(image.width)
  image.resize(int(float(image.width) * float(scale)), height)

#goku-ss
#vegeta-ss
#trunks
#gohan-y
#freeza
#majinboo-z
#cell
#kuririn
#piccolo
#no16
#no18
#goku-ssgss
#vegeta-ssgss
#yamcha
#tenshinhan
#nappa
#ginyu
#gotenks
#gohan
#majinBoo

leftchar = "cell"
midchar = "freeza"
rightchar = "majinBoo"

bg_url = "http://dba.bn-ent.net/mode/images/bg_modeTtl.jpg"
left_url = "http://dba.bn-ent.net/character/images/" + leftchar + "/portrait.png"
mid_url = "http://dba.bn-ent.net/character/images/" + midchar + "/portrait.png"
right_url = "http://dba.bn-ent.net/character/images/" + rightchar + "/portrait.png"

character_distance_multiplier = 0.5
character_height_multiplier = 3

left_char_bigger = 0
mid_char_bigger = 0
right_char_bigger = 0


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
                print(img.size)
                print(left.size)

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
                display(img)
