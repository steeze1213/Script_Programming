def is_valid_ip(ip):
    parts = ip.split('.')
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    
    return True

ip = input("IP 주소를 입력하시오: ")

if is_valid_ip(ip):
    print("유효한 IP 주소입니다.")
else:
    print("유효하지 않은 IP 주소입니다.")
