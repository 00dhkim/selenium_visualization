# selenium_visualization

목적:

selenium을 사용하는데에 있어 내가 원하는 element의 경로를 찾는 과정이 항상 힘들었다.

마치 내가 원하는 디랙토리 경로를 가기 위해 일일이 ls 하고 cd 하고 ls 하고 cd 하는 느낌이다.

1. 어떤 element에 대해서 하위 element의 정보를 tree 구조로 보여줌

e.g. e.tree() -> 하위 element가 모두 보여짐

-> 이때 depth나 attribute 표시 여부를 설정할 수 있음

2. tree에서 각 element에 대한 고유 번호를 입력하면 해당 element에 대한 경로를 return 받을 수 있음

이 경로값을 python 코드에 쉽게 넣을 수 있다.

