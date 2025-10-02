import time
import random

def clear(line_length):
    print(' ' * line_length, end='\r')
    print('\r', end='')

def loading():
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    print("正在加载 DeepSleep-R1:latest...", end='', flush=True)
    
    for i in range(15):
        print(f"\r{frames[i % len(frames)]} 正在加载 DeepSleep-R1:latest......", end='', flush=True)
        i=i+1
        time.sleep(0.2)
    
    print("\r✅ 加载完成 DeepSleep-R1:latest")
    time.sleep(1)
    print("🎉 模型加载完成！")
    time.sleep(1)

def main():
        print("\n" + "="*50)
        print("DeepSleep-R1 启动完成！")
        print("输入 /bye 退出对话")
        print("="*50)
        while True:
            user_input = input("\n给DeepSleep发送消息: ").strip()

            if user_input == "/bye":
                print("\nBye~")
                time.sleep(2)
                break

            message = "思考中..."
            print(message, end='', flush=True)

            wait_time = random.randint(3, 8)
            time.sleep(wait_time)

            clear(len(message))
            print("服务器繁忙，请稍后再试。")
            time.sleep(2)

if __name__ == "__main__":
    try:
        loading()
        main()
    except KeyboardInterrupt:
        print("\nDeepSleep意外终止")