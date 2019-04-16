# Facial recognition system

Usage:
Recently I was working on a project on `face recognition`(recognizing faces in videos and pictures), and it's going pretty good.

we can impliment technology in our institutes or in our workplaces and improves our secuirity, it is not that hard.We only need minimal effort its not that expensive and Tech is changing the world we should be part of it and contribute to it.

#### Problems are all around us just pick one and solve it. It is really that simple.

i will be using my images with some of my friends for testing purpose for the whole project.

### Buliding a  `facial recognition system` includes four steps   

1. look at a picture and find all the faces in it
2. Focus on each face and be able to understand that even if a face is turned in a weird direction or in bad lighting, it is still the same person.
3. Be able to pick out unique features of the face that you can use to tell it apart from other people— like how big the eyes are, how long the face is, etc.
4. Finally, compare the unique features of that face to all the people you already know to determine the person’s name.


I will be solving each problem/step one by one with proper discription.

### Step 1: Face Detection.
 Method:  Histogram of Oriented Gradients  HOG
 
 Requirements:
 * [dlib](http://dlib.net/)
 * scikit-image
 
 Code: 
 * [Face_Detection](https://github.com/Zeeshanahmad4/face_recognition_using_openface_dlib/blob/master/face_detection.py)
 
 Result: Faces and there cordinates in the image.
 
<img src="https://github.com/Zeeshanahmad4/face_recognition_using_openface_dlib/blob/master/Resources/image.jpg" height="340" width="500">

### Step 2: Face landmarking and Projection

 Method:  face landmark estimation.
 
 Requirements:
 * [dlib](http://dlib.net/)
 * scikit-image
 * cv2
 * openface
 
  Code: 
 * [Face_Detection](https://github.com/Zeeshanahmad4/face_recognition_using_openface_dlib/blob/master/face_detection.py)
 
 Result: Faces and there cordinates in the image.
 
<img src="https://github.com/Zeeshanahmad4/face_recognition_using_openface_dlib/blob/master/Resources/image.jpg" height="340" width="500">
 
### Step 3: Encoding our face image

 Method:  Deep Convolutional Neural Network to generate 128 measurements for each face.
 
 Requirements:
 * openface
 
  Code: 
 * [Openface](https://github.com/cmusatyalab/openface/blob/master/batch-represent/batch-represent.lua)
 i am directly using  trained networks by OpenFace to Encode images, becuase it has to trained only once so trained    again would be a waste of time. 
 
Result:

<img src="https://github.com/Zeeshanahmad4/face_recognition_using_openface_dlib/blob/master/Resources/1_6kMMqLt4UBCrN7HtqNHMKw.png" height="340" width="500">
  
 
  ### Step 4: Final step

 Method:   linear SVM classifier.
 
 Requirements:
 * scikit learn
 
  Code: 
 * [Openface](https://github.com/cmusatyalab/openface/blob/master/batch-represent/batch-represent.lua)
 i am directly using  trained networks by OpenFace to Encode images, becuase it has to trained only once so trained    again would be a waste of time. 
 
Result:

Input
<img>src="https://github.com/Zeeshanahmad4/face_recognition_using_openface_dlib/blob/master/Resources/asad.jpg"height="340"width="500"><img>src="https://github.com/Zeeshanahmad4/face_recognition_using_openface_dlib/blob/master/Resources/hamza.jpg"height="340"width="500"><img>src="https://github.com/Zeeshanahmad4/face_recognition_using_openface_dlib/blob/master/Resources/zeeshan.jpg" height="340" width="500">
  
 
 
 
 
 
 














