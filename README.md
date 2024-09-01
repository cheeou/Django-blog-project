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



## URL 구조(모놀리식)
-  main

| App      | URL                  | View Function  | HTML File Name         | Note                  |
|----------|----------------------|----------------|-------------------------|-----------------------|
| main     | `/`                  | LoginView(Django module)   | main/index.html   | 블로그 초기화면 |
| main     | `main/`              | main           | main/main.html         | 블로그 메인화면      |

- blog

| App      | URL                  | View Function  | HTML File Name         | Note                  |
|----------|----------------------|----------------|-------------------------|-----------------------|
| blog     |  `post/<int:post_id>` | post_detail    | blog/post-view.html     | 글 상세보기     |
| blog     | `post/add/`         | post_add       | blog/post_add.html      | 글 작성            |
| blog     | `post/<int:post_id>/`| post_detail   | blog/post_detail.html   | 글 상세보기         |
| blog     | `post/edit/<int:post_id>/`| post_edit   | blog/post_edit.html   | 글 수정   |
| blog     | `post/update/<int:post_id>/`| post_update   | blog/post_edit.html   | 글 수정 내용 저장  |
| blog     | `post/delete/<int:post_id>/`| post_delete   | blog/post_confim_delete.html   | 글 삭제   |


- accounts

| App      | URL                  | View Function  | HTML File Name         | Note                  |
|----------|----------------------|----------------|-------------------------|-----------------------|
| accounts | `account/signup/`  | signup    | accounts/signup.html| 회원가입 페이지|
| accounts | `accounts/login/`  | LoginView(Django module)     | accounts/login.html| 로그인 페이지|
| accounts | `profile/edit`  | edit_profile     | accounts/profile.html| 프로필 페이지|



## 프로젝트 일정(WBS)

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


## 데이터베이스 모델링(ERD)
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
## 화면 설계 기획
| 실행화면 | 상세설명 |
|---------|-------------|
| ![login_page](https://github.com/user-attachments/assets/598b7160-8b88-4abc-ab54-8a2a0d4b0566) | **초기 페이지**<br>- 로그인<br>- 회원가입 링크<br>- 게스트 입장 링크 |
| ![create_account_page](https://github.com/user-attachments/assets/dd46d782-8a23-421c-b995-da609d0dcf16) | **회원가입 기능**<br> |
| ![main-post_list](https://github.com/user-attachments/assets/500e17b0-037e-4f0b-b0ae-cbe4d1690572) | **블로그 메인화면**<br>- 게시글 네비게이션<br>- 게시글 목록<br>- 검색 기능 |
| ![_post_detail (1)](https://github.com/user-attachments/assets/0ffdaa5f-8f2f-42bc-8b80-5401f7b491fc)| **게시글 보기**|
| ![_post_write](https://github.com/user-attachments/assets/acbd7285-5556-4048-910d-e90c8265466e)| **게시글 작성**|

