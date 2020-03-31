def song_decoder(song):
   song = song.replace("WUB", " ")
   while "  " in song:
      song = song.replace("  ", " ")
   return song.strip()

