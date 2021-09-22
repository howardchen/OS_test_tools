# judge os is 64 bit or not 根據是否有PROGRAMFILES(X86)資料夾判斷
import os
def Is64Windows():
  return 'PROGRAMFILES(X86)' in os.environ