from body.math_utils import relatively_close
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

left_palm_above_head_rule = GenericPoseRule(lambda b: b.left_palm().y < b.face_center().y)
right_palm_above_head_rule = GenericPoseRule(lambda b: b.right_palm().y < b.face_center().y)

tree_pose_left_knee_bent = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(15, 30, 30),
    left_elbow_angle_rule=RangePoseRule(130, 70, 70),
    right_elbow_angle_rule=RangePoseRule(130, 70, 70),
    left_hip_angle_rule=RangePoseRule(125, 30, 30),
    right_hip_angle_rule=RangePoseRule(180, 30, 30),
    left_knee_angle_rule=RangePoseRule(50, 50, 50),
    right_knee_angle_rule=RangePoseRule(180, 30, 30),
    left_palm_above_head_rule=left_palm_above_head_rule,
    right_palm_above_head_rule=right_palm_above_head_rule
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
    left_palm_above_head_rule=left_palm_above_head_rule,
    right_palm_above_head_rule=right_palm_above_head_rule
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
    left_palm_above_head_rule=left_palm_above_head_rule,
    right_palm_above_head_rule=right_palm_above_head_rule
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
    left_palm_above_head_rule=left_palm_above_head_rule,
    right_palm_above_head_rule=right_palm_above_head_rule
)

# =========================================================================================== |
# =================================== Downward Dog ========================================== |
# =========================================================================================== |

hips_above_shoulders_rule = GenericPoseRule(lambda b: b.hips_center().y < b.shoulders_center().y)
shoulders_above_face_rule = GenericPoseRule(lambda b: b.shoulders_center().y < b.face_center().y)

downward_dog_pose_left = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(10, 50, 50),
    right_shoulder_angle_rule=RangePoseRule(340, 50, 50),
    left_elbow_angle_rule=RangePoseRule(200, 40, 40),
    right_elbow_angle_rule=RangePoseRule(160, 40, 40),
    left_hip_angle_rule=RangePoseRule(90, 50, 50),
    right_hip_angle_rule=RangePoseRule(270, 50, 50),
    left_knee_angle_rule=RangePoseRule(200, 30, 30),
    right_knee_angle_rule=RangePoseRule(160, 30, 30),
    hips_above_shoulders_rule=hips_above_shoulders_rule,
    shoulders_above_face_rule=shoulders_above_face_rule
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
    hips_above_shoulders_rule=hips_above_shoulders_rule,
    shoulders_above_face_rule=shoulders_above_face_rule
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
    hips_above_shoulders_rule=hips_above_shoulders_rule,
    shoulders_above_face_rule=shoulders_above_face_rule
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
    hips_above_shoulders_rule=hips_above_shoulders_rule,
    shoulders_above_face_rule=shoulders_above_face_rule
)

# =========================================================================================== |
# ====================================== Snake ============================================== |
# =========================================================================================== |

hips_below_shoulders_rule = GenericPoseRule(lambda b: b.hips_center().y > b.shoulders_center().y)
palms_below_hips_rule = GenericPoseRule(lambda b: b.left_palm().y > b.hips_center().y and b.right_palm().y > b.hips_center().y)

snake_pose_left = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(150, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(210, 30, 30),
    left_elbow_angle_rule=RangePoseRule(170, 40, 40),
    right_elbow_angle_rule=RangePoseRule(170, 40, 40),
    left_hip_angle_rule=RangePoseRule(200, 50, 50),
    right_hip_angle_rule=RangePoseRule(140, 50, 50),
    left_knee_angle_rule=RangePoseRule(160, 30, 30),
    right_knee_angle_rule=RangePoseRule(200, 30, 30),
    hips_below_shoulders_rule=hips_below_shoulders_rule,
    palms_below_hips_rule=palms_below_hips_rule
)

snake_pose_right = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(210, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(150, 30, 30),
    left_elbow_angle_rule=RangePoseRule(170, 40, 40),
    right_elbow_angle_rule=RangePoseRule(170, 40, 40),
    left_hip_angle_rule=RangePoseRule(140, 50, 50),
    right_hip_angle_rule=RangePoseRule(200, 50, 50),
    left_knee_angle_rule=RangePoseRule(200, 30, 30),
    right_knee_angle_rule=RangePoseRule(160, 30, 30),
    hips_below_shoulders_rule=hips_below_shoulders_rule,
    palms_below_hips_rule=palms_below_hips_rule
)

