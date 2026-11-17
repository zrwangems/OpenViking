---
type: simulink-block
title: 'Hadamard Code Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Sequence Generators'
documentation_page: 'hadamardcodegenerator'
documentation_source_path: 'ref/hadamardcodegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Hadamard Code Generator

## 端口

R2025b 中未记录。

## 参数

**Code length**
:   一个为 2 的幂的正整数，用于指定 Hadamard 码的长度。

**Code index**
:   一个介于 0 和 *N*-1 之间的整数，其中
    *N* 是 **Code length**，用于指定
    Hadamard 矩阵的一行。

**Sample time**
:   正标量，用于指定输出信号每个采样点之间的时间（以秒为单位）。如果将采样时间设置为 `-1`，则输出
    信号将从下游继承采样时间。有关
    **Sample time** 与 **Samples per frame** 参数之间关系的信息，
    请参见
    Sample Timing。

**Samples per frame**
:   每帧采样数，指定为一个正整数，表示输出数据一个通道中每帧的采样点数。有关
    **Sample time** 与
    **Samples per frame** 之间关系的信息，请参见 Sample Timing。

**输出数据类型**
:   该模块的输出类型可以指定为
    `int8` 或 `double`。默认情况下，
    该模块将其设置为 `double`。

**Simulate using**
:   选择仿真模式。

    `Code generation`
    :   在首次模型运行时，进行仿真并生成代码。如果
        模块的结构不发生变化，则后续模型运行不会重新生成代码。

        如果仿真模式为 `Code
        generation`，则与
        这些模块对应的 System object 最多接受九个输入。

    `Interpreted execution`
    :   在不生成代码的情况下对模型进行仿真。此选项会带来
        更快的启动时间，但可能会减慢后续仿真
        性能。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2020a：现有模型会自动将此模块更新到当前版本

从 R2020a 开始，Simulink® 不再允许您使用 R2015b 之前可用的 Hadamard Code Generator 模块版本。

现有模型会自动更新，以加载在 Source blocks output frames of contiguous time samples but do not use frame attribute 中宣布的 Hadamard Code Generator 模块版本。有关模块转发的更多信息，请参见 Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink)。

## 描述

从正交码集合生成 Hadamard 码

Hadamard Code Generator 模块从 Hadamard 矩阵生成 Hadamard 码，
该矩阵的各行构成一个正交码集合。正交码可用于
接收机与发射机完全同步的通信系统中的扩频。
在这些系统中，解扩操作是理想的，因为这些码完全去相关。

Hadamard 码是 Hadamard 矩阵的各行。Hadamard 矩阵是
元素为 +1 或 -1 的方阵，并且其各行和各列彼此
正交。如果 *N* 是 2 的非负次幂，
则 *N*×*N* Hadamard 矩阵记作
*H*N，其递归定义如下。

H1=[1]H2N=[HNHNHN−HN]

N×N Hadamard 矩阵具有以下性质

*H*N*H*NT
= *N**I*N

其中 *I*N 是
*N*×*N* 单位矩阵。

Hadamard Code Generator 模块输出
*H*N 的一行。输出为双极性。您可以通过 **Code length**
参数指定码的长度 *N*。**Code length** 必须是 2 的幂。您可以通过
**Code index** 参数指定 Hadamard 矩阵行的索引，该索引是范围 [0, 1, ... ,
*N*-1] 内的整数。
