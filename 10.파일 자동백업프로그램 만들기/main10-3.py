from distutils.dir_util import copy_tree
from win10toast import ToastNotifier

# 'ToastNotifier()'를 호출해 'toaster' 객체 생성. 객체를 통해 나중에 알림을 보여줄 수 있음.
toaster = ToastNotifier()

원본_폴더 = r'C:\일잘러 파이썬과 40개의 작품들 코드\10.파일 자동백업프로그램 만들기\원본'
백업될_폴더 = r'C:\일잘러 파이썬과 40개의 작품들 코드\10.파일 자동백업프로그램 만들기\백업'
result = copy_tree(원본_폴더,백업될_폴더,update=1) # 'update=1' 매개변수는 대상 폴더의 내용을 업데이트할 수 있도록 함.

toaster.show_toast("백업이 완료되었습니다.",원본_폴더 + ">>>" + 백업될_폴더,duration=10) # 알림이 10초 동안 표시