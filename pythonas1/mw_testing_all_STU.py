import os

# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model


# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img



# entry point, run the example
end = False

# load model

model = load_model('s235458.h8')   # <=== MODIFY TO YOUR MODEL FILE NAME **** #


correct=0;
wrong=0;
count=0;

#
# Test cases for MAN
#
basedir = 'testing/man' #CHANGE to your testing images for man. E.g. "testing/man"

for file in os.listdir(basedir):
    count+=1;
    img = load_image(os.path.join(basedir, file))   
    # predict the class
    result = model.predict(img)
    # check result
    if result > 0.5:
        wrong+=1
    else:
        correct+=1
    if (count % 50 == 0):
        print("Man: Images {}, Correct {}, Wrong {}".format(count, correct, wrong))

print("Man: Images {}, Correct {}, Wrong {}".format(count, correct, wrong))


#
# Test cases for WOMAN
#


basedir = 'testing/woman' #CHANGE to your testing images for man. E.g. "testing/woman"

correct=0;
wrong=0;
count=0;

for file in os.listdir(basedir):
    count+=1;
    img = load_image(os.path.join(basedir, file))   
    # predict the class
    result = model.predict(img)
    # check result
    if result <= 0.5:
        wrong+=1
    else:
        correct+=1
    if (count % 50 == 0):
        print("Woman: Images {}, Correct {}, Wrong {}".format(count, correct, wrong))
        
print("Woman: Images {}, Correct {}, Wrong {}".format(count, correct, wrong))
input("Press any key to exit from the program")