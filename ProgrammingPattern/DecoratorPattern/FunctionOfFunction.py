# 하스 스톤의 안녕 로봇
def annoy_o_tron(message):
    # 안녕 로봇이 인사할 수 있도록 해주는 내부 구현
    def greeting(name):
        print(f"{message} - {name}!")
    return greeting

    # annoy_o_tron 함수의 반환 값은 def greeting(name): print(...)
    # print(f'Hello - {name}') 함수를 값처럼 가지고 있는 상태라고 할 수 있다.
    hello_o_tron = annoy_o_tron('Hello')
    
    # print('Hello - Doodoony!') 함수를 호출함
    hello_o_tron('Doodoony') # Hello - Doodoony!
    hello_o_tron('velog') # Hello - velog!