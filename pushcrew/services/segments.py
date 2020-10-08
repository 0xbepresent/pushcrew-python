import json

from ..schemas import create_object_from_json

import sys
if sys.version_info[0] < 3:
    from urllib import urlencode
else:
    from urllib.parse import urlencode

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
        params = urlencode({
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
        params = json.dumps({"delete_list": delete_list})
        response = self.pushcrew.segments(segment_id).subscribers().PUT(
            data=params)
        return create_object_from_json('StatusSegment', response)

    def get_subscribers_from_segment(self, segment_id):
        """
        This endpoint is used to get a list of subscribers present in a
        segment.
        The request method of this call needs to be "GET".
        """
        response = self.pushcrew.segments(segment_id).subscribers().GET(
            params={'page': 1, 'per_page': 1024})
        cf = create_object_from_json('SegmentSubscribers', response)
        pages = int((cf.data.count_total / 1024) + 2)
        subscribers_list = [] + cf.data.subscriber_list
        for page in range(2, pages):
            response = self.pushcrew.segments(
                segment_id).subscribers().GET(
                    params={'page': page, 'per_page': 1024})
            cf = create_object_from_json('SegmentSubscribers', response)
            subscribers_list = subscribers_list + cf.data.subscriber_list
        return subscribers_list
