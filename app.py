# Import the required libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from googleapiclient.discovery import build
from textblob import TextBlob


# Load the dataset
@st.cache_resource
def load_data():
    # Load your YouTube dataset here
    return pd.read_excel("Final_Merge(Final).xlsx")  # Update with your dataset path
df = load_data()

# Set up YouTube API key and build service
API_KEY = 'AIzaSyAYFsIiNVuar2ruuDER36UUzzYpzoh18cA'
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to get video comments using YouTube API
def get_video_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=100
    )
    while request:
        response = request.execute()
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
        request = youtube.commentThreads().list_next(request, response)
    return comments


# Function to analyze sentiment of comments
def analyze_sentiment(comments):
    positive = 0
    negative = 0
    neutral = 0
    total_comments = len(comments)

    for comment in comments:
        analysis = TextBlob(comment)
        if analysis.sentiment.polarity > 0:
            positive += 1
        elif analysis.sentiment.polarity < 0:
            negative += 1
        else:
            neutral += 1

    # Calculate percentages
    positive_percent = (positive / total_comments) * 100
    negative_percent = (negative / total_comments) * 100
    neutral_percent = (neutral / total_comments) * 100

    sentiment_percentages = {
        'positive': positive_percent,
        'negative': negative_percent,
        'neutral': neutral_percent
    }
    return sentiment_percentages

# Function to Exract the thumnail link
def get_thumbnail_url(video_id):
    # Make a request to the videos endpoint
    request = youtube.videos().list(
        part='snippet',
        id=video_id
    )
    response = request.execute()

    # Extract the thumbnail URL from the response
    thumbnail_url = response['items'][0]['snippet']['thumbnails']['default']['url']
    return thumbnail_url

# Sidebar input for video link
# video_link = st.sidebar.text_input("Enter Video Link:")

#main page
st.image("Youtubelogo.png", width=100)
st.title('Youtube Dahsboard')
st.markdown('##')

# Streamlit UI
video_id = st.sidebar.text_input("Enter YouTube Video ID (e.g., YlvcFJOE-OE):")

# Filter data based on video_id
video_data = df[df['video_id'] == video_id ]

if not video_data.empty:
    st.write("Video Title:")
    st.subheader(f"{video_data['title'].iloc[0]}")

    # Show video thumbnail
    st.image(get_thumbnail_url(video_id),width=500)

    #formating the count of KPI
    def format_number(num):
        if num >= 1_000_000:
            return f"{num / 1_000_000:.2f}M"
        elif num >= 1_000:
            return f"{num / 1_000:.1f}K"
        else:
            return num
    # st.write("Key Performance Indicators:")
    like_count = int((video_data['likeCount']))
    comment_count = int((video_data['commentCount']))
    view_count = int((video_data['viewCount']))

    # Arranging the KPI in single row
    left_column, center_column, right_column = st.columns(3)
    with left_column:
        st.subheader('Like Count')
        formatted_like_count = format_number(like_count)
        st.markdown(f"<h1 style='text-align: left; color: red; margin-bottom: 0;'>{formatted_like_count}</h1>", unsafe_allow_html=True)
        #st.subheader(f"{like_count}")
    with center_column:
        st.subheader("Comment Count")
        formatted_like_count = format_number(comment_count)
        st.markdown(f"<h1 style='text-align: left; color: red; margin-bottom: 0;'>{formatted_like_count}</h1>",
                    unsafe_allow_html=True)
        # st.subheader(f"{comment_count}")
    with right_column:
        st.subheader("View Count")
        formatted_like_count = format_number(view_count)
        st.markdown(f"<h1 style='text-align: left; color: red; margin-bottom: 0;'>{formatted_like_count}</h1>",
                    unsafe_allow_html=True)
        #st.subheader(f"{view_count}")

    # Sentiment analysis of comments (donut chart)
    st.subheader("Sentiment Analysis of Comments:")
    video_id = video_data['video_id'].iloc[0]
    comments = get_video_comments(video_id)
    sentiment_percentages = analyze_sentiment(comments)
    sentiment_labels = list(sentiment_percentages.keys())
    sentiment_values = list(sentiment_percentages.values())
    fig_sentiment = px.pie(names=sentiment_labels, values=sentiment_values, hole=0.5)
    st.plotly_chart(fig_sentiment)

    # Example: Bar chart of likeCount and commentCount
    st.subheader("Like Count vs. Comment Count")
    fig1 = px.bar(video_data, x='channelTitle', y=['likeCount', 'commentCount'], barmode='group')
    st.plotly_chart(fig1)

    # Donut chart of viewCount and likeCount
    st.subheader("View Count vs. Like Count")
    fig2 = px.pie(values=[view_count, like_count], names=["View Count", "Like Count"], hole=0.5)
    st.plotly_chart(fig2)

    # st.sidebar.markdown(f"**Selected Video Title:** {video_data['title'].iloc[0]}")
    st.sidebar.markdown(f"**Channel:** {video_data['channelTitle'].iloc[0]}")

    # Show video description
    st.sidebar.subheader("Video Description:")
    st.sidebar.text(video_data['description'].iloc[0])

else:
    # Display these of the video_id is not provided
    st.write("No data found for the provided video link.")


