class Song:
    def __init__(self, sounds):
        self.sounds = sounds
    
    def get_remaining_sounds(self, starting_sound):
        if starting_sound in self.sounds:
            index = self.sounds.index(starting_sound)
            return self.sounds[index+1:]
        return []

class Explorer:
    def __init__(self, songs):
        self.songs = songs
    
    def find_remaining_sounds(self, sound):
        result = []
        for song in self.songs:
            if sound in song.sounds:
                remaining_sounds = song.get_remaining_sounds(sound)
                if remaining_sounds:
                    result.append(remaining_sounds)
                else:
                    print("End")
        return result

# definicion de las canciones
song1 = Song(["brr", "fiu", "cric-cric", "brrah"])
song2 = Song(["pep", "birip", "trri-trri", "croac"])
song3 = Song(["bri-bri", "plop", "cric-cric", "brrah"])

explorer = Explorer([song1, song2, song3])

input_sound = "brr"
output = explorer.find_remaining_sounds(input_sound)
for o in output:
    print(o)

input_sound = "plop"
output = explorer.find_remaining_sounds(input_sound)
for o in output:
    print(o)

input_sound = "croac"
output = explorer.find_remaining_sounds(input_sound)
for o in output:
    print(o)
