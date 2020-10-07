


from locust import User, task, between

class MyUser(User):
    @task
    def my_task(self):
        print("executing data")
        self.client.post("/train/test")

