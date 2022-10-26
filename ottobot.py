# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:42:38 2022

@author: nayeem
"""

import praw
import random
import time
reddit = praw.Reddit(
    client_id="UpkkS1hNaYsJsG7v1m3CZQ",
    client_secret="QdpeDbVZuZ_yv_5WKiUFgPApf0QzrQ",
    user_agent="<console:OttoBot:1.0>",
    username = "Otto-Hightower", 
    password = "Kontol42069", 
    check_for_async=False
)

subreddit = reddit.subreddit("ottobot_test")

otto_quotes = ["The road ahead is uncertain, but the end is clear.",
               "The time is coming, Alicent. Either you prepare Aegon to rule, or you cleave to Rhaenyra and pray for her mercy.",
               "The gods have yet to make a man who lacks the patience for absolute power.",
               "No king has ever lived that hasn’t had to forfeit the lives of a few to protect the many.", 
               "A seat at the King’s table does not make you his equal.", 
               "We play an ugly game. And now, for the first time, I see that you have the determination to win it.", 
               "Stale oaths will not put you on the Iron Throne, Princess. The succession changed the day your father sired a son. I only regret that you and he were the last to see the truth of it.", 
               "I promise you, in time, you and I together will prevail.", 
               "All of you, Sheath the fucking steel"]

for submission in subreddit.hot(limit=10):
    #print(submission.title)
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if "otto" in comment_lower:
                print("---------")
                print(comment.body)
                random_index = random.randint(0, len(otto_quotes) - 1)
                comment.reply(otto_quotes[random_index])
                time.sleep(2)
                