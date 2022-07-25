def create_youtube_video(title, description):
	youtubeVideo = {`"title": title,
	"description": description,
	"likes": 0,
	"dislikes" : 0,
	 comments {"username": }}
	 return youtubeVideo

def likes(youtubeVideo)
	if "likes" in youtubeVideo:
		youtubeVideo[likes] += 1
	return youtubeVideo

def dislikes(youtubeVideo)
	if "dislikes" in youtubeVideo:
		youtubeVideo[dislikes] += 1
	return youtubeVideo

def add_comment(youtubeVideo, username, comment_text)
	youtubeVideo["comments"][username]=comment_text
	return youtubeVideo
