from instagramy import InstagramUser
 

# Connecting the profile
user = InstagramUser("geeks_for_geeks")
 
# printing the basic details like
# followers, following, bio
print(user.is_verified())
print(user.popularity())
print(user.get_biography())
 
# return list of dicts
posts = user.get_posts_details()
 
print('\n\nLikes', 'Comments')
for post in posts:
    likes = post["likes"]
    comments = post["comment"]
    print(likes,comments)