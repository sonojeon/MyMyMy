has_owner = ''

while has_owner != '예':

    my_money = int(input('현재 가지고 있는 돈을 입력하세요 : '))
    if my_money <= 0:
        print('통행료를 낼 수 없군요.')
        break
    
    in_space = input('''우주정거장에 있나요?
있다면 예
없다면 아니요
를 입력해주세요
''')
    if in_space == '예':
        print('처음으로 다시 돌아갑니다.')
        continue

    has_owner = input('''땅 주인이 있나요?
있다면 예
없다면 아니요
를 입력해주세요
''')
    if has_owner == '예':
        print('통행료를 내세요')
    elif has_owner == '아니요':
        print('그냥 통과하세요')
    else:
        print('잘못 입력하셨습니다')








