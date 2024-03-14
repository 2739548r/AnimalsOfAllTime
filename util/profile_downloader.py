import concurrent.futures
import json
import os
import requests
import shutil


class ProfileDownloader:
    @classmethod
    def __get_json(cls, count):
        url = f'https://randomuser.me/api/?inc=email,login,picture&results={count}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data

    @classmethod
    def __save_image(cls, entry) -> str:
        img_url = entry['picture']['large']
        with requests.get(img_url, stream=True) as response:
            filename = os.path.join('media\\profile_images', os.path.basename(img_url))
            with open(filename, 'wb') as out_file:
                out_file.write(response.content)
            img_path = os.path.join('profile_images', os.path.basename(img_url))
            return img_path
        
    @classmethod
    def __get_data(cls, entry) -> tuple[str, str, str]:
        try:
            username = entry['login']['username']
            email = entry['email']
            password = entry['login']['password']
            if username and password:
                image_path = cls.__save_image(entry)
                if image_path:
                    return username, email, password, image_path
        except:
            pass
        
    @classmethod
    def download(cls, count=50) -> dict[str, dict[str, str]]:
        profile_dict = cls.__get_json(count)
        output_dict = {}

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(cls.__get_data, entry) for entry in profile_dict['results']]

            for future in concurrent.futures.as_completed(futures):
                result = future.result() 
                if result is not None:
                    username, email, password, image_path = result
                    output_dict[username] = {
                        'email': email,
                        'password' : password,
                        'image_path' : image_path
                    }

        with open("profile.json", "w") as f:
            json.dump(output_dict, f, indent=2)
        return output_dict

    @classmethod
    def clear(cls) -> None:
        if os.path.exists("profile.json"):
            os.remove("profile.json")

        for item in os.listdir("media\\profile_images"):
            item_path = os.path.join("media\\profile_images", item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            else:
                shutil.rmtree(item_path)
        