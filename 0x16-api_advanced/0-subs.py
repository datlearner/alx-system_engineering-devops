import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'SubSleuthBot'}  # Set a custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

# Example usage:
subreddit_name = 'python'
print(f"The number of subscribers in r/{subreddit_name} is: {number_of_subscribers(subreddit_name)}")

