# HotCake

## 📝목차
[1. 프로젝트 소개](#1-🎉프로젝트-소개)<br>
[2. 팀 소개](#2-🧑팀-소개)<br>
[3. 개발 전략](#3-💡개발-전략)<br>
[4. 개발 환경 및 개발 일정(WBS)](#4-🧐개발-환경-및-개발-일정wbs)<br>
[5. 배포 URL 및 프로젝트 구조](#5-📦-배포-url-및-프로젝트-구조)<br>
[6. 데이터베이스 모델링(ERD)](#6-🔍데이터베이스-모델링erd)
[7. URL 명세](#7-🔨-url-명세)
[8. 와이어프레임/UI](#8-💄와이어프레임ui)<br>
[9. 메인 기능](#9-✨메인-기능)<br>
[10. 트러블 슈팅](#10-💥트러블-슈팅)<br>
[11. 개발하며 느낀 점](#11-💬개발하며-느낀-점)<br>


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
```
서비스를 이용해볼 수 있는 테스트 계정입니다.
ID:
PWD:
```

```
저희 팀은 트렌드에 민감한 젊은 층을 겨냥하여 핫 트렌드에 관한 정보를 제공하는 SNS 서비스를 제작하였습니다.

핫 트렌드, Hot trend
최신의 유행 또는 많은 사람들이 따르는 경향이나 추세를 이르는 용어를 뜻합니다.

핫케이크 서비스는 현재 가장 뜨거운 최신 트렌드를 사용자에게 제공하여 사용자들이 해당 트렌드에 대한 의견을 댓글로 함께 나눌 수 있도록 합니다. 
또 사용자들은 해당 트렌드에 대한 경험을 인증할 수 있습니다. 
이를 통해 미션 리스트를 모두 채우면 스탬프를 받아 공유할 수 있습니다.

핫케이크 서비스의 이름 또한 핫 트렌드와 단어의 유사성을 갖추었을 뿐만 아니라, 핫케이크 음식의 특성상 함께 나누어 먹는 모습을 연상시켜 트렌드를 함께 나누고 공유한다는 의미를 담고 있습니다.
```


## 2. 🧑팀 소개
 #### 안녕하세요. Team Tanghuru입니다!
 |고동우       |김나영                |박정현    | 이수빈      |
|:---------|:------------------|:---------|:----------|
|<a href="https://github.com/Ko-udon">🔗Ko-udon</a>|<a href="https://github.com/nayeongdev">🔗nayeongdev</a>|<a href="https://github.com/jungloopy">🔗jungloopy</a>|<a href="https://github.com/hantang820">🔗hantang820</a>|

 
 ![20231227_105321](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/22988154-efab-4004-94e2-70429447db8f)


## 3. 💡개발 전략
### 3-1. 코드 컨벤션 [각 항목별로 접어두기]
#### 3-1-1. Python
- Black Fomatter 사용
- 변수명: snake_case
```
user_input
```
- 함수명: snake_case
```
get_user_input
```
- 클래스명: CapWords
```
TestClass
```
#### 3-1-2. HTML
#### HTML
" 먼저 ' 이후  
 ```
 " '맞아요' "
 ```
- 모든 태그는 lowercase
- 들여쓰기 2칸
- 클래스명 : 이름은 알파벳 영문 소문자, 숫자, 대쉬(-)만 작성 (예시 input-text)
- d명 : 영문 소문자, 숫자, 언더스코어(_)만 사용할 수 있다. (예시 card_list)
- HTML에서 주석 사용은 지양하기
- 컴포넌트 시작과 끝에 주석 달기
```
<!-- BEGIN NAVBAR -->
<nav>
.....
</nav>
<!-- END NAVBAR -->
```
#### script 태그
- 맨 아래 배치
  - 본문과 스크립트의 로딩 순서의 문제로 오류 발생 가능
- script를 아래 두고도 해결이 안되면 defer 속성 추가

#### 접근성
- 이미지에 alt 태그 사용
  - 로드, 경로 문제 등으로 이미지가 나오지 않을 때 텍스트가 표시되도록
- 하나의 페이지에는 하나의 h1
  - h1~h5 순서대로 나올 수 있도록하고 글자 크기가 마음에 안 들 경우 CSS에서 수정
- 제목 및 메타 태그 사용
- 페이지 완성 시 HTML 유효성 확인 (w3c 유효성 검사기)

 #### 3-1-3. CSS
- " 먼저 ' 이후

- 들여쓰기 2칸
- 인라인 스타일 사용 지양
  - (예외) 인라인 크리티컬 CSS : 중요한 CSS의 경우 맨 위에 배치

 #### 3-1-4. JavaScript
 - 먼저 ' 이후
 - 들여쓰기 2칸
 - 소스파일의 이름은 알파벳 소문자, 대쉬(-) 또는 밑줄(_)으로만 작성 (예시 main_function.js, 또는 main-function.js)
   - 대쉬(-) 또는 밑줄(_) 중 한가지만 사용
- 인라인 스크립트 사용 지양

 ### 3-2. 커밋 컨벤션 [내용 추가+접어두기]
- Commit Message 구조
```
################(필수)
# <타입> : <제목> 의 형식으로 제목을 아래 공백줄에 작성
# 제목은 50자 이내 / 변경사항이 "무엇"인지 명확히 작성 / 끝에 마침표 금지
# 예) Feat : 로그인 기능 추가

# 바로 아래 공백은 지우지 마세요 (제목과 본문의 분리를 위함)

################(권장)
# 본문(구체적인 내용)을 아랫줄에 작성
# 여러 줄의 메시지를 작성할 땐 "-"로 구분 (한 줄은 72자 이내)
# 예) 로그인 페이지를 만들고, 사용자가 이메일과 비밀번호를 입력해서 로그인할 수 있는 기능을 추가했습니다.
 로그인에 성공하면 사용자에게 성공 메시지를 표시하고, 실패하면 오류 메시지를 표시하는 기능도 추가했습니다.

################(선택)
# 꼬릿말(footer)을 아랫줄에 작성 (현재 커밋과 관련된 이슈 번호 추가 등)
# 예) Close #7
```
<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/eed15ef9-ee58-4ecd-8662-bcb460a0f464" width="50%"> 

 ### 3-3. 브랜치 전략
 [추가 작성 필요]

 ### 3-4. 협업
 - 협업 도구: <a href="https://www.notion.so/02f7c45d8b764c719ff4f2d86020f703">🔗Notion</a>, Discord
- 매일 10:00/16:00 DAILY SCRUM 진행

## 4. 🧐개발 환경 및 개발 일정(WBS)
 ### 4-1. 개발 환경

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

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/c8fc3316-595f-4668-a2a2-9319355d5983" width="80%"> 

<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/9908dfee-85a6-480f-8017-39aa497f85b8" width="80%"> 



- [기획] 주제 선명 및 기획·화면 설계<br>
 2023-12-08 ~ 2023-12-12

- [개발]<br>
2023-12-13 ~ 2023-12-22

- [배포 및 연동]<br>
2023-12-23 ~ 2023-12-26

- [발표자료 제작 및 코드 리펙토링]<br>
2023-12-27 ~ 2023-12-28



## 5. 📦 배포 URL 및 프로젝트 구조
### 5-1. 배포 URL
#### 5-1-1. Front-End
- http://team-hotcake.s3-website.ap-northeast-2.amazonaws.com/
- Front-End Repo: https://github.com/HotCake-Tanghuru/HotCake-FE

#### 5-1-2. Back-End
- http://43.202.230.2/oauth/kakao/login
- Back-End Repo: https://github.com/HotCake-Tanghuru/HotCake-BE

### 5-2. 아키텍처
![20231226_112511](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/103997c8-9445-4a10-9336-79761b905211)


### 5-3. 기능명세
![20231227_110230](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/da5c8d16-fc50-451e-8d4f-40fb55062857)


### 5-4. 플로우차트

![20231226_154237](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/aaa7e956-650d-4daf-8c7d-34752c53f38f)


## 6. 🔍데이터베이스 모델링(ERD)
#### ERD는 <a href="https://www.erdcloud.com/d/auuFJgN4MHHFGfG4Z">🔗ERDcloud</a>에서 제작하였습니다.

![20231227_125840](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/0ea857b3-f779-4b46-9fcb-7d628b4663b8)

## 7. 🔨 URL 명세

<a href="http://43.202.230.2/oauth/kakao/login">🔗 Swagger</a>
<br>
<a href="http://43.202.230.2/oauth/kakao/login">🔗 카카오 회원가입</a>

 - 인증/인가

| App       | URL                                        | Method    | HTML File Name      | Note           |
|-----------|--------------------------------------------|-------------------|---------------------|----------------|
| accounts      | '/oauth/kakao/login'   | GET        | login.html       |카카오 로그인 페이지 이동 |
| accounts      | '/oauth/kakao/login/callback'| GET | login.html   |로그인(토큰 생성)|
| accounts      | '/oauth/kakao/logout'    | POST| login.html |카카오 로그아웃 페이지 이동 |
| accounts      | '/oauth/kakao/logout/callback'      | GET | login.html | 로그아웃(토큰 삭제) |
| accounts      | '/oauth/kakao/unlink/'  | POST | login.html | 회원탈퇴 (연결 끊기) |


- 사용자

| App       | URL                                        | Method    | HTML File Name      | Note           |
|-----------|--------------------------------------------|-------------------|---------------------|----------------|
| accounts      | 'account/users/{userId}'   | GET  | user_profile.html |사용자 프로필 조회 |
| accounts      | 'account/users/{userId}'   | PATCH  | .html |사용자 프로필 수정 |
| accounts      | 'account/users/{userId}/following'   | GET  | .html |팔로잉 조회 |
| accounts      | 'account/users/{userId}/following/{followingId}'   | POST  | .html |팔로잉 추가 |
| accounts      | 'account/users/{userId}/following/{followingId}'   | DELETE  | .html |팔로잉 취소 |
| accounts      | 'account/users/{userId}/follower'   | GET  | .html |팔로워 조회 |
| accounts      | 'account/users/{userId}/follower/{followerId}'   | DELETE  | .html |팔로워 삭제 |
| accounts      | 'account/users?nickname={nickname}'   | POST  | .html |유저 검색 |


- 핫 트렌드

| App       | URL                                        | Method    | HTML File Name      | Note           |
|-----------|--------------------------------------------|-------------------|---------------------|----------------|
| trends     | 'trends'   | GET  | .html |핫 트렌드 조회 |
| trends     | 'trends/{trendId}'   | GET  | .html |핫 트렌드 상세 조회 |
| trends     | 'trends/{trendId}/likes'   | GET  | .html |좋아요 목록 조회 |
| trends     | 'trends/{trendId}/likes'   | PATCH  | .html |좋아요 누르기 |
| trends     | 'trends/{trendId}/likes'   | DELETE  | .html |좋아요 취소 |



- 트렌드 미션

| App       | URL                                        | Method    | HTML File Name      | Note           |
|-----------|--------------------------------------------|-------------------|---------------------|----------------|
| trend-missions | 'trend-missions/create'   | POST  | .html |미션 생성 |
| trend-missions | 'trend-missions/{userid}' | GET  | .html |사용자의 미션 리스트 조회 |
| trend-missions | 'trend-missions/about/{trendMissionId}'   | GET  | .html |미션 페이지 상세 조회 |
| trend-missions | 'trend-missions/mission-item/{userTrendMissionId}/edit'   | PATCH  | .html |미션 수정 |
| trend-missions | 'trend-missions/{trendMissionId}/likes'   | PUT  | .html |미션 좋아요+좋아요 취소 |
| trend-missions | 'trend-missions/comments'   | POST  | .html |댓글 작성 |
| trend-missions | 'trend-missions/comments'   | PATCH  | .html |댓글 수정 |
| trend-missions | 'trend-missions/comments'   | POST  | .html |댓글 삭제 |
| trend-missions | 'trend-missions/comments/{commentId}/replies'   | POST  | .html |대댓글 작성 |
| trend-missions | 'trend-missions/comments/{commentId}/replies'   | PATCH  | .html |대댓글 수정 |
| trend-missions | 'trend-missions/comments/{commentId}/replies'   | DELETE  | .html |대댓글 삭제 |


- 스탬프

| App       | URL                                        | Method    | HTML File Name      | Note           |
|-----------|--------------------------------------------|-------------------|---------------------|----------------|
| trend-missions | 'trend-missions/{trendMissionId}/complete'   | PATCH  | .html |스탬프 발급 |
| trend-missions | 'users/{userId}/stamp'   | GET | .html |스탬프 목록 조회 |
| trend-missions | 'users/stamp/{stampId}'   | GET | .html |스탬프 상세 조회 |


## 8. 💄와이어프레임/UI
#### 와이어프레임 및 화면설계는 <a href="https://www.figma.com/file/b1Z1IOn1wkd32PatV0r66t/Hotcake%EC%99%80%EC%9D%B4%EC%96%B4%ED%94%84%EB%A0%88%EC%9E%84-%EA%B3%B5%EA%B0%9C%EC%9A%A9?type=design&node-id=0-1&mode=design&t=66Ysr5jxikCB9WDh-0">🔗Figma</a>에서 제작하였습니다.


### 8-1. 와이어프레임
![사용자](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/60b131d6-305e-4fd7-9c5b-cf823b8278a7)

![트렌드](https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/ac9d06ae-822c-4dfb-b8be-5d7279b25bcc)

### 8-2. 화면설계
| | |
|:-:|:-:|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/71d7d4b3-5d86-4309-a50c-60dba87b3504" width="100%">카카오 로그인|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/759d414f-6085-4370-a119-92ed166f9523" width="100%">메인 페이지|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/4d4eb452-1055-4469-af40-cbf9bb9c2dfd" width="100%">사용자 프로필|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/219ff5d4-e032-4ab4-a61b-4714abc90213" width="100%">프로필 수정|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/261d2d8f-b6bb-4727-86e3-82cc76ae8df0" width="100%">스탬프 조회|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/f8398aef-df32-4d0a-923b-61563cee9001" width="100%">스탬프 상세조회|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/38e5fbc4-35c8-4aba-af43-de3a215b3bb2" width="100%">팔로잉 조회|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/abbed917-f6b1-44b8-b7a1-ea8b474ff5e6" width="100%">유저 검색|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/0ed3daaa-9b7e-4932-97b4-b32d6de5baa6" width="100%">팔로워 검색|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/1f20bf82-e289-47f3-9250-c0f445071e54" width="100%">좋아요 트렌드 목록|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/ca2f058a-a4f6-41d7-bf77-f7530b82f298" width="100%">트렌드 상세조회|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/84f08c89-8649-48c3-a9a1-84a5732dac37" width="100%">트렌드 미션|
|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/682c1e0f-681b-4c39-857c-844cf3e5af17" width="100%">트렌드 미션 업로드|<img src="https://github.com/HotCake-Tanghuru/HotCake-BE/assets/142385695/79d652cf-13f4-4372-9b01-6ec8ddf194da" width="100%">트렌드 미션 상세조회|


## 9. ✨메인 기능 [gif 추가]
### 1. 로그인
#### A. 카카오 로그인

#### B. 로그아웃

#### C. 회원 탈퇴


### 2. 사용자 관련
#### A. 프로필 조회

#### B. 프로필 수정

#### C. 팔로잉 조회·추가·삭제

#### D. 팔로워 조회·삭제

#### E. 사용자 검색


### 3. 트렌드
#### A. 핫 트렌드 페이지 조회

#### B. 트렌드 상세 조회

#### C. 트렌드에 좋아요 등록·취소

#### D. 사용자의 트렌드 리스트(트렌드 미션에 참여한)조회

### 4. 트렌드 미션
#### A. 사용자의 트렌드 미션 리스트 조회

#### B. 트렌드 미션 생성

#### C. 트렌드 미션의 각 아이템 수정

#### D. 댓글 작성·수정·삭제

#### E. 대댓글 작성·수정·삭제

#### F. 트렌드 미션 페이지 좋아요 등록·취소

#### G. 트렌드 미션 페이지 상세 조회

### 5. 스탬프

#### A. 스탬프 발급

#### B. 스탬프 리스트 조회

#### C. 스탬프 상세 조회


## 10. 💥트러블 슈팅

[작성필요]

## 11. 💬개발하며 느낀 점
```
고동우
```

```
김나영
```

```
박정현
```

```
이수빈
```






