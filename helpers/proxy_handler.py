from browsermobproxy import Server
import json

class ProxyHandler:
    def __init__(self, path_to_browsermob_proxy):
        self.server = Server(path_to_browsermob_proxy)
        self.server.start()
        self.proxy = self.server.create_proxy()

    def set_request_interceptor(self, headers):
        headers_json = json.dumps(headers)
        js_code = f"""
            var headers = {headers_json};
            function (request) {{
                for (var name in headers) {{
                    request.headers().add(name, headers[name]);
                }}
            }}
        """
        self.proxy.request_interceptor = js_code

    def start_har_capture(self):
        self.proxy.new_har("session", options={"captureContent": True})

    def stop(self):
        self.server.stop()