# 가로쓰레기통 알리미 (Tensorflow)
- 가로쓰레기통 알리미 앱의 딥러닝 파트 레포입니다.
- 본 프로젝트는 imagenet으로 훈련된 MobileNetV2 모델을 base model로 사용합니다.
- 플라스틱, 종이, 병, 캔, 고철, 스티로폼, 비닐 등 15가지 재활용 쓰레기 정보를 예측합니다.
- 쓰레기 이미지의 분류 예측 결과를 Flask REST API를 이용하여 확인할 수 있습니다.

## 참가자
|역할|학과|이름|
|---------|------------|-------|
|팀장, 프론트엔드|컴퓨터과학과|[정한수](https://github.com/8471919)|
|프론트엔드|컴퓨터과학과|[김진용](https://github.com/imagine97kim)|
|백엔드|컴퓨터과학과|[최종현](https://github.com/lun4-light)|
|백엔드|식품영양학과|[김혜주](https://https://github.com/201210302)|
|데이터분석|컴퓨터과학과|[윤윤호](https://github.com/YUN-YUNHO)|

## Architecture
![architecture](https://user-images.githubusercontent.com/27190811/169642422-4f963b5d-f471-47f5-8dc6-6581e8fdf05f.png)
- 언어: Python
- 프레임워크: TensorFlow, Keras, Flask
- 개발 환경: Windows Server 2022
- 배포 서버 환경: Amazon EC2 (Ubuntu 20.04.4 LTS)

## Usage
### 데이터 전처리
```commandline
python preprogress.py
usage: preprocess.py [-h] --src_dir SRC_DIR --dst_dir DST_DIR
optional arguments:
  -h, --help         show this help message and exit
  --src_dir SRC_DIR  source path
  --dst_dir DST_DIR  destination path
```
### 모델 훈련 및 예측
```commandline
현재 image_classifier.py 에 클래스만 정의함.
해당 실행 파일은 추후 추가하겠음.
```
### 모델 사용 예시
[model-usage-mobilenetv2.ipynb](model-usage-mobilenetv2.ipynb)
![prediction](https://user-images.githubusercontent.com/27190811/169643857-3d23c6e2-0d24-400f-a9f8-790f0d8f66c7.png)

## Deployment
### 1. Docker
[도커 사용법](https://lively-goose-8b9.notion.site/Docker-4dcaf3b93a894fbe9b86efbe9c7d1eee)
```commandline
docker pull yoon36399/trash-image:0.1
```

### 2. git clone
[모델 파일 다운로드](https://drive.google.com/drive/folders/1FmgiOhPQUALF6Z-prt2oS69vsrO8oAtm?usp=sharing)
```commandline
pip install -r requirements.txt
# 다운로드한 모델 파일을 DL/models/savings로 이동한다.
python server.py
```

## Reference
- [NIA 생활 폐기물 이미지 데이터셋](https://aihub.or.kr/aidata/27708)
- [Tensorflow](https://www.tensorflow.org/)
