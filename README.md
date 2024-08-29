# 📚 ᗷOOKᒪOG
## 기술 스택
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=black"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=black"> 

## 프로젝트 목표(작성중)
## 주요 기능(작성중)
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
    User ||--o{ blog_post : writes
    User ||--o{ comment : writes
    User ||--o{ like : gives
    blog_post ||--o{ Comment : has
    blog_post ||--o{ Like : receives
    blog_post }o--|| Category : belongs_to
    blog_post ||--o{ Image : contains

    account_user {
        int id PK
        string username
        string email
        string password
        datetime last_login
    }
    blog_post {
        int id PK
        string title
        text content
        datetime created_at
        datetime updated_at
        int author_id FK
        int category_id FK
        int main_image_id FK
    }
    blog_postImage {
        int id PK
        string file_path
        string alt_text
        int order
        int review_id FK
    }
    blog_postComment {
        int id PK
        text content
        datetime created_at
        int review_id FK
        int user_id FK
    }
    blog_category {
        int id PK
        string name
    }
    blog_postLike {
        int id PK
        int user_id FK
        int review_id FK
        datetime created_at
    }
```
## 화면 설계(작성중)
![booklog-화면설계](https://github.com/user-attachments/assets/f6c4606f-7a6f-453b-993b-edfdef71f87a)