# TODO: tune these relaxed versions of Snake

snake_pose_left_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(150, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(210, 30, 30),
    left_elbow_angle_rule=RangePoseRule(170, 40, 40),
    right_elbow_angle_rule=RangePoseRule(170, 40, 40),
    left_hip_angle_rule=RangePoseRule(200, 50, 50),
    right_hip_angle_rule=RangePoseRule(140, 50, 50),
    left_knee_angle_rule=RangePoseRule(160, 30, 30),
    right_knee_angle_rule=RangePoseRule(200, 30, 30),
    hips_below_shoulders_rule=hips_below_shoulders_rule,
    palms_below_hips_rule=palms_below_hips_rule
)

snake_pose_right_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(210, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(150, 30, 30),
    left_elbow_angle_rule=RangePoseRule(170, 40, 40),
    right_elbow_angle_rule=RangePoseRule(170, 40, 40),
    left_hip_angle_rule=RangePoseRule(140, 50, 50),
    right_hip_angle_rule=RangePoseRule(200, 50, 50),
    left_knee_angle_rule=RangePoseRule(200, 30, 30),
    right_knee_angle_rule=RangePoseRule(160, 30, 30),
    hips_below_shoulders_rule=hips_below_shoulders_rule,
    palms_below_hips_rule=palms_below_hips_rule
)

# =========================================================================================== |
# ====================================== Cat ================================================ |
# =========================================================================================== |

head_below_shoulders_rule = GenericPoseRule(lambda b: b.face_center().y > b.shoulders_center().y)

