from bs4 import BeautifulSoup
import urllib2

current_file = 101
soup = BeautifulSoup(urllib2.urlopen('https://fangj.github.io/friends/season/0' + str(current_file) + '.html').read(), 'lxml')

span = soup.find("html")
paras = [x for x in span.findAllNext("p")]

start = span.string
middle = "".join(["".join(x.findAll(text=True)) for x in paras[:-1]])
last = paras[-1].contents[0]

print "%s\n\n%s\n\n%s" % (start, middle, last)
