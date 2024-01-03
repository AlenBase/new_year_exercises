from abc import ABC, abstractmethod
from datetime import datetime

class SocialMedia(ABC):

    @abstractmethod
    def create_post(self, content):
        pass

    @abstractmethod
    def view_posts(self):
        pass

    @abstractmethod
    def leave_comment(self, post, content):
        pass

    @abstractmethod
    def manage_profile(self, name, contact_info):
        pass

class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.now()
        self.comments = []

class Comment:
    def __init__(self, user, post, content):
        self.user = user
        self.post = post
        self.content = content
        self.timestamp = datetime.now()

class TextPostInterface(ABC):

    @abstractmethod
    def get_text_content(self):
        pass

class ImagePostInterface(ABC):

    @abstractmethod
    def get_image_content(self):
        pass

class TextPost(Post, TextPostInterface):
    def __init__(self, user, text_content):
        super().__init__(user, None)
        self.text_content = text_content

    def get_text_content(self):
        return self.text_content

class ImagePost(Post, ImagePostInterface):
    def __init__(self, user, image_content):
        super().__init__(user, None)
        self.image_content = image_content

    def get_image_content(self):
        return self.image_content

class SocialMediaPlatform(SocialMedia):

    def __init__(self):
        self.users = []
        self.posts = []

    def create_post(self, user, content, post_type='text'):
        if post_type == 'text':
            new_post = TextPost(user, content)
        elif post_type == 'image':
            new_post = ImagePost(user, content)
        else:
            raise ValueError("Invalid post type")

        self.posts.append(new_post)

    def view_posts(self):
        for post in self.posts:
            print(f"{post.user.name} - {post.timestamp}: {post.content}")

    def leave_comment(self, user, post, content):
        new_comment = Comment(user, post, content)
        post.comments.append(new_comment)

    def manage_profile(self, user, name, contact_info):
        user.name = name
        user.contact_info = contact_info

if __name__ == "__main__":
    platform = SocialMediaPlatform()

    user1 = User("Maria", "maria@mail.ru")
    platform.users.append(user1)

    user2 = User("John", "john@email.com")
    platform.users.append(user2)

    platform.create_post(user1, "Hello, this is my first post!", post_type='text')
    platform.create_post(user2, "Check out this amazing photo!", post_type='image')

    platform.view_posts()

    platform.leave_comment(user1, platform.posts[0], "Nice post, Maria!")

    platform.manage_profile(user1, "Maria Gabriekyan", "newemail@email.com")

    print("\nAfter managing")
