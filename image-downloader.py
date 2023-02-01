import requests
import io
from PIL import Image
import shutil
import concurrent.futures
import os

# def download_image(download_path, url, filename):
#     try:
#         image_content = requests.get(url, stream=True).content
#         # image_content = requests.get(url, stream=True).raw
#     except Exception as e:
#         print(f"ERROR - Could not download {url} - {e}")

#     try:
#         image_file = io.BytesIO(image_content)
#         image = Image.open(image_file).convert('RGB')
#         file_path = download_path + filename
#         with open(file_path, 'wb') as f:
#             image.save(f, "JPEG", quality=85)
#         print(f"SUCCESS - saved {url} - as {file_path}")
#     except Exception as e:
#         print(f"ERROR - Could not save {url} - {e}")

link = 'https://elements-cover-images-0.imgix.net/f223ce8d-5a80-4e09-9bbc-c809e4c76b76?auto=compress%2Cformat&fit=max&w=433&s=30397a9afa9b31cd51efb9130e5c1705 433w, https://elements-cover-images-0.imgix.net/f223ce8d-5a80-4e09-9bbc-c809e4c76b76?auto=compress%2Cformat&fit=max&w=632&s=650904d6e65dd5dcb6c54e5a98ac6fa7 632w, https://elements-cover-images-0.imgix.net/f223ce8d-5a80-4e09-9bbc-c809e4c76b76?auto=compress%2Cformat&fit=max&w=710&s=922dc5c574a4b37e468e1d353a107019 710w, https://elements-cover-images-0.imgix.net/f223ce8d-5a80-4e09-9bbc-c809e4c76b76?auto=compress%2Cformat&fit=max&w=866&s=43777e39df2446220a9fdc90a19c9350 833w, https://elements-cover-images-0.imgix.net/f223ce8d-5a80-4e09-9bbc-c809e4c76b76?auto=compress%2Cformat&fit=max&w=900&s=8da385c63e3a9af9d53d7022576c15f0 900w, https://elements-cover-images-0.imgix.net/f223ce8d-5a80-4e09-9bbc-c809e4c76b76?auto=compress%2Cformat&fit=max&w=1019&s=710308d6a4ee537e2adb6d946d224511 1019w, https://elements-cover-images-0.imgix.net/f223ce8d-5a80-4e09-9bbc-c809e4c76b76?auto=compress%2Cformat&fit=max&w=1170&s=7ba1f40849a995ff2852a781be1df0cb 1170w, https://elements-cover-images-0.imgix.net/f223ce8d-5a80-4e09-9bbc-c809e4c76b76?auto=compress%2Cformat&fit=max&w=1370&s=87c6b26e0008eb702a2ae137ce7d5da2 1370w, https://elements-cover-images-0.imgix.net/f223ce8d-5a80-4e09-9bbc-c809e4c76b76?auto=compress%2Cformat&fit=max&w=2038&s=b2672cdcf603100fc82fcef160531a8e 2038w'

vague_links = link.split(' ')
links = filter(lambda x: 'https' in x, vague_links)

# for link in links:
#     print(link)

# def download_image(download_path, url, filename):
#     file_path = download_path + filename
#     try:
#         with requests.Session().get(url, stream=True) as response:
#             with open(file_path, 'wb') as file:
#                 shutil.copyfileobj(response.raw, file)
#         print('success!!!')
#     except Exception as e:
#         print(e)
#         print('Could not download image')

def download_image(url):
    file_path = "images/" + url[-5:] + ".jpg"
    try:
        with requests.get(url, stream=True) as response:
            with open(file_path, 'wb') as file:
                shutil.copyfileobj(response.raw, file)
        print('success!!!')
    except Exception as e:
        print(e)
        print('Could not download image')

def download(urls):    
    with concurrent.futures.ThreadPoolExecutor( max_workers=5 ) as executor:
        future_to_url = {
            executor.submit(download_image, url): url for url in urls
        }
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                future.result()
            except Exception as exc:
                print("%r generated an exception: %s" % (url, exc))

# for i, url in enumerate(links):
#     download_image("images/", url, f"{i}.jpg")

download(links)