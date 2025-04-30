import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from moveit2 import MoveIt2
from moveit2.ros2_interface import MoveIt2Interface
import franka_control_bindings

class MoveFrankaArm(Node):
    def __init__(self):
        super().__init__('move_franka_arm')
        self.moveit2 = MoveIt2Interface()
        self.moveit2_arm = MoveIt2(
            node=self,
            joint_names=[
                "fr3_joint1", "fr3_joint2", "fr3_joint3", 
                "fr3_joint4", "fr3_joint5", "fr3_joint6", 
                "fr3_joint7"
            ],
            base_link_name="fr3_link0",
            end_effector_name="fr3_link8",
            group_name="fr3_arm"
        )

    def move_to_xyz(self, x, y, z):
        target_pose = PoseStamped()
        target_pose.header.frame_id = "fr3_link0"
        target_pose.pose.position.x = x
        target_pose.pose.position.y = y
        target_pose.pose.position.z = z

        # Fixed orientation (identity quaternion - pointing forward)
        target_pose.pose.orientation.x = 0.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 1.0

        self.get_logger().info(f"Moving to x={x}, y={y}, z={z}")
        self.moveit2_arm.move_to_pose(target_pose)

def main(args=None):
    rclpy.init(args=args)
    move_node = MoveFrankaArm()
    move_node.move_to_xyz(0.4, 0.0, 0.3)  # Example XYZ
    rclpy.spin(move_node)

if __name__ == '__main__':
    main()