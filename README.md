# OpenCV-image_color_extraction-change

### 프로젝트 개요
***

### 예시 이미지
***


### 사용한 패키지 및 버전
***   
1.openCV2 (install 필요, python 에서 작동하므로 ``` pip install opencv-python ```로 작성필요)   
사용된 버전:4.10.0

2.numpy (install 불필요)   
사용된 버전:1.26.4

3.matplotlib.pyplot   
(pyplot는 matplotlib안에 있는 sub-module이므로 ``` pip install matplotlib ``` 로 install)   
사용된 버전: 3.8.0

### 실행 방법
***

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
