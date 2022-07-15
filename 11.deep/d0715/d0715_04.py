from konlpy.tag import Okt
# from konlpy import jvm
# jvm.init_jvm()
# jvm_path = "/Library/Java/JavaVirtualMachines/zulu-15.jdk/Contents/Home/bin/java"

okt = Okt()
malist = okt.pos('아버지 가방에 들어가신다',norm=True,stem=True)
print(malist)