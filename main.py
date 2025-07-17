import tweepy
import re
from textblob import TextBlob
import pandas as pd

# ✅ Step 1: Twitter API v2 Authentication
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOtZ3AEAAAAALKip03ycqgdYZUffcxqc0MXV4%2Bw%3DuDIuwQTCDZ9yMufEKlbf3TihJyV8H8vdSGZOpxEFGD3XaWbRz9"  # Replace with your token
client = tweepy.Client(bearer_token=bearer_token)

# ✅ Step 2: Test authentication
try:
    username = "elonmusk"
    user = client.get_user(username=username)

    if user.data:
        print("✅ Twitter API v2 authentication successful!")
        print(f"Fetched user: {user.data.name} (@{user.data.username})")
    else:
        print("❌ User not found or access denied.")
except Exception as e:
    print("❌ Error occurred:")
    print(e)

# ✅ Step 3: Use Dummy Tweets to Bypass Rate Limits
tweets = [
    "Zomato's food delivery is always on time and the packaging is great!",
    "Terrible experience. I got stale food and the delivery guy was rude.",
    "I use Zomato weekly. It’s decent but Swiggy is faster sometimes.",
    "Great discounts and offers every weekend. Love using this app!",
    "Why does Zomato cancel my order without notice?! So frustrating.",
]

print("\n📄 Sample Tweets:")
for t in tweets:
    print("-", t)

# ✅ Step 4: Sentiment Analysis Function
def analyze_sentiment(tweets):
    sentiments = []

    for tweet in tweets:
        analysis = TextBlob(tweet)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        sentiments.append((tweet, sentiment, polarity))

    df = pd.DataFrame(sentiments, columns=["Tweet", "Sentiment", "Polarity"])
    return df

# ✅ Run Sentiment Analysis
df = analyze_sentiment(tweets)

print("\n📊 Sentiment Analysis Preview:")
print(df.head())

# ✅ Save to CSV
df.to_csv("zomato_sentiments.csv", index=False)
print("\n✅ Sentiment CSV saved as 'zomato_sentiments.csv'")


import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ✅ Bar chart for sentiment distribution
def plot_sentiment_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='Sentiment', palette='pastel')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Tweet Count')
    plt.tight_layout()
    plt.savefig('sentiment_bar_chart.png')  # Save as image
    plt.show()

# ✅ Word cloud from all tweet text
def plot_word_cloud(df):
    all_text = ' '.join(df['Tweet'])
    wc = WordCloud(width=800, height=400, background_color='white').generate(all_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Tweets')
    plt.tight_layout()
    plt.savefig('word_cloud.png')  # Save as image
    plt.show()

# ✅ Run the visualization functions
plot_sentiment_distribution(df)
plot_word_cloud(df)
