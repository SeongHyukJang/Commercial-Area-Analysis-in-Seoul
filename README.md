# Commercial Area Analysis in Seoul

## (1) 가설
  - 경쟁 상대가 적고 매출이 높으며, 유동인구수가 높은 구역은 수익이 높을 것이다.
  
### (2) 인터넷을 통한 데이터 획득
  - 서울시 열린 데이터 광장
    - 서울시 우리 마을 가게 상권 분석 서비스 (상권-점포)
    - 서울시 우리 마을 가게 상권 분석 서비스 (상권-추정매출)
    - 서울시 우리 마을 가게 상권 분석 서비스 (상권-추정유동인구)

### (3) 분석을 위한 데이터의 가공
  - sort_by_month() : csv파일을 월단위로 구분하여 새로운 csv파일을 만든다.
  - sort_by_address() : 비정형화된 주소 데이터를 정형화한다.
  - ranking_by_address_in_ascending_order() : 데이터를 키 값을 기준으로 오름차순으로 정렬한다.
  - ranking_by_address_in_descending_order(): 데이터를 키 값을 기준으로 내림차순으로 정렬한다.
  - address_shop_index_in_list() : 주소별로 정리된 데이터를 업종데이터와 묶는다.
  - ranking_by_address() : 주소별로 업종의 순위를 정한다.
  - A_Result_Dictionary() : (A)의 결과를 dictionary형태로 저장한다.
  - A_Result() : (A)의 결과를 Series 형태로 보여준다.
  - GetAddressRank() : (A)를 바탕으로 주소를 검색하면 순위를 보여준다.
  - B_Result_DataFrame() : (B)의 결과를 Data Frame형태로 보여준다.
  - B_Result() : (B)의 결과를 IPython모듈을 이용하여 보여준다.
  - GetAddressInfo() : (B)를 바탕으로 주소를 검색하면 업종들의 순위를 보여준는 함수

### (4) 분석 결과 도출
  - (A)
    - '점포' 자료와 '추정 매출' + '추정 유동 인구 수' 자료의 상관관계를 분석
  - (B)
    - '점포' 자료와 '추정 매출' 자료의 상관관계를 분석

### (5) 결론 및 성과
  - 업종에 상관없이 서울의 어느 구역을 정할 때 사용하는 함수 : A_Result(), GetAddressRank()
  - 구역은 정했지만 업종을 선택 하지 않았을 때 사용하는 함수 : GetAddressInfo()

### (6) 참고문헌
  - https://docs.python.org/3/
  - https://3months.tistory.com/292
  - https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html
  - https://datascienceschool.net/
