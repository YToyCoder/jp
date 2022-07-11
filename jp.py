
import binascii
import functools


import numpy as np

def read(file: str) -> None:
  allBytes = np.array([])
  with open(file) as f :
    lines = f.readlines()
    for line in lines :
      bytes =  np.array(handleByteLine(line))
      allBytes = np.concatenate((allBytes, bytes[2:len(bytes) - 1]))
  return allBytes

def formatStr(content: str) -> str:
  return "-" * 10 + f"\n{content}\n" + "-" * 10

def handleByteLine(line : str) -> list[str]:
  return line.split(" ")

def hexadecimal2int(val: str) -> int:
  return int(val, 16)

def hexStr2str(hex: str) -> str:
  hex.encode("utf-8")
  return binascii.unhexlify(hex).decode("utf-8")


strTypeMap = {
  1 : "Utf8",
  3 : "Int",
  4 : "Float",
  5 : "Long",
  6 : "JDouble",
  7 : "Class",
  8 : "String",
  9 : "Fieldref",
  10 : "Methodref",
  11 : "InterfaceMethodref",
  12 : "NameAndType",
  15 : "MethodHandle",
  16 : "MethodType",
  17 : "Dynamic",
  18 : "InvokeDynamic",
  19 : "Module",
  20 : "Package"
}

def array2string(arr, split = " ") -> str:
  def combine(a, b):
    return f"{a}{split}{b}"
  return functools.reduce(combine, arr)

class JavaConstantType:
  def __init__(self, flag: str) -> None:
    self.flag = int(flag, 16)
  
  def handle(self, bytesArr: list[str]) -> int:
    return -1

  def __str__(self) -> str:
    return strTypeMap[self.flag]
  
