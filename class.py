class member:
    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password

    def display_member_info(member):
        print(f"회원 이름: {member.name}")
        print(f"회원 아이디: {member.id}")

    def display(self):
        print(f"Name: {self.name}, Id: {self.id}")

class post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

members = []


member1 = member("Kim ji ho","kimjiho","password1")
member2 = member("Lee seung ho", "leeseungho","password2")
member3 = member("Na tae gyung","nataegyung","password3")

members.append(member1)
members.append(member2)
members.append(member3)

for member in members:
    member.display()

posts = []

post1 = post("First Post", "Good Morning", member1.id)
post2 = post("Second Post", "Nice to meet you", member2.id)
post3 = post("Third Post", "Have a nice day", member3.id)
post4 = post("Fourth Post", "Keep in all", member1.id)
post5 = post("Fifth Post", "Take this", member2.id)
post6 = post("Sixth Post", "Nice Content", member3.id)
post7 = post("Seventh Post", "This content is interesting", member1.id)
post8 = post("Eighth Post", "What is this content?", member2.id)
post9 = post("Ninth Post", "Take over the content", member3.id)

posts.append(post1)
posts.append(post2)
posts.append(post3)
posts.append(post4)
posts.append(post5)
posts.append(post6)
posts.append(post7)
posts.append(post8)
posts.append(post9)

for post in posts:
    if post.author == member1.id:
        print(post.title)

search_word = "content"
for post in posts:
    if search_word in post.content:
        print(post.title)
