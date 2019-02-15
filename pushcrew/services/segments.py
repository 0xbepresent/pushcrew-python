import urllib


class SegmentsMixin:

    def get_segments(self):
        """
        Get a list of segment names with their unique Segment IDs.
        """
        response = self.pushcrew.segments().GET()
        return response

    def add_segment(self, name):
        """
        This endpoint is used to add a segment.
        """
        params = {'name': name}
        response = self.pushcrew.segments().POST(data=params)
        return response

    def add_suscriber_to_segment(self, segment_id, subscriber_list):
        """
        This API endpoint is used to add subscribers to a segment.
        """
        params = urllib.urlencode({
            "subscriber_list": {"subscriber_list": subscriber_list}})
        params_encoded = params.replace("%27", "%22").replace("+", "")
        response = self.pushcrew.segments(segment_id).subscribers().POST(
            data=params_encoded)
        return response
