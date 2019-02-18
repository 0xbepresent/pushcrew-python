from collections import namedtuple
from decimal import Decimal

from marshmallow import Schema, post_load


class BaseSchema(Schema):
    """
    Provides an easy way to an object (namedtuple) from a schema.
    """
    def __init__(self, object_name, many=False):
        self.object_name = object_name
        super(BaseSchema, self).__init__(many=many)

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object(self.object_name, data)

    @staticmethod
    def create_object(object_name, data):
        fields = data.keys()
        o = namedtuple(object_name, fields)
        return o(**data)


def create_object_from_json(object_name, res, many=False):
    """
    Creates an object with the name `object_name` from an API
    response (assumes that the response has valid JSON attached to it).
    """
    res.raise_for_status()

    schema_class = _get_schema_class(object_name)
    schema = schema_class(object_name, many=many)

    user_data = res.json(parse_float=Decimal)
    print user_data
    result = schema.load(user_data)
    return result


def _get_schema_class(object_name):
    '''
    Basically a factory method to get the appropriate schema class
    based on the object_name.
    '''
    # Key is the name of the object, value is the schema class
    from .segment import SegmentsSchema, AddSegmentSchema, StatusSchema

    schema_dict = {
        'Segments': SegmentsSchema,
        'AddSegment': AddSegmentSchema,
        'StatusSegment': StatusSchema
    }

    schema_class = schema_dict.get(object_name)

    if not schema_class:
        raise Exception('Invalid object_name passed in: "%s"' % object_name)

    return schema_class
