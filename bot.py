import praw

#secret: y8IvOQA3KZrwAr0Qhk9e7E3mSn4
#name: FootballStatsBot
#username: FootballStatsBot
#password: Vandyhacksf17

r = praw.Reddit(client_id='rfYN_lq0etP5xg',
                     client_secret='y8IvOQA3KZrwAr0Qhk9e7E3mSn4',
                     user_agent='FootballStatsBot prototype (by /u/hodsonus and /u/xMutations)',
                     username='FootballStatsBot',
                     password='Vandyhacksf17')

print(r.read_only)

subr = r.subreddit('news')

print(subr)
