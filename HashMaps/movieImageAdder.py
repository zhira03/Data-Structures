import json

def checkImageKey(movieInfo, movieTitle):
    return "image" in movieInfo[movieTitle]

def add_image_to_Title(movieBankPath, imageURLs):
    try:
        with open(movieBankPath, "r") as file:
            movieInfo = json.load(file)

        url_index = 0

        default_image_url = "https://preview.redd.it/the-poster-for-dune-2-is-a-reference-to-the-fact-that-some-v0-5d1g5aceja8c1.jpeg?width=1080&crop=smart&auto=webp&s=dc87b9046e239aadba31e6adf17e16c0750cd3fa"
        
        for movieTitle in movieInfo:
            if not checkImageKey(movieInfo, movieTitle):
                if url_index < len(imageURLs):
                    movieInfo[movieTitle]["image"] = imageURLs[url_index]
                    url_index += 1
                else:
                    movieInfo[movieTitle]["image"] = default_image_url
                    print(f"Assigned default image to {movieTitle} due to insufficient URLs.")
        
        with open(movieBankPath, "w") as file:
            json.dump(movieInfo, file, indent=4)
        print("Images added to movie titles.")

    except FileNotFoundError:
        print("No movie data found.")
    except json.JSONDecodeError:
        print("Can't Decode JSON data.")
    except Exception as e:
        print("An error occurred:", e)


