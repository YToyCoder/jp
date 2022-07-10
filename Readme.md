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