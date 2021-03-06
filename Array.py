"""
基于数组的序列
    在计算机的内存中，为了能跟踪信息存储在哪个字节，计算机抽象了一个概念：存储地址
    每个存储字节都与唯一一个存储地址相关联
    一组相关变量能够一个接一个地存储在计算机存储器的一块连续区域内，这样的表示法称为数组
    数组的每个单元必须占据相同数量的字节,目的是为了能够按常量时间访问数组中的任意元素
    
引用数组：
    在Python中，想存储不同长度的字符串时，会使用到列表来存储，这似乎违背了数组的定义（每个单元必须占据相同字节）
    因此在list中存储的实际上是对象的内存地址
Python中的紧凑数组：
    在数组底层存储的直接是数据，而不是对象的引用，这样做会占据更少的内存。
    在python中靠array模块提供支撑，该模块提供了一个类array
动态数组和摊销
    在计算机底层，创建低层次数组的时候，必须声明数组的大小，以便系统分配连续的内存，并且不允许长度超过声明的值
    但在Python的list类中，则可以对列表进行增加元素。----动态数组
    list类创建时，系统会在底层分配一个更大的数组，当list中的数据占满数组时，系统会重新分配一块更大数组，并使得前部分相同
    


"""