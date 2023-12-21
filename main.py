import requests

url = "https://cdn77.91p49.com//mp43/916423.mp4?st=4655e551d1028e41a68663dbe4027b5f"
filename = "video.mp4"

response = requests.get(url)

with open(filename, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

print("文件下载完成")
