# 가로쓰레기통 알리미 (Tensorflow)
- 가로쓰레기통 알리미 앱의 딥러닝 레포입니다.
- 플라스틱, 종이, 병, 캔, 고철, 스티로폼 비닐 등 15가지에 대한 이미지 분류 모델

## 사용기술 및 환경
- 언어: Python
- 프레임워크: TensorFlow, Keras
- 개발 환경: Windows Server 2022
- 배포서버 환경: Amazon EC2

## 참가자
|역할|학과|이름|
|---------|------------|-------|
|팀장, 프론트엔드|컴퓨터과학과|[정한수](https://github.com/8471919)|
|프론트엔드|컴퓨터과학과|[김진용](https://github.com/imagine97kim)|
|백엔드|컴퓨터과학과|[최종현](https://github.com/lun4-light)|
|백엔드|식품영양학과|[김혜주](https://https://github.com/201210302)|
|데이터분석|컴퓨터과학과|[윤윤호](https://github.com/YUN-YUNHO)|

## Architecture
```commandline
추가 예정
```

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
```commandline
model-usage-mobilenetv2.ipynb
```
### Flask server 구동
```commandline
python server.py
```

## Deployment
- Docker image
- [도커 설치법](https://lively-goose-8b9.notion.site/Docker-4dcaf3b93a894fbe9b86efbe9c7d1eee)
```commandline
docker pull yoon36399/trash-image:0.1
```

## Reference
- [NIA 생활 폐기물 이미지 데이터셋](https://aihub.or.kr/aidata/27708)
- [Tensorflow](https://www.tensorflow.org/)
