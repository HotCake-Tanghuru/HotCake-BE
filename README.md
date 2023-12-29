# HotCake

## 📝목차
[1. 프로젝트 소개](#1-🎉프로젝트-소개)<br>
[2. 팀 소개](#2-🧑팀-소개)<br>
[3. 개발 환경 및 개발 일정(WBS)](#3-🧐개발-스택-및-개발-일정wbs)<br>
[4. 배포 URL 및 프로젝트 구조](#4-📦-배포-url-및-프로젝트-구조)<br>
[5. 데이터베이스 모델링(ERD)](#5-🔍데이터베이스-모델링erd)
[6. API 명세](#6-🔨-api-명세)<br>
[7. 화면설계/UI](#7-💄화면설계ui)<br>
[8. 메인 기능](#8-✨메인-기능-gif-추가)<br>
[9. 트러블 슈팅](#9-💥트러블-슈팅)<br>
[10. 회고](#10-💬회고)<br>


## 1. 🎉프로젝트 소개
 ### 1-1. 목표
 - 최신 트렌드들에 대한 정보 제공과 공유
 - 트렌드에 맞는 활동 인증과 공유
 - 젊은 층에 맞는 소셜 서비스

 ### 1-2. 기능
- 사용자에게 트렌드 정보 제공
- 트렌드에 해당하는 항목, 활동들에 대한 인증 글 게시, 공유 기능

 ### 1-3. 프로젝트 소개

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/0e5756d6-4045-4931-b1ba-f58158c35a9c" width="30%"> 

<a href="http://team-hotcake.s3-website.ap-northeast-2.amazonaws.com/">🔗핫케이크 바로가기</a>

[swagger](http://43.202.230.2/api/schema/swagger-ui/#/)

```
저희 팀은 트렌드에 민감한 젊은 층을 겨냥하여 핫 트렌드에 관한 정보를 제공하는 SNS 서비스를 제작하였습니다.

핫 트렌드, Hot trend
최신의 유행 또는 많은 사람들이 따르는 경향이나 추세를 이르는 용어를 뜻합니다.

핫케이크 서비스는 현재 가장 뜨거운 최신 트렌드를 사용자에게 제공하여 사용자들이 해당 트렌드에 대한 의견을 댓글로 함께 나눌 수 있도록 합니다. 
또 사용자들은 해당 트렌드에 대한 경험을 인증할 수 있습니다. 
이를 통해 미션 리스트를 모두 채우면 스탬프를 받아 공유할 수 있습니다.

핫케이크 서비스의 이름 또한 핫 트렌드와 단어의 유사성을 갖추었을 뿐만 아니라, 핫케이크 음식의 특성상 함께 나누어 먹는 모습을 연상시켜 트렌드를 함께 나누고 공유한다는 의미를 담고 있습니다.
```

- 배포 URL: http://team-hotcake.s3-website.ap-northeast-2.amazonaws.com/

- Front-End Repo: https://github.com/HotCake-Tanghuru/HotCake-FE

- Back-End Repo: https://github.com/HotCake-Tanghuru/HotCake-BE



## 2. 🧑팀 소개
 #### 안녕하세요. Team Tanghuru입니다!
|고동우   |김나영   |박정현   | 이수빈   |
|:---------:|:---------:|:---------:|:---------:|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/a05d6f23-c3b7-48a5-a2e8-2b4b191d46d7" width="180">|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/4e42f092-04f8-453c-959b-d83adda8d9b5" width="150"> |<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/3eeb909d-d323-4326-898a-0b29cfdd83be" width="150"> |<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/9858822d-5ab9-4b1c-9f33-14856685627a" width="150"> |
|<a href="https://github.com/Ko-udon" >🔗Ko-udon</a>|<a href="https://github.com/nayeongdev">🔗nayeongdev</a>|<a href="https://github.com/jungloopy">🔗jungloopy</a>|<a href="https://github.com/hantang820">🔗hantang820</a>|


 
![20231229_122313](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/72a29212-c3f4-486f-b7d1-759c92122285)


## 3. 🧐개발 스택 및 개발 일정(WBS)
 ### 3-1. 개발 스택

 [FE]
<div>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"> 
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"> 
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"> 
</div><br>

[BE]
 <div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> 
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
</div><br>

[배포]
 <div>
    <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> 
    <img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white">
    <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=anginx&logoColor=white">
    <img src="https://img.shields.io/badge/amazons3-569A31?style=for-the-badge&logo=amazons3&logoColor=white">
</div><br>


[DB]
 <div>
    <img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"> 
</div><br>

[개발 환경]
 <div>
    <img src="https://img.shields.io/badge/VisualStudioCode-007ACC?style=for-the-badge&logo=VisualStudioCode&logoColor=white"> 
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
</div>

### 개발 일정(WBS)

#### WBS는 <a href="https://docs.google.com/spreadsheets/d/1J4k44lXZYbcFF4Ug5bMtNz-qDwemjhtLyBUYsz7a90U/edit#gid=0">🔗Google Sheets</a>에서 작성되었습니다.

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/1a8439ee-f4bf-4539-8848-3c4deba8c2a7" width="80%"> 

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/3d31bd1c-be24-4320-a04e-d9b4149fb4d9" width="80%"> 

- [기획] 주제 선정 및 기획·화면 설계<br>
 2023-12-08 ~ 2023-12-12

- [개발]<br>
2023-12-13 ~ 2023-12-22

- [배포 및 연동]<br>
2023-12-23 ~ 2023-12-26

- [발표자료 제작 및 코드 리펙토링]<br>
2023-12-27 ~ 2023-12-28

## 4. 📦 배포 URL 및 프로젝트 구조
### 4-1. 폴더 트리
### 4-1-1. BE 프로젝트 구조
```
📦HotCake-BE
 ┣ 📂.git
 ┣ 📂.github
 ┃ ┣ 📂ISSUE_TEMPLATE
 ┃ ┃ ┣ 📜✨feature.md
 ┃ ┃ ┗ 📜🐛bug.md
 ┃ ┗ 📂workflows
 ┃ ┃ ┗ 📜django.yml
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📂pycache
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜init.py
 ┣ 📂docs
 ┃ ┗ 📜pull_request_template.md
 ┣ 📂hotcake
 ┃ ┣ 📂pycache
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜init.py
 ┣ 📂media
 ┃ ┣ 📂image
 ┃ ┗ 📂media
 ┣ 📂staticfiles
 ┃ ┣ 📂admin
 ┃ ┃ ┣ 📂css
 ┃ ┃ ┣ 📂img
 ┃ ┃ ┗ 📂js
 ┃ ┗ 📂rest_framework
 ┃ ┃ ┣ 📂css
 ┃ ┃ ┣ 📂fonts
 ┃ ┃ ┣ 📂img
 ┃ ┃ ┗ 📂js
 ┣ 📂trends
 ┃ ┣ 📂migrations
 ┃ ┣ 📂pycache
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜init.py
 ┣ 📂trend_missions
 ┃ ┣ 📂migrations
 ┃ ┣ 📂pycache
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜init.py
 ┣ 📂venv
 ┃ ┣ 📂Include
 ┃ ┣ 📂Lib
 ┃ ┣ 📂Scripts
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```
### 4-1-2. FE 프로젝트 구조

```
📦HotCake-FE
 ┣ 📂.git
 ┣ 📂.github
 ┃ ┣ 📂ISSUE_TEMPLATE
 ┃ ┃ ┣ 📜✨feature.md
 ┃ ┃ ┗ 📜🐛bug.md
 ┃ ┗ 📂workflows
 ┃ ┃ ┗ 📜main.yml
 ┣ 📂src
 ┃ ┣ 📂assets
 ┃ ┃ ┣ 📂fonts
 ┃ ┃ ┗ 📂images
 ┃ ┣ 📂css
 ┃ ┃ ┣ 📜common.css
 ┃ ┃ ┣ 📜edit_user.css
 ┃ ┃ ┣ 📜follow.css
 ┃ ┃ ┣ 📜index.css
 ┃ ┃ ┣ 📜like_trends.css
 ┃ ┃ ┣ 📜login.css
 ┃ ┃ ┣ 📜my_stamp.css
 ┃ ┃ ┣ 📜trend.css
 ┃ ┃ ┣ 📜trend_mission.css
 ┃ ┃ ┣ 📜trend_mission_detail.css
 ┃ ┃ ┗ 📜user.css
 ┃ ┣ 📂js
 ┃ ┃ ┣ 📂html2canvas
 ┃ ┃ ┃ ┗ 📜html2canvas.min.js
 ┃ ┃ ┣ 📜edit_user.js
 ┃ ┃ ┣ 📜like_trends.js
 ┃ ┃ ┣ 📜main.js
 ┃ ┃ ┣ 📜my_stamp.js
 ┃ ┃ ┣ 📜scripts.js
 ┃ ┃ ┣ 📜trend.js
 ┃ ┃ ┣ 📜trend_mission.js
 ┃ ┃ ┣ 📜trend_mission_detail.js
 ┃ ┃ ┣ 📜trend_mission_edit.js
 ┃ ┃ ┗ 📜user.js
 ┃ ┗ 📂pages
 ┃ ┃ ┣ 📜edit_user.html
 ┃ ┃ ┣ 📜followers.html
 ┃ ┃ ┣ 📜followings.html
 ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┣ 📜like_trends.html
 ┃ ┃ ┣ 📜login.html
 ┃ ┃ ┣ 📜my_stamp.html
 ┃ ┃ ┣ 📜trend.html
 ┃ ┃ ┣ 📜trend_mission.html
 ┃ ┃ ┣ 📜trend_mission_detail.html
 ┃ ┃ ┣ 📜trend_mission_edit.html
 ┃ ┃ ┗ 📜user.html
 ┗ 📜login.html
```



### 4-2. 아키텍처
![image](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/fe2cad3f-e434-4c29-ad6d-a6d8b18097c5)


### 4-3. 기능명세
![20231227_110230](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/da5c8d16-fc50-451e-8d4f-40fb55062857)


### 4-4. 플로우차트

![20231226_154237](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/aaa7e956-650d-4daf-8c7d-34752c53f38f)


## 5. 🔍데이터베이스 모델링(ERD)
#### ERD는 <a href="https://www.erdcloud.com/d/xokQ3Ex8QogtsFsot">🔗ERDcloud</a>에서 제작하였습니다.

![20231227_125840](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/0ea857b3-f779-4b46-9fcb-7d628b4663b8)

## 6. 🔨 API 명세

<a href="http://43.202.230.2/oauth/kakao/login">🔗 Swagger</a>
<br>

 - 인증/인가

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/3c304f32-90be-463b-8c17-402b44140ed9" width="80%"> 


- 사용자

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/a658862f-d356-4bc2-9350-68b8a0970f9f" width="80%"> 


- 핫 트렌드

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/58e974b8-3350-4b55-93b1-e55fb3cdbe5a" width="80%"> 


- 트렌드 미션

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/81460535-4d80-4807-a7ce-b0b952f47a7d" width="80%"> 


- 스탬프

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/cf6c2c25-f87f-4160-99df-2efc878b4acf" width="80%"> 


## 7. 💄화면설계/UI
#### 화면설계 및 UI 이미지 제작은 <a href="https://www.figma.com/file/b1Z1IOn1wkd32PatV0r66t/Hotcake%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%84-%EA%B3%B5%EA%B0%9C%EC%9A%A9?type=design&node-id=0-1&mode=design&t=66Ysr5jxikCB9WDh-0">🔗Figma</a>에서 하였습니다.


### 7-1. 화면 설계
<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/60b131d6-305e-4fd7-9c5b-cf823b8278a7" width="80%">

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/ac9d06ae-822c-4dfb-b8be-5d7279b25bcc" width="80%">

### 7-2. UI
| | |
|:-:|:-:|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/71d7d4b3-5d86-4309-a50c-60dba87b3504" width="80%"><br>카카오 로그인|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/759d414f-6085-4370-a119-92ed166f9523" width="80%"><br>메인 페이지|
<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/4d4eb452-1055-4469-af40-cbf9bb9c2dfd" width="80%"><br>사용자 프로필|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/219ff5d4-e032-4ab4-a61b-4714abc90213" width="80%"><br>프로필 수정|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/261d2d8f-b6bb-4727-86e3-82cc76ae8df0" width="80%"><br>스탬프 조회|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/f8398aef-df32-4d0a-923b-61563cee9001" width="80%"><br>스탬프 상세조회|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/38e5fbc4-35c8-4aba-af43-de3a215b3bb2" width="80%"><br>팔로잉 조회|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/abbed917-f6b1-44b8-b7a1-ea8b474ff5e6" width="80%"><br>유저 검색|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/0ed3daaa-9b7e-4932-97b4-b32d6de5baa6" width="80%"><br>팔로워 검색|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/1f20bf82-e289-47f3-9250-c0f445071e54" width="80%"><br>좋아요 트렌드 목록|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/ca2f058a-a4f6-41d7-bf77-f7530b82f298" width="80%"><br>트렌드 상세조회|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/84f08c89-8649-48c3-a9a1-84a5732dac37" width="80%"><br>트렌드 미션|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/682c1e0f-681b-4c39-857c-844cf3e5af17" width="80%"><br>트렌드 미션 업로드|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/79d652cf-13f4-4372-9b01-6ec8ddf194da" width="80%"><br>트렌드 미션 상세조회|


## 8. ✨메인 기능
### 1. 로그인
| | |
|:-:|:-:|
|![카카오 로그인](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/bb97093e-e6ca-4936-a8fb-08ff01de5532)<br>카카오 로그인|![로그아웃](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/2dc17fe5-1346-4d8b-885a-3f9c5e240275)<br>카카오 로그아웃|

<br>

- 카카오 계정을 입력하여 로그인 할 수 있습니다.

- 로그아웃 시 서비스에서만 로그아웃/카카오 계정과 함께 로그아웃 중 선택할 수 있습니다.

- 로그인
  
  [구조]
  1. 백엔드에서 oauth/kakao/login/ 요청에 대해 카카오 로그인 페이지로 리다이렉트
  2. 사용자 로그인 완료
  3. 카카오 서버가 oauth/kakao/login/로 리다이렉트
  4. 회원가입 or 로그인이 되며 JWT 생성

- 로그인

  [구조]
  1. 백엔드에서 oauth/kakao/logout/ 요청에 대해 카카오 로그아웃 페이지로 리다이렉트
  2. 사용자 로그아웃 완료
  3. 카카오 서버가 oauth/kakao/logout/callback/로 리다이렉트
  4. 로그아웃 되며 JWT 토큰을 블랙리스트에 추가

- 회원가입

  [구조]
  1. 백엔드에서  oauth/kakao/unlink/ 요청이 오면 카카오계정과 함께 회원탈퇴
  2. 카카오 연결끊기 요청 후 user에서 delete

<br>

### 2. 사용자 관련

| | |
|:-:|:-:|
|![프로필 조회](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/57cc7003-3506-491f-acd1-d1137546ab7b)<br>프로필 조회|![프로필 수정](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/c658ba17-89c6-4ed7-ba81-44d436dd2df5)<br>프로필 수정|
|![팔로워](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/77c527c9-919f-4845-be83-843f2e0f5490)<br>팔로워 조회|![팔로잉](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/629778d3-4771-4fdc-96bc-c4105ef74f21)<br>팔로잉 조회|
|![사용자 검색](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/43ef7352-39b1-4bef-9d8a-4348bb1c9765)<br>사용자 검색|![좋아요 리스트 들어가기](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/40e7e829-368e-403a-925b-094306cd3f05)<br>좋아요한 트렌드|

<br>

- 사용자 프로필 조회가 가능합니다.

- 자신의 프로필에서는 프로필 사진, 닉네임, 자기소개를 수정할 수 있습니다.

- 팔로워 목록과 팔로잉 목록 조회가 가능합니다.

- 팔로잉 목록과 팔로잉 목록에서는 닉네임을 통해 유저 검색이 가능합니다. 팔로잉/팔로워 관계가 아닌 유저도 검색할 수 있습니다.

- 프로필에서 자신이 좋아요를 누른 트렌드 목록을 확인할 수 있습니다. 좋아요 한 트렌드 목록에서 트렌드 이름을 누르면 트렌드의 상세 페이지로 이동합니다.

<br>

### 3. 트렌드
| | |
|:-:|:-:|
|![핫 트렌드 페이지 조회](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/cd4ba3a4-3dbe-4db1-b695-88062e613fc6)<br>핫 트렌드 페이지 조회|![친구 프로필](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/b31fbd3c-abc8-4d67-94c6-69891b36e7c3)<br>다른 유저 프로필 조회|
![트렌드 좋아요,취소](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/71e1de18-4ade-4b70-9c9e-368a3ecda5a4)<br>트렌드 좋아요 등록, 취소||

<br>

- 메인 페이지에서는 슬라이드를 넘기며 핫 트렌드를 확인할 수 있습니다.

- 메인 페이지 하단에는 내가 팔로우한 유저들의 미션 인증 사진이 랜덤으로 출력됩니다. 

- 유저의 이름을 누르면 해당 유저의 프로필로 이동할 수 있습니다. 다른 유저의 프로필에서 팔로우/팔로우 취소가 가능합니다.

- 핫 트렌드를 눌러 트렌드 상세 페이지로 이동할 수 있습니다.

- 트렌드 상세 페이지에는 트렌드에 해당하는 각종 아이템들이 있습니다.

- 트렌드 상세페이지에서 해당 트렌드에 좋아요를 누를 수 있습니다. 한 번 누르면 하트가 채워지며 좋아요 수가 올라가고, 한 번 더 누르면 하트가 비워지며 좋아요 수가 내려갑니다.

<br>


### 4. 트렌드 미션

| | |
|:-:|:-:|
|![사용자의 트렌드 미션 리스트 조회](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/b6a25df3-81ac-4f4d-bd99-f0ff1146c853)<br>사용자 트렌드 미션 리스트 조회|![트렌드 상세 조회](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/6f16999c-4d33-40a3-98e0-9826f0a7b897)<br>트렌드 미션 생성|
|![트렌드 미션의 각 아이템 수정](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/bb328633-600a-4e77-b800-768ebc0373b3)<br>트렌드의 각 아이템 수정|![댓글 작성,수정,삭제](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/b99b8064-8dfd-42c2-88e0-e09d744ad9e3)<br>댓글 작성, 수정, 삭제|
|![대댓글 작성,수정,삭제](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/d63797fb-5e2c-49e2-9b85-ccd781bdbb33)<br>대댓글 작성, 수정, 삭제|![트렌드 미션 상세조회](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/0a36e455-8f8c-4e72-b995-42f9b8fdd50e)<br>트렌드 미션 페이지 상세 조회|

<br>

- 유저 프로필에서 사용자가 참여한 트렌드 미션 리스트를 확인할 수 있습니다.

- 트렌드 상세보기 페이지에서 [나도 이 트렌드 참여하기]를 누르면 트렌드 미션이 생성됩니다.

- 트렌드 상세보기 페이지에서는 해당 트렌드 미션에 좋아요/좋아요 취소를 할 수 있습니다.

- 트렌드 인증 미션으로 업로드한 아이템들은 수정할 수 있습니다.

- 댓글과 대댓글을 작성하고 자신이 작성한 댓글, 대댓글을 수정, 삭제할 수 있습니다.

<br>

### 5. 스탬프

| | |
|:-:|:-:|
|![트렌드 미션 좋아요](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/acff9700-3dc4-4fbd-93a4-0cc26328b95d)<br>스탬프 발급|![스탬프 조회](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/f63b36a8-d94c-4a66-bde0-36ae98c04202)<br>스탬프 조회|
|![스탬프 상세](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/b207bb4d-c21d-4153-b3c9-9f0f359f187e)<br>스탬프 상세 조회||

 <img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385528/9ee99b68-8ba2-47d1-803d-256c451c7e3f" width="80%"> 


<br>

- 트렌드 미션 아이템을 모두 인증했다면 스탬프를 발급 받을 수 있습니다.

- 지금까지 받은 스탬프는 프로필에서 확인할 수 있습니다. 

- 발급 받은 스탬프를 클릭하면 해당 스탬프를 발급 받은 인증 아이템과 날짜를 확인할 수 있고 [더보기]를 통해 트렌드 미션 페이지로 이동할 수 있습니다.

- [스탬프 공유하기]를 누르면 내 스탬프의 이미지가 자동으로 저장됩니다.

<br>

## 9. 💥트러블 슈팅
### 9-1. TDD many-to-many set is prohibited. fields.set() instead 에러
- 문제점
  - Django에서 Many-to-Many 관계를 다룰 때 발생할 수 있는 에러
  - TDD(Test-Driven Development) 관련 에러
  - 이 에러는 Django의 테스트 코드에서 Many-to-Many 관계에 대한 set() 메서드를 사용했을 때 발생할 수 있습니다. 
  - Django의 Many-to-Many 관계를 설정할 때는 set() 대신에 add(), remove(), clear()와 같은 메서드를 사용해야 한다고 합니다.
- 해결
  - 테스트 코드에서 set() 부분을 add()로 수정하였고 테스트 작동에 성공했습니다.

### 9-2. Django Model 필드명에서 id가 중복되는 문제
- 문제점
  - Django에서는 모델의 기본 키 필드에 대해 자동으로 'id'를 부여합니다. 따라서 기본적으로 필드명_'id'를 사용하게 되는데 그 부분을 간과하고 모델 id 필드명을 모델_id 형식으로 정의하였습니다.
  - 이로 인해 serializer로 직렬화 시 필드명_id_id로 나오는 문제가 발생하였습니다.
- 해결
  - model을 모두 재정의하여 해결하였습니다.

### 9-3. Cross-Origin Res6ource Sharing, CORS에러
- 문제점
  - 프록시 서버인 nginx설정에 add_header에 Access-Control-Allow-Credentials를 True로, Access-Control-Allow-Origin을 ‘*’로 설정하였더니 다음과 같은 에러가 발생했습니다.

  <img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/8e9fd891-61b7-49c0-8a79-78dafa4e1b12" width="80%"> 

  ```
  The value of the 'Access-Control-Allow-Origin' header in the response 
  must not be the wildcard '*' when the request's credentials mode is 'include' 
  The 'Access-Control-Allow-Origin' header contains multiple values
  ```

  - 요청의 credentials 모드가 'include'로 설정되어 있을 때 서버에서 Access-Control-Allow-Origin 헤더의 값으로 와일드카드 '*'를 사용하여 발생하였습니다. 와일드카드 '*'는 어떤 출처에서도 리소스에 접근할 수 있도록 허용하는 것을 의미하는데, credentials(쿠키 또는 HTTP 인증 등)가 요청에 포함될 때는 허용되지 않아 에러가 발생하였습니다.

- 해결
  - nginx에서 설정하지 않고 Django 프로젝트에서 와일드카드 '*' 대신 허용되는 출처를 명시적으로 설정하였고 CREDENTIALS를 True로 설정하여 해결했습니다.

  <img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/38a2f9d0-b003-49c1-8002-985ee75fcccf" width="80%"> 

### 9-4. Admin 페이지 접속 시 에러 발생
- 문제점
  - [AbstractBaseUser을 사용했을때의 상황]
     1. python manage.py createsuperuser 로 슈퍼계정 생성
     2. admin 페이지에 접속하면 에러 발생
  - AbstractBaseUser사용시 admin 페이지에 접속하려면 is_staff, is_superuser 속성과 has_perm, has_module_perms 메서드를 추가해야 하여 에러가 발생하였습니다.

- 해결
  - 너무 많은 속성을 설정해야 하므로 AbstractUser를 사용하여 해결했습니다.

### 9-5. AbstractUser사용하면서 email을 기본 필드로 사용했을 때 에러 발생
- 문제점
  - supercreateuser를 만들려고하면 다음과 같은 에러가 발생했습니다.
  ```
  TypeError: UserManager.create_superuser() missing 1 required positional argument: 'username'
  ```
  - username을 없애고 email을 기본 필드로 하도록 했는데 create_superuser은 username이 필요하다는 것이었습니다.
  - 에러 발생 원인은 AbstractUser는 username 필드를 요구한다는 것입니다. 이 모델은 Django의 내장 UserManager와 함께 제공됩니다. 만약 email을 기본 필드로 사용하고자 한다면, 커스텀한 사용자 모델을 만들어야 합니다.
- 해결
  - AbstractUser에 커스텀한 사용자 모델을 넣어 의도한 대로 실행할 수 있었습니다.



## 10. 💬회고
#### ✅고동우
- 프로젝트 회고
```
[다양한 기술 스택 경험]
프론트엔드도 직접 구현하여 HTML, JavaScript, 백엔드는 Python Django, DB는 PostgreSQL,
테스트는 TDD, 인프라로 Lightsail, RDS, S3 등 아주 다양한 기술 스택을 다루어 볼 수 있었습니다.

[테스트 코드의 중요성]
TDD를 적용하여 새로운 API를 개발하고 이전의 다른 API들이 문제없이 작동하는지 테스트를 해 볼 수 있어서 너무 좋았고 
팀원들의 코드에 신뢰성이 더해지는 큰 장점이 있다는 걸 경험했습니다.
테스트에 실패하면 어느 부분이 틀렸는지 추적하는 재미도 있었던 것 같습니다.

[PR, 소통의 중요성]
팀원의 최소 2인 이상이 승인하지 않으면 PR를 merge 하지 못하도록 하여 작업을 합치기 위해선 꼭 승인받아야 했습니다. 
그 때문에 매일 데일리 스크럼을 통해 만나기로 하여 진행 중인 작업을 공유하고 
하루 계획과 목표를 정하면서 프로젝트를 진행했기 때문에  팀원 간의 소통이 활발해졌고, 계획대로 프로젝트를 완수할 수 있었습니다.
```
- 프로젝트 소감
```
django를 배운 게 엊그제 같은데 어느새 하나의 프로젝트를 기획하고 직접 구현해 보았다는 게 믿기지 않았습니다. 
처음으로 팀장으로서 프로젝트를 이끌어 보게 되어 문서 작업도, notion과 같은 협업 도구도 다루는데 서툴렀지만 
팀원분들의 뛰어난 실력과 활발한 소통, 협력으로 잘 마무리 할 수 있었습니다. 
이번 기회를 통해 개발, 서버 배포, CI/CD, 브랜치 전략 등 값진 경험을 해 볼 수 있었습니다.
부족한 팀장인데도 잘 따라준 팀원들께 다시금 감사드립니다.
```

#### ✅김나영
- 프로젝트 회고
```
[기술 스택에 대한 고민]
프로젝트를 시작하면서 기술 스택을 결정하는 과정에서 많은 고민이 있었습니다. 
파이썬과 장고를 선택하는 것은 상대적으로 자연스러운 선택이었지만,
모놀리식과 마이크로서비스 중 어떤 방향으로 나아갈지부터 시작하여 프론트엔드, 데이터베이스, 배포 방식 등을 고민하게 되었습니다.
이러한 결정에 있어 가장 큰 고려 요소는 비용이었으며, 
그 다음으로 프로젝트 규모와 기술 구현력을 고려하여 결정하게 되었습니다. 
특히 기술 구현력은 프로젝트의 성공에 중요한 영향을 미칠 것으로 판단하여 이를 심사숙고하게 되었습니다.

[소셜 로그인 과정]
보다 쉽고 편리한 사용자 경험을 제공하기 위해 소셜 로그인을 하기로 결정했습니다. 
카카오 소셜 로그인을 도입하려고 했지만, 직접 구현하는 과정에서 예상보다 복잡하고 어려운 작업이었습니다. 
소셜 로그인의 동작 원리를 깊게 공부하기위해 alluth 라이브러리 도움 없이 직접 REST API활용을 하게 되었는데, 
소셜로그인이 되는 과정을 이해하고 작업하는 기간이 많이 필요했습니다. 
백엔드위주로 생각하고 작업을 했었는데, 
프론트로 연결하는 과정에서 미처 생각하지도 못한 리다이렉트하는 과정이 있어서 이 문제를 급하게 수습하느라 작업 시간이 꽤 길어진 것이 아쉽습니다. 
다음에는 프론트에서 code를 받아 백엔드에서 처리한후 프론트서버로 리다이렉트하는 절차를 고려하여 구현할 계획입니다.

[확인의 중요성]
이번 프로젝트를 통해 Pull Request를 통해 코드 리뷰를 진행하는 소중한 경험을 하였습니다. 
개발 과정에서 아직 부족한 부분이 많았기에 적극적으로 코멘트를 달지 못했던 것이 아쉬웠습니다. 
그러나 팀원들과의 코드 리뷰를 통해 다양한 시각과 의견을 접하고, 이를 반영함으로써 프로젝트 코드의 품질을 상승시킬 수 있었습니다.
더불어, 테스트 코드의 중요성을 더욱 깨닫게 되었습니다. 
이전에는 코드 변경 시 수동으로 확인하고 테스트했지만, 
이번 프로젝트에서 테스트 코드를 작성하고 자동화된 테스트를 통해 코드 변경 시 자동으로 확인할 수 있었습니다. 
이를 통해 테스트 코드 작성이 코드 품질을 향상시키는 데에 필수적임을 더욱 명확하게 이해하게 되었습니다. 
코드의 변경이나 추가 시 테스트 코드를 작성하고 실행함으로써 개발 과정에서 발생할 수 있는 오류를 사전에 방지할 수 있다는 것을 깨달았습니다.
```
- 프로젝트 소감
```
프로젝트 기획을 구현하기 위해 개인적인 여건을 배제하고 작업에 몰입했습니다. 
작업 속도가 느린 편이어서 구현이 어려울 것이라 생각했지만, 그래서 오히려 휴식 없이 열심히 노력했습니다. 
때로는 포기하고 싶은 마음도 있었지만, 
서로 응원하면서 격려하는 분위기 덕분에 견뎌낼 수 있었습니다.
개인적으로 이것저것 모두 해보고 싶었지만 작업할 수 있는 시간이 한정적이다보니 할 수 있는 것들을 찾아서 하느라 아쉬움이 있는데, 
PR 리뷰와 데일리 스크럼 같은 협업 과정을 경험하면서 개발자로 성장하는 기회를 얻게 되어 매우 뿌듯합니다.
팀원들과 함께하는 과정이 정말 값진 경험이었습니다. 
이런 경험을 바탕으로 다른 환경에서도 쉽게 적응할 수 있는 개발자로 성장한 것 같습니다.
```

#### ✅박정현
- 프로젝트 회고
```
[코드에 대한 공부]
코드에 대해 제대로 알아보지 않고 사용했다가 다른 팀원분이 시간을 더 할애하여 코드를 수정해 주시게 되었습니다.
앞으로는 코드 하나를 쓰더라도 무턱대고 사용하지 않고
다른 곳에 영향은 없는지, 어떤 뜻을 가지고 있는지 한번 돌아보고 사용해야 겠다고 느꼈습니다.

[협업]
잘 모르는 분야가 있으면 서로 도와주는 팀원들을 통해 많은 것을 배웠습니다.
남들에게 내가 알려주는 것을 나누는 것이 쉽지 않은데, 선뜻 시간을 내서 도와준 팀원들에게 감사합니다.
기초적인 것을 헷갈리고 모르더라도 천천히 알려주는 팀원들 덕분에 여기까지 올 수 있었습니다.
나도 남들에게 나의 지식을 이런 방식으로 나누고 도와주고 싶다는 생각을 하였습니다.

[시작이 반이다]
프로젝트 시작에 대한 두려움이 앞섰습니다.
늘 시작하는 것을 어렵게 생각하였습니다. 
이번에도 하나의 창을 띄우기까지 오래 걸렸으나 막상 시작해보니 생각보다 코드가 금방 완성되었습니다. 
이를 통해 우선 무턱대고 시작해보는것이 얼마나 시간을 단축 시켜주는지를 깨달았습니다.
```

- 프로젝트 소감
```
소통의 가치에 대해 깨닫게 되는 프로젝트였습니다.
개인적으로 느끼는 아쉬운 것은 제가 더 소통을 잘했으면 하는 아쉬움이 남습니다.
처음 만난 네 사람이 서로 다른 성향, 서로 다른 방식을 가지고 협업하기란 쉬운 것이 아니었습니다.
하지만 끊임없는 소통을 하였고 서로가 배려하며 하나의 목표를 위해 달려갔습니다.
상대방의 입장에서 생각해 보며 서로의 마음을 더 이해하게 된 것 같습니다.
스스로도 부끄러운 실수도 있었고 도움이 많이 되지 못 한것 같아 반성하는 마음을 가졌습니다.
그래서 코드 뿐만 아니라 외적인 곳에도 신경을 쓰게 되었는데, 그것 또한 새로운 경험이 되었습니다.
많이 배려해준 팀원들 덕분에 좋은 결과물을 낼 수 있어서 감사한 마음이 듭니다.
```

#### ✅이수빈
- 프로젝트 회고
```
[GitHub 활용]
이번 팀 프로젝트에서 깃허브를 활용하여 협업하는 과정을 경험했습니다. 
각 팀원이 개별적인 브랜치에서 작업을 진행하고, PR을 통해 변경 내용을 함께 검토하며 통합해나갔습니다. 
깃허브 이슈와 PR을 함께 활용하여 진행하니 프로젝트의 전반적인 진행 상황을 명확히 확인할 수 있었습니다. 
PR을 올릴 때는 템플릿을 활용했는데 PR을 올리기 전, 템플릿을 작성하며 내가 작성한 코드, 구현한 기능에 대해서 다시 한번 생각해보고 돌아보는 시간을 가질 수 있었습니다.

[개발 환경]
이번 프로젝트에서는 프론트엔드 개발과 백엔드 개발, 배포까지 다양한 환경에서 다양한 기술을 접할 수 있었습니다. 
낯설었던 만큼 어려운 부분이 많아 속도가 더디고 힘들기도 했지만 다양한 경험을 해볼 수 있어서 즐거웠습니다.
```

- 프로젝트 소감
```
배운 것도 얻어가는 것도 많았던 프로젝트였습니다. 
기획 단계부터 배포까지 꾸준히 열정적인 팀원분들 덕분에 자극을 받아 저도 끝까지 열심히 할 수 있었습니다. 
처음 프로젝트를 시작할 때는 내가 정말 끝까지 잘할 수 있을까하는 걱정이 컸고, 걱정했던 만큼 API를 개발하는 것, TDD를 작성하는 것, 개발한 것을 배포하는 것 모두 쉽지 않았습니다. 
하지만 포기하지 않고 공부하고 팀원분들의 도움을 받아 해냈을 때의 성취감이 더 컸습니다.
포기하지 않고 끝까지 해내서 결과를 만들어낸 과정이 저에게 정말 소중한 경험이 되었습니다. 
```
 
