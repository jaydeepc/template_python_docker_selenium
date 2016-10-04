import json

from cafe.engine.models.base import AutoMarshallingModel


class Opportunities(AutoMarshallingModel):

    def __init__(self, opportunities):
        self.opportunities = opportunities

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str.decode("utf-8"))
        opportunities = None
        if 'opportunities' in json_dict:
            opportunities = Opportunity._list_to_obj(json_dict['opportunities'])

        return Opportunities(opportunities=opportunities)


class Opportunity:

    def __init__(self, cdt_id, cdt_name, id, metrics, modified_date, name, status, type):
        self.cdt_id = cdt_id
        self.cdt_name = cdt_name
        self.id = id
        self.metrics = metrics
        self.modified_date = modified_date
        self.name = name
        self.status = status
        self.type = type

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = serialized_str
        metrics = None
        if 'metrics' in json_dict:
            metrics = Metrics._list_to_obj(json_dict['metrics'])

        response = Opportunity(cdt_id=json_dict.get("cdt_id"), cdt_name=json_dict.get("cdt_name"),
                               id=json_dict.get("id"), metrics=metrics,
                               modified_date=json_dict.get("modified_date"), name=json_dict.get("name"),
                               status=json_dict.get("status"), type=json_dict.get("type"))
        return response

    @classmethod
    def _list_to_obj(cls, dict_list):
        items = []
        for item in dict_list:
            item_obj = cls._json_to_obj(item)
            items.append(item_obj)
        return items


class Metrics:

    def __init__(self, actualValue, changeInValue, code, displayName, displayScalingUnitLabel, displayScalingValue, displayUnits, percentageValue,
                 simulatedValue, type, valueType):
        self.actualValue = actualValue
        self.changeInValue = changeInValue
        self.code = code
        self.displayName = displayName
        self.displayScalingUnitLabel = displayScalingUnitLabel
        self.displayScalingValue = displayScalingValue
        self.displayUnits = displayUnits
        self.percentageValue = percentageValue
        self.simulatedValue = simulatedValue
        self.type = type
        self.valueType = valueType

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = serialized_str

        response = Metrics(actualValue=json_dict.get("actualValue"), changeInValue=json_dict.get("changeInValue"), code=json_dict.get("code"),
                           displayName=json_dict.get("displayName"), displayScalingUnitLabel=json_dict.get("displayScalingUnitLabel"),
                           displayScalingValue=json_dict.get("displayScalingValue"), displayUnits=json_dict.get("displayUnits"),
                           percentageValue=json_dict.get("percentageValue"), simulatedValue=json_dict.get("simulatedValue"), type=json_dict.get("type"),
                           valueType=json_dict.get("valueType"))
        return response


    @classmethod
    def _list_to_obj(cls, dict_list):
        items = []
        for item in dict_list:
            item_obj = cls._json_to_obj(item)
            items.append(item_obj)
        return items


class CreateOpportunity:
    def __init__(self, opportunity, status):
        self.opportunity = opportunity
        self.status = status

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str.decode("utf-8"))
        opportunity = None
        if 'Opportunity' in json_dict:
            opportunity = CreatedOpportunity._json_to_obj(json_dict['Opportunity'])

        return CreateOpportunity(opportunity=opportunity, status=json_dict.get("Status"))


class CreatedOpportunity:
    def __init__(self, cdt_id, submitted, id, details, create_date, name, submitted_by, submitted_date, type):
        self.cdt_id = cdt_id
        self.submitted = submitted
        self.id = id
        self.details = details
        self.create_date = create_date
        self.name = name
        self.submitted_by = submitted_by
        self.type = type
        self.submitted_date = submitted_date

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = serialized_str
        details = None
        if 'details' in json_dict:
            details = Details._list_to_obj(json_dict['details'])

        response = CreatedOpportunity(cdt_id=json_dict.get("cdt_id"), submitted=json_dict.get("submitted"),
                               id=json_dict.get("id"), details=details,
                               create_date=json_dict.get("create_date"), name=json_dict.get("name"),
                               submitted_by=json_dict.get("submitted_by"), submitted_date=json_dict.get("submitted_date"),
                               type=json_dict.get("type"))
        return response


class Details:

    def __init__(self, market_id, metrics, simulation_id):
        self.market_id = market_id
        self.metrics = metrics
        self.simulation_id = simulation_id

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = serialized_str
        metrics = None
        if 'metrics' in json_dict:
            metrics = Metrics._list_to_obj(json_dict['metrics'])

        response = Details(market_id=json_dict.get("market_id"), metrics=metrics, simulation_id=json_dict.get("simulation_id"))
        return response


    @classmethod
    def _list_to_obj(cls, dict_list):
        items = []
        for item in dict_list:
            item_obj = cls._json_to_obj(item)
            items.append(item_obj)
        return items


class DeletedOpportunity:
    def __init__(self, opportunity_ids_successfully_deactivated, status):
        self.opportunity_ids_successfully_deactivated = opportunity_ids_successfully_deactivated
        self.status = status

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str.decode("utf-8"))

        return DeletedOpportunity(opportunity_ids_successfully_deactivated=json_dict.get("opportunity_ids_successfully_deactivated"),
                                  status=json_dict.get("Status"))