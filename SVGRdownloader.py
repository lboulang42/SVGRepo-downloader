import sys, os, requests
from urllib.parse import urlparse

def download_svg(url, filename):
	print(f"downloading {filename}... ", end="")
	dlresp = requests.get(url, stream=True)
	if dlresp.status_code != 200:
		print(f"Error: {dlresp.status_code} calling {url}")
	with open(f"svg/{filename}", 'wb') as f:
		for chunk in dlresp.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	print("done")
	
def scrape(base_url) : 
	fetch_count = 0; 
	while True : 
		r = requests.get(f'{base_url}&limit=50&start={fetch_count}')
		if (r.status_code != 200) :
			print(f"Error: {r.status_code} calling {base_url}")
			return ; 
		jsn = r.json()
		if (fetch_count == 0) :
			print(f'collection total icons: {jsn["count"]}')   
		for icon in jsn['icons'] : 
			print(f"{fetch_count}/{jsn['count']}... ", end="")
			download_svg(f"https://www.svgrepo.com/download/{icon['id']}/{icon['slug']}.svg", f"{icon['slug']}.svg")
			fetch_count += 1
		if (jsn['next']) == None : 
			return ; 

def parseurl(argurl):
	parsed_url = urlparse(argurl)
	path_parts = parsed_url.path.strip('/').split('/')
	if len(path_parts) >= 2 and path_parts[0] == 'collection':
		return path_parts[1]
	else:
		raise ValueError("Invalid URL")

if __name__ == "__main__" : 
	if (len(sys.argv) < 2) : 
		print('usage: py ./SVGRdownloader.py <collection url>')
		sys.exit(1); 
	collection_name = parseurl(sys.argv[1])
	base_url = f"http://api.svgrepo.com/collection/?term={collection_name}"
	os.makedirs('svg', exist_ok=True)
	scrape(base_url); 