from typing import Tuple

from body.body import Body


def exactly_one(*args) -> bool:
    """
    Check if exactly one of the arguments is True.
    """
    return sum(args) == 1


def is_angle(angle: float, target: float, tolerance: float) -> bool:
    """
    Check if the angle is within the target ± tolerance.
    """
    return abs(angle - target) <= tolerance


def is_warrior2(body: Body) -> bool:
    """
    Check if the body parts correspond to Warrior II pose.
    """

    # Check that the arms are 90 degrees from the torso
    left_arm_perpendicular = is_angle(body.left_shoulder_angle(), 90, 15)
    right_arm_perpendicular = is_angle(body.right_shoulder_angle(), 90, 15)

    # Check that one leg is bent and the other is straight
    right_leg_angle = body.right_knee_angle()
    left_leg_angle = body.left_knee_angle()
    one_bent = exactly_one(is_angle(right_leg_angle, 105, 15), is_angle(left_leg_angle, 105, 15))
    one_straight = exactly_one(body.is_left_leg_straight(), body.is_right_leg_straight())

    return (
            body.is_right_hand_straight()
            and body.is_left_hand_straight()
            and left_arm_perpendicular
            and right_arm_perpendicular
            and one_bent
            and one_straight
    )

def is_tree(body: Body) -> bool:
    """
    Check if the body parts correspond to Tree pose.
    """

    # Check that one leg is bent and lifted and the other is straight
    one_leg_bent_and_lifted = exactly_one(
        is_angle(body.left_knee_angle(), 45, 15),
        is_angle(body.right_knee_angle(), 45, 15),
    ) and exactly_one(
        is_angle(body.left_hip_angle(),125,15),
        is_angle(body.right_hip_angle(),125,15),
    )
    one_leg_straight = exactly_one(
        body.is_left_leg_straight(),
        body.is_right_leg_straight()
    ) and exactly_one(
        is_angle(body.left_hip_angle(),180,15),
        is_angle(body.right_hip_angle(),180,15)
    )

    # Palms together above the head
    left_arm_ok = is_angle(body.left_shoulder_angle(), 15, 15) and is_angle(body.left_elbow_angle(),110,20)
    right_arm_ok = is_angle(body.right_shoulder_angle(), 15, 15) and is_angle(body.right_elbow_angle(),110,20)


    return (
        one_leg_bent_and_lifted
        and one_leg_straight
        and left_arm_ok
        and right_arm_ok
    )

def is_downward_dog(body: Body) -> bool:
    """
    Check if the body parts correspond to Downward Dog pose.
    """
    # Facing left:
    left_arm_straight = is_angle(body.left_elbow_angle(),200,15)
    right_arm_straight = is_angle(body.right_elbow_angle(),160,15)
    left_leg_straight = is_angle(body.left_knee_angle(),200,15)
    right_leg_straight = is_angle(body.right_knee_angle(),160,15)



def detect_pose(body: Body) -> Tuple[bool, str]:
    """
    Detect the pose of the body and return a tuple indicating if a pose is detected and its name.


    returns:
        Tuple[bool, str]: (is_pose_detected, pose_name)
    """
    if is_warrior2(body):
        return True, "Warrior II Pose"
    if is_tree(body):
        return True, "Tree Pose"
    return False, "No Recognized Pose"

