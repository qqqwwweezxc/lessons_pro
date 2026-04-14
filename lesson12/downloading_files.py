import requests
import threading


url_first_image = "https://images.unsplash.com/photo-1775748525937-81ebe1f64827?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
url_second_image = "https://images.unsplash.com/photo-1775807346196-c12ab3c53d73?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

def download_file(url: str, filename: str) -> None:
    """Function for download one file"""

    print(f"Downloading file {filename}...")

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        filepath = "./lesson12/downloaded_files/" + filename

        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"Dowloading complete for file {filename}.")
    except Exception as error:
        print(f"Failed downloading. Error: {error}")


def main() -> None:
    """Program downloads multiple files from the network simultaneously using streams"""

    files_to_download = [
        ("https://images.unsplash.com/photo-1775748525937-81ebe1f64827?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "image_1.png"),
        ("https://images.unsplash.com/photo-1775807346196-c12ab3c53d73?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "image_2.png")
    ]
    
    threads = []

    for url, filename in files_to_download:
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\n--- All tasks completed! ---")

if __name__ == "__main__":
    main()