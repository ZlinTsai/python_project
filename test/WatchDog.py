import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):
    # 文件移动
    def on_moved(self, event):
        print("文件移动触发")
        print(event)

    def on_created(self, event):
        print("文件创建触发")
        print(event)

    def on_deleted(self, event):
        print("文件删除触发")
        print(event)

    def on_modified(self, event):
        print("文件编辑触发")
        print(event)


if __name__ == '__main__':

    observer = Observer()  # 创建观察者对象
    file_handler = MyEventHandler()  # 创建事件处理对象
    observer.schedule(file_handler, "./misc", recursive=False)  # 向观察者对象绑定事件和目录
    observer.start() # 启动
    print("Start watchdog.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("\nExit watchdog.")