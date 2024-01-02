import random
import time

songs = [
    'Don\'t blame me', 'Send my love', 'Adore you', 'Die for you', 'Lover',
    'One thing', 'How long', 'Tightrope', 'Wildest Dreams', 'Wushang Clan',
    'History'
]


def play():
  last_song = None

  while True:
    available_songs = [song for song in songs if song != last_song]

    if not available_songs:
      last_song = None
      continue

    current_playing = random.choice(available_songs)
    print(current_playing)
    last_song = current_playing
    time.sleep(2)


play()
