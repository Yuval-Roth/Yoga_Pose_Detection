from pose_detection.pose_rules import RangePoseRule, AcceptAllPoseRule, GenericPoseRule
from pose_detection.pose_test import PoseTest

# =========================================================================================== |
# =================================== Warrior II ============================================ |
# =========================================================================================== |

warrior_pose_left_knee_bent = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(90, 15, 15),
    right_shoulder_angle_rule=RangePoseRule(90, 15, 15),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=AcceptAllPoseRule(),
    right_hip_angle_rule=AcceptAllPoseRule(),
    left_knee_angle_rule=RangePoseRule(105, 15, 15),
    right_knee_angle_rule=RangePoseRule(180, 15, 15),
)

warrior_pose_right_knee_bent = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(90, 15, 15),
    right_shoulder_angle_rule=RangePoseRule(90, 15, 15),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=AcceptAllPoseRule(),
    right_hip_angle_rule=AcceptAllPoseRule(),
    left_knee_angle_rule=RangePoseRule(180, 15, 15),
    right_knee_angle_rule=RangePoseRule(105, 15, 15),
)

warrior_pose_left_knee_bent_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(90, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(90, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 60, 60),
    right_elbow_angle_rule=RangePoseRule(180, 60, 60),
    left_hip_angle_rule=AcceptAllPoseRule(),
    right_hip_angle_rule=AcceptAllPoseRule(),
    left_knee_angle_rule=RangePoseRule(105, 30, 30),
    right_knee_angle_rule=RangePoseRule(180, 30, 30),
)

warrior_pose_right_knee_bent_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(90, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(90, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 60, 60),
    right_elbow_angle_rule=RangePoseRule(180, 60, 60),
    left_hip_angle_rule=AcceptAllPoseRule(),
    right_hip_angle_rule=AcceptAllPoseRule(),
    left_knee_angle_rule=RangePoseRule(180, 30, 30),
    right_knee_angle_rule=RangePoseRule(105, 30, 30),
)

# =========================================================================================== |
# ====================================== Tree =============================================== |
# =========================================================================================== |

tree_pose_left_knee_bent = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    left_elbow_angle_rule=RangePoseRule(130, 70, 70),
    right_elbow_angle_rule=RangePoseRule(130, 70, 70),
    left_hip_angle_rule=RangePoseRule(125, 30, 30),
    right_hip_angle_rule=RangePoseRule(180, 30, 30),
    left_knee_angle_rule=RangePoseRule(50, 50, 50),
    right_knee_angle_rule=RangePoseRule(180, 30, 30),
)

tree_pose_right_knee_bent = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    left_elbow_angle_rule=RangePoseRule(130, 70, 70),
    right_elbow_angle_rule=RangePoseRule(130, 70, 70),
    left_hip_angle_rule=RangePoseRule(180, 30, 30),
    right_hip_angle_rule=RangePoseRule(125, 30, 30),
    left_knee_angle_rule=RangePoseRule(180, 30, 30),
    right_knee_angle_rule=RangePoseRule(50, 50, 50),
)

# TODO: tune these relaxed versions of Tree

tree_pose_left_knee_bent_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    left_elbow_angle_rule=RangePoseRule(130, 70, 70),
    right_elbow_angle_rule=RangePoseRule(130, 70, 70),
    left_hip_angle_rule=RangePoseRule(125, 30, 30),
    right_hip_angle_rule=RangePoseRule(180, 30, 30),
    left_knee_angle_rule=RangePoseRule(50, 50, 50),
    right_knee_angle_rule=RangePoseRule(180, 30, 30),
)

tree_pose_right_knee_bent_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    left_elbow_angle_rule=RangePoseRule(130, 70, 70),
    right_elbow_angle_rule=RangePoseRule(130, 70, 70),
    left_hip_angle_rule=RangePoseRule(180, 30, 30),
    right_hip_angle_rule=RangePoseRule(125, 30, 30),
    left_knee_angle_rule=RangePoseRule(180, 30, 30),
    right_knee_angle_rule=RangePoseRule(50, 50, 50),
)

# =========================================================================================== |
# =================================== Downward Dog ========================================== |
# =========================================================================================== |

downward_dog_pose_left = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(10, 50, 50),
    right_shoulder_angle_rule=RangePoseRule(340, 50, 50),
    left_elbow_angle_rule=RangePoseRule(200, 40, 40),
    right_elbow_angle_rule=RangePoseRule(160, 40, 40),
    left_hip_angle_rule=RangePoseRule(90, 50, 50),
    right_hip_angle_rule=RangePoseRule(270, 50, 50),
    left_knee_angle_rule=RangePoseRule(200, 30, 30),
    right_knee_angle_rule=RangePoseRule(160, 30, 30),
    hips_above_shoulders=GenericPoseRule(lambda b: b.hips_center().y < b.shoulders_center().y),
    shoulders_above_face=GenericPoseRule(lambda b: b.shoulders_center().y < b.face_center().y)
)

downward_dog_pose_right = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(340, 50, 50),
    right_shoulder_angle_rule=RangePoseRule(10, 50, 50),
    left_elbow_angle_rule=RangePoseRule(160, 40, 40),
    right_elbow_angle_rule=RangePoseRule(200, 40, 40),
    left_hip_angle_rule=RangePoseRule(270, 50, 50),
    right_hip_angle_rule=RangePoseRule(90, 50, 50),
    left_knee_angle_rule=RangePoseRule(160, 30, 30),
    right_knee_angle_rule=RangePoseRule(200, 30, 30),
    hips_above_shoulders=GenericPoseRule(lambda b: b.hips_center().y < b.shoulders_center().y),
    shoulders_above_face=GenericPoseRule(lambda b: b.shoulders_center().y < b.face_center().y)
)

# TODO: tune these relaxed versions of Downward Dog

downward_dog_pose_left_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(10, 50, 50),
    right_shoulder_angle_rule=RangePoseRule(340, 50, 50),
    left_elbow_angle_rule=RangePoseRule(200, 40, 40),
    right_elbow_angle_rule=RangePoseRule(160, 40, 40),
    left_hip_angle_rule=RangePoseRule(90, 50, 50),
    right_hip_angle_rule=RangePoseRule(270, 50, 50),
    left_knee_angle_rule=RangePoseRule(200, 30, 30),
    right_knee_angle_rule=RangePoseRule(160, 30, 30),
    hips_above_shoulders=GenericPoseRule(lambda b: b.hips_center().y < b.shoulders_center().y),
    shoulders_above_face=GenericPoseRule(lambda b: b.shoulders_center().y < b.face_center().y)
)

downward_dog_pose_right_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(340, 50, 50),
    right_shoulder_angle_rule=RangePoseRule(10, 50, 50),
    left_elbow_angle_rule=RangePoseRule(160, 40, 40),
    right_elbow_angle_rule=RangePoseRule(200, 40, 40),
    left_hip_angle_rule=RangePoseRule(270, 50, 50),
    right_hip_angle_rule=RangePoseRule(90, 50, 50),
    left_knee_angle_rule=RangePoseRule(160, 30, 30),
    right_knee_angle_rule=RangePoseRule(200, 30, 30),
    hips_above_shoulders=GenericPoseRule(lambda b: b.hips_center().y < b.shoulders_center().y),
    shoulders_above_face=GenericPoseRule(lambda b: b.shoulders_center().y < b.face_center().y)
)