from typing import Any, Optional
import cv2
import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np

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
