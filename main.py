print("Enter 1: Stream List manual")
print("Enter 2: Steam Auto-select (recommended)")
script_choice = input()

if script_choice == "1":
  # Run the first script
  import pytube

  video_url = input("Enter the YouTube video URL: ")

  
  yt = pytube.YouTube(video_url)

  video_title = yt.title

  video_streams = yt.streams

  print(f"Title: {video_title}")
  print("Streams:")
  for i, stream in enumerate(video_streams):
    print(f"{i}: {stream}")

  stream_to_download = int(input("Enter the number of the stream to download: "))

  chosen_stream = video_streams[stream_to_download]

  print(f"Download link: {chosen_stream.url}")
elif script_choice == "2":
  # Run the second script
  import pytube
  print ("by wuku#4042")
  video_url = input("Enter the YouTube video URL: ")

  yt = pytube.YouTube(video_url)

  video_title = yt.title

  video_streams = yt.streams

  best_video_with_audio = video_streams.filter(
    progressive=True,
    file_extension='mp4').order_by('resolution').desc().first()

  print(f"Title: {video_title}")
  print(f"Chosen stream: {best_video_with_audio}")

  print(f"Download link: {best_video_with_audio.url}")
else:
  print("Invalid input. Please enter 1 or 2.")
