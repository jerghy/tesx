import requests

url = "https://cdn77.91p49.com//mp43/697090.mp4?st=600e5d8ac15ab7fca8240de05a37d317"
filename = "demo.mp4"

response = requests.get(url)

with open(filename, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

print("文件下载完成")
