import scraper

print("Maindeck\n")
print(scraper.search('2020', '04', '14', 'main', 'Karn, the Great Creator'))
print('\nSideboard\n')
print(scraper.search('2020', '04', '14', 'side', 'defense grid'))
