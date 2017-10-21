import praw

#client id: rfYN_lq0etP5xg
#secret: y8IvOQA3KZrwAr0Qhk9e7E3mSn4
#username: FootballStatsBot
#password: Vandyhacksf17

#create reddt instance that has permission to write
reddit = praw.Reddit(client_id='rfYN_lq0etP5xg',
                     client_secret='y8IvOQA3KZrwAr0Qhk9e7E3mSn4',
                     user_agent='FootballStatsBot prototype (by /u/hodsonus and /u/xMutations)',
                     username='FootballStatsBot',
                     password='Vandyhacksf17')

#subreddit that we will be operating in
subr = reddit.subreddit('fakeid')

#for a submission, subm, in the subreddit we are operating in. look at 'limit' amount of hot submissions.
for subm in subr.hot(limit=1):

    print("Title: ", subm.title)
    print("Text: ", subm.selftext)
    print("Score: ", subm.score)
    print("---------------------------------\n")

    #remove all instances of 'MoreComments' in the CommentForest
    subm.comments.replace_more(limit=0)

    #scan over each comment instance in the CommentForest
    for comm in subm.comments.list():
        print(comm.body, "\n")
        comm.body.find("retard")
