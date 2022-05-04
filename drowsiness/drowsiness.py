# Nessecary Libraries for drowsiness detection

from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import os


# To find Eye Aspect ratio


def eye_aspect_ratio(eye):
    # caluclating of euclidian Distance btween the points
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    C = dist.euclidean(eye[0], eye[3])

    E_A_R = (A + B) / (2.0 * C)

    return E_A_R
