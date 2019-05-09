from bs4 import BeautifulSoup
import requests
import os
import csv

demo_source = requests.get('http://coreyms.com').text
demo_soup = BeautifulSoup(demo_source, 'lxml')
demo_article = demo_soup.find_all('article')

# dir_csv = 'C:\\Users\\lamborghni\\Documents\\GitHub\\allinone\\python\\app_1'
dir_csv = 'C:\\Users\\yangy\\Documents\\GitHub\\allinone\\python\\app_1'
csv_file = open(dir_csv+'\\'+'demo_link.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','link'])

for i in demo_article:
    headline = i.h2.a.text
    summary = i.find('div', class_='entry-content').p.text

    try:
        vid_src = i.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'

    except Exception as e:
        yt_link = None

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
