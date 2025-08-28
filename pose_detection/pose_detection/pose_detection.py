from body.body import Body
from pose_detection.pose_definitions import *


def exactly_one(*args) -> bool:
    """
    Check if exactly one of the arguments is True.
    """
    return sum(args) == 1


def is_warrior2(body: Body) -> bool:
    """
    Check if the body parts correspond to Warrior II pose.
    """
    if body.active_pose == "Warrior II":
        return exactly_one(warrior_pose_left_knee_bent_relaxed.is_satisfied(body), warrior_pose_right_knee_bent_relaxed.is_satisfied(body))

    return exactly_one(warrior_pose_left_knee_bent.is_satisfied(body), warrior_pose_right_knee_bent.is_satisfied(body))


def is_tree(body: Body) -> bool:
    """
    Check if the body parts correspond to Tree pose.
    """
    if body.active_pose == "Tree":
        return exactly_one(tree_pose_left_knee_bent_relaxed.is_satisfied(body), tree_pose_right_knee_bent_relaxed.is_satisfied(body))

    return exactly_one(tree_pose_left_knee_bent.is_satisfied(body), tree_pose_right_knee_bent.is_satisfied(body))


def is_downward_dog(body: Body) -> bool:
    """
    Check if the body parts correspond to Downward Dog pose.
    """
    if body.active_pose == "Downward Dog":
        return exactly_one(downward_dog_pose_left_relaxed.is_satisfied(body), downward_dog_pose_right_relaxed.is_satisfied(body))

    return exactly_one(downward_dog_pose_left.is_satisfied(body), downward_dog_pose_right.is_satisfied(body))


def is_snake(body: Body) -> bool:
    """
    Check if the body parts correspond to Cobra pose.
    """
    if body.active_pose == "Snake":
        return exactly_one(snake_pose_left_relaxed.is_satisfied(body), snake_pose_right_relaxed.is_satisfied(body))

    return exactly_one(snake_pose_left.is_satisfied(body), snake_pose_right.is_satisfied(body))


def is_cat(body: Body) -> bool:
    """
    Check if the body parts correspond to Cat pose.
    """
    if body.active_pose == "Cat":
        return exactly_one(cat_pose_left_relaxed.is_satisfied(body), cat_pose_right_relaxed.is_satisfied(body))

    return exactly_one(cat_pose_left.is_satisfied(body), cat_pose_right.is_satisfied(body))


def is_frog(body: Body) -> bool:
    """
    Check if the body parts correspond to Frog pose.
    """
    if body.active_pose == "Frog":
        return frog_pose_relaxed.is_satisfied(body)

    return frog_pose.is_satisfied(body)

def is_shark(body: Body) -> bool:
    """
    Check if the body parts correspond to Shark pose.
    """
    if body.active_pose == "Shark":
        return exactly_one(shark_pose_left_relaxed.is_satisfied(body), shark_pose_right_relaxed.is_satisfied(body))

    return exactly_one(shark_pose_left.is_satisfied(body), shark_pose_right.is_satisfied(body))


def detect_pose(body: Body) -> str | None:
    """
    Detect the pose of the body and return a tuple indicating if a pose is detected and its name.

    returns:
        Tuple[bool, str]: (is_pose_detected, pose_name)
    """

    if is_warrior2(body):
        body.active_pose = "Warrior II"
        return "Warrior II"
    if is_tree(body):
        body.active_pose = "Tree"
        return "Tree"
    if is_downward_dog(body):
        body.active_pose = "Downward Dog"
        return "Downward Dog"
    if is_snake(body):
        body.active_pose = "Snake"
        return "Snake"
    if is_cat(body):
        body.active_pose = "Cat"
        return "Cat"
    if is_frog(body):
        body.active_pose = "Frog"
        return "Frog"
    if is_shark(body):
        body.active_pose = "Shark"
        return "Shark"

    body.active_pose = None
    return None