class Utf8(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("1")
    self.length = []
    self.bytes = []
  
  def handle(self, bytesArr: list[str]) -> int:
    tag = bytesArr[0]
    self.length = bytesArr[1:3]
    strlen = int(bytesArr[1] + bytesArr[2], 16)
    self.bytes = np.array(bytesArr)[3:(strlen + 3)]
    return strlen + 3
  
  def __str__(self) -> str:
    string  = super().__str__() 
    string += f" len ({int(self.length[0] + self.length[1], 16):2}) {array2string(self.length)}"
    string += f" bytes {array2string(self.bytes)} "
    string += f" {hexStr2str(array2string(self.bytes, ''))}"
    return string
  
class JInt(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("3")
    self.bytes = []

  def handle(self, bytesArr: list[str]):
    self.bytes = np.array(bytesArr)[1:5]
    return 5

  def __str__(self) -> str:
    return super().__str__() + f" val {hexadecimal2int(array2string(self.bytes,''))}"

class JFloat(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("4")
    self.bytes = []

  def handle(self, bytesArr: list[str]) -> int:
    self.bytes = np.array(bytesArr)[1:5]
    return 5

  def __str__(self) -> str:
    return super().__str__() + f" val {hexadecimal2int(array2string(self.bytes,''))}"

class JLong(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("5")
    self.bytes = []
  
  def handle(self, bytesArr: list[str]) -> int:
    self.bytes = np.array(bytesArr)[1:9]
    return 9

  def __str__(self) -> str:
    return super().__str__() + f" val {hexadecimal2int(array2string(self.bytes,''))}"

class JDouble(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("6")
    self.bytes = []
  
  def handle(self, bytesArr: list[str]) -> int:
    self.bytes = np.array(bytesArr)[1:9]
    return 9

  def __str__(self) -> str:
    return super().__str__() + f" val {hexadecimal2int(array2string(self.bytes,''))}"

class JClass(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("7")
    self.index = []
  
  def handle(self, bytesArr: list[str]) -> int:
    self.index = np.array(bytesArr)[1:3]
    return 3
  
  def __str__(self) -> str:
    return super().__str__() + f" index #{hexadecimal2int(array2string(self.index, ''))}"

class JString(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("8")
    self.index = []

  def handle(self, bytesArr: list[str]) -> int:
    self.index = np.array(bytesArr)[1:3]
    return 3
  def __str__(self) -> str:
    return super().__str__() + f" index #{hexadecimal2int(array2string(self.index, ''))}"

class Fieldref(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("9")
    self.classIndex = []
    self.nameIndex = []

  def handle(self, bytesArr: list[str]) -> int:
    nbArr = np.array(bytesArr)
    self.classIndex = nbArr[1:3]
    self.nameIndex = nbArr[3:5]
    return 5

  def __str__(self) -> str:
    return super().__str__() + f" class-index #{hexadecimal2int(array2string(self.classIndex, ''))}" + f" name-index #{hexadecimal2int(array2string(self.nameIndex, ''))}"

class Methodref(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("10")
    self.classIndex = []
    self.nameIndex = []

  def handle(self, bytesArr: list[str]) -> int:
    nbArr = np.array(bytesArr)
    self.classIndex = nbArr[1:3]
    self.nameIndex = nbArr[3:5]
    return 5

  def __str__(self) -> str:
    return super().__str__() + f" class-index #{hexadecimal2int(array2string(self.classIndex, ''))}" + f" name-index #{hexadecimal2int(array2string(self.nameIndex, ''))}"

class InterfaceMethodref(JavaConstantType): 
  def __init__(self) -> None:
    super().__init__("11")
    self.classIndex = []
    self.nameIndex = []

  def handle(self, bytesArr: list[str]) -> int:
    nbArr = np.array(bytesArr)
    self.classIndex = nbArr[1:3]
    self.nameIndex = nbArr[3:5]
    return 5

  def __str__(self) -> str:
    return super().__str__() + f" class-index #{hexadecimal2int(array2string(self.classIndex, ''))}" + f" name-index #{hexadecimal2int(array2string(self.nameIndex, ''))}"

class NameAndType(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("c")
    self.classIndex = []
    self.nameIndex = []

  def handle(self, bytesArr: list[str]) -> int:
    nbArr = np.array(bytesArr)
    self.classIndex = nbArr[1:3]
    self.nameIndex = nbArr[3:5]
    return 5

  def __str__(self) -> str:
    return super().__str__() + f" name-index #{hexadecimal2int(array2string(self.classIndex, ''))}" + f" const-index #{hexadecimal2int(array2string(self.nameIndex, ''))}"

class MethodHandle(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("e")
    self.reference_kind = []
    self.reference_index = []

  def handle(self, bytesArr: list[str]) -> int:
    nbArr = np.array(bytesArr)
    self.reference_kind = nbArr[1:2]
    self.reference_index = nbArr[2:4]
    return 4
  def __str__(self) -> str:
    return super().__str__() + f" kind {hexadecimal2int(array2string(self.reference_kind, ''))}" + f" index #{hexadecimal2int(array2string(self.reference_index, ''))}"

class JMethodType(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("10")
    self.descriptor_index = []
  
  def handle(self, bytesArr: list[str]) -> int:
    self.descriptor_index = np.array(bytesArr)[1:3]
    return 3

  def __str__(self) -> str:
    return super().__str__() + f" index #{hexadecimal2int(array2string(self.descriptor_index, ''))}"
  
class Dynamic(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("11")
    self.bootstrap_method_attr_index = []
    self.name_and_type_index = []

  def handle(self, bytesArr: list[str]) -> int:
    nbArr = np.array(bytesArr)
    self.bootstrap_method_attr_index = nbArr[1:3]
    self.name_and_type_index = nbArr[3:5]
    return 5

class JInvokeDynamic(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("12")
    self.bootstrap_method_attr_index = []
    self.name_and_type_index = []

  def handle(self, bytesArr: list[str]) -> int:
    nbArr = np.array(bytesArr)
    self.bootstrap_method_attr_index = nbArr[1:3]
    self.name_and_type_index = nbArr[3:5]
    return 5

class JModule(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("13")
    self.name_index = []

  def handle(self, bytesArr: list[str]) -> int:
    self.name_index = np.array(bytesArr)[1:3]
    return 3

class JPackage(JavaConstantType):
  def __init__(self) -> None:
    super().__init__("14")
    self.name_index = []

  def handle(self, bytesArr: list[str]) -> int:
    self.name_index = np.array(bytesArr)[1:3]
    return 3

typeMap = {
  1 : Utf8,
  3 : JInt,
  4 : JFloat,
  5 : JLong,
  6 : JDouble,
  7 : JClass,
  8 : JString,
  9 : Fieldref,
  10 : Methodref,
  11 : InterfaceMethodref,
  12 : NameAndType,
  15 : MethodHandle,
  16 : JMethodType,
  17 : Dynamic,
  18 : JInvokeDynamic,
  19 : JModule,
  20 : JPackage
}

def getType(tag : str) -> JavaConstantType:
  return typeMap[int(tag, 16)]

def handleIt(bytes: list[str]):
  store = []
  # remove cafe babe && version 
  for i in range(0,8):
    # print(f"remove {i} {bytes}")
    del bytes[0]
  # size const pool
  size = int(bytes[0] + bytes[1], 16) - 1
  print(f"total size is {size}")
  del bytes[0]
  del bytes[0]
  for i in range(0, size):
    byteType = getType(bytes[0])
    java_type = byteType()
    blen = java_type.handle(bytes)
    store.append(java_type)
    for i in range(0, blen):
      del bytes[0]
  flags = JClsFlags(np.array(bytes)[0:2])
  return JClsFile(store, flags)
  print(flags)

ACC_PUBLIC = 0x0001
ACC_FINAl  = 0x0010
ACC_SUPER  = 0x0020
ACC_INTERFACE = 0x0200
ACC_ABSTRACT = 0x0400
ACC_SYNTHETIC = 0x1000
ACC_ANNOTATION = 0x2000
ACC_ENUM = 0x4000
ACC_MODULE = 0x8000

flagRules = [
  {"label": "public", "val": ACC_PUBLIC},
  {"label": "final", "val": ACC_FINAl},
  {"label": "-", "val": ACC_SUPER},
  {"label": "interface", "val": ACC_INTERFACE},
  {"label": "abstract", "val": ACC_ABSTRACT},
  {"label": "synthetic", "val": ACC_SYNTHETIC},
  {"label": "annotation", "val": ACC_ANNOTATION},
  {"label": "enum", "val": ACC_ENUM},
  {"label": "MODULE", "val": ACC_MODULE},
]

class JClsFlags:
  def __init__(self, bytes: list) -> None:
    self.source = bytes

  def isFlag(flags: int, flag: int):
    return flags & flag == flag
  
  def getFlag(flags: int):
    flagsStr = []
    for flag in flagRules:
      if JClsFlags.isFlag(flags, flag['val']):
        flagsStr.append(flag['label'])
    return array2string(flagsStr)
  
  def __str__(self) -> None:
    return JClsFlags.getFlag(hexadecimal2int(array2string(self.source,'')))


class JClsThisAndSuper: 
  def __init__(self, bytes) -> None:
    self.source = bytes

  def handle(source: list):
    size = 4
    interfaceSize = hexadecimal2int(bytes[4])
    size += 2 + interfaceSize * 2
    return (JClsThisAndSuper(np.array(bytes)[0:size]))


class JClsFile: 
  def __init__(self, cp = [], aflgs = None ) -> None:
    self.const_pool = cp
    self.access_flags = aflgs
  
  def __str__(self) -> str:
    ans = ""
    for i in range(0, len(self.const_pool)):
      ans += f"#{(i + 1):04} {self.const_pool[i]}\n"
    ans += f"{self.access_flags}\n"
    return ans


if __name__ == "__main__":
  # print(read("ACClazz.bn"))
  # print(getType("01"))
  bs = list(read("resources/ACClazz.bn"))
  st = []
  jf = handleIt(bs)
  print(jf)



# // size (00 1f) 31 

# 0a : 10 Methodref ( u1 u2 u2 )  tag index   index 0a 00 02 00 03
# 07 :  7 Class     ( u1 u2    )  tag index         07 00 04
# 0c : 12 NameAndTy ( u1 u2 u2 )  tag index   index 0c 00 05 00 06 
# 01 :  1 Utf8      ( u1 u2 u1 )  tag length  bytes 01 00 10 | 6a 61 76 61 | 2f 6c 61 6e | 67 2f 4f 62 | 6a 65 64 74   // 16 
