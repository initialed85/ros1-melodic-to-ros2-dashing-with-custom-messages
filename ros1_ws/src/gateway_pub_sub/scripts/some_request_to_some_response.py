#!/usr/bin/python

import time

import rospy
from gateway_msgs.msg import SomeRequest, SomeResponse

_NODE_NAME = 'some_request_to_some_response'
_REQUEST_TOPIC = 'some_request'
_RESPONSE_TOPIC = 'some_response'
_QOS = {
    'latch': True,
    'queue_size': 1
}
_SOURCE_ID = 1


class SomeRequestToResponseNode(object):
    def __init__(self):
        rospy.init_node(_NODE_NAME)

        self.publisher = rospy.Publisher(
            _RESPONSE_TOPIC,
            SomeResponse,
            **_QOS
        )

        self.subscription = rospy.Subscriber(
            _REQUEST_TOPIC,
            SomeRequest,
            self.some_request_handler
        )

    def some_request_handler(self, msg):
        rospy.loginfo('Received: {}'.format(msg))

        response_msg = SomeRequest()
        response_msg.timestamp = rospy.Time.from_seconds(time.time())
        response_msg.source_id = _SOURCE_ID
        response_msg.destination_id = msg.source_id
        response_msg.conversation_id = msg.conversation_id
        response_msg.data = 'You sent: {}'.format(repr(msg.data))

        self.publisher.publish(response_msg)

        rospy.loginfo('Sent: {}'.format(response_msg))


if __name__ == '__main__':
    node = SomeRequestToResponseNode()

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
