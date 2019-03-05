from marshmallow import fields, post_load, Schema

from .base import BaseSchema


class SubscriberSchema(Schema):
    """
    Subscriber Schema
    """
    subscriber_id = fields.String(data_key="subscriber_id")
    ip_address = fields.String(data_key="ip_address")
    user_agent = fields.String(data_key="user_agent")
    browser = fields.String(data_key="browser")
    browser_version = fields.String(data_key="browser_version")
    platform = fields.String(data_key="platform")
    device_platform = fields.String(data_key="device_platform")
    operating_system = fields.String(data_key="operating_system")
    device = fields.String(data_key="device")
    country = fields.String(data_key="country")
    region = fields.String(data_key="region")
    city = fields.String(data_key="city")
    is_inactive = fields.Boolean(data_key="is_inactive")
    is_ghost = fields.Boolean(data_key="is_ghost")
    subscriber_added_timestamp = fields.String(data_key="subscriber_added_timestamp")
    added_to_segment_timestamp = fields.String(data_key="added_to_segment_timestamp")

    @post_load()
    def post_load(self, data):
        return BaseSchema.create_object('Subscriber', data)
