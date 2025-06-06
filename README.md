# 🚀 PyCRC-Gen

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange)

> 🧮 A simple Python tool to generate CRC checksums using custom polynomials.


# 주제 - Checksum
## 🔧 CRC 생성기 (Cyclic Redundancy Check Generator)

이 프로젝트는 **주어진 다항식을 기반으로 전송 데이터에 CRC(순환 중복 검사, Cyclic Redundancy Check) 체크섬을 생성하는 파이썬 프로그램**입니다. 
오류 검출 방식의 대표적인 방법인 CRC를 이해하고 직접 구현하는 데 목적이 있습니다.

---

### ✅ 기능 요약

* `x^n` 형식의 다항식을 2진수 리스트로 변환
* 전송 데이터에 0을 패딩한 후, XOR 연산을 통해 CRC 체크섬 계산
* 체크섬이 포함된 전송 데이터를 생성

---

### 📄 코드 구조

#### 1. `parse_polynomial(input_str: str) -> List[int]`

* 사용자가 입력한 다항식 문자열 (예: `"x^5 + x^2 + 1"`)을 2진 리스트 형태로 변환합니다.
* 최대 차수 기준으로 비트를 배치하여 CRC 다항식을 구성합니다.

#### 2. `xor_division(data: List[int], polynomial: List[int]) -> List[int]`

* 다항식 나눗셈에 해당하는 XOR 연산을 수행해 \*\*CRC 나머지(체크섬)\*\*를 계산합니다.
* 다항식의 앞자리를 기준으로 1이 나올 때마다 XOR 연산을 수행합니다.

#### 3. `generate_crc(data: List[int], polynomial: List[int]) -> Tuple[List[int], List[int]]`

* 입력된 데이터에 `(다항식 차수 - 1)`개의 0을 패딩하여 준비합니다.
* `xor_division()`을 호출해 체크섬을 계산한 뒤, 원래 데이터 뒤에 붙여 최종 전송 데이터를 생성합니다.

---

### 🧪 사용 예시

```
다항식을 입력 : x^5 + x^2 + 1
전송데이터를 입력(공백 구분) : 1 0 1 0 1
```

**출력 예시:**

```
체크섬이 포함된 데이터:  [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
체크섬:  [1, 0, 0, 1, 0]
```

---

### 📌 참고 사항

* 입력 다항식은 `x^3 + x + 1`, `x^5 + x^2 + 1` 등과 같은 수학적 표현으로 입력받습니다.
* 전송 데이터는 `0`과 `1`로 구성된 리스트이며, 공백으로 구분하여 입력합니다.
* 실제 통신 시스템에서의 CRC와 동일한 방식으로 작동합니다. 학습용으로 매우 적합합니다.

---

### 📂 파일 구조

```
├── crc_generator.py     # CRC 계산 및 전송 데이터 생성 코드
└── README.md            # 프로젝트 설명서 (현재 문서)
```

---

### 📚 CRC란?

CRC(Cyclic Redundancy Check)는 디지털 통신에서 **데이터 전송 중 오류 검출**을 위해 널리 사용되는 방식입니다.
다항식을 기반으로 계산된 체크섬을 데이터에 붙여 전송하고, 수신 측에서 같은 방식으로 나머지를 계산하여 오류 여부를 판단합니다.
