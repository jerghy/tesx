import requests
import time

# 指定下载的URL
url = "https://desktop.figma.com/win/FigmaSetup.exe"
# 设定要保存的文件名
filename = "video.mp4"

# 发起请求获取内容
with requests.get(url, stream=True) as response:
    response.raise_for_status()  # 如果请求遇到问题则抛出异常
    total_length = int(response.headers.get('content-length'))  # 获取文件总大小
    # 打开文件进行写入
    with open(filename, 'wb') as file:
        downloaded = 0
        start_time = time.time()
        for chunk in response.iter_content(chunk_size=8192):  # 按块读取内容
            duration = time.time() - start_time
            if duration >= 1:  # 每过一秒输出进度
                percent = (downloaded / total_length) * 100  # 计算下载百分比
                print(f"下载进度：{downloaded} / {total_length} ({percent:.2f}%)")
                start_time = time.time()  # 重置开始时间
            file.write(chunk)
            downloaded += len(chunk)

print(f"文件已下载并保存为 {filename}")
