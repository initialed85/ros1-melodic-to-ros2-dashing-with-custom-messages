import time
import unittest

import rospy
from gateway_msgs.msg import SomeRequest, SomeResponse

_NODE_NAME = 'some_request_to_some_response_test'
_REQUEST_TOPIC = 'some_request'
_RESPONSE_TOPIC = 'some_response'
_QOS = {
    'latch': True,
    'queue_size': 1
}

_SOURCE_ID = 2
_DESTINATION_ID = 1
_CONVERSATION_ID = 8008135
_DATA = 'Some message'

_TIMEOUT = 10


class SomeRequestToSomeResponseNodeTest(unittest.TestCase):
    def setUp(self):
        rospy.init_node(_NODE_NAME)

    def test_some_request_to_some_response(self):
        publisher = rospy.Publisher(
            _REQUEST_TOPIC,
            SomeRequest,
            **_QOS
        )

        request = SomeRequest()
        request.timestamp = rospy.Time.from_seconds(time.time())
        request.source_id = _SOURCE_ID
        request.destination_id = _DESTINATION_ID
        request.conversation_id = _CONVERSATION_ID
        request.data = _DATA

        publisher.publish(request)

        response = rospy.wait_for_message(_RESPONSE_TOPIC, SomeResponse, timeout=_TIMEOUT)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, SomeResponse)
        self.assertEqual(response.source_id, _DESTINATION_ID)  # reversed
        self.assertEqual(response.destination_id, _SOURCE_ID)  # reversed
        self.assertEqual(response.data, 'You sent: {}'.format(repr(_DATA)))
