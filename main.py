#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import os
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import time

import webSocketHandler as ws
from faceDetect import FaceDetect

def _send_message(socket, data):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(socket.write_message(data))
    except:
        print("failed to send")
    finally:
        loop.close()
        asyncio.set_event_loop(None)

def send_message(data):
    for client in ws.get_client():
        t = Thread(target=_send_message, args=[client, data])
        t.daemon = True
        t.start()
        t.join()


def face_detect_and_send_message_run(filepath: str, interval: int):
    fd = FaceDetect(filepath)

    while True:
        # face detection
        # check detect result
        if fd.check_face():
            send_message("detected!\n")
            
            print("Face detected")
        else:
            print("Face not detected")

        time.sleep(interval)


def main():
    print("start")

    ws.make_handler()
    print("maked websocket handler")

    dir = os.environ.get("OBSERVATION_DIR", r"/var/lib/aion/Data/analyze")
    file = os.environ.get("OBSERVATION_FILE", r"standbyImageForFaceDetection.jpg")
    filepath = os.path.join(dir, file)

    try:
        interval = int(os.environ.get("DETECT_INTERVAL"))
    except:
        interval = 5

    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(face_detect_and_send_message_run, filepath, interval)
    print("thread exec face_detect_and_send_message_run")

    ws.websocket_run()



if __name__ == "__main__":
    main()
