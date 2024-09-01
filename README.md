# 📚 ᗷOOKᒪOG
## 기술 스택
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=black"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=black"> 

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
| accounts | `profile/edit`  | edit_profile     | accounts/profile.html| 회원가입 페이지|



## 프로젝트 일정(WBS)

```mermaid
gantt
    title Django Blog
    dateFormat YYYY-MM-DD
    axisFormat %m/%d
    tickInterval 1day
    section 기획
    화면설계    :active, 2024-08-26, 1d
    ERD 작성    :active, 2024-08-26, 1d
    환경세팅    :active, 2024-08-26, 1d
    section 기능 개발
    모델 및 기본 뷰 개발       :active,    2024-08-27, 1d
    뷰 및 템플릿 개발          :active,    2024-08-28, 1d
    사용자 인증 및 추가 기능   :active,  2024-08-29, 1d
    section 화면 디자인 작업
    스타일링 및 마무리         :         2024-08-30, 1d
    section 최종 점검 및 테스트
    테스트 및 최종 점검        :         2024-08-31, 1d
    section 사이트 배포
    AWS Lightsail 사이트 배포  :         2024-09-01, 1d
   
```


## 데이터베이스 모델링(ERD)
```mermaid
erDiagram
    account_User ||--o{ blog_Post : writes
    account_User ||--o{ blog_PostComment : writes
    account_User ||--o{ blog_PostLike : gives
    blog_Post ||--o{ blog_PostComment : has
    blog_Post ||--o{ blog_PostLike : receives
    blog_Post }o--|| blog_PostCategory : belongs_to
    blog_Post ||--o{ blog_PostImage : contains

    account_User {
        int id PK
        string username
        string email
        string password
        datetime last_login
    }
    blog_Post {
        int id PK
        string title
        text content
        datetime created_at
        datetime updated_at
        int author_id FK
        int category_id FK
        int main_image_id FK
    }
    blog_PostImage {
        int id PK
        string file_path
        string alt_text
        int order
        int review_id FK
    }
    blog_PostComment {
        int id PK
        text content
        datetime created_at
        int review_id FK
        int user_id FK
    }
    blog_PostCategory {
        int id PK
        string name
    }
    blog_PostLike {
        int id PK
        int user_id FK
        int review_id FK
        datetime created_at
    }
```
## 화면 설계(작성중)
![booklog-화면설계](https://github.com/user-attachments/assets/f6c4606f-7a6f-453b-993b-edfdef71f87a)
