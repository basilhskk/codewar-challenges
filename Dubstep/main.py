def song_decoder(song):
    return " ".join(list(filter(None, song.split("WUB")))).strip()


song_decoder("AWUBWUBWUBBWUBWUBWUBC")