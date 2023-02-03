import discogs_client

def test(old_metadata):
    old_artist = old_metadata[0]
    old_title = old_metadata[1]
    old_album = old_metadata[2]

    d = discogs_client.Client('Raihan/0.1', user_token="zHnuhsjcRNtdSeLzMwntiEeWOvjbzZWEgpWpZyGn")

    results = d.search(old_artist, type='artist')

    print(results)
    for x in results:
        print(x)
    # artist = results[0].artists[0]
    # print(artist.name)


