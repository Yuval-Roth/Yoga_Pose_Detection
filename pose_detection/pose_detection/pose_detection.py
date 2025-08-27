from typing import Tuple, List

from body.body import Body
from body.math_utils import angle_diff


def exactly_one(*args) -> bool:
    """
    Check if exactly one of the arguments is True.
    """
    return sum(args) == 1


def is_angle(angle: float, target: float, tolerance: float, _range: Tuple[int] = None) -> bool:
    """
    Check if the angle is within the target ± tolerance.
    """
    if _range:
        if angle < _range[0] or angle > _range[1]:
            return False
    return angle_diff(angle,target) <= tolerance


def is_warrior2(body: Body) -> bool:
    """
    Check if the body parts correspond to Warrior II pose.
    """
    # Check that the hands are straight
    left_hand_straight = is_angle(body.left_elbow_angle(), 180, 40)
    right_hand_straight = is_angle(body.right_elbow_angle(), 180, 40)

    # Check that the arms are 90 degrees from the torso
    left_arm_perpendicular = is_angle(body.left_shoulder_angle(), 90, 15)
    right_arm_perpendicular = is_angle(body.right_shoulder_angle(), 90, 15)

    # Check that one leg is bent and the other is straight
    right_leg_angle = body.right_knee_angle()
    left_leg_angle = body.left_knee_angle()
    one_bent = exactly_one(is_angle(right_leg_angle, 105, 15), is_angle(left_leg_angle, 105, 15))
    one_straight = exactly_one(is_angle(right_leg_angle, 180, 15), is_angle(left_leg_angle, 180, 15))

    return (
            left_hand_straight
            and right_hand_straight
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
        is_angle(body.left_knee_angle(), 50, 50),
        is_angle(body.right_knee_angle(), 50, 50),
    ) and exactly_one(
        is_angle(body.left_hip_angle(),125,30),
        is_angle(body.right_hip_angle(),125,30),
    )
    one_leg_straight = exactly_one(
        is_angle(body.left_knee_angle(),180,30),
        is_angle(body.right_knee_angle(),180,30)
    ) and exactly_one(
        is_angle(body.left_hip_angle(),180,30),
        is_angle(body.right_hip_angle(),180,30)
    )

    # Palms together above the head
    left_arm_ok = is_angle(body.left_shoulder_angle(), 15, 30) and is_angle(body.left_elbow_angle(),130,70)
    right_arm_ok = is_angle(body.right_shoulder_angle(), 15, 30) and is_angle(body.right_elbow_angle(),130,70)

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
    left_arm_straight = is_angle(body.left_elbow_angle(),200,40)
    right_arm_straight = is_angle(body.right_elbow_angle(),160,40)
    left_leg_straight = is_angle(body.left_knee_angle(),200,30)
    right_leg_straight = is_angle(body.right_knee_angle(),160,30)
    left_hip_angle_ok = is_angle(body.left_hip_angle(),90,50)
    right_hip_angle_ok = is_angle(body.right_hip_angle(),270,50)
    left_shoulder_angle_ok = is_angle(body.left_shoulder_angle(),10,50)
    right_shoulder_angle_ok = is_angle(body.right_shoulder_angle(),340,50)
    hips_above_shoulders = body.hips_center().y < body.shoulders_center().y
    shoulders_above_face = body.shoulders_center().y < body.face_center().y

    if left_arm_straight and right_arm_straight and left_leg_straight and right_leg_straight and left_hip_angle_ok and right_hip_angle_ok and left_shoulder_angle_ok and right_shoulder_angle_ok and hips_above_shoulders and shoulders_above_face:
        return True

    # Facing right:
    left_arm_straight = is_angle(body.left_elbow_angle(),160,40)
    right_arm_straight = is_angle(body.right_elbow_angle(),200,40)
    left_leg_straight = is_angle(body.left_knee_angle(),160,30)
    right_leg_straight = is_angle(body.right_knee_angle(),200,30)
    left_hip_angle_ok = is_angle(body.left_hip_angle(),270,50)
    right_hip_angle_ok = is_angle(body.right_hip_angle(),90,50)
    left_shoulder_angle_ok = is_angle(body.left_shoulder_angle(),340,50)
    right_shoulder_angle_ok = is_angle(body.right_shoulder_angle(),10,50)
    hips_above_shoulders = body.hips_center().y < body.shoulders_center().y
    shoulders_above_face = body.shoulders_center().y < body.face_center().y

    return left_arm_straight and right_arm_straight and left_leg_straight and right_leg_straight and left_hip_angle_ok and right_hip_angle_ok and left_shoulder_angle_ok and right_shoulder_angle_ok and hips_above_shoulders and shoulders_above_face

