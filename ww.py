import random
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word=random.choice(word_bank)
c=['_']*len(word)
n=10
while(n>0):
    print("Current Word:",*c)
    s=input("Guess a Letter:").lower()
    if s in word:
        for i in range(len(word)):
            if word[i]==s:
                c[i]=sS
        print("Great guess!")
        if c==list(word):
            print(f"Congrulation ! you guessed the word:{word}")
            break
    else:
        n-=1
        print(f"Wrong guess! Attempts left: {n}")
    
    
    
