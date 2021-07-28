import requests 
from bs4 import BeautifulSoup as bs
#beautifulsoup veri kazıma için kullanılan python kütüphanesidir.

github_user = input('Input GitHub User: ')
url = 'https://github.com/'+github_user
r = requests.get(url)
 #html kodlarını parçalayarak içinden istenen github fotosunu çeker.
soup = bs(r.content, 'html.parser') 
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_image) #fotografı tarayıcıda gösterir

