# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os

# 读取source文件夹下的HTML文件
directory = "./sources"
if os.path.exists(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    html_content = f.read()

# 解析HTML内容并选择redirect目标行链接
soup = BeautifulSoup(html_content, "html.parser")
trs = soup.select("tbody tr")[3:]

#是否重定向判定方法
def is_redirected(url,targetUrl):
   
   headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
   
   try:
       response = requests.get(url, allow_redirects=True, timeout=5, headers=headers)
       if response.history:
           if response.url == targetUrl:
                print(f"{url} 301跳转到: {targetUrl}")
                return True
       else:
           print(f"{url} 未跳转")
           return False
   except requests.exceptions.RequestException as e:
       print(f"请求失败: {e}")
       return False

# 向目标内容添加新内容
# def add_content(url, target_content, new_content):
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         target = soup.find(string=target_content)
#         target.replace_with(new_content)
#     except requests.exceptions.RequestException as e:
#       print(f"请求失败: {e}")

for row in trs:
    rowEle = BeautifulSoup(str(row), "html.parser")
    columns = rowEle.select("td")
    if len(columns) > 1:
        #选择redirect目标列链接
        content = columns[1].get_text()
        tagrgetContent = columns[0].get_text()
        is_redirected(content,tagrgetContent)



