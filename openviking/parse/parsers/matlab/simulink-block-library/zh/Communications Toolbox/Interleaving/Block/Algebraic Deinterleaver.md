---
type: simulink-block
title: 'Algebraic Deinterleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'algebraicdeinterleaver'
documentation_source_path: 'ref/algebraicdeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Algebraic Deinterleaver

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**类型**：该模块用于解交织的置换表类型。
    可选值为 `Takeshita-Costello` 和
    `Welch-Costas`。

**Number of elements**
:   输入向量中的元素数量 *N*。

**Multiplicative factor**
:   该模块用于计算对应交织器循环向量的因子。仅当将 **Type** 设置为
    `Takeshita-Costello` 时，此字段才会出现。

**Cyclic shift**
:   该模块在创建对应交织器的置换表时对索引进行移位的量。仅当将 **Type** 设置为
    `Takeshita-Costello` 时，此字段才会出现。

**Primitive element**
:   有限域 GF(N+1) 中阶为 *N* 的元素。仅当 **Type** 设置为
    `Welch-Costas` 时，此字段才会出现。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用代数推导的置换恢复输入符号的顺序

Algebraic Deinterleaver 模块恢复使用 Algebraic Interleaver 模块交织的序列的原始顺序。在典型用法中，两个模块中的参数具有相同的值。

**Number of elements** 参数 *N* 表示输入向量中有多少个数字。该模块接受列向量输入信号。

该模块接受以下数据类型：`int8`、
`uint8`、`int16`、`uint16`、
`int32`、`uint32`、`boolean`、
`single`、`double` 和定点。输出信号的数据类型继承自输入信号。

**Type** 参数表示该模块用于生成相应置换表的代数方法。可选值为
`Takeshita-Costello` 和
`Welch-Costas`。这些方法各自都有特定的参数和限制；这些内容在 Algebraic Interleaver 模块的参考页中有所描述。
