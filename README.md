# aiot-manager-python

Advantech AIOT 정화조25팀 메인 프로그램 입니다.

1. WISE-4012 간 Modbus 활용한 센서 데이터 수신 및 DataHub 업로드
2. LSTM Model 활용하여 모터 등 효율적 제어
3. 메인 프로그램 외 Modbus/Serial 모니터 제공

## 설치

본 프로젝트는 Python 3.8 이상에서 정상 작동합니다.
Dependency 설치를 위해 아래를 입력하세요.

    pip install -r requirements.txt

tensorflow 설치 시 문제가 있는 경우 아래를 먼저 실행해주세요

    pip install --upgrade pip
    pip install --upgrade setuptools

## 실행

모니터 실행을 원하시면 monitor 디렉터리 밑의 파이썬 파일을 실행하시면 됩니다.

    python modbusmonitor.py
    python serialmonitor.py

메인 프로그램 실행은 최상위 디렉터리의 main.py 파일을 실행하시면 됩니다.
