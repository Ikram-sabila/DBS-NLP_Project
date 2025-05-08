from google_play_scraper import Sort, reviews
import csv
import pandas as pd

scrapreview, _ = reviews(
    'id.bmri.livin',
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=15000,
)

with open('ulasan_aplikasi.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scrapreview:
        writer.writerow([review['content']])

apps_reviews_df = pd.DataFrame(scrapreview)

jumlah_ulasan, jumlah_kolom = apps_reviews_df.shape
print(f"Jumlah ulasan: {jumlah_ulasan}, Jumlah kolom: {jumlah_kolom}")

apps_reviews_df.to_csv('ulasan_aplikasi_full.csv', index=False)

print("Data ulasan aplikasi telah disimpan ke 'ulasan_aplikasi_full.csv' dan 'ulasan_aplikasi.csv'.")