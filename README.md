# 📚 ᗷOOKᒪOG
## 기술 스택
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=black"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=black"> <img src="https://img.shields.io/badge/Figma-941711?style=flat-square&logo=Figma&logoColor=white"> 

## 프로젝트 목표
Django의 핵심 기능인 `Admin 인터페이스`, `데이터베이스 관리`, `보안 기능`, 그리고 웹사이트 구축에 필요한 `Django 라이브러리들`을 활용하여 실무적인 기술을 익히고 경험을 쌓는 것을 목표로 합니다.
## 1. 주요 기능
### 1.1. 사용자 인증 시스템
- `django.contrib.auth`를 활용한 회원가입, 로그인 및 사용자 프로필 관리
- Django의 내장 인증 시스템을 이용한 안전한 사용자 인증 처리

   
### 1.2. 게시글 관리
- 게시글 작성, 수정, 삭제 기능
- Django의 ORM을 활용한 카테고리별 게시글 분류 및 조회

### 1.3. 게시글 네비게이션
- Django의 `Paginator` 클래스를 사용한 효율적인 페이지네이션
- `django-filter` 라이브러리를 활용한 카테고리 필터링 및 맞춤형 콘텐츠 접근



## 2. URL 구조(모놀리식)
-  main

| App      | URL                  | View Function  | HTML File Name         | Note                  |
|----------|----------------------|----------------|-------------------------|-----------------------|
| main     | `/`                  | LoginView(Django module)   | main/index.html   | 블로그 초기화면 |
| main     | `main/`              | main           | main/main.html         | 블로그 메인화면      |

- blog

| App      | URL                  | View Function  | HTML File Name         | Note                  |
|----------|----------------------|----------------|-------------------------|-----------------------|
| blog     | `post/add/`         | post_add       | blog/post_add.html      | 글 작성            |
| blog     |  `post/<int:post_id>` | post_detail    | blog/post-view.html     | 글 상세보기     |
| blog     | `post/edit/<int:post_id>/`| post_edit   | blog/post_edit.html   | 글 수정   |
| blog     | `post/update/<int:post_id>/`| post_update   | blog/post_edit.html   | 글 수정 내용 저장  |
| blog     | `post/delete/<int:post_id>/`| post_delete   | blog/post_confim_delete.html   | 글 삭제   |


- accounts

| App      | URL                  | View Function  | HTML File Name         | Note                  |
|----------|----------------------|----------------|-------------------------|-----------------------|
| accounts | `account/signup/`  | signup    | accounts/signup.html| 회원가입 페이지|
| accounts | `accounts/login/`  | LoginView(Django module)     | accounts/login.html| 로그인 페이지|
| accounts | `profile/edit`  | edit_profile     | accounts/profile.html| 프로필 페이지|



## 3. 프로젝트 일정(WBS)

```mermaid
gantt
    title Django Blog
    dateFormat YYYY-MM-DD
    axisFormat %m/%d
    tickInterval 1day
    section 기획
    화면설계    :done, 2024-08-26, 1d
    환경세팅    :done, 2024-08-26, 1d
    화면설계 마무리       :done,    2024-08-27, 2d
    ERD 작성          :done,    2024-08-27, 2d
    section 기능 개발
    모델 정의 및 기본 뷰 개발       :done,    2024-08-29, 1d
    게시물 CRUD 기능   :done,  2024-08-29, 3d
    사용자 인증 기능   :done,  2024-08-30, 2d
    프로필 변경  페이지 :done         2024-09-01, 1d
    CSS 수정 및 테스트 : done        2024-09-01, 1d

```


## 4. 데이터베이스 모델링(ERD)
```mermaid
erDiagram
    User ||--o{ Post : writes
    Post }o--|| PostCategory : belongs_to

    User {
        int id PK
        string username
        string password
        string nickname
        string profile_image
        text   bio
    }
    Post {
        int id PK
        string postTitle
        text content
        datetime pub_date
        datetime modify_date
        int author_id FK
        int category_id FK
    }

    PostCategory {
        int id PK
        string name
    }

```
## 5. 화면 설계 기획(피그마)
![booklog-화면설계](https://github.com/user-attachments/assets/ba39b540-3ef1-462d-bd0a-44cafcd4589f)

## 6. 프로젝트 구조
```
📦accounts
📦blog
📦config
📦main
📦media
 ┣ 📂accounts
 ┃ ┗ 📂proile
📦static
📦templates
 ┣ 📂accounts
 ┃ ┣ 📜login.html
 ┃ ┣ 📜profile.html
 ┃ ┗ 📜signup.html
 ┣ 📂blog
 ┃ ┣ 📜post_add.html
 ┃ ┣ 📜post_confirm_delete.html
 ┃ ┣ 📜post_detail.html
 ┃ ┗ 📜post_edit.html
 ┣ 📂main
 ┃ ┣ 📜index.html
 ┃ ┗ 📜main.html
 ┣ 📜base.html
 ┗ 📜form_errors.html
 ```


## 7. 주요 기능 설명
 실행화면      | 기능 설명                 | 
|----------|----------------------|
| ![login](https://github.com/user-attachments/assets/597bb517-17a8-4f59-877d-9ac957d53b71) | 사이트 초기 진입페이지-회원 로그인  | 
| ![게스트입장](https://github.com/user-attachments/assets/62da6124-58ee-4fab-ac5d-443a961bd01f) | 사이트 초기 진입페이지-게스트 입장  | 
| ![회원가입-유효성검사](https://github.com/user-attachments/assets/3061305c-96b5-47f2-a398-f28f64e784ef) | 회원가입 - 유효성 검사  | 
| ![내가쓴글](https://github.com/user-attachments/assets/5ce1347d-c6a3-41d8-83ba-ed589a472266) | 1. 내가 쓴 글보기 <br>2.카테고리별 글 목록 조회  | 
| ![프로필편집](https://github.com/user-attachments/assets/c47da4a9-b12b-4614-9ded-a86dfd56d2d8)| 프로필 편집 기능  | 
| ![페이징처리](https://github.com/user-attachments/assets/0fd37b1b-ce13-4051-8541-bbe102715858) | 게시글 페이징처리  | 
| ![게시글상세 수정 삭제](https://github.com/user-attachments/assets/ce3a621e-f624-4f04-a7e8-8cd7f5172c86) | 게시글 보기&수정&삭제  | 



## 8.마치며 
### 프로젝트를 진행하며 느낀 점

이전에 미니 프로젝트를 진행한 경험이 있었지만, 이번 프로젝트는 웹 프레임워크를 활용하여 기획부터 사이트의 전반적인 기능을 구현하는 큰 규모의 작업이다 보니 개인적으로 부담이 조금 느껴졌던 것 같습니다.

- 개발 초기 어려움
<br>웹 프레임워크의 전체적인 구조와 작업 순서에 대한 이해가 다소 부족하여 프로젝트 시작 후 처음 이틀 동안은 어디서부터 시작해야 할지 방향을 잡지 못하여 일정 관리에 차질이 생겨 아쉬움이 있었습니다.

- 돌파구<br>
기본적인 CRUD(Create, Read, Update, Delete) 기능 구현을 시작점으로 삼아 프로젝트에 진전을 이루기 시작했습니다.


이번 프로젝트로 스스로 한계에 부딪히는 느낌이라 불안과 고통이 따르긴 했지만(?) 장고 웹프레임워크에 대해 이해하는 데 큰 도움이 되었습니다. 미흡하지만 하나의 서비스 결과물을 만들어 낼 수 있다는 것에 의의를 두며 더 공부를 열심히 해야겠다고 다짐하였습니다.