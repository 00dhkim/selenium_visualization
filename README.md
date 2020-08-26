# selenium_visualization

summary notion link:  
https://www.notion.so/SW-0543f52cc8c14e11941ec8f69ab0c6dc

Demo link:  
https://youtu.be/WxnLk0PqI40

## 목적

selenium을 사용하는데에 있어 내가 원하는 element의 경로를 찾는 과정이 항상 힘들었다.

마치 내가 원하는 디랙토리 경로를 가기 위해 일일이 ls 하고 cd 하고 ls 하고 cd 하는 느낌이다.

1. 어떤 element에 대해서 하위 element의 정보를 tree 구조로 보여줌

e.g. e.tree() -> 하위 element가 모두 보여짐

-> 이때 depth나 attribute 표시 여부를 설정할 수 있음

2. tree에서 각 element에 대한 고유 번호를 입력하면 해당 element에 대한 경로를 return 받을 수 있음

이 경로값을 python 코드에 쉽게 넣을 수 있다.

## ToDo

- selenium의 WebElement의 id만으로 선택하기
- 특정 element에 대한 자식 element 리스트 출력하기
- 기존의 패키지에 추가할지, 새로운 패키지를 만들지 결정하기

## example

```python
body = driver.find_element_by_tag_name("body")
<selenium.webdriver.remote.webelement.WebElement (session="3d8d880fc4bedfbc781afa8b62d094d3", element="80153561-a62f-42a7-acc2-ea5e03c089ec")>

type(body)
<class 'selenium.webdriver.remote.webelement.WebElement'>

body.id
'80153561-a62f-42a7-acc2-ea5e03c089ec'
```

## useful URLs

- selenium tutorials
  - https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html
- selenium xpath
  - https://wkdtjsgur100.github.io/selenium-xpath/
- selenium child list
  - https://stackoverflow.com/questions/24795198/get-all-child-elements
  - https://sqa.stackexchange.com/questions/33774/selenium-web-driver-how-to-select-child-elements
- Dohyun's selenium sample codes
  - https://github.com/kimdo331/mini-code/blob/master/source_code/selenium_example.py
  - https://github.com/kimdo331/melon2vibe/blob/master/melonCrawl.py
  - https://github.com/kimdo331/melon2vibe/blob/master/vibeAdd.py
- selenium Docs
  - https://selenium-python.readthedocs.io/

