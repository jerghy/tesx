import requests

url = "https://cdn77.91p49.com//mp43/916318.mp4?st=d1b558944dc8b6eaacd2e7d193dadf3d"
filename = "video.mp4"

response = requests.get(url)

with open(filename, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

print("文件下载完成")
