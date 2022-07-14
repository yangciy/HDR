from lotto import LottoCreat as lt

cnt=int(input('구입할 로또의 개수를 입력하세요 (최대 10장)'))

lt.lottoCreat()   # 당첨번호 호출

for i in range(cnt):
    lt.lottoInput()
    lt.lottoConfirm()
    print('[{}번째 로또]'.format(i+1))
    lt.lottoOutput()