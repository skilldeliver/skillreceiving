def generate_hashtag(s):
    hashtag = "#" + "".join(i.strip().title() for i in s.split())
    return False if len(hashtag) > 140 or len(hashtag) == 1 else hashtag