import re

def xor_division(data, polynomial):
    """주어진 데이터와 다항식을 XOR 연산하여 나머지를 계산"""
    data = data[:]  # 원본 데이터를 수정하지 않도록 복사
    for i in range(len(data) - len(polynomial) + 1):
        if data[i] == 1:  # 첫 비트가 1이면 다항식과 XOR 연산 수행
            for j in range(len(polynomial)):
                data[i + j] ^= polynomial[j]  # XOR 연산
    return data[-(len(polynomial)-1):]  # 나머지 값 반환 (체크섬)


def generate_crc(data, polynomial):
    """입력 데이터를 주어진 다항식을 사용해 체크섬을 추가한 데이터를 반환"""
    # 데이터 끝에 다항식의 길이 - 1 만큼 0을 추가
    padded_data = data + [0] * (len(polynomial) - 1)
    
    # XOR 연산을 통해 나머지 계산 (체크섬 구하기)
    checksum = xor_division(padded_data, polynomial)
    
    # 전송 데이터에 체크섬 추가
    return data + checksum, checksum


def parse_polynomial(input_str):
    """x^n 형식의 다항식을 파싱하여 2진수 리스트로 변환"""
    # 공백을 제거하고, 각 항목을 +로 구분해서 추출
    input_str = input_str.replace(" ", "")
    
    # 개선된 정규식: x^n, x, 상수항(1) 패턴을 추출하는 정규식
    terms = input_str.split("+")

    term_degrees = []
    for term in terms:
        if 'x^' in term:  # x^n의 경우
            degree = int(term.split('^')[1])
            term_degrees.append(degree)
        elif term == 'x':  # x의 경우 (차수는 1)
            term_degrees.append(1)
        elif term == '1':  # 상수항 1의 경우 (차수는 0)
            term_degrees.append(0)

    # 최대 차수 계산
    max_degree = max(term_degrees)

    # 다항식의 각 항을 2진수 리스트로 변환
    polynomial = [0] * (max_degree + 1)
    for degree in term_degrees:
        polynomial[max_degree - degree] = 1

    return polynomial


# 다항식을 입력받음 (예: x^5 + x^2 + 1)
polynomial_input = input("다항식을 입력 : ")
polynomial = parse_polynomial(polynomial_input)  # 다항식을 리스트로 변환

# 전송 데이터를 입력받음 (예: 1 0 1 0 1)
data_input = input("전송데이터를 입력(공백 구분) : ")
data = list(map(int, data_input.split()))  # 전송 데이터를 리스트로 변환

# 체크섬을 포함한 송신 데이터 생성
transmission_data, checksum = generate_crc(data, polynomial)

# 결과 출력
print("체크섬이 포함된 데이터: ", transmission_data)
print("체크섬: ", checksum)
