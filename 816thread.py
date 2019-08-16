import time, threading
def threadFunction():
    while True:
        print(11111)
        time.sleep(10)


def maudio(self):
    path = r'C:\Users\15845\Pictures\intel\audio\music\sample-files\16k.wav'
    from audio import SpeechRecognition
    self.tt.append ( SpeechRecognition.test ( path ) )
    result = SpeechRecognition.test ( path )
    return result


# 用于命名，可以通过threading.current_thread().name获得
t = threading.Thread(target=threadFunction, name='funciton')
# 如果线程有参数
t = threading.Thread(target=threadFunction, args=(), name='funciton')
t.start()