import requests
import time

for i in range(636):
    url = "https://baseweb.leshuazf.com//leposweb/home/validcode.do?m=0.4832802191027594"
    resp = requests.get(url)
    if resp.status_code == 200:
        img = resp.content
        open(f"./images/test_{i}.png", "wb").write(img)
        print(f"image {i} 下载成功")
    else:
        print("出现错误")
    time.sleep(1)
print("下载结束")