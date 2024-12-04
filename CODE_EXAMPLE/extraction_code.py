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

# 옷과 배경 영역 추출 함수
def extract_regions(image, cloth_lower, cloth_upper, bg_lower, bg_upper):
    # 이미지를 HSV 색공간으로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 옷 영역 추출
    cloth_mask = cv2.inRange(hsv, cloth_lower, cloth_upper)
    cloth_region = cv2.bitwise_and(image, image, mask=cloth_mask)

    # 배경 영역 추출
    bg_mask = cv2.inRange(hsv, bg_lower, bg_upper)
    bg_region = cv2.bitwise_and(image, image, mask=bg_mask)

    return cloth_region, bg_region

# 메인 함수
def main():
    # 이미지 파일 경로
    image_path = "test.png"  # 이미지 파일 경로를 변경하세요
    image = cv2.imread(image_path)

    if image is None:
        print("이미지를 불러오지 못했습니다. 경로를 확인하세요.")
        return

    # 옷과 배경 색상 범위 설정 (HSV 값)
    cloth_lower = np.array([90, 50, 50])  # 옷 색상 하한값
    cloth_upper = np.array([130, 255, 255])  # 옷 색상 상한값
    bg_lower = np.array([20, 50, 50])  # 배경 색상 하한값
    bg_upper = np.array([40, 255, 255])  # 배경 색상 상한값

    # 옷과 배경 영역 추출
    cloth_region, bg_region = extract_regions(image, cloth_lower, cloth_upper, bg_lower, bg_upper)

    # 추출된 영역 출력
    show_image(cloth_region, "Extracted Cloth Region")
    show_image(bg_region, "Extracted Background Region")

# 프로그램 실행
if __name__ == "__main__":
    main()
