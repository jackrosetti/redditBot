import praw
import time
 
# Initialize PRAW with a custom User-Agent
 
r = praw.Reddit('AP Comp Sci Principles project')
 
incorrect_users = set()   # to avoid duplicates
 
for i in xrange(0,500):  # Run the loop 500 times
    comments = r.get_comments('askreddit')
    for comment in comments:
        body = comment.body.lower()
        if body.find("hard day") != -1 or body.find("bad day") != -1:
            bad_day_users.add(comment.author)
    time.sleep(120)   # Sleep for 2 minutes
 
print "You can make it through the day!"
for user in bad_day_users:
    print user