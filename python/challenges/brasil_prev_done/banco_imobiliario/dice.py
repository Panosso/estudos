from random import choice


def dice_face():
    faces = [x for x in range(1, 7)]

    face = choice(faces)

    return face
