1. 웹의 용도 : 생각 정리, 복기
2. 필요한 기능
3. ERD
4. 디자인
5. 상세 기능

- 1. 웹의 용도
```markdown
생각 정리, 복기. 이에 대한 다른 사람들의 생각. 예시, 등등. 이를 위해서 글에 대한 흥미를 일으킬 수 있는 것들. 
```

- 2. 필요한 기능
```markdown
1. navbar
  - 카테고리: 기술/자유글, 질문방, 자유글, 로그인, 검색
  	- 기술: 펼쳐지게끔. css, js, html, python, 등등
  	- 유저: 디테일, 북마크, 자신의 글 모음 등
  	- 고정 x
2. 유저
  - 구글, 네이버, 깃헙으로 로그인 기능.
  - 팔로우
  - 레벨(신뢰도)
3. 글
  - 제목
  - 내용: 이미지 배치가 가능하게. 마크다운처럼
  - 추천/비추천
  - 북마크
  - 댓글: 대댓글 달 수 있게. 
4. 검색
  - 자동완성
  - 카테고리별로 다른 화면
```
- 3. ERD
```markdown
- 모델: user, article, comment, 
  - user: nickname, email, level, follow, like_total(레벨 위해서)
  - article: user, title, content, like, hashtag, bookmark
  - comment: user, article, content, like
  - answer: user, article, content, like, 
```
- 4. 디자인
```markdown
배경은 화려하지 않아서 글에 집중할 수 있게 설정. 군더더기 없고, 깔끔하게. 전문적인 이미지를 추구. 
웹의 모든 페이지는 강조하는 부분을 제외하고는 눈에 편한 색으로 구성. 

```