#
# Given a rows x cols screen and a sentence represented as a list of strings, 
# return the number of times the given sentence can be fitted on the screen.
# The order of words in the sentence must remain unchanged, 
# and a word cannot be split into two lines. A single space must separate two consecutive words in a line.


# 359. Logger Rate Limiter
# Runtime: 32 ms, faster than 95.79% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 14.3 MB, less than 31.99% of Python3 online submissions for Bulls and Cows.

class Solution1 :
    from collections import Counter
    def getHint(self, secret: str, guess: str) -> str:
        cows = bulls = 0 
        for i in range(len(secret)) :
            if guess[i] == secret[i]:
                bulls += 1 
        secret_cnt = Counter(secret)
        guess_cnt =  Counter(guess)
        guess_cnt_keys = guess_cnt.keys()
        for key in secret_cnt.keys():
            if key in guess_cnt_keys :
                cows += min(guess_cnt[key], secret_cnt[key])
                
        cows -= bulls 
        return "{}A{}B".format(bulls, cows)
