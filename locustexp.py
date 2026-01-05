from locust import task,User, constant

class Myexp1(User):
    weight = 2
    wait_time = constant(1)

    @task
    def task1(self):
        print("exp1 task1")
    @task
    def task2(self):
        print("exp1 task2")


class Myexp2(User):
    weight = 2
    wait_time = constant(1)

    @task
    def task3(self):
        print("exp2 11111")

    @task
    def task4(self):
        print("exp2 task22222")
# class HelloWorldUser(HttpUser):
#     @task
#     def hello_world(self):
#         response=self.client.get("/1")
#         #self.client.get("/world")
#         response.status_code == 200 
#         print("Response status code:", response.status_code)
#         print("Response content:", response.text)
#         print(response.json().get("id")==1)
