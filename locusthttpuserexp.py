from locust import HttpUser, task, constant

class MyHttpUser(HttpUser):
    wait_time = constant(1)
    host= "https://api.restful-api.dev/objects"
    @task
    def task1(self):
        response = self.client.get("/1")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)
        print(response.json().get("id"))
        print("ID is 1:", response.json().get("id") == '1')

    @task
    def task2(self):
        header = {"Content-Type": "application/json"}   
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        # Use json=payload to send as JSON
        response = self.client.post("", json=payload, headers=header)
        print("Response status code:", response.status_code)
        print("Response content:", response.text)
        #print("ID is 2:", response.json().get("id") == 2)