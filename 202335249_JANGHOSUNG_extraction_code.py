pip install opencv-python matplotlib

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

# 흰색(호랑이)과 빨간색(배경) 영역 추출 함수
def extract_regions(image, white_lower, white_upper, red_lower1, red_upper1, red_lower2, red_upper2):
    # 이미지를 HSV 색공간으로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 흰색 영역 마스크 생성
    white_mask = cv2.inRange(hsv, white_lower, white_upper)
    white_region = cv2.bitwise_and(image, image, mask=white_mask)

    # 빨간색 영역 마스크 생성 (두 영역으로 나누어서 처리)
    red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
    red_mask = red_mask1 | red_mask2
    red_region = cv2.bitwise_and(image, image, mask=red_mask)

    return white_region, red_region

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

    # 흰색과 빨간색 영역 추출
    white_region, red_region = extract_regions(image, white_lower, white_upper, red_lower1, red_upper1, red_lower2, red_upper2)

    # 추출된 영역 출력
    show_image(white_region, "Extracted White Region (Tiger)")
    show_image(red_region, "Extracted Red Region (Background)")

# 프로그램 실행
if __name__ == "__main__":
    main()
