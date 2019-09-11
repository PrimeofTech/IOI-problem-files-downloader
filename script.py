import requests
import os
import errno
import time

BASE_URL = 'https://ioinformatics.org/files/'
DOWNLOAD_PATH = './IOI-Downloads/'

start_year = 1989
end_year = 2019


def downloader(filename, download_path_prefix):
    url = BASE_URL + filename

    try:
        time.sleep(0.2)
        request = requests.get(url, allow_redirects=False)
    except:
        print(f"=={filename} wasn't downloaded, because there was an error \
							=> status code:{request.status_code}; url: {url};")

    if int(request.status_code) == 302:
        print(f"=={filename} wasn't downloaded, because it probably doesn't exist.")
        return

    filename = download_path_prefix + '/' + filename

    os.makedirs(DOWNLOAD_PATH + os.path.dirname(filename), exist_ok=True)

    with open(DOWNLOAD_PATH + filename, 'wb') as file:
        file.write(request.content)

    print(f"=={filename} successfully downloaded.")


for year in range(start_year, end_year + 1):
    print(f"=={year}/")
    # These years instead of problems, there are rounds.
    if year == 1990 or year == 1991 or year == 1992:
        for x in range(2):
            downloader(f'ioi{year}round{x+1}.pdf', str(year))
    else:
        for x in range(6):
            if year == 1993:
                if x+1 == 5 or x+1 == 6:
                    continue
            downloader(f'ioi{year}problem{x+1}.pdf', str(year))
