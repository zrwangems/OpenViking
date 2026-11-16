---
type: simulink-block
title: 'Hadamard Code Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Sources and Sinks / Sources'
documentation_page: 'hadamardcodegenerator'
documentation_source_path: 'ref/hadamardcodegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Hadamard Code Generator

## 端口

R2025b 中未提供文档。

## 参数

**码长**
:   一个正整数，且必须为 2 的幂，用于指定 Hadamard 码的长度。

**码索引**
:   一个介于 0 和 *N*-1 之间的整数，其中 *N* 为**码长**，用于指定
    Hadamard 矩阵的一行。

**采样时间**
:   正标量以 seconds 为单位指定输出信号各采样点之间的时间。如果将采样时间设置为 `-1`，则输出
    信号从下游继承采样时间。有关
    **采样时间**与**每帧采样数**参数之间关系的信息，
    请参阅“采样时序”。

**每帧采样数**
:   每帧的采样数，指定为正整数，表示输出数据单个通道中每帧的采样数。有关
    **采样时间**与**每帧采样数**之间关系的信息，请参阅“采样时序”。

**输出数据类型**
:   模块的输出类型可以指定为
    `int8` 或 `double`。默认情况下，
    模块将其设置为 `double`。

**仿真方式**
:   选择仿真模式。

    `Code generation`
    :   在首次运行模型时，进行仿真并生成代码。如果
        模块的结构未发生变化，则后续运行模型时不会重新生成代码。

        如果仿真模式为 `Code generation`，则与模块对应的
        System 对象最多接受九个输入。

    `Interpreted execution`
    :   在不生成代码的情况下对模型进行仿真。此选项可实现
        更快的启动速度，但可能会降低后续仿真的性能。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

### R2020a：现有模型会自动将此模块更新为当前版本

从 R2020a 开始，Simulink® 不再允许您使用 R2015b 之前提供的 Hadamard Code Generator 模块版本。

现有模型会自动更新，以加载在“源模块输出连续时间采样的帧，但不使用帧属性”中公布的 Hadamard Code Generator 模块版本。有关模块转发的详细信息，请参阅“使用转发表保持库模块的兼容性 (Simulink)”。

## 描述

从正交码集中生成 Hadamard 码

Hadamard Code Generator 模块根据 Hadamard 矩阵生成 Hadamard 码，该矩阵的各行构成一组正交码。在接收机与发射机完全同步的通信系统中，正交码可用于扩频。在这类系统中，由于码完全去相关，解扩操作是理想的。

Hadamard 码是 Hadamard 矩阵的各行。Hadamard 矩阵是方阵，其元素为 +1 或 -1，且各行之间和各列之间均相互正交。如果 *N* 是 2 的非负次幂，则 *N*×*N* Hadamard 矩阵（记为 *H*N）的递归定义如下。

H1=[1]H2N=[HNHNHN−HN]

*N*×*N* Hadamard 矩阵具有以下性质：

*H*N*H*NT
= *N**I*N

其中，*I*N 是 *N*×*N* 单位矩阵。

Hadamard Code Generator 模块输出 *H*N 的一行。输出为双极性信号。通过**码长**参数指定码长 *N*。**码长**必须是 2 的幂。通过**码索引**参数指定 Hadamard 矩阵的行索引，该索引是范围 [0, 1, ... , *N*-1] 内的整数。
