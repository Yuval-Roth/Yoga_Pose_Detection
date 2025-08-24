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
from pose_detection import detect_pose

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
        body = Body(pose_landmarks, w, h)


        # Draw angles on the image
        cv2.putText(annotated_image, f"{int(body.left_elbow_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_ELBOW].x * w), int(pose_landmarks[PoseLandmark.LEFT_ELBOW].y * h)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.right_elbow_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_ELBOW].x * w), int(pose_landmarks[PoseLandmark.RIGHT_ELBOW].y * h)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.left_knee_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_KNEE].x * w), int(pose_landmarks[PoseLandmark.LEFT_KNEE].y * h)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.right_knee_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_KNEE].x * w), int(pose_landmarks[PoseLandmark.RIGHT_KNEE].y * h)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.left_shoulder_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_SHOULDER].x * w), int(pose_landmarks[PoseLandmark.LEFT_SHOULDER].y * h)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.right_shoulder_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_SHOULDER].x * w), int(pose_landmarks[PoseLandmark.RIGHT_SHOULDER].y * h)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.left_hip_angle())}", (int(pose_landmarks[PoseLandmark.LEFT_HIP].x * w), int(pose_landmarks[PoseLandmark.LEFT_HIP].y * h)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2),
        cv2.putText(annotated_image, f"{int(body.right_hip_angle())}", (int(pose_landmarks[PoseLandmark.RIGHT_HIP].x * w), int(pose_landmarks[PoseLandmark.RIGHT_HIP].y * h)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        detected,pose = detect_pose(body)
        if detected:
            cv2.putText(annotated_image, f"{pose}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

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
    while not cap.isOpened():
        camera_index += 1
        cap = cv2.VideoCapture(camera_index)
        print(f"Camera not found in index {camera_index}, retrying...")

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

def run_image(image_path: str):
    base_options = python.BaseOptions(model_asset_path="model/pose_landmarker_heavy.task")
    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.IMAGE,
        output_segmentation_masks=False,
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
    # run_image("poses/02_downward_facing_dog.png")




