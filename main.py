import face_recognition as fr
import cv2
import numpy as np
import os

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# camera setup
# [CAMERA_PORT, X_RESOLUTION, Y_RESOLUTION, VIDEO_FPS] = [1, 1920, 1080, 60]
[CAMERA_PORT, X_RESOLUTION, Y_RESOLUTION, VIDEO_FPS] = [0, 1280, 720, 60]
cap = cv2.VideoCapture(CAMERA_PORT)
cap.set(3, X_RESOLUTION)
cap.set(4, Y_RESOLUTION)
cap.set(5, VIDEO_FPS)

# automatically loads the images in the known_faces folder
known_face_encodings = []
known_face_names = []
path = os.path.join(os.path.dirname(__file__), "known_faces")
facelist = os.listdir(path)

for name in facelist:
    if name[0] == ".":  # skip hidden files
        continue
    known_face_encodings.append(
        fr.face_encodings(fr.load_image_file("./known_faces/" + name))[0])
    # remove the file extension from the name
    name = name.split(".")[0]
    # handle duplicate names for people with more than 1 sample image
    if len(name.split()) > 1:
        known_face_names.append(name.split()[0])
    else:
        known_face_names.append(name)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which fr uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = fr.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = fr.face_distance(known_face_encodings,
                                              face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        boxColor = (255, 128, 0)  #BGR format

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), boxColor, 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), boxColor,
                      cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0,
                    (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video Feed', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
cap.release()
cv2.destroyAllWindows()