def is_snake(body: Body) -> bool:
    """
    Check if the body parts correspond to Cobra pose.
    """
    # Facing left:
    left_arm_straight = is_angle(body.left_elbow_angle(),170,40)
    right_arm_straight = is_angle(body.right_elbow_angle(),170,40)
    left_leg_straight = is_angle(body.left_knee_angle(),160,30)
    right_leg_straight = is_angle(body.right_knee_angle(),200,30)
    left_hip_angle_ok = is_angle(body.left_hip_angle(),200,50)
    right_hip_angle_ok = is_angle(body.right_hip_angle(),140,50)
    left_shoulder_angle_ok = is_angle(body.left_shoulder_angle(),150,30)
    right_shoulder_angle_ok = is_angle(body.right_shoulder_angle(),210,30)
    hips_below_shoulders = body.hips_center().y > body.shoulders_center().y
    palms_below_hips = body.left_palm().y > body.hips_center().y and body.right_palm().y > body.hips_center().y

    if left_arm_straight and right_arm_straight and left_leg_straight and right_leg_straight and left_hip_angle_ok and right_hip_angle_ok and left_shoulder_angle_ok and right_shoulder_angle_ok and hips_below_shoulders and palms_below_hips:
        return True


    # Facing right:
    left_arm_straight2 = is_angle(body.left_elbow_angle(),170,40)
    right_arm_straight2 = is_angle(body.right_elbow_angle(),170,40)
    left_leg_straight2 = is_angle(body.left_knee_angle(),200,30)
    right_leg_straight2 = is_angle(body.right_knee_angle(),160,30)
    left_hip_angle_ok2 = is_angle(body.left_hip_angle(),140,50)
    right_hip_angle_ok2 = is_angle(body.right_hip_angle(),200,50)
    left_shoulder_angle_ok2 = is_angle(body.left_shoulder_angle(),210,30)
    right_shoulder_angle_ok2 = is_angle(body.right_shoulder_angle(),150,30)
    hips_below_shoulders2 = body.hips_center().y > body.shoulders_center().y
    palms_below_hips2 = body.left_palm().y > body.hips_center().y and body.right_palm().y > body.hips_center().y
    return left_arm_straight2 and right_arm_straight2 and left_leg_straight2 and right_leg_straight2 and left_hip_angle_ok2 and right_hip_angle_ok2 and left_shoulder_angle_ok2 and right_shoulder_angle_ok2 and hips_below_shoulders2 and palms_below_hips2

def is_cat(body: Body) -> bool:
    """
    Check if the body parts correspond to Cat pose.
    """
    # Facing left:
    left_arm_straight = is_angle(body.left_elbow_angle(),180,40)
    right_arm_straight = is_angle(body.right_elbow_angle(),180,40)
    left_shoulder_angle_ok = is_angle(body.left_shoulder_angle(),270,30)
    right_shoulder_angle_ok = is_angle(body.right_shoulder_angle(),90,30)
    left_hip_angle_ok = is_angle(body.left_hip_angle(),260,50)
    right_hip_angle_ok = is_angle(body.right_hip_angle(),100,50)
    left_leg_angle_ok = is_angle(body.left_knee_angle(),260,30)
    right_leg_angle_ok = is_angle(body.right_knee_angle(),90,30)
    head_below_shoulders = body.face_center().y > body.shoulders_center().y

    if left_arm_straight and right_arm_straight and left_shoulder_angle_ok and right_shoulder_angle_ok and left_hip_angle_ok and right_hip_angle_ok and left_leg_angle_ok and right_leg_angle_ok and head_below_shoulders:
        return True

    # Facing right:
    left_arm_straight2 = is_angle(body.left_elbow_angle(),180,40)
    right_arm_straight2 = is_angle(body.right_elbow_angle(),180,40)
    left_shoulder_angle_ok2 = is_angle(body.left_shoulder_angle(),90,30)
    right_shoulder_angle_ok2 = is_angle(body.right_shoulder_angle(),270,30)
    left_hip_angle_ok2 = is_angle(body.left_hip_angle(),100,50)
    right_hip_angle_ok2 = is_angle(body.right_hip_angle(),260,50)
    left_leg_angle_ok2 = is_angle(body.left_knee_angle(),90,30)
    right_leg_angle_ok2 = is_angle(body.right_knee_angle(),260,30)
    head_below_shoulders2 = body.face_center().y > body.shoulders_center().y
    return left_arm_straight2 and right_arm_straight2 and left_shoulder_angle_ok2 and right_shoulder_angle_ok2 and left_hip_angle_ok2 and right_hip_angle_ok2 and left_leg_angle_ok2 and right_leg_angle_ok2 and head_below_shoulders2

