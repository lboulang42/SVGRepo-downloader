# SVGRepo-downloader
Batch Downloader for [SVGRepo](https://www.svgrepo.com)

I had to download a bunch of SVGs files to illustrate some other projects.
I found svgrepo.com that had huge collections of icons without any kind of download limits or register to use terms.
The only down sight was the lacking of bulk download and no free API (9.90$ per month lol).

SVGRepo have a CloudFlare CDN on the main domain https://www.svgrepo.com/ but while playing a bit with the website I found what seems to be an internal API.
I built this in 10 minutes, its not optimized and only works for `/collection/` because I dont need anything else.

# Usage
`py ./SVGRdownloader.py <collection url>`