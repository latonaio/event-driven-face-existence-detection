# event-driven-face-existence-detection   
何らかのイベントをトリガーとして、入力された画像における顔の存在を検知するマイクロサービスです。   

### Clone and Build
```
$ git clone git@bitbucket.org:latonaio/event-driven-face-existence-detection.git
$ cd /path/to/event-driven-face-existence-detection
$ make docker-build
```

### Edit Environment K8s Resource
```
          env:
            - name: PORT
              value: "8888"
            - name: OBSERVATION_DIR
              value: "/var/lib/aion/Data/analyze"
            - name: OBSERVATION_FILE
              value: "standbyImageForFaceDetection.jpg"
            - name: DETECT_INTERVAL
              value: "5"
            - name: TZ
              value: Asia/Tokyo
```

### How to Use ###

* Access `ws://event-driven-face-existence-detection:8888/websocket` (Only access internal k8s cluster network.)
* Cliant receive　the message like
```json
{
  "0": {"status": true, "type": "human", "x": 92, "y": 136, "w": 276, "h": 276},
  "1": {"status": true, "type": "human", "x": 10, "y": 111, "w": 250, "h": 246}
}
```
paramator
* 0 : detection number.
* status : detected result.
* type : detected object type. (now only human)
* x, y, w, h : detected object postion and size.