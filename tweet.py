from collections import Counter

tweets  = ['sachin tweet_id_1', 'sehwag tweet_id_2', 'sachin tweeet_id_3']
names = [tweet_name.split()[0] for tweet_name in tweets]
times = Counter(names)
print(times)




