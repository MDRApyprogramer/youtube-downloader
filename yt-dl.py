import pytube  # import tools
YouTube = pytube.YouTube


def show_progress(stream, chunk, bytes_remaining):  # Show percentage downloaded
    """ You must pass this function as a parameter to the instance of the YouTube class """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"\rDownload progress: {percentage_of_completion:.1f}%", end="")


while True:
    print('')
    link = input('link video :  ')
    res = input('res video :  ') + 'p'

    try:
        yt = YouTube(link, on_progress_callback=show_progress)
    except pytube.exceptions.RegexMatchError:
        print('please give a valid link \n')

    else:
        streams: bool = yt.streams.filter(progressive=True, res=res)
        if streams:
            print('download')
            streams.first().download()
            print('\n')
        else:
            print(f'There not is file with this res : {format(res)} \n')
