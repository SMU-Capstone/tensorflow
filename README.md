# 가로쓰레기통 알리미 (Tensorflow)
- 가로쓰레기통 알리미 앱의 딥러닝 레포입니다.
- 플라스틱, 종이, 병, 캔, 고철, 스티로폼 비닐 등 15가지에 대한 이미지 분류 모델

## 사용기술
- 언어 : Python
- 프레임워크 : TensorFlow, Keras

## 참가자
|역할|학과|이름|
|---------|------------|-------|
|데이터분석|컴퓨터과학과|[윤윤호](https://github.com/YUN-YUNHO)|
|팀장|컴퓨터과학과|[정한수](https://github.com/8471919)|
|백엔드| 컴퓨터과학과 |[최종현](https://github.com/lun4-light)|
|프론트엔드|컴퓨터과학과|[김진용](https://github.com/imagine97kim)|
|백엔드|식품영양학과|[김혜주](https://https://github.com/201210302)|

## Usage
```commandline
python preprogress.py
이미지 데이터의 전처리
usage: preprocess.py [-h] --src_dir SRC_DIR --dst_dir DST_DIR
optional arguments:
  -h, --help         show this help message and exit
  --src_dir SRC_DIR  source path
  --dst_dir DST_DIR  destination path
```
```commandline
model-usage-mobilenetv2.ipynb
전반적인 모델의 사용 예시
```

## Reference
- [NIA 생활 폐기물 이미지 데이터셋](https://aihub.or.kr/aidata/27708)
- [Tensorflow](https://www.tensorflow.org/)
