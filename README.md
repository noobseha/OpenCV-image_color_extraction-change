# OpenCV-image_color_extraction-change

### 프로젝트 개요
***

### 예시 이미지
***
1. 원본 이미지
2. 옷과 배경을 추출한 이미지
3. 추출한 이미지의 색상을 바꿔 원본에 적용한 이미지

![](https://ifh.cc/g/SLBnF4.png)
![](https://ifh.cc/g/sdfbzR.png)
![](https://ifh.cc/g/Q5wRRb.png)
![](https://ifh.cc/g/27HcM0.png)

### 사용한 패키지 및 버전
***   
1.openCV2 (install 필요, python 에서 작동하므로 ``` pip install opencv-python ```로 작성필요)      
사용된 버전:4.10.0

2.numpy (install 불필요)      
사용된 버전:1.26.4

3.matplotlib.pyplot (pyplot은 matplotlib안에 있는 sub-module이므로 ``` pip install matplotlib ``` 로 install)      
사용된 버전: 3.8.0

---

### 실행 방법
1. **이미지를 HSV 색상 공간으로 변환:**  
   입력 이미지를 BGR에서 HSV로 변환하여 색상 기반 분할을 간소화합니다.

2. **추출을 위한 색상 범위 정의:**  
   관심 있는 색상의 HSV 범위를 정의합니다.

3. **컬러 마스크 생성:**  
   `cv2.inRange`를 사용하여 각 색상에 대한 바이너리 마스크를 생성합니다.  
   빨간색은 색상 랩어라운드를 처리하기 위해 두 가지 범위를 사용하여 분리합니다.

4. **추출 영역에 마스크 적용:**  
   비트 연산을 이용해 흰색 및 빨간색 마스크에 해당하는 영역을 추출합니다.

5. **결과 표시:**  
   Matplotlib을 사용하여 추출된 영역을 시각화하고 분할이 성공적으로 이루어졌는지 확인합니다.

---

## 가정:
- 대상 영역은 HSV 색상 범위에 따라 명확히 분리될 수 있습니다.
- 입력 이미지의 조명이 적절하고 색상이 크게 왜곡되지 않습니다.
- 선택한 HSV 임계값은 의도한 영역을 정확하게 커버합니다. (다양한 이미지에 따라 임계값을 조정할 수 있습니다.)

---

## 애플리케이션:
- 이 방법은 색상 속성을 기반으로 이미지를 분할하고 측정하는 데 확장될 수 있습니다.
- 윤곽선 감지와 결합하여 물체의 크기, 위치 또는 모양을 계산할 수 있습니다.
- 참조 개체를 사용하여 개체 감지, 추적, 차원 계산 등의 작업에 유용합니다.


### 한계
***
1. **색상 의존성:**  
   - 이 기술은 HSV 범위 선택에 크게 의존하므로 조명, 그림자, 유사한 색상으로 인해 색상이 정확히 추출되지 않을 가능성이 있습니다.  

2. **이미지 품질의 영향:**  
   - 조명이 어둡거나 해상도가 낮은 이미지, 또는 노이즈가 많은 경우 색상 추출 정확도가 떨어질 수 있습니다.  

3. **고정된 임계값:**  
   - 수동으로 설정한 HSV 범위는 이미지나 환경에 따라 유연하게 적용되지 않을 수 있어, 각 사례마다 범위를 미세하게 조정해야 할 필요가 있습니다.  

### 참고 자료
***
링크 : <https://engineer-mole.tistory.com/236>