cat_pose_left = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(270, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(90, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(260, 50, 50),
    right_hip_angle_rule=RangePoseRule(100, 50, 50),
    left_knee_angle_rule=RangePoseRule(260, 30, 30),
    right_knee_angle_rule=RangePoseRule(90, 30, 30),
    head_below_shoulders_rule=head_below_shoulders_rule
)

cat_pose_right = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(90, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(270, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(100, 50, 50),
    right_hip_angle_rule=RangePoseRule(260, 50, 50),
    left_knee_angle_rule=RangePoseRule(90, 30, 30),
    right_knee_angle_rule=RangePoseRule(260, 30, 30),
    head_below_shoulders_rule=head_below_shoulders_rule
)

# TODO: tune these relaxed versions of Cat


cat_pose_left_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(270, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(90, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(260, 50, 50),
    right_hip_angle_rule=RangePoseRule(100, 50, 50),
    left_knee_angle_rule=RangePoseRule(260, 30, 30),
    right_knee_angle_rule=RangePoseRule(90, 30, 30),
    head_below_shoulders_rule=head_below_shoulders_rule
)

cat_pose_right_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(90, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(270, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(100, 50, 50),
    right_hip_angle_rule=RangePoseRule(260, 50, 50),
    left_knee_angle_rule=RangePoseRule(90, 30, 30),
    right_knee_angle_rule=RangePoseRule(260, 30, 30),
    head_below_shoulders_rule=head_below_shoulders_rule
)

# =========================================================================================== |
# ====================================== Frog =============================================== |
# =========================================================================================== |

hips_below_shoulders_rule = GenericPoseRule(lambda b: b.hips_center().y > b.shoulders_center().y)
palms_below_hips_rule = GenericPoseRule(lambda b: b.left_palm().y > b.hips_center().y and b.right_palm().y > b.hips_center().y)

frog_pose = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(160, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(160, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(70, 30, 30),
    right_hip_angle_rule=RangePoseRule(70, 30, 30),
    left_knee_angle_rule=RangePoseRule(70, 30, 30),
    right_knee_angle_rule=RangePoseRule(70, 30, 30),
    hips_below_shoulders_rule=hips_below_shoulders_rule,
    palms_below_hips_rule=palms_below_hips_rule
)

# TODO: tune these relaxed versions of Frog

frog_pose_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(160, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(160, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(70, 30, 30),
    right_hip_angle_rule=RangePoseRule(70, 30, 30),
    left_knee_angle_rule=RangePoseRule(70, 30, 30),
    right_knee_angle_rule=RangePoseRule(70, 30, 30),
    hips_below_shoulders_rule=hips_below_shoulders_rule,
    palms_below_hips_rule=palms_below_hips_rule
)

# =========================================================================================== |
# ====================================== Shark ============================================== |
# =========================================================================================== |

shoulders_height_close_to_knees_rule = GenericPoseRule(lambda b: relatively_close(b.knees_center().y, b.shoulders_center().y, 1.2))

shark_pose_left = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(200, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(160, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(200, 50, 50),
    right_hip_angle_rule=RangePoseRule(140, 50, 50),
    left_knee_angle_rule=RangePoseRule(160, 30, 30),
    right_knee_angle_rule=RangePoseRule(200, 30, 30),
    shoulders_height_close_to_knees_rule=shoulders_height_close_to_knees_rule
)

shark_pose_right = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(160, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(200, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(140, 50, 50),
    right_hip_angle_rule=RangePoseRule(200, 50, 50),
    left_knee_angle_rule=RangePoseRule(200, 30, 30),
    right_knee_angle_rule=RangePoseRule(160, 30, 30),
    shoulders_height_close_to_knees_rule=shoulders_height_close_to_knees_rule
)

# TODO: tune these relaxed versions of Shark

shark_pose_left_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(200, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(160, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(200, 50, 50),
    right_hip_angle_rule=RangePoseRule(140, 50, 50),
    left_knee_angle_rule=RangePoseRule(160, 30, 30),
    right_knee_angle_rule=RangePoseRule(200, 30, 30),
    shoulders_height_close_to_knees_rule=shoulders_height_close_to_knees_rule
)

shark_pose_right_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(160, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(200, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(140, 50, 50),
    right_hip_angle_rule=RangePoseRule(200, 50, 50),
    left_knee_angle_rule=RangePoseRule(200, 30, 30),
    right_knee_angle_rule=RangePoseRule(160, 30, 30),
    shoulders_height_close_to_knees_rule=shoulders_height_close_to_knees_rule
)

# =========================================================================================== |
# ======================================= Monkey ============================================ |
# =========================================================================================== |

left_palm_below_head_rule = GenericPoseRule(lambda b: b.left_palm().y > b.face_center().y)

monkey_pose_left = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(250, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(0, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(90, 100, 100),
    right_hip_angle_rule=RangePoseRule(90, 100, 100),
    left_knee_angle_rule=AcceptAllPoseRule(),
    right_knee_angle_rule=AcceptAllPoseRule(),
    right_palm_above_head_rule=right_palm_above_head_rule,
    left_palm_below_head_rule=left_palm_below_head_rule
)

monkey_pose_right = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(0, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(250, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(90, 100, 100),
    right_hip_angle_rule=RangePoseRule(90, 100, 100),
    left_knee_angle_rule=AcceptAllPoseRule(),
    right_knee_angle_rule=AcceptAllPoseRule(),
    right_palm_above_head_rule=right_palm_above_head_rule,
    left_palm_below_head_rule=left_palm_below_head_rule
)

monkey_pose_left_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(250, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(0, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(90, 100, 100),
    right_hip_angle_rule=RangePoseRule(90, 100, 100),
    left_knee_angle_rule=AcceptAllPoseRule(),
    right_knee_angle_rule=AcceptAllPoseRule(),
    right_palm_above_head_rule=right_palm_above_head_rule,
    left_palm_below_head_rule=left_palm_below_head_rule
)

monkey_pose_right_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(0, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(250, 30, 30),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(90, 100, 100),
    right_hip_angle_rule=RangePoseRule(90, 100, 100),
    left_knee_angle_rule=AcceptAllPoseRule(),
    right_knee_angle_rule=AcceptAllPoseRule(),
    right_palm_above_head_rule=right_palm_above_head_rule,
    left_palm_below_head_rule=left_palm_below_head_rule
)

# =========================================================================================== |
# ==================================== Eagle ================================================ |
# =========================================================================================== |

left_leg_crossed_rule = GenericPoseRule(lambda b: b.right_ankle().x > b.left_ankle().x)
right_leg_crossed_rule = GenericPoseRule(lambda b: b.left_ankle().x < b.right_ankle().x)

eagle_pose_left_leg_crossed_right_arm_under = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(230, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(180, 30, 30),
    left_elbow_angle_rule=RangePoseRule(280, 40, 40),
    right_elbow_angle_rule=RangePoseRule(315, 40, 40),
    left_hip_angle_rule=RangePoseRule(200, 20, 20),
    right_hip_angle_rule=RangePoseRule(180, 20, 20),
    left_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_knee_angle_rule=RangePoseRule(180, 30, 30),
    left_leg_crossed_rule=left_leg_crossed_rule
)

eagle_pose_left_leg_crossed_left_arm_under = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(180, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(230, 30, 30),
    left_elbow_angle_rule=RangePoseRule(315, 40, 40),
    right_elbow_angle_rule=RangePoseRule(280, 40, 40),
    left_hip_angle_rule=RangePoseRule(180, 20, 20),
    right_hip_angle_rule=RangePoseRule(200, 20, 20),
    left_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_knee_angle_rule=RangePoseRule(180, 30, 30),
    left_leg_crossed_rule=left_leg_crossed_rule
)

eagle_pose_right_leg_crossed_left_arm_under = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(180, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(230, 30, 30),
    left_elbow_angle_rule=RangePoseRule(315, 40, 40),
    right_elbow_angle_rule=RangePoseRule(280, 40, 40),
    left_hip_angle_rule=RangePoseRule(180, 20, 20),
    right_hip_angle_rule=RangePoseRule(200, 20, 20),
    left_knee_angle_rule=RangePoseRule(180, 30, 30),
    right_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_leg_crossed_rule=right_leg_crossed_rule
)

eagle_pose_right_leg_crossed_right_arm_under = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(230, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(180, 30, 30),
    left_elbow_angle_rule=RangePoseRule(280, 40, 40),
    right_elbow_angle_rule=RangePoseRule(315, 40, 40),
    left_hip_angle_rule=RangePoseRule(180, 20, 20),
    right_hip_angle_rule=RangePoseRule(200, 20, 20),
    left_knee_angle_rule=RangePoseRule(180, 30, 30),
    right_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_leg_crossed_rule=right_leg_crossed_rule
)

# TODO: tune these relaxed versions of Eagle

eagle_pose_left_leg_crossed_right_arm_under_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(230, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(180, 30, 30),
    left_elbow_angle_rule=RangePoseRule(280, 40, 40),
    right_elbow_angle_rule=RangePoseRule(315, 40, 40),
    left_hip_angle_rule=RangePoseRule(200, 20, 20),
    right_hip_angle_rule=RangePoseRule(180, 20, 20),
    left_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_knee_angle_rule=RangePoseRule(180, 30, 30),
    left_leg_crossed_rule=left_leg_crossed_rule
)

eagle_pose_left_leg_crossed_left_arm_under_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(180, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(230, 30, 30),
    left_elbow_angle_rule=RangePoseRule(315, 40, 40),
    right_elbow_angle_rule=RangePoseRule(280, 40, 40),
    left_hip_angle_rule=RangePoseRule(180, 20, 20),
    right_hip_angle_rule=RangePoseRule(200, 20, 20),
    left_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_knee_angle_rule=RangePoseRule(180, 30, 30),
    left_leg_crossed_rule=left_leg_crossed_rule
)

eagle_pose_right_leg_crossed_left_arm_under_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(180, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(230, 30, 30),
    left_elbow_angle_rule=RangePoseRule(315, 40, 40),
    right_elbow_angle_rule=RangePoseRule(280, 40, 40),
    left_hip_angle_rule=RangePoseRule(180, 20, 20),
    right_hip_angle_rule=RangePoseRule(200, 20, 20),
    left_knee_angle_rule=RangePoseRule(180, 30, 30),
    right_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_leg_crossed_rule=right_leg_crossed_rule
)

eagle_pose_right_leg_crossed_right_arm_under_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(230, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(180, 30, 30),
    left_elbow_angle_rule=RangePoseRule(280, 40, 40),
    right_elbow_angle_rule=RangePoseRule(315, 40, 40),
    left_hip_angle_rule=RangePoseRule(180, 20, 20),
    right_hip_angle_rule=RangePoseRule(200, 20, 20),
    left_knee_angle_rule=RangePoseRule(180, 30, 30),
    right_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_leg_crossed_rule=right_leg_crossed_rule
)

# =========================================================================================== |
# ==================================== Crow ================================================= |
# =========================================================================================== |

palms_below_knees_rule = GenericPoseRule(lambda b: b.left_palm().y > b.knees_center().y and b.right_palm().y > b.knees_center().y)

crow_pose_right = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(140, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(225, 30, 30),
    left_elbow_angle_rule=RangePoseRule(120, 40, 40),
    right_elbow_angle_rule=RangePoseRule(235, 40, 40),
    left_hip_angle_rule=RangePoseRule(35, 30, 60),
    right_hip_angle_rule=RangePoseRule(330, 30, 60),
    left_knee_angle_rule=RangePoseRule( 70, 50, 50),
    right_knee_angle_rule=RangePoseRule(300, 50, 50),
    palms_below_knees_rule=palms_below_knees_rule
)

crow_pose_left = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(225, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(140, 30, 30),
    left_elbow_angle_rule=RangePoseRule(235, 40, 40),
    right_elbow_angle_rule=RangePoseRule(120, 40, 40),
    left_hip_angle_rule=RangePoseRule(330, 30, 60),
    right_hip_angle_rule=RangePoseRule(35, 30, 60),
    left_knee_angle_rule=RangePoseRule(300, 50, 50),
    right_knee_angle_rule=RangePoseRule(70, 50, 50),
    palms_below_knees_rule=palms_below_knees_rule
)

crow_pose_right_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(140, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(225, 30, 30),
    left_elbow_angle_rule=RangePoseRule(120, 40, 40),
    right_elbow_angle_rule=RangePoseRule(235, 40, 40),
    left_hip_angle_rule=RangePoseRule(35, 30, 60),
    right_hip_angle_rule=RangePoseRule(330, 30, 60),
    left_knee_angle_rule=RangePoseRule( 70, 50, 50),
    right_knee_angle_rule=RangePoseRule(300, 50, 50),
    palms_below_knees_rule=palms_below_knees_rule
)

crow_pose_left_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(225, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(140, 30, 30),
    left_elbow_angle_rule=RangePoseRule(235, 40, 40),
    right_elbow_angle_rule=RangePoseRule(120, 40, 40),
    left_hip_angle_rule=RangePoseRule(330, 30, 60),
    right_hip_angle_rule=RangePoseRule(35, 30, 60),
    left_knee_angle_rule=RangePoseRule(300, 50, 50),
    right_knee_angle_rule=RangePoseRule(70, 50, 50),
    palms_below_knees_rule=palms_below_knees_rule
)

# =========================================================================================== |
# ==================================== Crocodile ============================================ |
# =========================================================================================== |

palms_height_close_shoulders_rule = GenericPoseRule(lambda b: relatively_close(b.shoulders_center().y, b.palms_center().y, 1.2))

crocodile_pose_right = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(125, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(260, 30, 30),
    left_elbow_angle_rule=RangePoseRule(45, 40, 40),
    right_elbow_angle_rule=RangePoseRule(335, 40, 40),
    left_hip_angle_rule=RangePoseRule(200, 50, 50),
    right_hip_angle_rule=RangePoseRule(170, 50, 50),
    left_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_knee_angle_rule=RangePoseRule(200, 30, 30),
    shoulders_height_close_to_knees_rule = shoulders_height_close_to_knees_rule,
    palms_height_close_shoulders = palms_height_close_shoulders_rule
)

crocodile_pose_left = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(260, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(125, 30, 30),
    left_elbow_angle_rule=RangePoseRule(335, 40, 40),
    right_elbow_angle_rule=RangePoseRule(45, 40, 40),
    left_hip_angle_rule=RangePoseRule(170, 50, 50),
    right_hip_angle_rule=RangePoseRule(200, 50, 50),
    left_knee_angle_rule=RangePoseRule(200, 30, 30),
    right_knee_angle_rule=RangePoseRule(170, 30, 30),
    shoulders_height_close_to_knees_rule = shoulders_height_close_to_knees_rule,
    palms_height_close_shoulders = palms_height_close_shoulders_rule
)

# TODO: tune these relaxed versions of Crocodile

crocodile_pose_right_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(125, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(260, 30, 30),
    left_elbow_angle_rule=RangePoseRule(45, 40, 40),
    right_elbow_angle_rule=RangePoseRule(335, 40, 40),
    left_hip_angle_rule=RangePoseRule(200, 50, 50),
    right_hip_angle_rule=RangePoseRule(170, 50, 50),
    left_knee_angle_rule=RangePoseRule(170, 30, 30),
    right_knee_angle_rule=RangePoseRule(200, 30, 30),
    shoulders_height_close_to_knees_rule = shoulders_height_close_to_knees_rule,
    palms_height_close_shoulders = palms_height_close_shoulders_rule
)

crocodile_pose_left_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(260, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(125, 30, 30),
    left_elbow_angle_rule=RangePoseRule(335, 40, 40),
    right_elbow_angle_rule=RangePoseRule(45, 40, 40),
    left_hip_angle_rule=RangePoseRule(170, 50, 50),
    right_hip_angle_rule=RangePoseRule(200, 50, 50),
    left_knee_angle_rule=RangePoseRule(200, 30, 30),
    right_knee_angle_rule=RangePoseRule(170, 30, 30),
    shoulders_height_close_to_knees_rule = shoulders_height_close_to_knees_rule,
    palms_height_close_shoulders = palms_height_close_shoulders_rule
)

# =========================================================================================== |
# ========================================= Lotus =========================================== |
# =========================================================================================== |

lotus_pose = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(150, 50, 50),
    right_shoulder_angle_rule=RangePoseRule(150, 50, 50),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(100, 30, 30),
    right_hip_angle_rule=RangePoseRule(100, 30, 30),
    left_knee_angle_rule=RangePoseRule(15, 20, 20),
    right_knee_angle_rule=RangePoseRule(15, 20, 20),
)

# TODO: tune these relaxed versions of Lotus

lotus_pose_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(150, 50, 50),
    right_shoulder_angle_rule=RangePoseRule(150, 50, 50),
    left_elbow_angle_rule=RangePoseRule(180, 40, 40),
    right_elbow_angle_rule=RangePoseRule(180, 40, 40),
    left_hip_angle_rule=RangePoseRule(100, 30, 30),
    right_hip_angle_rule=RangePoseRule(100, 30, 30),
    left_knee_angle_rule=RangePoseRule(15, 20, 20),
    right_knee_angle_rule=RangePoseRule(15, 20, 20),
)

# =========================================================================================== |
# =================================== Butterfly ============================================= |
# =========================================================================================== |

def palms_close_to_ankles_func(b):
    palms_center = b.palms_center()
    ankles_center = b.ankles_center()
    return relatively_close(palms_center.x, ankles_center.x,1.2) and relatively_close(palms_center.y, ankles_center.y,1.2)
palms_close_to_ankles_rule = GenericPoseRule(palms_close_to_ankles_func)

butterfly_pose = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(170, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(170, 30, 30),
    left_elbow_angle_rule=RangePoseRule(200, 30, 30),
    right_elbow_angle_rule=RangePoseRule(200, 30, 30),
    left_hip_angle_rule=RangePoseRule(60, 30, 30),
    right_hip_angle_rule=RangePoseRule(60, 30, 30),
    left_knee_angle_rule=RangePoseRule(15, 20, 20),
    right_knee_angle_rule=RangePoseRule(15, 20, 20),
    palms_close_to_ankles_rule=palms_close_to_ankles_rule
)

butterfly_pose_relaxed = PoseTest(
    left_shoulder_angle_rule=RangePoseRule(170, 30, 30),
    right_shoulder_angle_rule=RangePoseRule(170, 30, 30),
    left_elbow_angle_rule=RangePoseRule(200, 30, 30),
    right_elbow_angle_rule=RangePoseRule(200, 30, 30),
    left_hip_angle_rule=RangePoseRule(60, 30, 30),
    right_hip_angle_rule=RangePoseRule(60, 30, 30),
    left_knee_angle_rule=RangePoseRule(15, 20, 20),
    right_knee_angle_rule=RangePoseRule(15, 20, 20),
    palms_close_to_ankles_rule=palms_close_to_ankles_rule
)



