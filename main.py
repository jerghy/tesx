import requests

url = "https://cdn77.91p49.com//mp43/906460.mp4?st=81bc6e4ea4e13bc7345b15ca204c5e41"
filename = "video.mp4"

response = requests.get(url)

with open(filename, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

print("文件下载完成")
