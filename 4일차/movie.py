import requests

def movie_rank(dt):
    url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={dt}'
    result = requests.get(url)  #url에서 가져온 모든 값은 기본적으로 string타입 
    result = result.json()  #dictionary, list로 바뀜

    boxOfficeResult = result['boxOfficeResult']
    dailyBoxOfficeList = boxOfficeResult['dailyBoxOfficeList']

    dailyBoxOfficeList = result['boxOfficeResult']['dailyBoxOfficeList']
    # print(dailyBoxOfficeList[0]['movieNm'])

    for mv in dailyBoxOfficeList:   #rank,movieCd,movieNm
        print(f"{mv['rank']} \t {mv['movieCd']}\t {mv['movieNm']}")


# movieCd - 상세정보조회함수 선언
# showTm, openDt, typeNm, actors

def movie_info(cd):
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=f5eef3421c602c6cb7ea224104795888&movieCd={cd}'
    result = requests.get(url)
    result = result.json()
    mv = result['movieInfoResult']['movieInfo'] 
        #dict {}
    print(f"{'개봉날짜 :'} \t {mv['openDt']}")
    print(f"{'상영시간 :'} \t {mv['showTm']}")
    print(f"{'영화제목 :'} \t {mv['movieNm']}")
    
    #출연배우
    for actor in mv['actors']:
        print(f"{actor['peopleNm']} \t {actor['cast']}")

    #첫번째 감독만 출력
    print("감독",mv['directors'][0]['peopleNm'])

if __name__ == "__main__":
    movie_info('20198429')
    