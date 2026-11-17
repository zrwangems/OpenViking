---
type: simulink-block
title: 'Algebraic Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'algebraicinterleaver'
documentation_source_path: 'ref/algebraicinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Algebraic Interleaver

## 端口

R2025b 中未记录。

## 参数

**类型**：模块用于交织的置换表的类型。

**Number of elements**
:   输入向量中元素的数量 *N*。

**Multiplicative factor**
:   用于计算交织器循环向量的因子。仅当 **Type** 设置为 `Takeshita-Costello` 时，此字段才会出现。

**Cyclic shift**
:   模块在创建置换表时对索引进行移位的量。仅当 **Type** 设置为 `Takeshita-Costello` 时，此字段才会出现。

**Primitive element**
:   有限域 GF(N+1) 中阶为 *N* 的元素。仅当 **Type** 设置为 `Welch-Costas` 时，此字段才会出现。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用代数推导的置换表对输入符号重新排序

Algebraic Interleaver 模块使用代数推导的置换对其输入向量的元素进行重新排列。**Number of elements** 参数 *N* 表示输入向量中有多少个数字。此模块接受列向量输入信号。

此模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。输出信号的数据类型继承自输入信号。

**Type** 参数表示模块用于生成相应置换表的代数方法。可选值为 `Takeshita-Costello` 和 `Welch-Costas`。这些方法各有其特定的参数和限制：

- 如果将 **Type** 设置为 `Welch-Costas`，则 *N* + 1 必须为素数。**Primitive element** 参数是一个介于 1 和 *N* 之间的整数 *A*，它表示有限域 GF(*N*+ 1) 的一个本原元素。这意味着 GF(*N* + 1) 的每个非零元素都可以表示为 *A* 的某个整数次幂。

  在 Welch-Costas 交织器中，置换将整数 *k* 映射为 mod(*Ak*,*N* + 1) - 1。
- 如果将 **Type** 设置为 `Takeshita-Costello`，则对于某个整数 *m*，*N* 必须为 2*m*。**Multiplicative factor** 参数 *k* 必须是小于 *N* 的奇整数。**Cyclic shift** 参数 *h* 必须是小于 *N* 的非负整数。

  Takeshita-Costello 交织器使用长度为 *N* 的*循环向量*，其第 *n* 个元素为

  c(n)=mod(k⋅n⋅(n−1)2,N)+1, n

  其中整数 n 介于 1 和 N 之间。中间置换函数通过以下关系获得：

  Π(c(n))=c(n+1)

  其中

  n=1:N

  交织器的实际置换向量是将置换向量 π 的元素按 **Cyclic shift** 参数 *h* 进行循环移位的结果。
