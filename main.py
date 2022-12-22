print("Enter 1: Stream List manual")
print("Enter 2: Steam Auto-select (recommended)")
script_choice = input()

if script_choice == "1":
  # Run the first script
  import pytube

  # Get the YouTube video URL
  video_url = input("Enter the YouTube video URL: ")

  # Create a YouTube object
  yt = pytube.YouTube(video_url)

  # Get the video's title
  video_title = yt.title

  # Get the video's streams
  video_streams = yt.streams

  # Print the video's title and streams
  print(f"Title: {video_title}")
  print("Streams:")
  for i, stream in enumerate(video_streams):
    print(f"{i}: {stream}")

  # Choose a stream to download
  stream_to_download = int(input("Enter the number of the stream to download: "))

  # Get the chosen stream
  chosen_stream = video_streams[stream_to_download]

  # Print the download link for the chosen stream
  print(f"Download link: {chosen_stream.url}")
elif script_choice == "2":
  # Run the second script
  import pytube
  print ("by wuku#4042")
  # Get the YouTube video URL
  video_url = input("Enter the YouTube video URL: ")

  # Create a YouTube object
  yt = pytube.YouTube(video_url)

  # Get the video's title
  video_title = yt.title

  # Get the video's streams
  video_streams = yt.streams

  # Filter the streams to only include the best resolution video with audio
  best_video_with_audio = video_streams.filter(
    progressive=True,
    file_extension='mp4').order_by('resolution').desc().first()

  # Print the video's title and the chosen stream
  print(f"Title: {video_title}")
  print(f"Chosen stream: {best_video_with_audio}")

  # Print the download link for the chosen stream
  print(f"Download link: {best_video_with_audio.url}")
else:
  print("Invalid input. Please enter 1 or 2.")
