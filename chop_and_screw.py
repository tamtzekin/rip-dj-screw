import os
from pydub import AudioSegment
from pydub.effects import low_pass_filter


song = AudioSegment.from_file("trax/aaliyah.mp3", format="mp3")


def speed_change(song, speed=1.0):
    # Overwrite frame_rate, play x samples per second
    sound_with_altered_frame_rate = song._spawn(song.raw_data, overrides={
        "frame_rate": int(song.frame_rate * speed)
    })
    # Converts sound back to standard frame rate so it can be played
    return sound_with_altered_frame_rate.set_frame_rate(song.frame_rate)
    

def chop_and_screw(song):
    track_title = os.path.splitext(os.path.basename("trax/aaliyah.mp3"))[0]
    print("processing '%s'..." % track_title)

    song = speed_change(song, 0.83)
    print('screwing the beat...')
    
    song = low_pass_filter(song, 1200) + 10
    print('bass boosting...')
    
    song.export("trax/%s_RIP-DJ-SCREW.mp3" % track_title, format="mp3", parameters=["-q:a", "0"], tags={'comments': 'chopped & screwed by python'})
    print("done------------")
    print("track saved as %s_RIP-DJ-SCREW.mp3" % track_title)


chop_and_screw(song)