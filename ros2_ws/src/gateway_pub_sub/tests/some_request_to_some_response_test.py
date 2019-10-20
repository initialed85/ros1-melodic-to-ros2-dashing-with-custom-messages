import time
import unittest
from queue import Queue, Empty

import rclpy
from gateway_interfaces.msg import SomeRequest, SomeResponse
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy

_NODE_NAME = 'some_request_to_some_response_test'
_REQUEST_TOPIC = 'some_request'
_RESPONSE_TOPIC = 'some_response'
_QOS = QoSProfile(depth=1)
_QOS.durability = QoSDurabilityPolicy.RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL
_QOS.history = QoSHistoryPolicy.RMW_QOS_POLICY_HISTORY_KEEP_LAST
_QOS.reliability = QoSReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_RELIABLE

_SOURCE_ID = 2
_DESTINATION_ID = 1
_CONVERSATION_ID = 8008135
_DATA = 'Some message'

_TIMEOUT = 10


class SomeRequestToSomeResponseNodeTest(unittest.TestCase):
    def setUp(self):
        self._messages = Queue()

        rclpy.init()

        self._node = rclpy.create_node(_NODE_NAME)

    def tearDown(self):
        rclpy.shutdown()

    def test_some_request_to_some_response(self):
        self._node.create_subscription(
            SomeResponse,
            _RESPONSE_TOPIC,
            self._messages.put,
            _QOS
        )

        publisher = self._node.create_publisher(
            SomeRequest,
            _REQUEST_TOPIC,
            _QOS
        )

        request = SomeRequest()

        unix_timestamp = time.time()
        request.timestamp.sec = int(unix_timestamp)
        request.timestamp.nanosec = int((unix_timestamp - int(unix_timestamp)) * 1e+9)

        request.source_id = _SOURCE_ID
        request.destination_id = _DESTINATION_ID
        request.conversation_id = _CONVERSATION_ID
        request.data = _DATA

        publisher.publish(request)

        rclpy.spin_once(self._node, timeout_sec=_TIMEOUT)

        try:
            response = self._messages.get_nowait()
        except Empty:
            response = None

        self.assertIsNotNone(response)
        self.assertIsInstance(response, SomeResponse)
        self.assertEqual(response.source_id, _DESTINATION_ID)  # reversed
        self.assertEqual(response.destination_id, _SOURCE_ID)  # reversed
        self.assertEqual(response.data, 'You sent: {}'.format(repr(_DATA)))
