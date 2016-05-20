import urllib.request
from optparse import OptionParser
from bs4 import BeautifulSoup
import sys

#說明文件
def usage():
	print (''' \033[92m	crawl from to get something. \n
	usage : python3 web_crawl.py [-g] [GameId]

	-h : help
	-g : Game Id

	By Maras. \033[0m''')
	sys.exit()

#取得參數輸入
def get_parameters():
	global gameId
	gameId = None
	optp = OptionParser(add_help_option=False,epilog="web_crawl")
	optp.add_option("-g","--gameId",dest="gameId",help="-g Steam App Game ID")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	if opts.help:
		usage()

	if opts.gameId is not None:
		gameId = opts.gameId

#開始
if __name__ == '__main__':
	if len(sys.argv) < 1:
		usage()
	get_parameters()
	url = None
	if appId is not None:
		url = "http://store.steampowered.com/app/" + gameId
	else: 
		print ('Please input -g or -h')

	if url is not None:
		#設置假的瀏覽器資訊
		headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
		#發送請求
		req = urllib.request.Request(url = url,headers=headers)
		page = urllib.request.urlopen(req)
		contentBytes = page.read()
		#進行分割
		soup = BeautifulSoup(str(contentBytes), "html.parser")
		matches = soup.find_all("div", { "class" : "game_purchase_price" })
		#將資訊顯示出來
		print(matches[0].string);
