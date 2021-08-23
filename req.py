# Request is only used to get data from website but it's not meant for parsing. We have Beatifulsoup for that.
import requests

r = requests.get("https://xkcd.com/353/")
# print(r)
# <Response [200]>
# print(r.text)
# html content of the page

# downloading image from websites
r1 = requests.get("https://imgs.xkcd.com/comics/python.png")
# print(r1.content)
# data in bytes
# saving the data in a file --> this will download the image
# with open('comic.png', 'wb') as f:
#     f.write(r1.content)

# returns the headers, that come back with response
print(r.headers)
# {'Connection': 'keep-alive', 'Content-Length': '2932', 'Server': 'nginx', 'Content-Type': 'text/html; charset=UTF-8', 'Last-Modified': 'Wed, 18 Aug 2021 04:00:02 GMT', 'ETag': 'W/"611c85c2-1cf5"', 'Expires': 'Wed, 18 Aug 2021 18:40:06 GMT', 'Cache-Control': 'max-age=300', 'Content-Encoding': 'gzip', 'Accept-Ranges': 'bytes', 'Date': 'Wed, 18 Aug 2021 19:02:17 GMT', 'Via': '1.1 varnish', 'Age': '230', 'X-Served-By': 'cache-qpg1249-QPG', 'X-Cache': 'HIT', 'X-Cache-Hits': '1', 'X-Timer': 'S1629313337.234766,VS0,VE1', 'Vary': 'Accept-Encoding'}