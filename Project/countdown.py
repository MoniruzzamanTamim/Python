import time

class coundown:
    def __init__(self, time):
        self.time = time
        
    def start(self):
        while self.time:
            minute,second = divmod(self.time,60)
            result = f"{minute}: {second}"
            print(result , end='\r')
            time.sleep(1)
            self.time -=1
    def stop(self):
        self.time = 0

user_input = int(input("Coundown Second: "))
user = coundown(user_input)
user.start()

