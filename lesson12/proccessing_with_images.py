from PIL import Image, ImageFilter
from concurrent.futures import ThreadPoolExecutor, as_completed


def filter_for_images(filename: str) -> None:
    """Function that processes image and applies a filter to it"""
    print(f"Opening {filename}...")

    try:
        filepath: str = "./lesson12/downloaded_files/" + filename
        new_name: str = "./lesson12/filtered_images/" + filename

        with Image.open(filepath) as img:
            img = img.convert("RGB")
            img = img.resize((300, 300))
            img = img.filter(ImageFilter.GaussianBlur(1))
            img = img.filter(ImageFilter.DETAIL)
            img.save(new_name)

        print(f"{filename} successfully filtered!")

    except FileNotFoundError:
        print(f"File with the {filename} not found!")

if __name__ == "__main__":
    files = ["image_1.png", "image_2.png"]

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(filter_for_images, f) for f in files]

        for future in as_completed(futures):
            future.result()