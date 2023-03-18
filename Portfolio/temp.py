from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"사과, 오렌지, 포도, 수박, 파인애플, 복숭아",
             "limit":50,
             "print_urls":True,
             "format":"jpg"}
paths = response.download(arguments)
print(paths)
