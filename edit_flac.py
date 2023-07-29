import mutagen
from mutagen import File
from mutagen.flac import Picture, FLAC


def add_flac_cover(audio: FLAC, albumart: str):
    assert albumart.endswith(".jpg") or albumart.endswith(".png")

    image = Picture()
    image.type = mutagen.id3.PictureType.COVER_FRONT
    image.mime = "image/jpeg" if albumart.endswith(".jpg") else "image/png"
    with open(albumart, "rb") as f:
        image.data = f.read()

    audio.clear_pictures()
    audio.add_picture(image)
    audio.save()


def main():
    cover_path = "/path/to/cover.jpg"

    flacs = [
        "/path/to/music01.flac",
        "/path/to/music02.flac",
    ]
    for i, flac in enumerate(flacs):
        audio = FLAC(flac)
        audio["album"] = "album name"
        audio["tracktotal"] = "10"
        audio["tracknumber"] = str(i + 1)
        audio["artist"] = "artist"
        audio["title"] = "album title"
        add_flac_cover(audio, cover_path)

        # Printing all the metadata
        print(audio.pprint())
        if 0:
            audio.save()


if __name__ == "__main__":
    main()
