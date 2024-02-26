import time
import json

class HarHandler:
    @staticmethod
    def poll_har_data(proxy, target_url, timeout_sec):
        timeout = time.time() + timeout_sec
        found_request = False
        post_data_dict = {}
        print("Searching for HAR data entries...")
        while not found_request and time.time() < timeout:
            har_data = proxy.har
            for entry in har_data['log']['entries']:
                if target_url in entry['request']['url']:
                    post_data_text = entry['request']['postData']['text']
                    try:
                        post_data_dict = json.loads(post_data_text)
                        found_request = True
                        print("Successfully found the request URL and parsed the data entry:")
                        break
                    except KeyError as e:
                        print(f"Key error: {e}, the postData field may not exist.")
                    except json.JSONDecodeError as e:
                        print(f"JSON parsing error: {e}")
            time.sleep(0.5)
        if not found_request:
            print("No matching request or postData field found.")
        return post_data_dict