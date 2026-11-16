---
type: simulink-block
title: 'Gyrator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'gyrator'
documentation_source_path: 'ref/gyrator.html'
language: zh-CN
chinese_source: worker-translation
---

# Gyrator

## 端口

该模块具有四个电气守恒端口。极性由 + 和 – 号指示。
标为 1+ 和 1– 的端口连接到初级绕组。标为 2+ 和 2– 的端口
连接到次级绕组。

## 参数

**回转电导**
:   回转电导常量 *G*。
    默认值为 `1`。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

电气系统中的理想回转器

可以使用回转器和电容器来实现电感器。
其主要优点是，可以使用物理尺寸小得多的电容器来创建
等效电感。在实践中，回转器由运算放大器和其他无源元件实现。

Gyrator 模块对无损耗的理想回转器进行建模，
其方程如下：

I1=G·V2

I2=G·V1

其中：

|  |  |
| --- | --- |
| *`V1`* | 输入电压 |
| *`V2`* | 输出电压 |
| *`I1`* | 流入输入 + 端子的电流 |
| *`I2`* | 流出输出 + 端子的电流 |
| *`G`* | 回转电导 |

连接到初级绕组和次级绕组的两个电气网络
必须各自具有自己的 Electrical Reference 模块。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用
模块对话框或属性检查器中的**初始目标**部分。
有关详细信息，请参阅“设置模块变量的优先级和初始目标”。

标称值提供了一种指定模型中变量预期量级的方法。
使用基于标称值的系统缩放可提高仿真的稳健性。标称
值可以来自不同来源，其中之一是模块对话框或属性检查器中的**标称
值**部分。有关详细信息，请参阅“修改模块变量的标称值”。
