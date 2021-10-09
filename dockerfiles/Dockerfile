FROM python:3.9.6-slim-buster

# Definition of a Device & Service
ENV POSITION=FaceDetection \
    SERVICE=face-detection-from-directory \
    AION_HOME=/var/lib/aion

RUN mkdir ${AION_HOME}
WORKDIR ${AION_HOME}
# Setup Directoties
RUN mkdir -p \
    $POSITION/$SERVICE
WORKDIR ${AION_HOME}/$POSITION/$SERVICE/

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    libglib2.0 \
    libgl1 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY . .
# COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python3", "-u", "main.py"]
