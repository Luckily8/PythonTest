import sys

sys.path.append(r"H:\Library\知识\pythonText\Ordinary study\堆栈区")

import func_pack.pack1

from func_pack import func1

print(func_pack.func1)
print(func1, func_pack.func1 is func1)
print("func_pack is in sys :", "func_pack" in sys.modules)
print("func_pack.pack1 is in sys :", "func_pack.pack1" in sys.modules)
print("func_pack.pack1.func1 is in sys :", "func_pack.pack1.func1" in sys.modules)
