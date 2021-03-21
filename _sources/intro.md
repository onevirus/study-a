Configure Python on Mac
=======================

## pyenv

이것만 이용할 것.
사용 전 아래 기타 python 정리 필요.
brew install pyenv


## Apple-provided python

격리 대상.
쓰레기.
변경하려고 하지 말고, 사용하지도 말고, 개발 환경에서 격리시켜야 될 대상.
혹시라도 사용중인 python 기반 app 이나 개발 환경이 이 쓰레기를 기반으로 동작하는지 확인 또 확인해야 됨.
From https://docs.python.org/3/using/mac.html
> The Apple-provided build of Python is installed in /System/Library/Frameworks/Python.framework and /usr/bin/python, respectively. You should never modify or delete these, as they are Apple-controlled and are used by Apple- or third-party software.


## Python 3 from the Python website (https://www.python.org)

삭제 대상.
최신 버전을 설치할 수 있지만, 업그레이드 및 관리가 번거로움.
Installer 가 하는 것들.
Applications 폴더에 Python folder 가 생성.
/Library/Frameworks/Python.framework 에 Framework 설치.
shell path 에 위 경로 추가.
Python executable 의 symlink 가 /usr/local/bin 에 추가.

정상적인 Application 삭제 방법으로 삭제 후, 위 경로를 확인하여 남아 있는 쓰레기 삭제.


## Brew installed python

삭제 대상.
3.x 버전별로 설치할 수 있지만, 3.x.y 까지의 버전 관리가 안되고, 버전 간 스위칭이 쉽지 않음.
brew 로 할 건 pyenv 설치밖에 없음.
brew list | grep python 로 확인후 python@3.x 가 보이면
brew uninstall python@3.x 로 삭제
Error: Refusing to uninstall /usr/local/Cellar/python@3.9/3.9.2_1
because it is required by a, b and c, which are currently installed.
이런 메세지가 나오면 a, b, c 는 잘 못 설치된 것들. 다 삭제.


## Conda installed python

격리 대상.
Conda 는 python 가상화 툴이 아니라 package 가상화 툴 임. Conda 로 파이선을 관리하겠다는 멍청한 생각은 하지 말 것.

