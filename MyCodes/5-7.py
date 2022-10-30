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

