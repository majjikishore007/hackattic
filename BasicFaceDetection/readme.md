# problem statemnt 

Given a grid of images 
- That is of 8 X 8 matrix  (800px X 800px)

To return 
- the indexes of all the faces in the grid 

Approach
(lagugage used python)
1. Get the image url and load the image using `requests`
2. The idea is to crop the grid and scan individual iamge using `openCV`
3. If the image contains a face then add the row and col to the result list

4. To crop the iamge and get individual tile , I have defined a tile wth `(100px X 100px) width and height ` as the hole grid is `(800px X 800px)` in size 

5. Now the next step is to loop through the entire list and check for each tile and add to the result if iamge is detected 

## The iamge detection logic is in the code and done using openCV 