import threading, time

class Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    # def flash(self, flag, display, obj, locatio):
    #     while flag:
    #         display.blit(obj, location)

    def flash(self):
        for i in range (0, 10):
            print i
            time.sleep(2)
