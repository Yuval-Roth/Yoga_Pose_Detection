import cv2
import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np


def draw_landmarks_on_image(rgb_image, detection_result):
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected poses to visualize.
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Draw the pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image

while True:
    cap = cv2.VideoCapture(0)  # 0 = default webcam
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            exit(1)

        # STEP 2: Create an PoseLandmarker object.
        base_options = python.BaseOptions(model_asset_path='model/pose_landmarker_heavy.task')
        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            output_segmentation_masks=True,
            num_poses=5,
        )
        detector = vision.PoseLandmarker.create_from_options(options)

        # Convert OpenCV frame (BGR → RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert numpy array → MediaPipe Image
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # STEP 4: Detect pose landmarks from the input image.
        detection_result = detector.detect(image)

        # STEP 5: Process the detection result. In this case, visualize it.
        annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
        cv2.imshow("Mediapipe Pose", cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))

        # segmentation_mask = detection_result.segmentation_masks[0].numpy_view()
        # visualized_mask = np.repeat(segmentation_mask[:, :, np.newaxis], 3, axis=2) * 255
        # cv2.imshow("2", visualized_mask)

        # cv2.imshow("Camera Feed", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

