from pathlib import Path
from socket import timeout
import httpx
urls = ["https://ru.pinterest.com/amagomedova2225/%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8/", "https://www.google.com/search?sca_esv=1b71ba01ffc76c1b&sxsrf=AKL5yDilyjs2ZWfNmfpYCmObAltDgkUaVA:1794479569000&udm=2&fbs=ACAhTvxHM53nx_0OLHZ1FTf0apsbBdIiuZzNqanB1SKz49V7NT7lWo3HN1R0wNca7m7v345dJtCsJFbefP36L0p_gZ92T-s739DIQNxblWu_5GlkosXFoxeQwSuBb9sZuS2um_cNLfyDkso-I9SO_Z5sCeJ3RHljequICh8JVrMW6Pow8Fpm6XbXeLcN8vJEYVI3RpNdLIno6gbeheWNJVpr34uH8f2dtNCLjJgCkKFkpnJhvFR9EiRK6U5z51-YCWiguhx_IDj-TGTbyyGgsOBUrHkXXi2dvA&q=%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8&sa=X&ved=2ahUKEwj7sJCqnYKYAxWkcbAFHV2tFDgQtKgLegQIHxAB&biw=1920&bih=953&dpr=1#sv=CAMSUxoyKhBlLWthSnhDRV9ZUF9xUmlNMg5rYUp4Q0VfWVBfcVJpTToOMFpDUFFUbDBzMVBWOU0gBCoXCgFzEhBlLWthSnhDRV9ZUF9xUmlNGAEwAVACGAcgjPTPvwRKCBACGAEgAigB", "https://www.python-httpx.org/compatibility/"]

class PageDownloader:
    def __init__(self):
        headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
        self.client = httpx.Client(follow_redirects = True, headers = headers, timeout = 30.0)
    def get_url(self, url: str):
        return self.client.get(url)
    

def save_html_content(rep: httpx.Response, folder: str, filename: str):
    folder_path = Path(folder)
    folder_path.mkdir(parents=True, exist_ok=True)
    file_path = folder_path/filename
    with open(file_path, "w", encoding = "utf-8") as file:
        file.write(rep.text)

downloader = PageDownloader()


rep1 = downloader.get_url(urls[0])
rep2 = downloader.get_url(urls[1])
rep3 = downloader.get_url(urls[2])

for i, rep in enumerate([rep1, rep2, rep3], start=1):
    if rep.status_code == 200:
        save_html_content(rep, "htmls", f"page{i}.html")
        print(f"Страница {i} успешно загружена !")
    else:
        print(f"Страницу {i} не удалось загрузить")
    
