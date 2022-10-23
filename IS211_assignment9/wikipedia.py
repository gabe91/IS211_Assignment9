import urllib.request
from bs4 import BeautifulSoup

def downloadata(url):
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    return response


if __name__ == "__main__":
    wiki_url = "https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals"
    url_text = downloadata(wiki_url)
    soup = BeautifulSoup(url_text, features="lxml")
    #print(url_text)
    result_table = soup.find_all('table', class_='wikitable plainrowheaders sortable')
    rows = result_table[0].find_all('tr')
    #print(rows)
    headers = rows[0].find_all('th')
    print(f"{headers[0].text.strip():<15} - {headers[1].text.strip():<30} - {headers[2].text.strip():<15} - {headers[3].text.strip():<15}")
    for row in rows:
        cells = row.find_all('td')
        #print(cells)
        if not cells:
            continue
        print(f"{cells[0].text.strip():<15} - {cells[1].text.strip():<30} - {cells[2].text.strip():<15} - {cells[3].text.strip():<15}")
    result_table = soup.find_all('table', class_='wikitable plainrowheaders sortable')

