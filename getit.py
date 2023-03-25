import pytube
import os

def download_video(url, path):
    try:
        # Use pytube to get the YouTube video
        yt = pytube.YouTube(url)

        # Get the highest resolution video stream
        video = yt.streams.get_highest_resolution()

        # Download the video to the specified path
        video.download(output_path=path)
        print(f"Voilà! Your Video has been downloaded to {path}")
    except pytube.exceptions.VideoUnavailable:
        print("Sorry, this video is unavailable.")
    except pytube.exceptions.RegexMatchError:
        print("Invalid URL. Please enter a valid YouTube URL.")
    except Exception as e:
        # Catch and display any other errors
        print(f"An error occurred: {e}")

# Main program
if __name__ == '__main__':
    # Get the YouTube video URL
    url = input("Enter the URL of the YouTube video: ")
    
    # Validate the URL
    if not (url.startswith("https://www.youtube.com/") or url.startswith("https://youtu.be/")):
        print("Invalid URL. Please enter a valid YouTube URL.")
        exit()
    
    # Get the desired download path
    path = input("Enter the path to download the video (default is current directory): ") or os.getcwd()

    download_video(url, path)
