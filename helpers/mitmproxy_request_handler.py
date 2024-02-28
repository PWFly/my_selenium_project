from mitmproxy import http
import json

captured_data = []

def request(flow: http.HTTPFlow) -> None:
    
    if "https://api.segment.io/v1/t" in flow.request.url:
        captured_request = {
            "url": flow.request.url,
            "method": flow.request.method,
            "payload": flow.request.content
        }
        captured_data.append(captured_request)

def done():

    data_file_path = '/home/mitmproxy/sources/received_data.json'

    decoded_data = [item.decode('utf-8') for item in captured_data]

    with open(data_file_path, "w") as json_file:
        json.dump(decoded_data, json_file)