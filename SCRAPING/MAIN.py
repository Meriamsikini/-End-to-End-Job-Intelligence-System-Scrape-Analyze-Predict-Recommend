import os

print("➡️ Running Emploi.ma Scraper...")
os.system('python SCRAPPING\\SCRAPPING\\Emploi.ma_SCRAPER.py')

print("➡️ Running Jobbom Scraper...")
os.system('python SCRAPPING\\SCRAPPING\\Jobboom_SCRAPER.py')

print("➡️ Running Marocannounces Scraper...")
os.system('python SCRAPPING\\SCRAPPING\\Marocannonces_SCRAPER.py')

print("➡️ Running Remoteok Scraper...")
os.system('python SCRAPPING\\SCRAPPING\\Remoteok_SCRAPER.py')


print("✅scrapers finished and saved into jobs.csv")
