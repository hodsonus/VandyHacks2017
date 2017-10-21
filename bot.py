import praw

#secret: y8IvOQA3KZrwAr0Qhk9e7E3mSn4
#name: FootballStatsBot
#username: FootballStatsBot
#password: Vandyhacksf17

r = praw.Reddit(user_agent= 'FootballStatsBot prototype (by /u/hodsonus and /u/xMutations)')

r.login('FootballStatsBot', 'Vandyhacksf17')

submissions = r.get_subreddit('news').get_top(limit=10)

print submissions

# subreddit = redditInstance.()
