---
type: simulink-block
title: 'General Block Deinterleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'generalblockdeinterleaver'
documentation_source_path: 'ref/generalblockdeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# General Block Deinterleaver

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Permutation vector source**
:   一个选择项，用于指定置换向量的来源。来源可以是 `Dialog` 或 `Input
    port`。默认值为
    `Dialog`。

**Permutation vector**
:   一个长度为 N 的向量，按顺序列出输出元素中来自输入向量的索引。仅当 **Permutation vector source** 设置为
    `Dialog` 时，此参数可用。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

恢复输入向量中符号的顺序

General Block Deinterleaver 模块重新排列其输入向量的元素，不重复或省略任何元素。如果输入包含 *N* 个元素，则 **Permutation vector** 参数是一个长度为 *N* 的列向量。该列向量按顺序指示输出元素中来自输入向量的索引。也就是说，对于 1 到 *N* 之间的每个整数 *k*，

Output(**Permutation vector**(*k*)) =
Input(*k*)

**Permutation vector** 参数必须包含 1 到 *N* 之间的唯一整数。

输入和 **Permutation vector** 参数都必须是列向量信号。

此模块可以输出在仿真期间长度变化的序列。有关长度变化的序列或可变大小信号的更多信息，请参阅 Variable-Size Signal Basics (Simulink)。

此模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。输出信号的数据类型继承自输入信号。

要将此模块用作 General Block Interleaver 模块的逆模块，请在两个模块中使用相同的 **Permutation vector** 参数。在这种情况下，这两个模块互为逆模块，即先应用 General Block Interleaver 模块再应用 General Block Deinterleaver 模块后，数据保持不变。
