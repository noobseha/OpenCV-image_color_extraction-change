import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 표시하는 함수
def show_image(image, title="Image"):
    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# 색상 변경 함수
def change_colors(image, white_lower, white_upper, red_lower1, red_upper1, red_lower2, red_upper2, new_white_color, new_red_color):
    # 이미지를 HSV 색공간으로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 흰색 영역 변경
    white_mask = cv2.inRange(hsv, white_lower, white_upper)
    image[np.where(white_mask != 0)] = new_white_color

    # 빨간색 영역 변경 (두 영역으로 나누어 처리)
    red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
    red_mask = red_mask1 | red_mask2
    image[np.where(red_mask != 0)] = new_red_color

    return image

# 메인 함수
def main():
    # 이미지 파일 경로
    image_path = "/content/tiger.png"  # Colab에서 업로드한 이미지 경로
    image = cv2.imread(image_path)

    if image is None:
        print("이미지를 불러오지 못했습니다. 경로를 확인하세요.")
        return

    # 흰색(호랑이)과 빨간색(배경) 범위 설정 (HSV 값)
    white_lower = np.array([0, 0, 200])  # 흰색 하한값
    white_upper = np.array([180, 30, 255])  # 흰색 상한값
    red_lower1 = np.array([0, 120, 70])  # 빨간색 하한값 (1)
    red_upper1 = np.array([10, 255, 255])  # 빨간색 상한값 (1)
    red_lower2 = np.array([170, 120, 70])  # 빨간색 하한값 (2)
    red_upper2 = np.array([180, 255, 255])  # 빨간색 상한값 (2)

    # 새로운 색상 (BGR 값)
    new_white_color = [0, 165, 255]  # 주황색 (BGR)
    new_red_color = [255, 191, 0]  # 하늘색 (BGR)

    # 색 변경 적용
    modified_image = change_colors(image.copy(), white_lower, white_upper, red_lower1, red_upper1, red_lower2, red_upper2, new_white_color, new_red_color)

    # 결과 이미지 출력
    show_image(modified_image, "Modified Image")

# 프로그램 실행
if __name__ == "__main__":
    main()
