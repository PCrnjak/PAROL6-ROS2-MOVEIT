from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_rsp_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("parol6", package_name="parol6_moveit").to_moveit_configs()
    return generate_rsp_launch(moveit_config)
