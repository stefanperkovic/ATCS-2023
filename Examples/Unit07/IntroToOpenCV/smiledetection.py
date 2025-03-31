"""
A program to detect faces and smiles in 
pictures and videos. 

@author: Nandhini Namasivayam
@version: March 2024

Adopted from GeeksforGeeks
"""
import cv2
from matplotlib import pyplot as plt

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def image_smile_detection(image=None, filepath=None, display=False):
    """
    Detects smiles in still images.
    Can take in an image or a filepath. By default, 
    does not display the image.
    Args:
        image (Image, optional): The image to identify smiles in. Defaults to None.
        filepath (String, optional): The filepath to the image. Defaults to None.
        display (bool, optional): If True, displays the image after detecting smiles. Defaults to False.

    Returns:
        Image: The RGB version of the image
    """
    # Load pre-trained classifiers
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    # Load the image
    if filepath != None:
        image = cv2.imread(filepath)
    
    # Change BRG image to Grayscale and RGB
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Find the face in the image
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minSize=(100,100))

    # Loop through each face
    for (start_x, start_y, width, height) in faces:
        end_x = start_x + width
        end_y = start_y + height

        # Draw a red rectangle around each face
        cv2.rectangle(img_rgb, (start_x, start_y), (end_x, end_y), RED, 2)

        # Section out the faces to find smiles
        section_gray = img_gray[start_y:end_y, start_x:end_x]
        section_rgb = img_rgb[start_y:end_y, start_x:end_x]

        smiles = smile_cascade.detectMultiScale(section_gray, minNeighbors=20)
    
        # Loop through and draw a blue rectangle around each smile
        for (sx, sy, w, h) in smiles:
            ex = sx + w
            ey = sy+ h

            # Draw a red rectangle around each smiler
            cv2.rectangle(section_rgb, (sx, sy), (ex, ey), BLUE, 2)


    # Display our images
    if display:
        plt.subplot(1, 1, 1)
        plt.imshow(img_rgb)
        plt.show()

    return img_rgb

def video_smile_detection():
    # Open factime camera for video input
    video = cv2.VideoCapture(0)

    # Loop until the end of the video
    while (video.isOpened()):
        # Read individual frames
        frame = video.read()[1]

        # Identify the faces and smiles in the image
        image = image_smile_detection(image=frame)
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Displaty the resultung frame
        cv2.imshow('Smiles', img_rgb)

        # Define q as the exit button
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    # Close our video stream
    video.release()
    cv2.destroyAllWindows()


    pass

def draw_box_on_head():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    box_height = 200
    # Open factime camera for video input
    video = cv2.VideoCapture(0)
    
    
    # Loop until the end of the video
    while (video.isOpened()):
        # Read individual frames
        frame = video.read()[1]

        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Identify the faces and smiles in the image
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minSize=(100,100))

        # Loop through each face
        for (start_x, start_y, width, height) in faces:
            end_x = start_x + width
            end_y = start_y + height

            # Draw a red rectangle above each face
            cv2.rectangle(img_rgb, (start_x, start_y), (end_x, start_y - box_height), BLUE, 2)


            # Section out the faces to find smiles
            section_gray = img_gray[start_y:end_y, start_x:end_x]
            section_rgb = img_rgb[start_y:end_y, start_x:end_x]

            smiles = smile_cascade.detectMultiScale(section_gray, minNeighbors=20)
        
            rectangle = False
            # Loop through and draw a blue rectangle around each smile
            for (sx, sy, w, h) in smiles:
                ex = sx + w
                ey = sy+ h

                # Draw a red rectangle around each smile
                cv2.rectangle(section_rgb, (sx, sy), (ex, ey), BLUE, 2)

                rectangle = True
            
            if rectangle == True:
                cv2.imshow("Box Hat", cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))  

        

        # Define q as the exit button
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    # Close our video stream
    video.release()
    cv2.destroyAllWindows()
    pass


def cowboy_hat_overlay():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the overlay image with an alpha channel (transparency)
    cowboy_hat = cv2.imread('data/cowboyhat.png', -1)

    # Capture video from the webcam
    video = cv2.VideoCapture(0)

    while video.isOpened():
        frame = video.read()[1]

        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Identify the faces and smiles in the image
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minSize=(100,100))

        # Loop through each face
        for (start_x, start_y, width, height) in faces:
            end_x = start_x + width
            end_y = start_y + height

            start_y -= 200
            
            # Code to get a cowboy hat on the screen
            y1, y2 = start_y, start_y + cowboy_hat.shape[0]
            x1, x2 = start_x, start_x + cowboy_hat.shape[1]

            alpha = cowboy_hat[:, :, 3] / 255.0

            cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), BLUE, 2)


            

            for c in range(0, 3):
                frame[y1:y2, x1:x2, c] = (alpha * cowboy_hat[:, :, c] +
                                        (1.0 - alpha) * frame[y1:y2, x1:x2, c])
            
            # Display the resulting frame
            cv2.imshow('Cowboy Hat', frame)
            
        # Break the loop when 'q' is pressed
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    # Release the capture
    video.release()
    cv2.destroyAllWindows()

    pass

if __name__ == "__main__":
    # image_smile_detection(filepath="data/smiles.jpeg", display=True)
    #video_smile_detection()
    #draw_box_on_head()
    cowboy_hat_overlay()
    pass