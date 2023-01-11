import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands= mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)


finger_tips=[8,12,16,20]


def drawHandLandmarks(image,hand_landmarks):
    if hand_landmarks:

        for lm_list in hand_landmarks:
            mp_drawing.draw_landmarks(image,landmarks,mp_hands.HAND_CONNECTIONS)

            
for tip in finger_tips:
    x,y = int(lm_list[tip].x*w),int(llm_list[tip].y*h)
    cv2.circle(img,(x,y),15,(255,0,0),cv2.FILLED)

    
    finger_fold_status=[]

    if lm_list[tip].x< lm_list[tip-2].x:
        cv2.circle(img,(x,y),15,(0,255,0),cv2.FILED)
        finger_fold_status.append(True)
    else:
        finger_fold_status.append(False)

    if all(finger_fold_status):
        if lm_list[thumb_tip].y< lm_list[thumb_tip-2].y:
            print("like")
            cv2.puText(img,"like", (20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,),3)
            
            if lm_list[thumb_tip].y>lm_list[thumb_tip-2].y:
                print("dislike")
                cv2.puText(img,"dislike", (20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,),3)

                

    
while True:
    success,image=cap.read()

    image = cv2.flip(image,1)

    results = hands.process(image)

    hand_landmarks = results.multi_hand_landmarks

    drawHandLandMarks(image,hand_landmarks)

    cv2.imshow("Media Controlller",image)

    key = cv2.waitkey(1)
    if key==32:
        break
cv2.destroyAllWindows()
