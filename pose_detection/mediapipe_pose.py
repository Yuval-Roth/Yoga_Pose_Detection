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

LAPTOP = True
FPS = 60
TIMESTAMP_STEP = int(1000 / FPS)
timestamp = 0
frame_width, frame_height = 1280, 720
# frame_width, frame_height = 1920, 1080
body = Body(frame_width, frame_height, avg_count=6)

# Global variable to hold last annotated frame
annotated_frame: Optional[np.ndarray[Any, np.dtype[Any]]] = None

def draw_landmarks_on_image(rgb_image, detection_result):
    pose_landmarks_list = detection_result.pose_landmarks
    annotated_image = np.copy(rgb_image)

    for idx in range(len(pose_landmarks_list)):
        pose_landmarks = pose_landmarks_list[idx]

        body.update(pose_landmarks)
        annotate_body(annotated_image)

        # detected_poses = detect_pose(body)
        # for i, pose in enumerate(detected_poses):
        #     cv2.putText(annotated_image, f"{pose}", (50, 50 + 30 * i), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    return annotated_image

def annotate_body(annotated_image):
    # =============================== #
    # new version with body smoothing #
    # ================================#

    nose = body.parts[BodyParts.HEAD].nose
    left_eye = body.parts[BodyParts.HEAD].left_eye
    right_eye = body.parts[BodyParts.HEAD].right_eye
    left_shoulder = body.parts[BodyParts.LEFT_ARM].shoulder
    left_elbow = body.parts[BodyParts.LEFT_ARM].elbow
    left_wrist = body.parts[BodyParts.LEFT_ARM].wrist
    right_shoulder = body.parts[BodyParts.RIGHT_ARM].shoulder
    right_elbow = body.parts[BodyParts.RIGHT_ARM].elbow
    right_wrist = body.parts[BodyParts.RIGHT_ARM].wrist
    left_hip = body.parts[BodyParts.LEFT_LEG].hip
    left_knee = body.parts[BodyParts.LEFT_LEG].knee
    left_ankle = body.parts[BodyParts.LEFT_LEG].ankle
    right_hip = body.parts[BodyParts.RIGHT_LEG].hip
    right_knee = body.parts[BodyParts.RIGHT_LEG].knee
    right_ankle = body.parts[BodyParts.RIGHT_LEG].ankle

    # Draw the smoothed landmarks
    cv2.line(annotated_image, (left_shoulder.x, left_shoulder.y), (left_elbow.x, left_elbow.y), (255, 0, 0), 2)
    cv2.line(annotated_image, (left_elbow.x, left_elbow.y), (left_wrist.x, left_wrist.y), (255, 0, 0), 2)
    cv2.line(annotated_image, (right_shoulder.x, right_shoulder.y), (right_elbow.x, right_elbow.y), (0, 255, 0), 2)
    cv2.line(annotated_image, (right_elbow.x, right_elbow.y), (right_wrist.x, right_wrist.y), (0, 255, 0), 2)
    cv2.line(annotated_image, (left_hip.x, left_hip.y), (left_knee.x, left_knee.y), (0, 0, 255), 2)
    cv2.line(annotated_image, (left_knee.x, left_knee.y), (left_ankle.x, left_ankle.y), (0, 0, 255), 2)
    cv2.line(annotated_image, (right_hip.x, right_hip.y), (right_knee.x, right_knee.y), (255, 255, 0), 2)
    cv2.line(annotated_image, (right_knee.x, right_knee.y), (right_ankle.x, right_ankle.y), (255, 255, 0), 2)
    cv2.line(annotated_image, (left_shoulder.x, left_shoulder.y), (left_hip.x, left_hip.y), (0, 255, 255), 2)
    cv2.line(annotated_image, (right_shoulder.x, right_shoulder.y), (right_hip.x, right_hip.y), (0, 255, 255), 2)
    cv2.line(annotated_image, (left_shoulder.x, left_shoulder.y), (right_shoulder.x, right_shoulder.y), (255, 0, 255), 2)
    cv2.line(annotated_image, (left_hip.x, left_hip.y), (right_hip.x, right_hip.y), (255, 0, 255), 2)
    cv2.circle(annotated_image, (nose.x, nose.y), 5, (0, 255, 255), -1)
    cv2.circle(annotated_image, (left_eye.x, left_eye.y), 5, (255, 0, 255), -1)
    cv2.circle(annotated_image, (right_eye.x, right_eye.y), 5, (255, 0, 255), -1)

    # Draw angles on the image
    cv2.putText(annotated_image, f"{int(body.left_elbow_angle())}", (left_elbow.x + 10, left_elbow.y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.right_elbow_angle())}", (right_elbow.x - 45, right_elbow.y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.left_knee_angle())}", (left_knee.x + 10, left_knee.y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.right_knee_angle())}", (right_knee.x - 45, right_knee.y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.left_shoulder_angle())}", (left_shoulder.x + 10, left_shoulder.y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.right_shoulder_angle())}", (right_shoulder.x - 45, right_shoulder.y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.left_hip_angle())}", (left_hip.x + 10, left_hip.y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.right_hip_angle())}", (right_hip.x - 45, right_hip.y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

def annotate_body_old(annotated_image, pose_landmarks):
    # ================================ #
    # old version with pose_landmarks  #
    # ================================ #

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
        # landmark_drawing_spec=None,
        solutions.drawing_styles.get_default_pose_landmarks_style()
    )

    cv2.putText(annotated_image, f"{int(body.left_elbow_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_ELBOW].x * frame_width), int(pose_landmarks[PoseLandmark.LEFT_ELBOW].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.right_elbow_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_ELBOW].x * frame_width), int(pose_landmarks[PoseLandmark.RIGHT_ELBOW].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.left_knee_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_KNEE].x * frame_width), int(pose_landmarks[PoseLandmark.LEFT_KNEE].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.right_knee_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_KNEE].x * frame_width), int(pose_landmarks[PoseLandmark.RIGHT_KNEE].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.left_shoulder_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_SHOULDER].x * frame_width), int(pose_landmarks[PoseLandmark.LEFT_SHOULDER].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.right_shoulder_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_SHOULDER].x * frame_width), int(pose_landmarks[PoseLandmark.RIGHT_SHOULDER].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.left_hip_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_HIP].x * frame_width), int(pose_landmarks[PoseLandmark.LEFT_HIP].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
    cv2.putText(annotated_image, f"{int(body.right_hip_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_HIP].x * frame_width), int(pose_landmarks[PoseLandmark.RIGHT_HIP].y * frame_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)



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
    print(f"** Searching for camera **")
    while not cap.isOpened() and camera_index < 10:
        print(f">> Camera not found in index {camera_index}")
        camera_index += 1
        cap = cv2.VideoCapture(camera_index)

    if cap.isOpened():
        print(f" -- Using camera index {camera_index} -- ")
    else:
        print(">> Trying default camera index 0...")
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print(f" -- Using camera index 0 -- ")

    # Force MJPG (instead of default YUYV)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    cap.set(cv2.CAP_PROP_FPS, FPS)
    if LAPTOP:
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
        print("\nGPU delegate is not supported on this platform, falling back to CPU.\n")
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
            if LAPTOP:
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


def test_fps():
    import cv2, time

    cap = cv2.VideoCapture(0)

    # Force MJPG (instead of default YUYV)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Warm-up
    for _ in range(10):
        cap.read()

    start = time.time()
    frames = 120
    for i in range(frames):
        ret, frame = cap.read()
    end = time.time()

    print("FPS:", frames / (end - start))
    cap.release()


if __name__ == "__main__":
    run_live_stream()
    # run_image("poses/07_shark.png")




