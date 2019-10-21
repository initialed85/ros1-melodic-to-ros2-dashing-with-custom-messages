import time
import unittest
from threading import Thread

import rospy
from Queue import Queue, Empty
from gateway_msgs.msg import SomeRequest, SomeResponse

_NODE_NAME = 'some_request_to_some_response_test'
_REQUEST_TOPIC = 'some_request'
_RESPONSE_TOPIC = 'some_response'
_QOS_REQUEST = {
    'latch': False,
    'queue_size': 1
}

_SOURCE_ID = 2
_DESTINATION_ID = 1
_CONVERSATION_ID = 8008135
_DATA = 'Some message'

_TIMEOUT = 5


class SomeRequestToSomeResponseNodeTest(unittest.TestCase):
    def setUp(self):
        self._messages = Queue()

        rospy.init_node(_NODE_NAME)

        self.subscription = rospy.Subscriber(
            _RESPONSE_TOPIC,
            SomeResponse,
            self._messages.put,
        )

        self.thread = Thread(target=rospy.spin)
        self.thread.start()

    def tearDown(self):
        rospy.signal_shutdown('tearDown')

        self.thread.join()

    def test_some_request_to_some_response(self):
        publisher = rospy.Publisher(
            _REQUEST_TOPIC,
            SomeRequest,
            **_QOS_REQUEST
        )

        time.sleep(1)

        request = SomeRequest()
        request.timestamp = rospy.Time.from_seconds(time.time())
        request.source_id = _SOURCE_ID
        request.destination_id = _DESTINATION_ID
        request.conversation_id = _CONVERSATION_ID
        request.data = _DATA

        publisher.publish(request)

        try:
            response = self._messages.get(timeout=_TIMEOUT)
        except Empty:
            response = None

        self.assertIsNotNone(response)
        self.assertIsInstance(response, SomeResponse)
        self.assertEqual(response.source_id, _DESTINATION_ID)  # reversed
        self.assertEqual(response.destination_id, _SOURCE_ID)  # reversed
        self.assertEqual(response.data, 'You sent: {}'.format(repr(_DATA)))
