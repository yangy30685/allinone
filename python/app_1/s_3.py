from bs4 import BeautifulSoup
import requests
import os
import csv

demo_0 = 'https://www.youtube.com/'
demo_1 = requests.get(demo_0).text
demo_2 = BeautifulSoup(demo_1, 'lxml')
demo_3 = demo_2.find_all('ytd-item-section-renderer')

dir_csv = 'C:\\Users\\lamborghni\\Documents\\GitHub\\allinone\\python\\app_1'
csv_file = open(dir_csv + '\\' + 'demo_youtube.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'link'])

for i in demo_3:
    print('--'*20)
    print(i)
        
    # try:
    #     vid_src = i.find('iframe', class_='youtube-player')['src']
    #     print(vid_src)

    #     vid_id = vid_src.split('/')[4]
    #     vid_id = vid_id.split('?')[0]

    #     yt_link = f'https://youtube.com/watch?v={vid_id}'
    # except Exception as e:
    #     yt_link = None

    # csv_writer.writerow([headline,summary,yt_link])

csv_file.close()
