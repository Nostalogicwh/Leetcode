# 题目
我们提供了一个类：

> public class Foo {  
   public void first() { print("first"); }  
   public void second() { print("second"); }  
   public void third() { print("third"); }  
 }

三个不同的线程将会共用一个 Foo 实例。  

- 线程 A 将会调用 first() 方法
- 线程 B 将会调用 second() 方法
- 线程 C 将会调用 third() 方法

请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。

# 解题思路
使用while确保执行顺序