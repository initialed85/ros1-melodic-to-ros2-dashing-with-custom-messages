#!/usr/bin/python3

import time

import rclpy
from gateway_interfaces.msg import SomeRequest, SomeResponse
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy

_NODE_NAME = 'some_request_to_some_response'
_REQUEST_TOPIC = 'some_request'
_RESPONSE_TOPIC = 'some_response'
_QOS = QoSProfile(depth=1)
_QOS.durability = QoSDurabilityPolicy.RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL
_QOS.history = QoSHistoryPolicy.RMW_QOS_POLICY_HISTORY_KEEP_LAST
_QOS.reliability = QoSReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_RELIABLE

_SOURCE_ID = 1


class SomeRequestToSomeResponseNode(Node):
    def __init__(self):
        super().__init__(_NODE_NAME)

        self.logger = self.get_logger()

        self.publisher = self.create_publisher(
            SomeResponse,
            _RESPONSE_TOPIC,
            _QOS
        )

        self.subscription = self.create_subscription(
            SomeRequest,
            _REQUEST_TOPIC,
            self.some_request_handler,
            _QOS
        )

    def some_request_handler(self, msg: SomeRequest):
        self.logger.info('Received: {}'.format(msg))

        response_msg = SomeResponse()

        unix_timestamp = time.time()

        response_msg.timestamp.sec = int(unix_timestamp)
        response_msg.timestamp.nanosec = int((unix_timestamp - int(unix_timestamp)) * 1e+9)

        response_msg.source_id = _SOURCE_ID
        response_msg.destination_id = msg.source_id
        response_msg.conversation_id = msg.conversation_id
        response_msg.data = 'You sent: {}'.format(repr(msg.data))

        self.publisher.publish(response_msg)

        self.logger.info('Sent: {}'.format(response_msg))


if __name__ == '__main__':
    import sys

    rclpy.init(args=sys.argv)

    node = SomeRequestToSomeResponseNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()
