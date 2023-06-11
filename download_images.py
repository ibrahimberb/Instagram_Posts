import instaloader
from tqdm import tqdm
import os
import os.path as op


class InstagramImageDownloader:
    def __init__(self, username, directory="images") -> None:
        self.username = username
        self.directory = directory

    def download_instagram_images(self, top_n=None):
        print(f"Downloading images from the profile '{self.username}'...")
        loader = instaloader.Instaloader()

        if not op.exists(self.directory):
            print(f"Creating directory '{self.directory}'...")
            os.mkdir(self.directory)

        try:
            profile = instaloader.Profile.from_username(loader.context, self.username)
            for i, post in tqdm(
                enumerate(profile.get_posts()), desc="Downloading posts"
            ):
                file_path = f"{self.directory}/{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                loader.download_pic(
                    filename=file_path,
                    url=post.url,
                    mtime=post.date_utc,
                )

                if i == top_n:
                    break

            print("All images downloaded successfully!")

        except instaloader.exceptions.ProfileNotExistsException:
            print(f"The profile '{self.username}' does not exist.")


if __name__ == "__main__":
    # username = "ts.lyrics13"
    username = "ltayswiftl"
    iid = InstagramImageDownloader(username)
    iid.download_instagram_images(top_n=25)
