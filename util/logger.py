import logging
from datetime import datetime
import os
import sys

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

class Logger(object) :
    _LOGGER = None

    @staticmethod
    def create_logger() :
        #루트 로거 생성
        Logger._LOGGER = logging.getLogger()
        Logger._LOGGER.setLevel(logging.INFO)
        #log 폴더 없을 시 생성
        if (os.path.exists('./log') == False) :
            os.makedirs('./log')
        #로그 포맷 생성
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s-%(funcName)s:%(lineno)s] >> %(message)s')
        #핸들러 생성
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        file_handler = logging.FileHandler('./log/' + datetime.now().strftime('%Y%m') +'.log')
        file_handler.setFormatter(formatter)
        Logger._LOGGER.addHandler(stream_handler)
        Logger._LOGGER.addHandler(file_handler)
    @classmethod
    def get_logger(cls) :
        return cls._LOGGER

def log(str, level=INFO):
    name = sys._getframe(1).f_code.co_filename.split("/")[-1]
    log_text = f"[{name}] {str}"
    Logger._LOGGER.log(level=level, msg=log_text)