from PIL import Image
import numpy as np

def get_img(img_name):
    img = Image.open("images/greyscale/"+img_name)
    return img

def get_array(img):
    arr = np.array(img)[:,:,0]
    return arr

# img = get_img("vermeil.png")
# arr = get_array(img)
# arr[500:600,500:600] = 256


# new_img = Image.fromarray(arr)
# new_arr = np.array(new_img)
# print(new_arr[500:600,500:600]) 
# new_img.show()

