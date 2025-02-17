#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')

        self.subscription = self.create_subscription(
            Image,
            '/camera1/image_raw',
            self.listener_callback,
            10)
        self.subscription

        self.bridge = CvBridge()

        self.processor = ImageProcessor()

        self.Imout = self.create_publisher(Image, 'out/image', 10)

    def listener_callback(self, data):
        self.get_logger().info("Received an image")
        try:
            imCV = self.bridge.imgmsg_to_cv2(data, 'bgr8')

            imCV = self.processor.process(imCV)

            msg = self.bridge.cv2_to_imgmsg(imCV, encoding="bgr8")
            self.Imout.publish(msg)
            
            cv2.imshow("Camera", imCV)
            cv2.waitKey(10)
        except Exception as e:
            self.get_logger().error(f"Failed to convert image: {e}")

class ImageProcessor:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def process(self, imCV):
        gray = cv2.cvtColor(imCV, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(imCV, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return imCV


def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()