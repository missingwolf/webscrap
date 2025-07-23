from bs4 import BeautifulSoup
import requests
import re
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
query_year = input("你需要查询哪年之后的电影：")
count = 0
for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    # all_title = soup.find_all("span", attrs={"class": "title"})
    items = soup.find_all("div", attrs={"class": "item"})
    for item in items:
        title = item.find("span", attrs={"class": "title"}).text
        info = item.find("p")
        if info:
            info_text = info.get_text(strip=False)
            year_match = re.search(r'(\d{4})', info_text)
            if year_match:
                year = year_match.group(1)
                if int(year) >= int(query_year):
                    count += 1
                    print(f"{title}，{query_year}")
            else:
                print(f"{title}，未找到年份")
        else:
            print(f"{title}，未找到信息")
    time.sleep(2)
print(f"{query_year}年之后的电影，总共{count}部。")