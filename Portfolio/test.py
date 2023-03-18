# 내장함수
from urllib.request import urlopen
# 명령행 파싱 모듈로 argparse 모듈 사용
import argparse
# request => 웹에 요청한 결과 값을 얻어올 수 있는 모듈
import requests as req
# 웹에다 요청한 결과를 보내는 모듈
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
#argparse 모듈에 ArgumentParse() 함수 사용하여 parser 생성

parser.add_argument("-name", "--people", required=True)
# 명령행 옵션을 지정하기 위해 사용. 명령행 옵션 인자는 -name으로 지정함

args = parser.parse_args()
#parse에 add_argument()함수 사용해 args 인스턴스생성

people = args.people
# 명령행에서 받은 인자값을 people에 값을 넘겨줌


def main():

# 구글 url https://www.google.co.kr/search?q=%EB%B2%A4&tbm=isch

    url_info = "https://www.google.co.kr/search?"

#params에다 딕션을 넣어줌
    params = {
#명령행에서 받은 인자값을 people로 넣어줌
        "q" : people,
        "tbm":"isch"
    }
#url을 요청하는 파싱값
    html_object = req.get(url_info,params) #html_object html source 값

    if html_object.status_code == 200:
        #페이지 status_code 가 200 일때 2XX 는 성공
        bs_object = BeautifulSoup(html_object.text,"html.parser")
        #인스턴스를 생성
        img_data = bs_object.find_all("img")
        #인스턴스에서 find_all 이라는 함수에 img 태그가 있으면 img_data에 넣어줌

        for i in enumerate(img_data[1:]):
            #딕셔너리를 순서대로 넣음
            t = urlopen(i[1].attrs['src']).read()


            filename = "img_"+str(i[0]+1)+'.jpg'


            with open(filename,"wb") as f:


                f.write(t)
                print("Img Save Success")


if __name__=="__main__":
    main()

