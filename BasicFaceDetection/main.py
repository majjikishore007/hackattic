import requests
import cv2
import numpy as np

BASE_URL='https://hackattic.com/challenges'
KEY='ab17bddaef9e90e4'

def get_data():
    res=requests.get(f'{BASE_URL}/basic_face_detection/problem?access_token={KEY}')
    return res.json()
def post_data(facelist):
    data={"face_tiles":facelist}
    
    res=requests.post(f'{BASE_URL}/basic_face_detection/solve?access_token={KEY}',json=data)
    return res.text
    
def load_iamge(image_url):
    response = requests.get(image_url)
    # Check that the request was successful
    if response.status_code == 200:
        # Save the image data to a file
        with open("image.jpg", "wb") as f:
            f.write(response.content)

if __name__=='__main__':
    data=get_data()
    print("data::::",data)
    load_iamge(data['image_url'])
    
    
    tile_size=(100,100)
    
    # reading the image using numpy
    image = cv2.imread("image.jpg")
   
    
    # detection model 
    haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
    face_tiles = []
    for row in range(8):
        for col in range(8):
            x1 = col * tile_size[0]
            y1 = row * tile_size[1]
            x2 = x1 + tile_size[0]
            y2 = y1 + tile_size[1]
            
            tile = image[y1:y2, x1:x2]
          
            faces = haar_cascade_face.detectMultiScale(tile, scaleFactor=1.2, minNeighbors=5)
            
            if len(faces)>0:
                face_tiles.append([row,col])
                
    print("faces:::::::::::::",face_tiles)
    res=post_data(face_tiles)
    print("result",res)