def is_frog(body: Body) -> bool:
    """
    Check if the body parts correspond to Frog pose.
    """
    left_hand_straight = is_angle(body.left_elbow_angle(),180,40)
    right_hand_straight = is_angle(body.right_elbow_angle(),180,40)
    left_leg_angle_ok = is_angle(body.left_knee_angle(),70,30)
    right_leg_angle_ok = is_angle(body.right_knee_angle(),70,30)
    left_hip_angle_ok = is_angle(body.left_hip_angle(),70,30)
    right_hip_angle_ok = is_angle(body.right_hip_angle(),70,30)
    hips_below_shoulders = body.hips_center().y > body.shoulders_center().y
    palms_below_hips = body.left_palm().y > body.hips_center().y and body.right_palm().y > body.hips_center().y

    return left_hand_straight and right_hand_straight and left_leg_angle_ok and right_leg_angle_ok and left_hip_angle_ok and right_hip_angle_ok and hips_below_shoulders and palms_below_hips

def is_shark(body: Body) -> bool:
    """
    Check if the body parts correspond to Shark pose.
    """
    # Facing left:
    left_arm_straight = is_angle(body.left_elbow_angle(),180,40)
    right_arm_straight = is_angle(body.right_elbow_angle(),180,40)
    left_knee_angle_ok = is_angle(body.left_knee_angle(),210,30)
    right_knee_angle_ok = is_angle(body.right_knee_angle(),145,30)
    left_shoulder_angle_ok = is_angle(body.left_shoulder_angle(),190,30)
    right_shoulder_angle_ok = is_angle(body.right_shoulder_angle(),170,30)
    left_hip_angle_ok = is_angle(body.left_hip_angle(),190,30)
    right_hip_angle_ok = is_angle(body.right_hip_angle(),170,30)
    shoulders_height_close_to_knees = abs(body.knees_center().y / body.shoulders_center().y) < 1.2

    if left_arm_straight and right_arm_straight and left_knee_angle_ok and right_knee_angle_ok and left_shoulder_angle_ok and right_shoulder_angle_ok and left_hip_angle_ok and right_hip_angle_ok and shoulders_height_close_to_knees:
        return True

    # Facing right:
    left_arm_straight2 = is_angle(body.left_elbow_angle(),180,40)
    right_arm_straight2 = is_angle(body.right_elbow_angle(),180,40)
    left_knee_angle_ok2 = is_angle(body.left_knee_angle(),145,60)
    right_knee_angle_ok2 = is_angle(body.right_knee_angle(),210,60)
    left_shoulder_angle_ok2 = is_angle(body.left_shoulder_angle(),190,50)
    right_shoulder_angle_ok2 = is_angle(body.right_shoulder_angle(),200,50)
    left_hip_angle_ok2 = is_angle(body.left_hip_angle(),170,30)
    right_hip_angle_ok2 = is_angle(body.right_hip_angle(),190,30)
    shoulders_height_close_to_knees2 = abs(body.knees_center().y / body.shoulders_center().y) < 1.2

    return left_arm_straight2 and right_arm_straight2 and left_knee_angle_ok2 and right_knee_angle_ok2 and left_shoulder_angle_ok2 and right_shoulder_angle_ok2 and left_hip_angle_ok2 and right_hip_angle_ok2 and shoulders_height_close_to_knees2


def detect_pose(body: Body) -> List[str]:
    """
    Detect the pose of the body and return a tuple indicating if a pose is detected and its name.

    returns:
        Tuple[bool, str]: (is_pose_detected, pose_name)
    """

    detected_poses = []
    if is_warrior2(body):
        detected_poses.append("Warrior II")
    if is_tree(body):
        detected_poses.append("Tree")
    if is_downward_dog(body):
        detected_poses.append("Downward Dog")
    if is_snake(body):
        detected_poses.append("Snake")
    if is_cat(body):
        detected_poses.append("Cat")
    if is_frog(body):
        detected_poses.append("Frog")
    if is_shark(body):
        detected_poses.append("Shark")

    return detected_poses


