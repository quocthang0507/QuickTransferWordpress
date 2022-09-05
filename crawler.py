# Crawler data from cntt.dlu.edu.vn

import datetime
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from utils import print_red

download_dir = os.path.join(os.getcwd(), "Downloads")

browser = webdriver.Edge(executable_path=os.path.join(
    os.getcwd(), 'drivers', 'msedgedriver.exe'))

browser.set_page_load_timeout(60)


def get_html_from_url(url: str):
    start_time = time.time()
    try:
        browser.get(url)
    except:
        end_time = time.time()
        print_red(
            f'Đã có lỗi khi truy cập địa chỉ {url} này, trong {round(end_time - start_time, 2)} giây')
        return None
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    return soup


def get_title(soup: BeautifulSoup):
    div = soup.find("div", {"class": "tuade"})
    if div != None:
        return div.text().strip("\"").strip()
    return None


def get_date(soup: BeautifulSoup):
    span = soup.find("span", {"class": "date-article"})
    if span != None:
        return datetime.datetime.strptime(span.text(), "%d/%m/%Y")
    return None


def get_content(soup: BeautifulSoup):
    div = soup.find("div", {"class": "chitietbaiviet"})
    return div


def get_pdf(soup: BeautifulSoup):
    div = soup.find("div", {"class": "noidungxem"})
    if div != None:
        obj_tags = div.find("object")
        for obj in obj_tags:
            yield obj["src"]
    return None


def save_file(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = url.split('/')[-1]
    file_path = os.path.join(download_dir, filename)

    request = requests.get(url, stream=True)
    if request.ok:
        print("Downloading to ", os.path.abspath(file_path))
        with open(file_path, 'wb') as file:
            for chunk in request.iter_content(chunk_size=1024*8):
                if chunk:
                    file.write(chunk)
                    file.flush()
                    os.fsync(file.fileno())
    else:
        print(
            f"Download failed: status code {request.status_code}\n{request.text}")


def get_subfolder_path(url: str):
    subfolder = url.split('/SubDomain/')[1]
    arr = subfolder.split('/')
    arr.pop()  # remove last item (file name)
    return '/'.join(arr)


def go_to_next_page(soup: BeautifulSoup):
    div = soup.find("div", {"class": "PageColumns"})
    if div != None:
