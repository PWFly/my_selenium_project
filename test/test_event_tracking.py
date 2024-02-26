# Import DataHandler
from src.utils.received_data import dataHandler
# Import compareData
from src.utils.compare_data import compareData

# Test event tracking
def test_event_tracking():
    try:
        # Initialize DataHandler instance, set the test page URL
        test_page_url = "https://qa-www.thebump.com"
        handler_instance = dataHandler(test_page_url)
        comparer = compareData()

        # Use get_har_data to get the tracked event data
        received_data = handler_instance.get_har_data()
        expected_event_name = "Sign Up Banner Impression"
        comparer.compare_data(received_data, expected_event_name)

    except Exception as e:
        print(f"Error occurred: {e}")
        
    finally:
        if handler_instance:
            handler_instance.close_driver()
            handler_instance.close_proxy()


# If the script is the main module, execute the test function
if __name__ == "__main__":
    test_event_tracking()
