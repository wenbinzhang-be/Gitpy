class washer():
    def __init__(self):
        self.width = 200
        self.highte = 800

    def print_info(self):
        print(f'洗衣机的宽为{self.width},\n洗衣机的高度为{self.highte}')


higher = washer()
higher.print_info()
