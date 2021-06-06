import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

urlString = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date='

my_token = '1849305952:AAHeFeV9S5ThmUWRsbzCiJoDM9GTGEPG4ks'

bot = telegram.Bot(token = my_token)

# date = input('날짜를 입력하세요(ex.20210606):')
date = '20210610'

date_message = date[4:6] + "월" +  date[6:] + "일"

def job_function():

    html = requests.get(urlString+date)

    soup = BeautifulSoup(html.text, 'html.parser')

    #imax오픈 여부 출력하기
    imax = soup.select_one('span.imax')

    #imax가 오픈되었다면 오픈된 영화 이름 출력
    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        imaxMovie_title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id = 1856435742, text = date_message + ' <' + imaxMovie_title + '> IMAX 예매가 오픈되었습니다.')
        print("메세지 전송 완료")
        schedulers.pause()

schedulers = BlockingScheduler()

bot_working = schedulers.add_job(job_function, 'interval', seconds = 30)

schedulers.start()
