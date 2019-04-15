import sys
import dlib
from skimage import io


#image path
file_name  = "/home/pythonist/Projects/facial_recognition/Detecting_faces/image.jpg"
Detector = dlib.get_frontal_face_detector()

#opning new wnidow and reading image
win = dlib.image_window()
image = io.imread(file_name)

#running HOG Detector it would give a list of faces in an image
faces = Detector(image, 1)

win.set_image(image)

for i, face_rect in enumerate(faces):


    #printing corrdinates
    print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))    
    win.add_overlay(face_rect)


dlib.hit_enter_to_continue()


