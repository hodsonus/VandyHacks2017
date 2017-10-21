import praw

#secret: y8IvOQA3KZrwAr0Qhk9e7E3mSn4
#name: FootballStatsBot
#username: FootballStatsBot
#password: Vandyhacksf17

reddit = praw.Reddit(client_id='rfYN_lq0etP5xg',
                     client_secret='y8IvOQA3KZrwAr0Qhk9e7E3mSn4',
                     user_agent='FootballStatsBot prototype (by /u/hodsonus and /u/xMutations)',
                     username='FootballStatsBot',
                     password='Vandyhacksf17')

#prints false because we have permission to write
print(reddit.read_only)

subr = reddit.subreddit('learnpython')

# print(subr.description)

# for submission in reddit.subreddit('learnpython').hot(limit=10):
#     print(submission.title)
