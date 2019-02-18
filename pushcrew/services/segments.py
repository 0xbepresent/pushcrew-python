import urllib

from ..schemas import create_object_from_json


class SegmentsMixin:

    def get_segments(self):
        """
        Get a list of segment names with their unique Segment IDs.
        """
        response = self.pushcrew.segments().GET()
        return create_object_from_json('Segments', response)

    def add_segment(self, name):
        """
        This endpoint is used to add a segment.
        name -- Name of the segment.
        """
        params = {'name': name}
        response = self.pushcrew.segments().POST(data=params)
        return create_object_from_json('AddSegment', response)

    def add_subscriber_to_segment(self, segment_id, subscriber_list):
        """
        This API endpoint is used to add subscribers to a segment.
        segment_id -- ID of the segment.
        subscriber_list -- List of the subscribers
        """
        params = urllib.urlencode({
            "subscriber_list": {"subscriber_list": subscriber_list}})
        params_encoded = params.replace("%27", "%22").replace("+", "")
        response = self.pushcrew.segments(segment_id).subscribers().POST(
            data=params_encoded)
        return create_object_from_json('StatusSegment', response)

    def remove_subscriber_from_segment(self, segment_id, delete_list):
        """
        This endpoint is used to remove subscribers from a segment.
        segment_id -- ID of the segment.
        delete_list -- List of the subscriber.
        """
        params = urllib.urlencode({
            "delete_list": {"delete_list": delete_list}})
        params_encoded = params.replace("%27", "%22").replace("+", "")
        response = self.pushcrew.segments(segment_id).subscribers().POST(
            data=params_encoded)
        return create_object_from_json('StatusSegment', response)
