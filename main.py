import requests

# 指定下载的URL
url = "https://desktop.figma.com/win/FigmaSetup.exe"
# 设定要保存的文件名
filename = "video.mp4"

# 发起请求获取内容
response = requests.get(url)

# 确保请求成功
if response.status_code == 200:
    # 打开文件进行写入
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"文件已下载并保存为 {filename}")
else:
    print("下载失败，状态码：", response.status_code)
