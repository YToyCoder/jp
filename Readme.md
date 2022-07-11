## jp

this is a simple java class file tool

#### support function

receive a string of java class file content && get the constant pool information

example:

"ca fe ba be 00 00 00 3d 00 1f 0a ..." 

    || 
    \/

total size is 30

#0001 MethodType class-index #2 name-index #3

#0002 Class index #4

#0003 NameAndType name-index #5 const-index #6

#0004 Utf8 len (16) 00 10 bytes 6a 61 76 61 2f 6c 61 6e 67 2f 4f 62 6a 65 63 74  java/lang/Object

#0005 Utf8 len ( 6) 00 06 bytes 3c 69 6e 69 74 3e  <init>

#0006 Utf8 len ( 3) 00 03 bytes 28 29 56  ()V

#0007 Class index #8

#0008 Utf8 len ( 7) 00 07 bytes 41 43 43 6c 61 7a 7a  ACClazz

#0009 Utf8 len ( 5) 00 05 bytes 66 69 65 6c 64  field


#### java class file

Java .class 文件格式

Java .class文件是一个二进制文件，该文件的最小单元是1个字节(1 byte).

Java的class文件的前4个字节是一个魔数，该值是一个不变的数，主要是用于标识该文件是一个java class文件。该值用16进制表示是`cafebabe`。

在魔数后面是Java class文件的版本号，总共4个字节，前2个字节是次版本号，后2个字节是主版本号。

版本号之后是常量池，常量池的前两个字节是常量池的大小。常量池是从1开始计数的，所以常量池的常量的数量是该值减1。
