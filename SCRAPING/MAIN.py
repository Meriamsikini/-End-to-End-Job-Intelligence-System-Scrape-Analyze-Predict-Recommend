import os

print("➡️ Running Hind Scraper...")
os.system('python SCRAPPING\\SCRAPPING\\Emploi.ma_SCRAPER.py')

print("➡️ Running Meryem Scraper...")
os.system('python SCRAPPING\\SCRAPPING\\Jobboom_SCRAPER.py')

print("➡️ Running Imane Scraper...")
os.system('python SCRAPPING\\SCRAPPING\\Marocannonces_SCRAPER.py')

print("➡️ Running Oumayma Scraper...")
os.system('python SCRAPPING\\SCRAPPING\\Remoteok_SCRAPER.py')


print("✅scrapers finished and saved into jobs.csv")
