from marshest.marshclients import MarshClient

from api.paa_api_clients.assortment_client.models.products_responses import Products
from api.paa_api_clients.assortment_client.models.simulation_requests import SimulationRequest
from api.paa_api_clients.assortment_client.models.simulation_responses import Simulation


class AssortmentAPIClient(MarshClient):

    def __init__(self, url):
        super(AssortmentAPIClient, self).__init__(format_for_serializing='json', format_for_deserializing='json')
        self.url = url
        self.default_headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def get_products_by_simulation_id(self, simulation_ids, kwargs=None):
        url = '{0}/products'.format(self.url)
        params = {"simulationIds": simulation_ids}
        return self.request('GET', url, params=params,
                            response_entity_type=Products,
                            headers=self.default_headers,
                            kwargs=kwargs)

    def run_simulation(self, cdt_id, delisted_products, data_load_id="1", kwargs=None):
        url = '{0}/simulation/run'.format(self.url)
        request_entity = SimulationRequest(cdt_id, delisted_products, data_load_id)
        return self.request('POST', url,
                            request_entity=request_entity,
                            response_entity_type=Simulation,
                            headers=self.default_headers,
                            kwargs=kwargs)

    def get_cdt_tree(self, tree_id, kwargs=None):
        url = '{0}/cdtree/{1}'.format(self.url, tree_id)
        return self.request('GET', url,
                            headers=self.default_headers,
                            kwargs=kwargs)
