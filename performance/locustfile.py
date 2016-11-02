from locust import TaskSet, HttpLocust, task
from api.paa_api_clients.opportunity_client.opportunity_client import Op

class HomePageLoad(TaskSet):

    @task(1)
    def get_all_opportunities(self):
        self.client.get("/OpportunityService/opportunities/")

    @task(1)
    def get_all_cdts(self):
        self.client.get("/AssortmentService/cdts")


class WebsiteUser(HttpLocust):
    task_set = HomePageLoad
    min_wait=5000
    max_wait=9000