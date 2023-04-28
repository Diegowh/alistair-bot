import requests

from bs4 import BeautifulSoup

url = "https://dragonage.fandom.com/wiki/Alistair/Dialogue"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

phrases = soup.findAll('li')

alistair_quotes = []

def remove_tags(tag_list, element):
    for tag in tag_list:
        for tag_element in element.find_all(tag):
            tag_element.decompose()
            
            

for phrase in phrases:
    tags_to_remove = ['i', 'a', 'img', 'svg']
    remove_tags(tags_to_remove, phrase)
    
    
    cleaned_quote = phrase.get_text(strip=True)
    alistair_quotes.append(cleaned_quote)
    
    

    
alistair_quotes = list(filter(None, alistair_quotes))


semi_final_quotes = [quote.replace('"', '') for quote in alistair_quotes[:82] if quote[0] == '"' and quote[-1] == '"']
alistair_quotes = alistair_quotes[82:]
print(f"Longitud previa: {len(semi_final_quotes)}")
for quote in alistair_quotes:
    if "Alistair: " in quote:
        semi_final_quotes.append(quote.replace("Alistair: ", ""))
        
    
print(f"Longitud final: {len(semi_final_quotes)}")

# for quote in semi_final_quotes:
#     quote = quote.replace(": ", "")



# with open("alistair_quotes.txt", "w", encoding="utf-8") as file:
#     for quote in semi_final_quotes:
#         file.write(quote + '\n')

with open("alistair_quotes.txt", "r", encoding="utf-8") as file:
    final_alistair_quotes = [line.rstrip() for line in file]
