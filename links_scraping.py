import bs4
import requests
import webbrowser

url = "https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww/playlists"
data = requests.get(url)

soup = bs4.BeautifulSoup(data.text, 'html.parser')
#print(soup.prettify())                    will fetch the source code of requested page

# find will give first result findall will return all matching content
# for para in soup.findAll('p'):
#     #print(para)
#     print(para.text)
#     with open('urls.txt', 'a') as u:
#         u.write(str(para))
#         u.write('\n')

#using string slicing
for links in soup.findAll('a'):
    link = links.get('href')
    if link[0:3] == "/wa":
        final_link = "https://www.youtube.com"+link
        webbrowser.open(final_link)
        with open('urls.txt', 'a') as u:
            u.write(final_link)
            u.write('\n')






