#1. 깃헙 레포지토리를 만든다. 좌측의 new에서 만들 수 있다.
#2. 깃헙 레포지토리를 만들면, 첫 화면에 가이드가 나온다. 가이드 보고 참고하는게 좋고, 아래 지시사항을 따라하면 좋다.
#3. 내가 저장하고 싶은 파일들이 있는 폴더 안으로 들어간다. 
#4. 터미널에서 git bash (우측 하단)를 킨다.
#5. git init (들어가 있는 폴더가 git에 의하여 통제 받을 구역이라는 것을 의미한다)
#6. git add . (.은 "현재 폴더"를 의미한다. 즉, git에 반영할 파일들은 이 폴더 내의 모든 파일을 의미한다)
#7. git commit -m "first commit" ("first commit"은 내가 이번 코드를 수정할 때 했던 작업을 자유롭게 넣는다, 어떠한 변동사항을 만들었는지 이름표를 만드는 것)
#8. git remote add origin [레포지토리 url 주소].git (예시 git remote add origin https://github.com/JUUUNEEE/git_test.git )
#코드를 올릴 주소를 설정하는 과정이다
#9. git push origin master (git add . 해서 모인 모든 파일들을 레포지토리에 올림)
#10. 코드나 파일이 수정되었을 때 6, 7, 9을 진행한다. 이 때 7에서 "first commit"을 내가 한 작업으로 변경하는 것만 다르다 (모든 수정 사항들이 다 반영된다)

print("마지막 수업")
