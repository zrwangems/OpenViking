---
type: simulink-block
title: 'General CRC Syndrome Detector'
family: 'error-detection-and-correction'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / CRC'
documentation_page: 'generalcrcsyndromedetector'
documentation_source_path: 'ref/generalcrcsyndromedetector.html'
language: zh-CN
chinese_source: worker-translation
---

# General CRC Syndrome Detector

## 端口

### 输入

### **In** — 接收到的码字二进制列向量

接收到的码字，指定为二进制列向量。

**数据类型：** `double` | `Boolean`

### 输出

### **Out** — 输出帧二进制列向量

输出帧，返回为继承输入信号数据类型的二进制列向量。输出帧包含移除了校验和的接收码字。

输出帧的长度为 *n* - *k* \* *r* 位，其中 *n* 是接收码字的大小，*k* 是每帧的校验和数量，*r* 是生成多项式的次数。

### **Err** — 校验和错误信号二进制列向量

校验和错误信号，返回为继承输入信号数据类型的二进制列向量。`Err` 的长度等于 **每帧校验和数** 的值。对于每次校验和计算，`Err` 中元素值 0 表示无校验和错误，`Err` 中元素值 1 表示校验和错误。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **生成多项式** — 生成多项式 `'z^16 + z^12 + z^5 + 1'`（默认）| 多项式字符向量 | 二进制行向量 | 整数行向量

CRC 算法的生成多项式，指定为以下项之一：

- 多项式字符向量，例如 `'z^3 + z^2 + 1'`。
- 二进制行向量，按降幂顺序表示生成多项式的系数。此向量的长度为 (*N*+1)，其中 *N* 是生成多项式的次数。例如，`[1 1 0 1]` 表示多项式 *x*3+ *z*2+ 1。
- 整数行向量，按降序包含多项式中非零项的 *z* 的指数。例如，`[3 2 0]` 表示多项式 *z*3 + *z*2 + 1。

有关详细信息，请参阅 Communications Toolbox 中的多项式表示。

默认值是 CRC-16-CCITT 生成多项式。此表列出了一些常用的生成多项式。

| CRC 名称 | 生成多项式 |
| --- | --- |
| CRC-32 | `'z^32 + z^26 + z^23 + z^22 + z^16 + z^12 + z^11 + z^10 + z^8 + z^7 + z^5 + z^4 + z^2 + z + 1'` |
| CRC-24 | `'z^24 + z^23 + z^14 + z^12 + z^8 + 1'` |
| CRC-16 | `'z^16 + z^15 + z^2 + 1'` |
| CRC-16-CCITT | `'z^16 + z^12 + z^5 + 1'` |
| Reversed CRC-16 | `'z^16 + z^14 + z + 1'` |
| CRC-8 | `'z^8 + z^7 + z^6 + z^4 + z^2 + 1'` |
| CRC-4 | `'z^4 + z^3 + z^2 + z + 1'` |

**示例：** `'z^7 + z^2 + 1'`、`[1 0 0 0 0 1 0 1]` 和 `[7 2 0]` 表示同一个多项式，*p*(*z*) = *z*7 + *z*2 + 1。

### **初始状态** — 内部移位寄存器的初始状态 `0`（默认）| `1` | 二进制行向量

内部移位寄存器的初始状态，指定为二进制标量或长度等于生成多项式次数的二进制行向量。标量值会扩展为长度等于生成多项式次数的行向量。

### **直接法** — 使用直接算法进行 CRC 校验和计算 `off`（默认）| `on`

选中此选项可使用直接算法进行 CRC 校验和计算。清除时，模块使用非直接算法进行 CRC 校验和计算。

有关直接和非直接算法的详细信息，请参阅错误检测和纠正。

### **反转输入字节** — 反转输入字节 `off`（默认）| `on`

选中此选项可在将数据输入移位寄存器之前按字节翻转接收到的码字。选中 **反转输入字节** 时，接收到的码字长度除以 **每帧校验和数** 参数的值必须是整数且为 `8` 的倍数。清除 **反转输入字节** 时，模块不翻转输入数据。

### **最终 XOR 前反转校验和** — 最终 XOR 前反转校验和 `off`（默认）| `on`

选中 **最终 XOR 前反转校验和** 可在输入数据完全通过移位寄存器后，围绕其中心翻转 CRC 校验和。清除 **最终 XOR 前反转校验和** 时，模块不翻转 CRC 校验和。

### **最终 XOR** — 最终 XOR `0`（默认）| `1` | 二进制行向量

最终 XOR，指定为二进制标量或长度等于生成多项式次数的二进制行向量。XOR 运算使用 **最终 XOR** 参数的值和 CRC 校验和，然后与输入校验和进行比较。标量值会扩展为长度等于生成多项式次数的行向量。设置为 `0` 等效于不进行 XOR 运算。

### **每帧校验和数** — 为每帧计算的校验和数量 `1`（默认）| 正整数

为每帧计算的校验和数量，指定为正整数。

## 所属库

Communications Toolbox / Error Detection and Correction / CRC

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

根据生成多项式检测接收到的码字帧中的错误

General CRC Syndrome Detector 模块为接收到的码字帧计算循环冗余校验 (CRC) 校验和。为了在通信系统链路中成功进行 CRC 检测，必须将 General CRC Syndrome Detector 模块的参数设置与配对的 General CRC Generator 模块对齐。

有关详细信息，请参阅 CRC Syndrome Detector Operation。
