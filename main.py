import cv2
import mediapipe as mp
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

camera = cv2.VideoCapture(0)

def finger_open(landmarks, hand_label):
    motherfinger_open = False
    if hand_label == 'Right':
        if landmarks[4].x <landmarks[3].x:
            motherfinger_open = True
    elif hand_label == 'Left':
        if landmarks[4].x > landmarks[3].x:
            motherfinger_open = False

    indexfinger_open = landmarks[8].y <landmarks[6].y

    middlefinger_open = landmarks[12].y < landmarks[10].y

    ringfinger_open = landmarks[16].y < landmarks[14].y

    littlefinger_open = landmarks[20].y < landmarks[18].y

    FingerOpenSum = sum([motherfinger_open, indexfinger_open, middlefinger_open, ringfinger_open, littlefinger_open])
    
    return FingerOpenSum, motherfinger_open, indexfinger_open, middlefinger_open, ringfinger_open, littlefinger_open

with mp_hands.Hands(
    model_complexity = 0,
    max_num_hands = 1,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
) as hands:
    
    gesture_text = "HI"
    last_gesture = ''

    while True:
        sts, frame = camera.read()

        if not sts:
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_idx, hand_landmarks in enumerate(result.multi_hand_landmarks):
                hand_label = result.multi_handedness[hand_idx].classification[0].label

                landmark_drawing_spec = mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2)      
                connection_drawing_spec = mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2)    

                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    landmark_drawing_spec,
                    connection_drawing_spec
                )

                finger_open_count, motherfinger, indexfinger, middlefinger, ringfinger, littlefinger = finger_open(hand_landmarks.landmark, hand_label)

                if finger_open_count == 5:
                    gesture_text = 'Jump'
                elif finger_open_count == 1 and indexfinger:
                    gesture_text = 'Left'
                elif finger_open_count == 2 and indexfinger and middlefinger:
                    gesture_text = 'Right'
                elif finger_open_count == 3 and indexfinger and middlefinger and ringfinger:
                    gesture_text = 'Hoverboard'
                elif finger_open_count == 0:
                    gesture_text = 'Roll'
        
        if gesture_text != last_gesture:
            if gesture_text == 'Jump':
                pyautogui.press('up')
            elif gesture_text == 'Left':
                pyautogui.press('left')
            elif gesture_text == 'Right':
                pyautogui.press('Right')
            elif gesture_text == 'Roll':
                pyautogui.press('down')
            elif gesture_text == 'Hoverboard':
                pyautogui.press('space')

            last_gesture = gesture_text

        cv2.putText(frame, gesture_text, (10,50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Gesture Control Subway Surfers', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()