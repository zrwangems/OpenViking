---
type: simulink-block
title: 'M-DPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'mdpskdemodulatorbaseband'
documentation_source_path: 'ref/mdpskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-DPSK Demodulator Baseband

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 DPSK 调制数据

M-DPSK Demodulator Baseband 模块解调使用 M 进制差分相移键控方法调制的信号。输入是调制信号的基带表示。该模块的输入和输出均为离散时间信号。该模块接受标量值或列向量输入信号。有关每个模块端口支持的数据类型的信息，请参阅本页的“支持的数据类型”表。

**M-ary number** 参数 M 是可以紧跟在给定输出符号之后的可能输出符号的数量。该模块将当前符号与前一个符号进行比较。该模块的第一个输出是零的初始条件（如果 **Output type** 参数设置为 `Bit`，则为一组零），因为不存在前一个符号。

### 整数值信号和二值信号

如果将 **Output type** 参数设置为 `Integer`，则该模块将相位差

θ + 2πk/M

解调为 *k*，其中 θ 表示 **Phase rotation** 参数，*k* 表示 `0` 到 *M*-1 之间的整数。

当将 **Output type** 参数设置为 `Bit` 时，该模块输出表示整数的二值信号。该模块使用一组 *K* = log2(*M*) 位来表示每个整数，其中 *K* 表示每个符号的位数。输出向量长度必须是 *K* 的整数倍。

在二进制输出模式下，符号可以是二进制解映射或格雷解映射。**Constellation ordering** 参数指示该模块如何将整数映射到对应的 *K* 个输出位组。有关详细信息，请参阅 M-DPSK Modulator Baseband 和 M-PSK Modulator Baseband 模块的参考页。
