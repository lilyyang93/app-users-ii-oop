class User:

    all_posts = []

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.user_post_storage = []
    
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nUsername: {self.username}\nEmail: {self.email}"
    
    def create_post(self, post):
        self.user_post = {}
        self.post = post
        self.user_post[self.username] = post
        self.user_post_storage.append(self.user_post)
        self.all_posts.append(self.user_post)

    def view_posts(self):
        return self.user_post_storage
    
    def delete_post(self, post):
        for p in self.user_post_storage:
            if p[self.username] == post: #this will access the value of the dictionary
                self.user_post_storage.remove(p)
        return self.user_post_storage
   
user1 = User('Lily', 'Yang', 'lilyyang', 'lilyyang@email.com')
user2 = User('Alex', 'Song', 'alexsong', 'alexsong@email.com')

user1.create_post('user 1 posting')
user2.create_post('user 2 posting')
user1.create_post('user 1 posting again')

print(User.all_posts)
print(user1.view_posts())
print(user1.delete_post('user 1 posting'))
