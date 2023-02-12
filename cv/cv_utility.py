import face_recognition as fr
import pickle
import os

known_face_encodings = []
known_face_names = []
path = os.path.join(os.path.dirname(__file__), "known_faces")
facelist = os.listdir(path)


def train_faces():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Encoding known faces.....')
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Done encoding known faces.....')


def save_known_faces():
    with open("known_faces.dat", "wb") as face_data_file:
        face_data = [known_face_encodings, known_face_names]
        pickle.dump(face_data, face_data_file)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Known faces backed up to disk.")


if __name__ == "__main__":
    train_faces()
    save_known_faces()