from typing import Any, Optional
import cv2
import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np

from body_parts.body_parts import build_body_parts, BodyParts
from body_parts.math_utils import Vec3

def exactly_one(*args) -> bool:
    """
    Check if exactly one of the arguments is True.
    """
    return sum(args) == 1

def is_warrior2(body_parts) -> bool:
    """
    Check if the body parts correspond to Warrior II pose.
    """
    right_arm = body_parts[BodyParts.RIGHT_ARM]
    left_arm = body_parts[BodyParts.LEFT_ARM]
    right_leg = body_parts[BodyParts.RIGHT_LEG]
    left_leg = body_parts[BodyParts.LEFT_LEG]
    torso = body_parts[BodyParts.TORSO]

    # Check if arms are straight
    right_straight = Vec3.angle2(right_arm.first.vector, right_arm.second.vector) < 40
    left_straight = Vec3.angle2(left_arm.first.vector, left_arm.second.vector) < 40

    # Check that the arms are 90 degrees from the torso
    right_arm_angle = Vec3.angle2(torso.right.vector, right_arm.first.vector)
    left_arm_angle = Vec3.angle2(torso.left.vector, left_arm.first.vector)
    left_arm_perpendicular = abs(left_arm_angle - 90) < 15
    right_arm_perpendicular = abs(right_arm_angle - 90) < 15

    # Check that one leg is bent and the other is straight
    right_leg_angle = Vec3.angle2(right_leg.first.vector, right_leg.second.vector)
    left_leg_angle = Vec3.angle2(left_leg.first.vector, left_leg.second.vector)
    one_bent = exactly_one(abs(right_leg_angle - 90) < 10, abs(left_leg_angle - 90) < 10)
    one_straight = exactly_one(right_leg_angle < 10, left_leg_angle < 10)

    return right_straight and left_straight and left_arm_perpendicular and right_arm_perpendicular and one_bent and one_straight



FPS = 60
TIMESTAMP_STEP = int(1000 / FPS)
timestamp = 0

# Global variable to hold last annotated frame
annotated_frame: Optional[np.ndarray[Any, np.dtype[Any]]] = None

def draw_landmarks_on_image(rgb_image, detection_result):
    pose_landmarks_list = detection_result.pose_landmarks
    annotated_image = np.copy(rgb_image)

    for idx in range(len(pose_landmarks_list)):
        pose_landmarks = pose_landmarks_list[idx]

        # Convert to protobuf
        pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        pose_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z)
            for landmark in pose_landmarks
        ])

        # Draw
        solutions.drawing_utils.draw_landmarks(
            annotated_image,
            pose_landmarks_proto,
            solutions.pose.POSE_CONNECTIONS,
            solutions.drawing_styles.get_default_pose_landmarks_style()
        )

        h,w, _ = annotated_image.shape
        body_parts = build_body_parts(pose_landmarks, w, h)

        # Draw body parts vectors in the center of the body part
        cv2.putText(annotated_image,
                f"{body_parts[BodyParts.RIGHT_ARM].first.vector}",
                (body_parts[BodyParts.RIGHT_ARM].first.center.x, body_parts[BodyParts.RIGHT_ARM].first.center.y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(annotated_image,
                f"{body_parts[BodyParts.RIGHT_ARM].second.vector}",
                (body_parts[BodyParts.RIGHT_ARM].second.center.x, body_parts[BodyParts.RIGHT_ARM].second.center.y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(annotated_image,
                f"{body_parts[BodyParts.LEFT_ARM].first.vector}",
                (body_parts[BodyParts.LEFT_ARM].first.center.x, body_parts[BodyParts.LEFT_ARM].first.center.y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(annotated_image,
                f"{body_parts[BodyParts.LEFT_ARM].second.vector}",
                (body_parts[BodyParts.LEFT_ARM].second.center.x, body_parts[BodyParts.LEFT_ARM].second.center.y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # check warrior2 pose
        if is_warrior2(body_parts):
            cv2.putText(annotated_image, "Warrior II Pose Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(annotated_image, "Not Warrior II Pose", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return annotated_image

# Callback for live stream results
def result_callback(result: vision.PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global annotated_frame
    rgb_view = output_image.numpy_view()
    annotated_frame = draw_landmarks_on_image(rgb_view, result)


def main():
    global annotated_frame

    # Open webcam
    cap = cv2.VideoCapture(3)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap.set(cv2.CAP_PROP_FPS, FPS)
    cv2.namedWindow("Mediapipe Pose Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Mediapipe Pose Live", 1920, 1080)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return


    base_options = python.BaseOptions(
        model_asset_path="model/pose_landmarker_heavy.task",
        delegate=python.BaseOptions.Delegate.GPU
    )

    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.LIVE_STREAM,
        result_callback=result_callback,
        output_segmentation_masks=False,
        num_poses=5
    )
    detector = vision.PoseLandmarker.create_from_options(options)

    global timestamp
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame = cv2.flip(frame,1)

        # BGR → RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Wrap frame in MediaPipe Image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # Send async frame to detector
        detector.detect_async(mp_image, timestamp)
        timestamp += TIMESTAMP_STEP

        # Show annotated frame if available
        frame_to_draw = annotated_frame
        if frame_to_draw is not None:
            frame_to_draw = cv2.resize(frame_to_draw, (2560, 1440))
            cv2.imshow("Mediapipe Pose Live", cv2.cvtColor(frame_to_draw, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()




