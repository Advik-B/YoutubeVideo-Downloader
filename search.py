def search(query , results:int=10) -> list:
    """
    Search: 
    -

    Will search `youtube.com` and fetch the number of requested results (default is `10`)
    
    If the number of results are not sufficient then it will return as much as it can find

       ie:
            if the number of results are `6` but you requested `10` then;
                
            it will return `as many results as possible` or `6` in our case.


    Note:
    -
    - The results is a `list` of (video) links
    """
    import urllib.request
    import urllib.parse
    import re

    format_of_link = r"watch\?v=(\S{11})"
    raw_query = query
    print()
    query = urllib.parse.quote(raw_query)
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")

    videos = re.findall(format_of_link , html.read().decode())
    tmp = [f'https://www.youtube.com/watch?v={video}' for video in videos]
    while True:
        try:
            return tmp[:results]
        except IndexError:
            results -= 1
            continue