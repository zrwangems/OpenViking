---
type: simulink-block
title: 'General QAM Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PAM/QAM'
documentation_page: 'generalqammodulatorbaseband'
documentation_source_path: 'ref/generalqammodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# General QAM Modulator Baseband

## 端口

R2025b 中未记录。

## 参数

**Signal constellation**
:   列出星座点的实数或复数向量。

**View Constellation**
:   在模块掩码上点击 **View
    Constellation**，以可视化指定模块参数的信号星座。在查看星座之前，请先应用参数设置。有关更多信息，请参阅 View Constellation of Modulator Block。

**输出数据类型**
:   输出数据类型，指定为 `double`、
    `single`、
    `fixdt(1,16)`、
    `fixdt(1,16,0)`、`Inherit via back
    propagation` 或 `<data type
    expression>`。

    将此参数设置为

    - `fixdt(1,16)`、
      `fixdt(1,16,0)` 或
      `<data type expression>` 会启用相应参数，您可以在其中进一步指定详细信息。
    - `Inherit via back propagation` 会将
      输出数据类型和定标设置为与后续模块匹配。

    有关指定数据类型的信息，请参阅 Data Type Assistant。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用正交幅度调制进行调制

General QAM Modulator Baseband 模块使用正交幅度调制进行调制。输出是已调制信号的基带表示。

**Signal constellation** 参数通过在一个长度为 *M* 的复数向量中列出星座点来定义星座。输入信号值必须是范围 [0, (*M*-1)] 内的整数。该模块将输入整数 m 映射到 **Signal
constellation** 向量中的第 (m+1) 个值。

该模块接受标量或列向量输入信号。有关每个模块端口支持的数据类型的信息，请参阅本页上的 Supported Data Types 表。
