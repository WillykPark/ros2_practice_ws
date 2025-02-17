import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([

        # launch.actions.IncludeLaunchDescription(
        #     launch.launch_description_sources.PythonLaunchDescriptionSource(
        #         ['/opt/ros/humble/share/usb_cam/launch/camera.launch.py']  
        #     )
        # ),
        
        
        launch_ros.actions.Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='camera1',
            namespace='camera1',
            output='screen',
            parameters=[
                {'video_device': '/dev/video0'},
                {'image_width': 640},
                {'image_height': 480},
                {'pixel_format': 'yuyv'},
                {'camera_frame_id': 'camera1_frame'}
            ],
            remappings=[
            ('/image_raw', '/camera1/image_raw')
            ]
        ),

        launch_ros.actions.Node(
            package='AutoRobo_pkg',
            executable='image_subscriber',
            name='image_subscriber',
            output='screen'
        ),

        launch_ros.actions.Node(
            package='rqt_image_view',
            executable='rqt_image_view',
            name='image_view',
            output='screen'
        ),
    ])
