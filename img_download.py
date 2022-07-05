import urllib.request

def download(url, file_path, file_name):
    full_path = file_path + file_name + ".jpg"
    urllib.request.urlretrieve(url, full_path)


url = input("Enter the URL of image you want to download:")
file_name = input("Enter file name to save as:")
download(url, 'image/', file_name)