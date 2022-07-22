## Varargs

Java可变参数是指那些定义在函数参数中，类型确定但是长度可变的参数.

这里是查看在字节码层面`Varargs`是如何实现和运行的。

先说结论 : 

*Java 最后将可变长度的参数封装成为一个数组。数组元素的类型就是可变长度参数的类型（即…之前的类型，在上面的例子中就是 int），数组的名称是参数名称（在上面的例子中是 nums）*

由于java的实现方式，因此会有如下限制:

  1. 变长参数位置如果被同等类型数组替代，不能构成重载，因为本质上是一个方法

同时还有如下限制:

  2. 变长参数必须是方法中的最后一个参数，避免无法区分变长参数和普通参数；
  3. 一个方法不能定义多个变长参数，避免参数错位；

下面从不同的角度去验证`限制1`

存在一个如下的java文件， 它存在一个可变长度参数的函数`varargsFn`，在调用时对于可变长度参数，可以不传参数调用，也可以传多个参数调用。

然后对其对应的字节码进行反汇编，可以看到该函数的描述符是`(I[Ljava/lang/String;)V`，该描述符说明这个函数是一个入参为`int`和`String[]`，返回类型是`void`的函数。对比`otherArrayFn`的类型可以发现两个函数的类型除了名称都是一样的。从这一点可以说明上面的结论是对的。

同时可以继续查看main函数的内容。可以发现在不对可变长度参数传值的时候会传入一个空数组。

**Java文件如下**

```java


public class Varargs {

  public static void main(String[] args) {
    varargsFn(0);
    varargsFn(1, "1");
    varargsFn(2, "1", "2");
  }

  public static void varargsFn(int i, String ...str){
  }

  public static void otherArrayFn(int i, String[] str){
  }
}

```

**反汇编结果如下**

```java
Classfile /D:/workspace/jtool/example/varargs/Varargs.class
  Last modified 2022��7��22��; size 495 bytes
  SHA-256 checksum 16ede68628e1354cc4a3b7f4957811d3ff6b5ac22734282fe1d2a4735a4c8647
  Compiled from "Varargs.java"
public class varargs.Varargs
  minor version: 0
  major version: 61
  flags: (0x0021) ACC_PUBLIC, ACC_SUPER
  this_class: #10                         // varargs/Varargs
  super_class: #2                         // java/lang/Object
  interfaces: 0, fields: 0, methods: 4, attributes: 1
Constant pool:
   #1 = Methodref          #2.#3          // java/lang/Object."<init>":()V
   #2 = Class              #4             // java/lang/Object
   #3 = NameAndType        #5:#6          // "<init>":()V
   #4 = Utf8               java/lang/Object
   #5 = Utf8               <init>
   #6 = Utf8               ()V
   #7 = Class              #8             // java/lang/String
   #8 = Utf8               java/lang/String
   #9 = Methodref          #10.#11        // varargs/Varargs.varargsFn:(I[Ljava/lang/String;)V
  #10 = Class              #12            // varargs/Varargs
  #11 = NameAndType        #13:#14        // varargsFn:(I[Ljava/lang/String;)V
  #12 = Utf8               varargs/Varargs
  #13 = Utf8               varargsFn
  #14 = Utf8               (I[Ljava/lang/String;)V
  #15 = String             #16            // 1
  #16 = Utf8               1
  #17 = String             #18            // 2
  #18 = Utf8               2
  #19 = Utf8               Code
  #20 = Utf8               LineNumberTable
  #21 = Utf8               main
  #22 = Utf8               ([Ljava/lang/String;)V
  #23 = Utf8               otherArrayFn
  #24 = Utf8               SourceFile
  #25 = Utf8               Varargs.java
{
  public varargs.Varargs();
    descriptor: ()V
    flags: (0x0001) ACC_PUBLIC
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 3: 0

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: (0x0009) ACC_PUBLIC, ACC_STATIC
    Code:
      stack=5, locals=1, args_size=1
         0: iconst_0
         1: iconst_0
         2: anewarray     #7                  // class java/lang/String
         5: invokestatic  #9                  // Method varargsFn:(I[Ljava/lang/String;)V
         8: iconst_1
         9: iconst_1
        10: anewarray     #7                  // class java/lang/String
        13: dup
        14: iconst_0
        15: ldc           #15                 // String 1
        17: aastore
        18: invokestatic  #9                  // Method varargsFn:(I[Ljava/lang/String;)V
        21: iconst_2
        22: iconst_2
        23: anewarray     #7                  // class java/lang/String
        26: dup
        27: iconst_0
        28: ldc           #15                 // String 1
        30: aastore
        31: dup
        32: iconst_1
        33: ldc           #17                 // String 2
        35: aastore
        36: invokestatic  #9                  // Method varargsFn:(I[Ljava/lang/String;)V
        39: return
      LineNumberTable:
        line 6: 0
        line 7: 8
        line 8: 21
        line 9: 39

  public static void varargsFn(int, java.lang.String...);
    descriptor: (I[Ljava/lang/String;)V
    flags: (0x0089) ACC_PUBLIC, ACC_STATIC, ACC_VARARGS
    Code:
      stack=0, locals=2, args_size=2
         0: return
      LineNumberTable:
        line 12: 0

  public static void otherArrayFn(int, java.lang.String[]);
    descriptor: (I[Ljava/lang/String;)V
    flags: (0x0009) ACC_PUBLIC, ACC_STATIC
    Code:
      stack=0, locals=2, args_size=2
         0: return
      LineNumberTable:
        line 15: 0
}
SourceFile: "Varargs.java"

```

修改`varargsFn`为如下:

```java

  public static void varargsFn(int i, String ...str){
    System.out.printf("i is %d , str length is %d\n", i, str.length);
  }

```
运行结果如下：

```java

i is 0 , str length is 0
i is 1 , str length is 1
i is 2 , str length is 2

```