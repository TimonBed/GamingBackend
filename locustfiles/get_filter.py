from locust import HttpUser, task, between


class HelloWorldUser(HttpUser):
    wait_time = between(1, 4)

    @task(1)
    def get_games(self):
        self.client.get("/references/games/")
