# Getit
Python YT downloader

The script uses the latest PyTube library and incorporate some enhancements to make it more robust.

We use yt.streams.get_highest_resolution() to get the highest resolution video stream available, rather than prompting the user to choose a video quality. We also catch the pytube.exceptions.VideoUnavailable exception in case the requested video is unavailable. Finally, we use output_path instead of path to specify the download location.
