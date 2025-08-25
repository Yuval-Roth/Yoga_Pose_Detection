from typing import Any, Optional
import cv2
import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
from mediapipe.python.solutions.pose import PoseLandmark
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np

from body.body import Body
from body.body_parts import *
from pose_detection import detect_pose

FPS = 60
TIMESTAMP_STEP = int(1000 / FPS)
timestamp = 0
frame_width, frame_height = 1280, 720
# frame_width, frame_height = 1920, 1080
body = Body(frame_width, frame_height, avg_count=15)

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
        # solutions.drawing_utils.draw_landmarks(
        #     annotated_image,
        #     pose_landmarks_proto,
        #     solutions.pose.POSE_CONNECTIONS,
        #     # landmark_drawing_spec=None,
        #     solutions.drawing_styles.get_default_pose_landmarks_style()
        # )

        body.update(pose_landmarks)

        # Draw the smoothed landmarks
        # left arm
        # cv2.line(annotated_image, (body.parts[BodyParts.LEFT_ARM].shoulder.x, body.parts[BodyParts.LEFT_ARM].shoulder.y),
        #          (body.parts[BodyParts.LEFT_ARM].elbow.x, body.parts[BodyParts.LEFT_ARM].elbow.y), (255, 0, 0), 6)
        # cv2.line(annotated_image, (body.parts[BodyParts.LEFT_ARM].elbow.x, body.parts[BodyParts.LEFT_ARM].elbow.y),
        #          (body.parts[BodyParts.LEFT_ARM].wrist.x, body.parts[BodyParts.LEFT_ARM].wrist.y), (255, 0, 0), 6)
        # cv2.circle(annotated_image, (body.parts[BodyParts.LEFT_ARM].shoulder.x, body.parts[BodyParts.LEFT_ARM].shoulder.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.LEFT_ARM].elbow.x, body.parts[BodyParts.LEFT_ARM].elbow.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.LEFT_ARM].wrist.x, body.parts[BodyParts.LEFT_ARM].wrist.y), 8, (0, 0, 255), -1)
        # # right arm
        # cv2.line(annotated_image, (body.parts[BodyParts.RIGHT_ARM].shoulder.x, body.parts[BodyParts.RIGHT_ARM].shoulder.y),
        #          (body.parts[BodyParts.RIGHT_ARM].elbow.x, body.parts[BodyParts.RIGHT_ARM].elbow.y), (255, 0, 0), 6)
        # cv2.line(annotated_image, (body.parts[BodyParts.RIGHT_ARM].elbow.x, body.parts[BodyParts.RIGHT_ARM].elbow.y),
        #          (body.parts[BodyParts.RIGHT_ARM].wrist.x, body.parts[BodyParts.RIGHT_ARM].wrist.y), (255, 0, 0), 6)
        # cv2.circle(annotated_image, (body.parts[BodyParts.RIGHT_ARM].shoulder.x, body.parts[BodyParts.RIGHT_ARM].shoulder.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.RIGHT_ARM].elbow.x, body.parts[BodyParts.RIGHT_ARM].elbow.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.RIGHT_ARM].wrist.x, body.parts[BodyParts.RIGHT_ARM].wrist.y), 8, (0, 0, 255), -1)
        # # left leg
        # cv2.line(annotated_image, (body.parts[BodyParts.LEFT_LEG].hip.x, body.parts[BodyParts.LEFT_LEG].hip.y),
        #          (body.parts[BodyParts.LEFT_LEG].knee.x, body.parts[BodyParts.LEFT_LEG].knee.y), (255, 0, 0), 6)
        # cv2.line(annotated_image, (body.parts[BodyParts.LEFT_LEG].knee.x, body.parts[BodyParts.LEFT_LEG].knee.y),
        #          (body.parts[BodyParts.LEFT_LEG].ankle.x, body.parts[BodyParts.LEFT_LEG].ankle.y), (255, 0, 0), 6)
        # cv2.circle(annotated_image, (body.parts[BodyParts.LEFT_LEG].hip.x, body.parts[BodyParts.LEFT_LEG].hip.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.LEFT_LEG].knee.x, body.parts[BodyParts.LEFT_LEG].knee.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.LEFT_LEG].ankle.x, body.parts[BodyParts.LEFT_LEG].ankle.y), 8, (0, 0, 255), -1)
        # # right leg
        # cv2.line(annotated_image, (body.parts[BodyParts.RIGHT_LEG].hip.x, body.parts[BodyParts.RIGHT_LEG].hip.y),
        #          (body.parts[BodyParts.RIGHT_LEG].knee.x, body.parts[BodyParts.RIGHT_LEG].knee.y), (255, 0, 0), 6)
        # cv2.line(annotated_image, (body.parts[BodyParts.RIGHT_LEG].knee.x, body.parts[BodyParts.RIGHT_LEG].knee.y),
        #          (body.parts[BodyParts.RIGHT_LEG].ankle.x, body.parts[BodyParts.RIGHT_LEG].ankle.y), (255, 0, 0), 6)
        # cv2.circle(annotated_image, (body.parts[BodyParts.RIGHT_LEG].hip.x, body.parts[BodyParts.RIGHT_LEG].hip.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.RIGHT_LEG].knee.x, body.parts[BodyParts.RIGHT_LEG].knee.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.RIGHT_LEG].ankle.x, body.parts[BodyParts.RIGHT_LEG].ankle.y), 8, (0, 0, 255), -1)
        # # torso
        # cv2.line(annotated_image, (body.parts[BodyParts.TORSO].left_shoulder.x, body.parts[BodyParts.TORSO].left_shoulder.y),
        #          (body.parts[BodyParts.TORSO].right_shoulder.x, body.parts[BodyParts.TORSO].right_shoulder.y), (255, 0, 0), 6)
        # cv2.line(annotated_image, (body.parts[BodyParts.TORSO].left_hip.x, body.parts[BodyParts.TORSO].left_hip.y),
        #          (body.parts[BodyParts.TORSO].right_hip.x, body.parts[BodyParts.TORSO].right_hip.y), (255, 0, 0), 6)
        # cv2.line(annotated_image, (body.parts[BodyParts.TORSO].left_shoulder.x, body.parts[BodyParts.TORSO].left_shoulder.y),
        #          (body.parts[BodyParts.TORSO].left_hip.x, body.parts[BodyParts.TORSO].left_hip.y), (255, 0, 0), 6)
        # cv2.line(annotated_image, (body.parts[BodyParts.TORSO].right_shoulder.x, body.parts[BodyParts.TORSO].right_shoulder.y),
        #          (body.parts[BodyParts.TORSO].right_hip.x, body.parts[BodyParts.TORSO].right_hip.y), (255, 0, 0), 6)
        # cv2.circle(annotated_image, (body.parts[BodyParts.TORSO].left_shoulder.x, body.parts[BodyParts.TORSO].left_shoulder.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.TORSO].right_shoulder.x, body.parts[BodyParts.TORSO].right_shoulder.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.TORSO].left_hip.x, body.parts[BodyParts.TORSO].left_hip.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.TORSO].right_hip.x, body.parts[BodyParts.TORSO].right_hip.y), 8, (0, 0, 255), -1)
        # # head
        # cv2.line(annotated_image, (body.parts[BodyParts.HEAD].nose.x, body.parts[BodyParts.HEAD].nose.y),
        #          (body.parts[BodyParts.HEAD].left_eye.x, body.parts[BodyParts.HEAD].left_eye.y), (255, 0, 0), 6)
        # cv2.line(annotated_image, (body.parts[BodyParts.HEAD].nose.x, body.parts[BodyParts.HEAD].nose.y),
        #          (body.parts[BodyParts.HEAD].right_eye.x, body.parts[BodyParts.HEAD].right_eye.y), (255, 0, 0), 6)
        # cv2.circle(annotated_image, (body.parts[BodyParts.HEAD].nose.x, body.parts[BodyParts.HEAD].nose.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.HEAD].left_eye.x, body.parts[BodyParts.HEAD].left_eye.y), 8, (0, 0, 255), -1)
        # cv2.circle(annotated_image, (body.parts[BodyParts.HEAD].right_eye.x, body.parts[BodyParts.HEAD].right_eye.y), 8, (0, 0, 255), -1)
        # # Draw centers
        # cv2.circle(annotated_image, (body.hips_center().x, body.hips_center().y), 10, (255, 255, 0), -1)
        # cv2.circle(annotated_image, (body.shoulders_center().x, body.shoulders_center().y), 10, (255, 255, 0), -1)
        # cv2.circle(annotated_image, (body.knees_center().x, body.knees_center().y), 10, (255, 255, 0), -1)
        # cv2.circle(annotated_image, (body.face_center().x, body.face_center().y), 10, (255, 255, 0), -1)


        # Draw angles on the image
        cv2.putText(annotated_image, f"{int(body.left_elbow_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_ELBOW].x * frame_width), int(pose_landmarks[PoseLandmark.LEFT_ELBOW].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.right_elbow_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_ELBOW].x * frame_width), int(pose_landmarks[PoseLandmark.RIGHT_ELBOW].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.left_knee_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_KNEE].x * frame_width), int(pose_landmarks[PoseLandmark.LEFT_KNEE].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.right_knee_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_KNEE].x * frame_width), int(pose_landmarks[PoseLandmark.RIGHT_KNEE].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.left_shoulder_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_SHOULDER].x * frame_width), int(pose_landmarks[PoseLandmark.LEFT_SHOULDER].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.right_shoulder_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_SHOULDER].x * frame_width), int(pose_landmarks[PoseLandmark.RIGHT_SHOULDER].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.left_hip_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_HIP].x * frame_width), int(pose_landmarks[PoseLandmark.LEFT_HIP].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.right_hip_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_HIP].x * frame_width), int(pose_landmarks[PoseLandmark.RIGHT_HIP].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        detected_poses = detect_pose(body)
        for i, pose in enumerate(detected_poses):
            cv2.putText(annotated_image, f"{pose}", (50, 50 + 30 * i), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    return annotated_image

# Callback for live stream results
def result_callback(result: vision.PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global annotated_frame
    rgb_view = output_image.numpy_view()
    annotated_frame = draw_landmarks_on_image(rgb_view, result)


def run_live_stream():
    global annotated_frame

    # Open webcam
    camera_index = 1
    cap = cv2.VideoCapture(camera_index)
    while not cap.isOpened() and camera_index < 10:
        camera_index += 1
        cap = cv2.VideoCapture(camera_index)
        print(f"Camera not found in index {camera_index}, retrying...")

    if not cap.isOpened():
        cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
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
    try:
        detector = vision.PoseLandmarker.create_from_options(options)
    except NotImplementedError:
        base_options = python.BaseOptions(
            model_asset_path="model/pose_landmarker_heavy.task"
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

def run_image(image_path: str):
    base_options = python.BaseOptions(model_asset_path="model/pose_landmarker_heavy.task")
    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.IMAGE,
        output_segmentation_masks=False,
        # min_pose_presence_confidence=0.1,
        # min_pose_detection_confidence=0.1,
        # min_tracking_confidence=0.1,
        num_poses=5
    )
    detector = vision.PoseLandmarker.create_from_options(options)

    # Load image
    bgr_image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)

    # Detect poses
    result = detector.detect(mp_image)

    # Annotate
    annotated = draw_landmarks_on_image(rgb_image, result)
    cv2.imshow("Pose on Image", cv2.cvtColor(annotated, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def run_on_video(video_path: str):
    base_options = python.BaseOptions(model_asset_path="model/pose_landmarker_heavy.task")
    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.VIDEO,
        output_segmentation_masks=False,
        num_poses=5
    )
    detector = vision.PoseLandmarker.create_from_options(options)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    timestamp_step = int(1000 / fps)
    timestamp = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        result = detector.detect_for_video(mp_image, timestamp)
        timestamp += timestamp_step

        annotated = draw_landmarks_on_image(rgb_frame, result)
        cv2.imshow("Pose on Video", cv2.cvtColor(annotated, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_live_stream()
    # run_image("poses/07_shark.png")




