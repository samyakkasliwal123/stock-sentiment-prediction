from googleapiclient.discovery import build

# Set up the YouTube Data API v3 service
api_key = "YOUR_API_KEY"  # Replace with your own API key
youtube = build('youtube', 'v3', developerKey=api_key)

# Define the search query
search_query = "stock sentiment prediction"  # Replace with your desired search query

# Execute the search request
search_response = youtube.search().list(
    q=search_query,
    part='snippet',
    maxResults=10
).execute()

# Process the search results
for search_result in search_response.get('items', []):
    video_title = search_result['snippet']['title']
    video_id = search_result['id']['videoId']
    print(f"Title: {video_title}")
    print(f"Video ID: {video_id}")
    print("")
