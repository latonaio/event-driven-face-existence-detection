#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ローカルでのテスト
# apt-get update
# apt-get install libgl1

import os
import traceback
import time

import cv2

HERE = os.path.dirname(__file__)
CASC_PATH = os.path.join(HERE, "haarcascade_frontalface_alt.xml")

face_cascade = cv2.CascadeClassifier(CASC_PATH)


class FaceDetect():
    def __init__(self, filepath):
        self.filepath = filepath

    def check_face(self):
        try:
            if not os.path.isfile(self.filepath):
                print('file not found')
                return False

            src = cv2.imread(self.filepath)
            src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(src_gray)

            print(faces)
            if len(faces):
                return True

            return False

        except Exception:
            traceback.print_exc()
            return False


def test():
    DIRECTORY = os.path.join(HERE, "test")
    INTERVAL = 5

    while True:
        filenames = os.listdir(DIRECTORY)
        filename = None
        for name in filenames:
            if os.path.splitext(name)[1].lower() in {'.jpg', '.png'}:
                filename = name
                break
        if filename is None:
            print('Error: file not found!')
            time.sleep(INTERVAL)
            continue

        filepath = os.path.join(DIRECTORY, filename)
        print(filepath)

        fd = FaceDetect(filepath)
        print(fd.check_face())
        time.sleep(INTERVAL)


if __name__ == "__main__":
    test()
