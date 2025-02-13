import time

def clear(line_length):
    print(' ' * line_length, end='\r')
    print('\r', end='')

def main():
    while True:
        input("给DeepSleep发送消息: ")

        message = "思考中..."
        print(message, end='', flush=True)

        time.sleep(10)

        clear(len(message))
        print("服务器繁忙，请稍后再试。")
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDeepSleep已终止")