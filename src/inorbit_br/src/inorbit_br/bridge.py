import rospy
from std_msgs.msg import String

AGENT_TOPIC = '/inorbit/custom_command'
GOAL_TOPIC = '/rviz_panel/goal_name'

class InorbitBrNode:
    def __init__(self, agent_topic='/inorbit/custom_command', goal_topic='/robot/goal_name'):
        self.pub = rospy.Publisher(goal_topic, String, queue_size=10)
        self.sub = rospy.Subscriber(agent_topic, String, self.callback)
        self.rate = rospy.Rate(10)
        self.msg = String()

    def callback(self, data: String):
        data: str = data.data
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
        # in the format "sig1:val1|sig2:val2"
        sub_cmds = data.split('|')
        for sub_cmd in sub_cmds:
            sig, val = sub_cmd.split(':')
            if sig == 'goal':
                self.msg.data = val
                self.pub.publish(self.msg)
            else:
                rospy.logwarn('Unknown control signal: %s', sig)
                self.msg.data = ''

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

def main():
    rospy.init_node('inorbit_br_node', anonymous=True)
    node = InorbitBrNode(
        agent_topic=AGENT_TOPIC,
        goal_topic=GOAL_TOPIC
    )
    node.run()

if __name__ == '__main__':
    main()