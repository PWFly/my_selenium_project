import json
class compareData:
    def compare_data(self,received_data, expected_event_name):
        """
        Compares received data with expected values.

        Parameters:
            received_data (dict): A dictionary of received data to compare.
            expected_values (dict): A dictionary of expected key-value pairs.

        Returns:
            dict: A dictionary with keys as received data keys and values as tuples of 
                (bool indicating match, actual value, expected value)
        """

        with open('sources/event_tracking_data.json','r') as file:
            data = json.load(file)

        properties = received_data.get('properties')
        event_name = received_data.get('event')
        if event_name == expected_event_name:
            expect_properties = data[expected_event_name]
            for key, expected_values in expect_properties.items():
                assert key in properties, f"{key} not found in properties"
                assert str(properties.get(key)) == str(expected_values),f"{key}: {properties.get(key)} (Expected: {expected_values})"
            print(f"{expected_event_name} event data matches expected values")
        else:
            print(f"Didn't find the event {expected_event_name}")
