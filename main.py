import requests

url = "https://d.pcs.baidu.com/file/5719cca34lde6cfe881563df29b6c4f2?fid=4160466670-250528-306141886068899&rt=pr&sign=FDtAERK-DCb740ccc5511e5e8fedcff06b081203-W0J8fA1HQCWTBGrwNAzdoXpoffY%3D&expires=8h&chkbd=0&chkv=0&dp-logid=944630657866084190&dp-callid=0&dstime=1700902391&r=824492936&vuk=4160466670&origin_appid=15195230&file_type=0"
filename = "video.mp4"

response = requests.get(url, stream=True, headers={"User-Agent": "pan.baidu.com", "Cookie": "BDUSS=XdoZ2xKYUhhc3I1WE94Y3oxZVdlSDY1YUllMlVDbWRRZEJhcjRRejlVOEJKMEZsSVFBQUFBJCQAAAAAAAAAAAEAAADg9zH~ztLX7rrDNTYwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGaGWUBmhlle"})

with open(filename, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

print("文件下载完成")
