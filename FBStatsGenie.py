#!/Users/johnhodson/anaconda/bin/python
import praw
import nflgame
import nflgame.player

#client id: rfYN_lq0etP5xg
#secret: y8IvOQA3KZrwAr0Qhk9e7E3mSn4
#username: FootballStatsBot
#password: Vandyhacksf17

#create reddit instance that has permission to write
reddit = praw.Reddit(client_id='rfYN_lq0etP5xg',
                     client_secret='y8IvOQA3KZrwAr0Qhk9e7E3mSn4',
                     user_agent='FBStatsGenie prototype (by /u/hodsonus and /u/xMutations)',
                     username='FBStatsGenie',
                     password='vandyhacksfall2017')

#subreddit that we will be operating in
subr = reddit.subreddit('FBStatsTestingGrounds')

commented = open("commented.txt", "r+")
lines = commented.readlines()

#for a submission, subm, in the subreddit we are operating in. look at 'limit' amount of hot submissions.
for subm in subr.new(limit=None):

    #remove all instances of 'MoreComments' in the CommentForest
    subm.comments.replace_more(limit=0)

    #scan over each comment instance in the CommentForest
    for comm in subm.comments.list():

        callIndex = comm.body.find("!FBStatsGenie")

        #looks to see if comment has been replied to before
        found = False
        for line in lines:
            if line.startswith(comm.id):
                found = True
                break

        #if the bot call is present in the comment and the comment has not been replied to
        if (callIndex >= 0) and not found:
            yearStart = -1
            playerStart = callIndex + 14

            #this try block assumes that the bot call is in propoer format.
            #the bot call should be formatted as '!FootballStats PLAYER NAME YEAR'
            #and should be the last part of the reddit comment
            try:
                #searches for the first instance of an integer after the bot call
                for i in range (len(comm.body)-playerStart):
                    if comm.body[i+playerStart].isdigit():
                        yearStart = i+playerStart
                        break

                #the player name is the start of the name through the start of the year minus one.
                #the year will be from the start of the year until the end of the string
                player = comm.body[playerStart:yearStart-1]
                year = int(comm.body[yearStart:])

                #create player object list and pull the first instance from the list
                playerObj = nflgame.find(player, team=None)[0]

                #format the response string and reply to the comment
                response = playerObj.name + ": " + str(year) + "\n\n" + playerObj.stats(year, week=None).formatted_stats()
                comm.reply(response)

                #append the comment ID to the commented.txt file to ensure that it is replied to
                #only once
                commented.write(comm.id)
                commented.write("\n")

            #if there was an exception thrown at any point through here, the bot call was not
            #properly formatted
            except:
                pass
