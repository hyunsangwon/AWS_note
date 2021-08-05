from .aes import CustomAES
from socket import *

cipher_key = "BCCNS18101061SK5"
ip = "211.216.53.46"
port = 35400

def reqeust_bluechip(euid):
    head_code = "01001"  # 업무 구분 코드
    head_body_length = None  # header를 제외한 암호화된 body 부분 length
    head_company_number = "61                  "  # 회사번호(공백 포함 20자리)
    head = None  # 전체 헤더

    body_stx = "#"  # 전문 시작 구분자
    body_hp_no = None  # 요청 전화번호(공백 포함 12자)
    body_company_number = "61"  # 회사번호
    body_etx = "$"  # 전문 종료 구분자
    body = None  # 전체 body
    encoded_body = None  # 암호화된 body

    request = None  # 전체 요청 전문(head + encoded_body)
    response = None  # 전체 응답 전문

    response_header = None  # 응답 헤더
    response_body = None  # 응답 body
    decoded_body = None  # 복호화된 body

    rcv_hp_no = None  # 요청 전화번호
    pos_address = None  # 주소(euc-kr)
    pos_postal_cd = None  # 우편번호
    pos_x = None  # x 좌표
    pos_y = None  # y 좌표
    ms_type = None  # 측위 구분
    telcom = None  # 결과 통신사
    code = None  # 결과 코드

    lat = 0.0
    lng = 0.0

    aes_cipher = CustomAES(cipher_key)

    try:
        body_hp_no = "012" + euid + " "
        body = body_stx + body_hp_no + body_company_number + body_etx
        encoded_body = aes_cipher.encrypt(body)

        head_body_length = str(len(encoded_body))
        padding = 7 - len(head_body_length)

        for i in range(padding):
            head_body_length += " "

        head = head_code + head_body_length + head_company_number
        request = head + encoded_body

        s = socket(AF_INET, SOCK_STREAM)
        s.connect((ip, port))

        s.send(request.encode())

        response = s.recv(1024).decode()

        s.close()

        response_header = response[:32]
        body_length = int(response_header[5:12].strip())

        response_body = response[32:32 + body_length]
        decoded_body = aes_cipher.decrypt(response_body)

        if decoded_body[0] == "#" and decoded_body[-1] == "$":
            rcv_hp_no = decoded_body[15:27]
            pos_address = decoded_body[27:-41]
            pos_postal_cd = decoded_body[-41:-34]
            pos_x = decoded_body[-34:-24]
            pos_y = decoded_body[-24:-14]
            ms_type = decoded_body[-14:-11]
            telcom = decoded_body[-11:-7]
            code = decoded_body[-7:-1]

            if rcv_hp_no == body_hp_no and code == "S00000":
                pos_x = pos_x.strip()
                pos_y = pos_y.strip()
                pos_address = pos_address.strip()

                pos_x = pos_x[:3] + "." + pos_x[3:]
                pos_y = pos_y[:2] + "." + pos_y[2:]

                lat = float(pos_y)
                lng = float(pos_x)

    except Exception as e:
        print(e)

    return {"lat": lat, "lng": lng, "address": pos_address}
