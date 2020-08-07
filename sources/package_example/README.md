# 파이썬 패키지

패키지 폴더에 있는 \_\_init.py\_\_를 통해 패키지를 정의할 수 있다.

package_example 폴더에 있는 \_\_init.py\_\_ 파일은 하위 패키지 파일들을 어떤 식으로 정의할 지 사용하고 있다.

from (pythonfilepath) import (fun,var,...) as (rename)
이 구문으로 package_example.folder.file.function() 을 package_example.function() 으로 축약시킬 수 있다.

현재는 tree 폴더 안 tree 파일 속 tree 함수를 tree라는 이름으로 재정의했으므로 from .tree.tree import tree as tree 가 된다.

나머지 폴더에 있는 \_\_init.py\_\_ 파일은 없어도 무방하나 이 폴더가 패키지라는 걸 명시하는 역할을 한다.

# webelement 객체

우리가 필요한 webelement 객체는 selenium.webdriver.remote.webelement.py 에 있음

여기에 find_by ... 함수가 정의되어 있는데 이걸 활용해야 할듯함
