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

FPS = 30
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
                f"({body_parts[BodyParts.RIGHT_ARM].first.vector})",
                (body_parts[BodyParts.RIGHT_ARM].first.center.x, body_parts[BodyParts.RIGHT_ARM].first.center.y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(annotated_image,
                f"({body_parts[BodyParts.RIGHT_ARM].second.vector})",
                (body_parts[BodyParts.RIGHT_ARM].second.center.x, body_parts[BodyParts.RIGHT_ARM].second.center.y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(annotated_image,
                f"({body_parts[BodyParts.LEFT_ARM].first.vector})",
                (body_parts[BodyParts.LEFT_ARM].first.center.x, body_parts[BodyParts.LEFT_ARM].first.center.y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(annotated_image,
                f"({body_parts[BodyParts.LEFT_ARM].second.vector})",
                (body_parts[BodyParts.LEFT_ARM].second.center.x, body_parts[BodyParts.LEFT_ARM].second.center.y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # put text at the top right corner
        wrists_angle = Vec3.angle(body_parts[BodyParts.RIGHT_ARM].second.vector, body_parts[BodyParts.LEFT_ARM].second.vector)
        wrists_parallel = wrists_angle < 15
        cv2.putText(annotated_image,
                    f"{"WRISTS PARALLEL" if wrists_parallel else ""}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2
        )


        # # Extract arm landmarks
        # if len(pose_landmarks) > 16:
        #     # Right arm landmarks
        #     right_shoulder = pose_landmarks[12]
        #     right_elbow = pose_landmarks[14]
        #     right_wrist = pose_landmarks[16]
        #     # Left arm landmarks
        #     left_shoulder = pose_landmarks[11]
        #     left_elbow = pose_landmarks[13]
        #     left_wrist = pose_landmarks[15]
        #
        #     # Convert normalized coordinates to pixel coordinates
        #     h, w, _ = annotated_image.shape
        #     right_shoulder_coord = (int(right_shoulder.x * w), int(right_shoulder.y * h), right_shoulder.z)
        #     right_elbow_coord = (int(right_elbow.x * w), int(right_elbow.y * h), right_elbow.z)
        #     right_wrist_coord = (int(right_wrist.x * w), int(right_wrist.y * h), right_wrist.z)
        #     left_shoulder_coord = (int(left_shoulder.x * w), int(left_shoulder.y * h), left_shoulder.z)
        #     left_elbow_coord = (int(left_elbow.x * w), int(left_elbow.y * h), left_elbow.z)
        #     left_wrist_coord = (int(left_wrist.x * w), int(left_wrist.y * h), left_wrist.z)
        #
        #     right_shoulder_cartesian_coord = pixel_to_cartesian(int(right_shoulder.x * w), int(right_shoulder.y * h), w, h)
        #     right_elbow_cartesian_coord = pixel_to_cartesian(int(right_elbow.x * w), int(right_elbow.y * h), w, h)
        #     right_wrist_cartesian_coord = pixel_to_cartesian(int(right_wrist.x * w), int(right_wrist.y * h), w, h)
        #     left_shoulder_cartesian_coord = pixel_to_cartesian(int(left_shoulder.x * w), int(left_shoulder.y * h), w, h)
        #     left_elbow_cartesian_coord = pixel_to_cartesian(int(left_elbow.x * w), int(left_elbow.y * h), w, h)
        #     left_wrist_cartesian_coord = pixel_to_cartesian(int(left_wrist.x * w), int(left_wrist.y * h), w, h)
        #
        #     # Draw text (coordinates) on the image
        #     cv2.putText(annotated_image, f"({right_shoulder_cartesian_coord[0]}, {right_shoulder_cartesian_coord[1]}, {right_shoulder_coord[2]})",
        #                 (right_shoulder_coord[0], right_shoulder_coord[1] - 10),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        #     cv2.putText(annotated_image, f"({right_elbow_cartesian_coord[0]}, {right_elbow_cartesian_coord[1]}, {right_elbow_coord[2]})",
        #                 (right_elbow_coord[0], right_elbow_coord[1] - 10),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        #     cv2.putText(annotated_image, f"({right_wrist_cartesian_coord[0]}, {right_wrist_cartesian_coord[1]}, {right_wrist_coord[2]})",
        #                 (right_wrist_coord[0], right_wrist_coord[1] - 10),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        #
        #     cv2.putText(annotated_image, f"({left_shoulder_cartesian_coord[0]}, {left_shoulder_cartesian_coord[1]}, {left_shoulder_coord[2]})",
        #                 (left_shoulder_coord[0], left_shoulder_coord[1] - 10),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        #     cv2.putText(annotated_image, f"({left_elbow_cartesian_coord[0]}, {left_elbow_cartesian_coord[1]}, {left_elbow_coord[2]})",
        #                 (left_elbow_coord[0], left_elbow_coord[1] - 10),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        #     cv2.putText(annotated_image, f"({left_wrist_cartesian_coord[0]}, {left_wrist_cartesian_coord[1]}, {left_wrist_coord[2]})",
        #                 (left_wrist_coord[0], left_wrist_coord[1] - 10),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    return annotated_image

# Callback for live stream results
def result_callback(result: vision.PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global annotated_frame
    rgb_view = output_image.numpy_view()
    annotated_frame = draw_landmarks_on_image(rgb_view, result)


def main():
    global annotated_frame

    # Open webcam
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, FPS)

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
            cv2.imshow("Mediapipe Pose Live", cv2.cvtColor(frame_to_draw, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
