---
type: simulink-block
title: 'General CRC Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / CRC'
documentation_page: 'generalcrcgenerator'
documentation_source_path: 'ref/generalcrcgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# General CRC Generator

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 二进制列向量
  direction: input
  data_types: double | Boolean
- name: Out
  summary: 输出码字帧 二进制列向量
  direction: output
```

### 输入

### **In** — 输入信号 二进制列向量

输入信号，指定为二进制列向量。输入帧的长度必须是 **Checksums per frame** 参数值的倍数。

**数据类型：** `double` | `Boolean`
### 输出

### **Out** — 输出码字帧 二进制列向量

输出码字帧，返回为继承输入信号数据类型的二进制列向量。输出包含附加了 CRC 比特序列的输入数据帧。

输出帧的长度为 *m* +
*k* \* *r*，其中
*m* 是输入帧的大小，
*k* 是每帧的校验和数量，
*r* 是生成多项式的阶数。
## 参数
```yaml
parameters:
- name: Generator polynomial
  summary: 生成多项式 'z^16 + z^12 + z^5 + 1'（默认）| 多项式字符向量 | 二进制行向量 | 整数行向量
  group: ''
- name: Initial states
  summary: 内部移位寄存器的初始状态 0（默认）| 1 | 二进制行向量
  group: ''
- name: Direct method
  summary: 使用直接算法进行 CRC 校验和计算 off（默认）| on
  group: ''
- name: Reflect input bytes
  summary: 反射输入字节 off（默认）| on
  group: ''
- name: Reflect checksums before final XOR
  summary: 在最终 XOR 之前反射校验和 off（默认）| on
  group: ''
- name: Final XOR
  summary: 最终 XOR 0（默认）| 1 | 二进制行向量
  group: ''
- name: Checksums per frame
  summary: 每帧计算的校验和数量 1（默认）| 正整数
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Generator polynomial** — 生成多项式 `'z^16 + z^12 + z^5 + 1'`（默认）| 多项式字符向量 | 二进制行向量 | 整数行向量

用于 CRC 算法的生成多项式，指定为以下之一：

- 多项式字符向量，例如 `'z^3 + z^2 +
  1'`。
- 二进制行向量，按降幂顺序表示生成多项式的系数。该向量的长度为 (*N*+1)，其中 *N* 是生成多项式的阶数。例如，`[1
  1 0 1]` 表示多项式
  *x*3+
  *z*2+ 1。
- 整数行向量，按降序包含多项式中非零项的
  *z* 的指数。例如，`[3 2 0]` 表示
  多项式 *z*3 +
  *z*2 + 1。

有关详细信息，请参阅 Representation of Polynomials in Communications Toolbox。

默认值为 CRC-16-CCITT 生成多项式。
下表列出了一些常用的生成多项式。

| CRC 名称 | 生成多项式 |
| --- | --- |
| CRC-32 | `'z^32 + z^26 + z^23 + z^22 + z^16 + z^12 + z^11 + z^10 + z^8 + z^7 + z^5 + z^4 + z^2 + z + 1'` |
| CRC-24 | `'z^24 + z^23 + z^14 + z^12 + z^8 + 1'` |
| CRC-16 | `'z^16 + z^15 + z^2 + 1'` |
| CRC-16-CCITT | `'z^16 + z^12 + z^5 + 1'` |
| Reversed CRC-16 | `'z^16 + z^14 + z + 1'` |
| CRC-8 | `'z^8 + z^7 + z^6 + z^4 + z^2 + 1'` |
| CRC-4 | `'z^4 + z^3 + z^2 + z + 1'` |

**示例：** `'z^7 + z^2 + 1'`、`[1 0 0 0 0 1 0
1]` 和 `[7 2 0]` 表示相同的
多项式，*p*(*z*) =
*z*
7 + *z*
2 + 1。

### **Initial states** — 内部移位寄存器的初始状态 `0`（默认）| `1` | 二进制行向量

内部移位寄存器的初始状态，指定为二进制标量或长度等于生成多项式阶数的二进制行向量。标量值将扩展为长度等于生成多项式阶数的行向量。

### **Direct method** — 使用直接算法进行 CRC 校验和计算 `off`（默认）| `on`

选择以使用直接算法进行 CRC 校验和计算。清除时，模块使用非直接算法进行 CRC 校验和计算。

有关直接和非直接算法的详细信息，请参阅 Error Detection and Correction。

### **Reflect input bytes** — 反射输入字节 `off`（默认）| `on`

选择以在将数据输入移位寄存器之前按字节翻转输入数据。当选择 **Reflect input bytes** 时，输入帧长度除以 **Checksums per frame** 参数的值必须是整数且为 `8` 的倍数。当清除 **Reflect input
bytes** 时，模块不翻转输入数据。

### **Reflect checksums before final XOR** — 在最终 XOR 之前反射校验和 `off`（默认）| `on`

选择以在输入数据完全通过移位寄存器后围绕其中心翻转 CRC 校验和。当清除 **Reflect checksums
before final XOR** 时，模块不翻转 CRC 校验和。

### **Final XOR** — 最终 XOR `0`（默认）| `1` | 二进制行向量

最终 XOR，指定为二进制标量或长度等于生成多项式阶数的二进制行向量。XOR 操作在将 CRC 附加到输入数据之前，使用 **Final XOR** 参数的值对 CRC 校验和执行。标量值将扩展为长度等于生成多项式阶数的行向量。设置为 `0` 等同于不执行 XOR 操作。

### **Checksums per frame** — 每帧计算的校验和数量 `1`（默认）| 正整数

每帧计算的校验和数量，指定为正整数。
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

**在 R2006a 之前推出**

## 描述

根据生成多项式生成 CRC 码比特并附加到输入数据帧

General CRC Generator 模块为每个输入数据帧生成循环冗余校验（CRC）码比特，并将它们附加到帧。有关详细信息，请参阅 CRC Generator Operation。
