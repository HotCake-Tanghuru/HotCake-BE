# HotCake-BE
서비스: 핫케이크 백엔드 개발 레포지토리


### 2.3 URL 구조
- 인증/인가

| App       | URL                                        | Method    | HTML File Name      | Note           |
|-----------|--------------------------------------------|-------------------|---------------------|----------------|
| accounts      | 'account/oauth/kakao/login'   | GET        | login.html       |카카오 소셜 로그인 |
| accounts      | '//kauth.kakao.com/oauth/authorize'| GET | login.html   |카카오 인가 코드 받기|
| accounts      | '//kauth.kakao.com/oauth/token'    | POST| login.html |카카오 토큰 받기 |
| accounts      | '//kapi.kakao.com/v2/user/me'      | GET | login.html | 카카오 사용자 정보 가져오기 |
| accounts      | '//kapi.kakao.com/v1/user/logout'  | POST | login.html | 로그아웃 (토큰 삭제) |
| accounts      | '//kapi.kakao.com/v1/user/unlink'  | POST | login.html | 회원 탈퇴(연결 끊기) |


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
| trends     | 'trends/{trendId}/likes'   | POST  | .html |좋아요 누르기 |
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
  







