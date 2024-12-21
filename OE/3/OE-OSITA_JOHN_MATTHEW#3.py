class SocialMediaAccount():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
            pass
    def post(self):
            pass
    
class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, num_of_followers):
        super().__init__(username, password)
        self.num_of_followers = num_of_followers
    def share_story(self):
        print(f"{self.username} has {self.password} and {self.num_of_followers}")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, num_of_tweets):
        super().__init__(username, password)
        self.num_of_tweets = num_of_tweets
    def tweet(self):
        print(f"{self.username} has {self.password} and {self.num_of_tweets}")

insta = InstagramAccount("Miya","123","51 followers")
xbird = TwitterAccount("Miya","123","51 tweets")

insta.share_story()
xbird.tweet()
