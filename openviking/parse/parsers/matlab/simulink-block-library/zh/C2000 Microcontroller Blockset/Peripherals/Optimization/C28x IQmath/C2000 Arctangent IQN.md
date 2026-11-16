---
type: simulink-block
title: 'C2000 Arctangent IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x IQmath'
documentation_page: 'c2000arctangentiqn'
documentation_source_path: 'ref/c2000arctangentiqn.html'
language: zh-CN
chinese_source: official
---

# C2000 Arctangent IQN

## 端口

R2025b 官方文档未提供。

## 参数

**函数**
:   要计算的反正切类型：

    - **atan2** - 计算四象限反正切值，输出以弧度表示，取值范围为 -pi 到 +pi。
    - **atan2PU** - 计算单位四象限反正切值。如果 `atan2(B,A)` 大于或等于 0，则 `atan2PU(B,A) = atan2(B,A)/2*pi`。否则，`atan2PU(B,A) = atan2(B,A)/2*pi+1`。输出结果以单位弧度表示，取值范围从 0 到 2π 弧度。

**注意**

Arctangent IQN 模块的输入顺序符合 Texas Instruments 约定，参量'A' 在顶部，'B' 在底部。

**函数**
:   要计算的反正切类型：

    - **atan2** - 计算四象限反正切值，输出以弧度表示，取值范围为 -pi 到 +pi。
    - **atan2PU** - 计算单位四象限反正切值。如果 `atan2(B,A)` 大于或等于 0，则 `atan2PU(B,A) = atan2(B,A)/2*pi`。否则，`atan2PU(B,A) = atan2(B,A)/2*pi+1`。输出结果以单位弧度表示，取值范围从 0 到 2π 弧度。

**注意**

Arctangent IQN 模块的输入顺序符合 Texas Instruments 约定，参量'A' 在顶部，'B' 在底部。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

四象限反正切

本页采用了机器翻译。点击此处可查看英文原文。

# C2000 Arctangent IQN

四象限反正切

反正切 IQN 模块计算 IQ 数输入的四象限反正切值，并生成 IQ 数输出。

**注意**

该模块的实现过程中，在代码生成期间不会调用相应的 Texas Instruments® 库函数。Texas Instruments 函数使用全局 Q 设置，而该模块使用的 MathWorks® 代码根据模块输入动态调整 Q 格式。有关更多信息，请参阅Using the IQmath Library。

- C2000 Arctangent IQN block

##
