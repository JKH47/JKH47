import hashlib

class Member:
    def __init__(self, name, username, password):
        if len(name) == 0 or len(username) == 0 or len(password) == 0:
            raise ValueError("이름, 아이디, 비밀번호는 비어있을 수 없습니다.")
        self.name = name
        self.username = username
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        print(f"이름: {self.name}, 아이디: {self.username}")

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

# 회원 인스턴스 생성
members = []
for i in range(3):
    while True:
        try:
            name = input(f"이름을 입력하세요 ({i + 1}번째 회원): ")
            username = input(f"아이디를 입력하세요 ({i + 1}번째 회원): ")
            password = input(f"비밀번호를 입력하세요 ({i + 1}번째 회원): ")
            member = Member(name, username, password)
            members.append(member)
            break
        except ValueError as e:
            print(f"입력이 잘못되었습니다. 다시 시도해주세요. 오류 메시지: {e}")

# 회원 정보 출력
for member in members:
    member.display()

# 게시글 입력 받기
posts = []
for i in range(3):
    title = input(f"게시글 제목을 입력하세요 ({i+1}번째회원의 게시물): ")
    content = input(f"게시글 내용을 입력하세요 ({i+1}번째회원의 게시물 내용): ")
    for j in range(3):
        post = Post(title, content, members[i].username)
        posts.append(post)

# 게시글 정보 출력
for post in posts:
    print(f"게시글 제목: {post.title}, 게시글 내용: {post.content}, 작성자: {post.author}")

# 특정 유저가 작성한 게시글 제목 프린트
for post in posts:
    if post.author == members[0].username:
        print(post.title)

# 특정 단어가 게시물 내용에 포함된 게시글 제목 프린트
for post in posts:
    if "content" in post.content:
        print(post.title)

# 특정 단어가 게시물 내용에 포함된 게시글 제목 프린트
while True:
    specific_word = input("특정 단어를 입력하세요: ")
    found = False
    for post in posts:
        if specific_word in post.content:
            print(post.title)
            found = True
    if not found:
        print("검색된 내용이 없습니다. 다시 검색해주세요.")
    else:
        break

# 게시물 재작성 여부 물어보기
while True:
    answer = input("게시물을 재작성하시겠습니까? (y/n): ")
    if answer.lower() == 'y':
        while True:
            username = input("아이디를 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            for member in members:
                if username == member.username and hashlib.sha256(password.encode()).hexdigest() == member.password:
                    title = input("게시글 제목을 입력하세요: ")
                    content = input("게시글 내용을 입력하세요: ")
                    post = Post(title, content, member.username)
                    posts.append(post)
                    break
            else:
                print("아이디 또는 비밀번호가 일치하지 않습니다. 다시 입력해주세요.")
                continue
            break
    elif answer.lower() == 'n':
        print("게시물 작성을 종료합니다.")
        print("작성한 게시물 목록을 출력합니다.")
        for post in posts:
            print(f"게시글 제목: {post.title}, 게시글 내용: {post.content}, 작성자: {post.author}")
        print("로그아웃 합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
