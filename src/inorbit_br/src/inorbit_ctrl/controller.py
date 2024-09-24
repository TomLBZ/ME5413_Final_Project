import rospy
import threading
from std_msgs.msg import String

AGENT_TOPIC = '/inorbit/custom_data/0'

class InOrbitCtrlNode:
    def __init__(self, agent_topic='/inorbit/custom_data/0'):
        self.pub = rospy.Publisher(agent_topic, String, queue_size=10)
        self.rate = rospy.Rate(10)
        self.msg = String()
        self.msg.data = ''
        self.input_thread = threading.Thread(target=self.get_input)
        self.input_thread.daemon = True
        self.input_thread.start()

    def get_input(self):
        while not rospy.is_shutdown():
            self.msg.data = input("Enter control signal (format: sig1:val1|sig2:val2...): ")

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()
            if len(self.msg.data) == 0:
                continue
            self.pub.publish(self.msg)

def main():
    rospy.init_node('inorbit_ctrl_node', anonymous=True)
    node = InOrbitCtrlNode(agent_topic=AGENT_TOPIC)
    node.run()

if __name__ == '__main__':
    main()
