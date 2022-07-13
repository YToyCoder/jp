package com.silence.jtool

trait JByte {
  def read(bs: Array[Byte])
  def tag() : String
}

object JByte extends Enumeration {
  val Utf8 = Value(1)
  val JInt = Value(3)
  val JFloat = Value(4)
  val JLong = Value(5)
  val JDouble = Value(6)
  val JClass = Value(7)
  val JString = Value(8)
  val JFieldref,
  JMethodref,
  JInterfaceMethodref,
  NameAndType,
  MethodHandle,
  MethodType,
  Dynamic,
  InvokeDynamic,
  JModule,
  JPackage= Value;
}
