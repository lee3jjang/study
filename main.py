# 주제 : 마우스, 키보드 자동화
# 목표 : pyautogui 모듈을 이용해 마우스, 키보드 제어한다

import pyautogui as pg
import time

# 인터넷 브라우저 접속
pg.moveTo(636, 1052)
pg.click()
time.sleep(1)

# 외부메일 접속
pg.write('https://mail.dbins.co.kr')
pg.hotkey('enter')
time.sleep(2)

# 사번, 비밀번호 입력
pg.write('id')
pg.write('password')
pg.hotkey('enter')

# 인증번호 입력
key = pg.prompt(text='인증번호를 입력하세요', title='인증번호')
pg.write(key)
pg.moveTo(653, 651)
pg.click()