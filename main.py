import requests

url = "https://desktop.figma.com/win/FigmaSetup.exe"
filename = "video.mp4"

response = requests.get(url)

with open(filename, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

print("文件下载完成")
