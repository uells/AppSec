print("\n\nЗадача 1: «Валидатор пароля»")
"""
Задача 1: «Валидатор пароля»
"""
# блок вспомогательных функций для задания 1
def has_upper(string: str) -> bool:
    for ch in string:
        if ch.isupper():
            return True
    return False

def has_lower(string: str) -> bool:
    for ch in string:
        if ch.islower():
            return True
    return False

def has_decimal(string: str) -> bool:
    for ch in string:
        if ch.isdecimal():
            return True
    return False

def has_alpha(string: str) -> bool:
    for ch in string:
        if ch.isalpha():
            return True
    return False

# Считаем все не буквенно-числовые значения спец символами
def has_noalnum(string: str) -> bool:
    for ch in string:
        if not ch.isalnum():
            return True  
    return False

# Валидатор пароля
def validate_password(password: str) -> bool:
    MIN_PW_LEN = 8
    pw = password.replace(' ', '').replace('\n', '')
    return has_upper(pw) and has_lower(pw) and has_decimal(pw) and has_alpha(pw) and has_noalnum(pw) and len(pw) >= MIN_PW_LEN

print(validate_password("123231Оываываыва.\n"))
print(validate_password("Abo$ba53"))
print(validate_password("Password20 \n   "))
print(validate_password("Ho%'3"))


print("\n\nЗадача 2: «Сканер портов (симуляция)»")
"""
Задача 2: «Сканер портов (симуляция)»
"""

def scan_ports(port: int) -> str:
    SAFE_PORTS = [80, 22, 443, 21, 3389]
    VULNERABLE_PORTS = [23, 135]

    if port in SAFE_PORTS:
        print(f"Port {port} is OPEN.")
        return
    if port in VULNERABLE_PORTS:
        print(f"Port {port} is OPEN and considered VULNERABLE!")
        return
    
    print(f"Port {port} is closed.")
    return

scan_ports(80)
scan_ports(22)
scan_ports(443)
scan_ports(21)
scan_ports(3389)
scan_ports(23)
scan_ports(135)
scan_ports(8000)
scan_ports(9000)


print("\n\nЗадача 3: «Анализатор логов на подозрительную активность»")
"""
Задача 3: «Анализатор логов на подозрительную активность»"
"""

def find_suspicious_activity(logs: list) -> tuple:
    scanners, suspicious = [], []
    for log in logs:
        code = int(log.split("' ")[-1])
        ip = log.split(' - - ')[0]
        if code == 404:
            scanners.append(ip)
        if code == 403:
            suspicious.append(ip)
    return (list(set(scanners)), list(set(suspicious)))

logs = [
    "192.168.1.1 - - [01/Jan/2024] 'GET /index.html HTTP/1.1' 200",
    "10.0.0.5 - - [01/Jan/2024] 'POST /login.php HTTP/1.1' 404",
    "10.0.0.5 - - [01/Jan/2024] 'POST /login.php HTTP/1.1' 404",
    "10.0.0.5 - - [01/Jan/2024] 'POST /login.php HTTP/1.1' 404",
    "10.0.0.5 - - [01/Jan/2024] 'POST /login.php HTTP/1.1' 404",
    "10.0.0.5 - - [01/Jan/2024] 'POST /login.php HTTP/1.1' 404",
    "192.168.1.1 - - [01/Jan/2024] 'GET /admin/panel HTTP/1.1' 403",
    "192.168.1.1 - - [01/Jan/2024] 'GET /admin/panel HTTP/1.1' 403",
    "192.168.1.1 - - [01/Jan/2024] 'GET /admin/panel HTTP/1.1' 403",
    "192.168.1.1 - - [01/Jan/2024] 'GET /admin/panel HTTP/1.1' 403",
    "10.0.0.5 - - [01/Jan/2024] 'GET /index.html HTTP/1.1' 200",
    "192.168.1.1 - - [01/Jan/2024] 'POST /login.php HTTP/1.1' 200"
]

print(find_suspicious_activity(logs))
        

