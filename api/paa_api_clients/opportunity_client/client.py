from cafe.engine.http.client import AutoMarshallingHTTPClient
from api.paa_api_clients.opportunity_client.models.opportunities_responses import Opportunities, CreateOpportunity, DeletedOpportunity
from api.paa_api_clients.opportunity_client.models.filters import FilterRequest
from api.paa_api_clients.opportunity_client.models.opportunities_requests import CreateRequest, DeleteRequest


class OpportunityAPIClient(AutoMarshallingHTTPClient):

    def __init__(self, url):
        super(OpportunityAPIClient, self).__init__(serialize_format='json', deserialize_format='json')
        self.url = url
        self.default_headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def get_all_opportunities(self, requestslib_kwargs=None):
        url = '{0}/opportunities/'.format(self.url)

        return self.request('GET', url,
                            response_entity_type=Opportunities,
                            headers=self.default_headers,
                            requestslib_kwargs=requestslib_kwargs)

    def get_filtered_opportunities(self, type, filter, requestslib_kwargs=None):
        url = '{0}/opportunities/filter'.format(self.url)
        request_entity = FilterRequest(type=type, filter=filter)

        return self.request('POST', url,
                            request_entity=request_entity,
                            response_entity_type=Opportunities,
                            headers=self.default_headers,
                            requestslib_kwargs=requestslib_kwargs)

    def create_opportunity(self, cdt_type, opportunity_type, name, data_load_id="1", requestslib_kwargs=None):
        url = '{0}/opportunities/create'.format(self.url)
        request_entity = CreateRequest(cdt_type, opportunity_type, name, data_load_id)

        return self.request('POST', url,
                            request_entity=request_entity,
                            response_entity_type=CreateOpportunity,
                            headers=self.default_headers,
                            requestslib_kwargs=requestslib_kwargs)

    def delete_opportunity(self, opportunity_ids, requestslib_kwargs=None):
        url = '{0}/opportunities/deactivate'.format(self.url)
        request_entity = DeleteRequest(opportunity_ids)

        return self.request('POST', url,
                            request_entity=request_entity,
                            response_entity_type=DeletedOpportunity,
                            headers=self.default_headers,
                            requestslib_kwargs=requestslib_kwargs)
