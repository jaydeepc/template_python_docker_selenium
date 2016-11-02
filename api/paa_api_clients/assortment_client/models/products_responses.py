import json

from marshest.marshmodels import MarshModel


class Products(MarshModel):

    def __init__(self, brand, current_measures, item_score, manufacturer, previous_measures,
                 product_display_name, product_id, recommendation, simulated_measures):
        self.brand = brand
        self.current_measures = current_measures
        self.item_score = item_score
        self.manufacturer = manufacturer
        self.previous_measures = previous_measures
        self.product_display_name = product_display_name
        self.product_id = product_id
        self.recommendation = recommendation
        self.simulated_measures = simulated_measures

    @classmethod
    def _json_to_object(cls, serialized_str):
        json_dict = json.loads(serialized_str.decode("utf-8"))
        new_product_list = []
        for product in json_dict:
            current_measures = None
            previous_measures = None
            simulated_measures = None
            if 'current_measures' in product:
                current_measures = Measures._json_to_object(product['current_measures'])
            if 'previous_measures' in product:
                previous_measures = Measures._json_to_object(product['previous_measures'])
            if 'simulated_measures' in product:
                simulated_measures = Measures._json_to_object(product['simulated_measures'])

            new_product_list.append(Products(brand=product.get("brand"), current_measures=current_measures,
                                             item_score=product.get("item_score"), manufacturer=product.get("manufacturer"),
                                             previous_measures=previous_measures,
                                             product_display_name=product.get("product_display_name"),
                                             product_id=product.get("product_id"),
                                             recommendation=product.get("recommendation"),
                                             simulated_measures=simulated_measures))
        return new_product_list


class Measures:

    def __init__(self, distribution, profit, revenue, volume):
        self.distribution = distribution
        self.profit = profit
        self.revenue = revenue
        self.volume = volume

    @classmethod
    def _json_to_object(cls, serialized_str):
        json_dict = serialized_str
        response = Measures(distribution=json_dict.get("distribution"),
                            profit=json_dict.get("profit"),
                            revenue=json_dict.get("revenue"),
                            volume=json_dict.get("volume"))
        return response
