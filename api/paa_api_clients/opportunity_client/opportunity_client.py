from marshest.marshclients import MarshClient
from api.paa_api_clients.opportunity_client.models.opportunities_responses import Opportunities, CreateOpportunity, CreatedOpportunity
from api.paa_api_clients.opportunity_client.models.filters import FilterRequest
from api.paa_api_clients.opportunity_client.models.opportunities_requests import CreateRequest, DeleteRequest

import random


class OpportunityAPIClient(MarshClient):

    def __init__(self, url):
        super(OpportunityAPIClient, self).__init__(format_for_serializing='json', format_for_deserializing='json')
        self.url = url
        self.default_headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def get_all_opportunities(self, kwargs=None):
        url = '{0}/opportunities/'.format(self.url)

        return self.request('GET', url,
                            response_entity_type=Opportunities,
                            headers=self.default_headers,
                            kwargs=kwargs)

    def get_filtered_opportunities(self, type, filter, kwargs=None):
        url = '{0}/opportunities/filter'.format(self.url)
        request_entity = FilterRequest(type=type, filter=filter)
        return self.request('POST', url,
                            request_entity=request_entity,
                            response_entity_type=Opportunities,
                            headers=self.default_headers,
                            kwargs=kwargs)

    def create_opportunity(self, cdt_type, opportunity_type, name, data_load_id="1", kwargs=None):
        url = '{0}/opportunity/create'.format(self.url)
        request_entity = CreateRequest(cdt_type, opportunity_type, name, data_load_id)

        return self.request('POST', url,
                            request_entity=request_entity,
                            response_entity_type=CreateOpportunity,
                            headers=self.default_headers,
                            kwargs=kwargs)

    def delete_opportunity(self, opportunity_ids, kwargs=None):
        url = '{0}/opportunities/deactivate'.format(self.url)
        request_entity = DeleteRequest(opportunity_ids)

        return self.request('POST', url,
                            request_entity=request_entity,
                            # response_entity_type=DeletedOpportunity,
                            headers=self.default_headers,
                            kwargs=kwargs)

    def get_opportunity_details(self, opportunity_id, kwargs=None):
        url = '{0}/opportunity/{1}'.format(self.url, opportunity_id)

        return self.request('GET', url,
                            response_entity_type=CreatedOpportunity,
                            headers=self.default_headers,
                            kwargs=kwargs)

    def get_existing_opportunity_or_create(self):
        all_opportunities = self.get_all_opportunities().object
        if len(all_opportunities.opportunities) !=0:
            return all_opportunities.opportunities[0]
        else:
            new_opportunity = self.create_opportunity("1", "MANUAL", "api_created_opportunity_{0}".format(random.randint(1, 100))).object
            if new_opportunity.status == "Success":
                return new_opportunity.opportunity
            else:
                raise Exception("New opportunity was not created, to setup data for test.")