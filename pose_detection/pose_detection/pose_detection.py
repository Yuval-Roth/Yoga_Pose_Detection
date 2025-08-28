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

def is_monkey(body: Body) -> bool:
    """
    Check if the body parts correspond to Monkey pose.
    """
    if body.active_pose == "Monkey":
        return exactly_one(monkey_pose_left_relaxed.is_satisfied(body), monkey_pose_right_relaxed.is_satisfied(body))

    return exactly_one(monkey_pose_left.is_satisfied(body), monkey_pose_right.is_satisfied(body))

def is_eagle(body: Body) -> bool:
    """
    Check if the body parts correspond to Eagle pose.
    """
    if body.active_pose == "Eagle":
        return exactly_one(
            eagle_pose_right_leg_crossed_right_arm_under_relaxed.is_satisfied(body),
            eagle_pose_left_leg_crossed_left_arm_under_relaxed.is_satisfied(body),
            eagle_pose_right_leg_crossed_left_arm_under_relaxed.is_satisfied(body),
            eagle_pose_left_leg_crossed_right_arm_under_relaxed.is_satisfied(body)
        )

    return exactly_one(
        eagle_pose_right_leg_crossed_right_arm_under.is_satisfied(body),
        eagle_pose_left_leg_crossed_left_arm_under.is_satisfied(body),
        eagle_pose_right_leg_crossed_left_arm_under.is_satisfied(body),
        eagle_pose_left_leg_crossed_right_arm_under.is_satisfied(body)
    )
#
def is_crocodile(body: Body) -> bool:
    """
    Check if the body parts correspond to Crocodile pose.
    """
    if body.active_pose == "Crocodile":
        return exactly_one(crocodile_pose_left_relaxed.is_satisfied(body), crocodile_pose_right_relaxed.is_satisfied(body))

    return exactly_one(crocodile_pose_left.is_satisfied(body), crocodile_pose_right.is_satisfied(body))
#
def is_lotus(body: Body) -> bool:
    """
    Check if the body parts correspond to Lotus pose.
    """
    if body.active_pose == "Lotus":
        return lotus_pose_relaxed.is_satisfied(body)

    return lotus_pose.is_satisfied(body)

def is_butterfly(body: Body) -> bool:
    """
    Check if the body parts correspond to Butterfly pose.
    """
    if body.active_pose == "Butterfly":
        return butterfly_pose_relaxed.is_satisfied(body)

    return butterfly_pose.is_satisfied(body)
#
def is_crow(body: Body) -> bool:
    """
    Check if the body parts correspond to Crow pose.
    """
    if body.active_pose == "Crow":
        return exactly_one(crow_pose_left_relaxed.is_satisfied(body), crow_pose_right_relaxed.is_satisfied(body))

    return exactly_one(crow_pose_left.is_satisfied(body), crow_pose_right.is_satisfied(body))


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
    if is_monkey(body):
        body.active_pose = "Monkey"
        return "Monkey"
    if is_eagle(body):
        body.active_pose = "Eagle"
        return "Eagle"
    if is_crocodile(body):
        body.active_pose = "Crocodile"
        return "Crocodile"
    if is_lotus(body):
        body.active_pose = "Lotus"
        return "Lotus"
    if is_butterfly(body):
        body.active_pose = "Butterfly"
        return "Butterfly"
    if is_crow(body):
        body.active_pose = "Crow"
        return "Crow"

    body.active_pose = None
    return None


