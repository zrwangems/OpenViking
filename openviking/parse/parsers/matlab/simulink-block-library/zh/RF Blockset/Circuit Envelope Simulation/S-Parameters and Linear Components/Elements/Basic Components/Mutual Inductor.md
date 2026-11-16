---
type: simulink-block
title: 'Mutual Inductor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / Basic Components'
documentation_page: 'mutualinductor'
documentation_source_path: 'ref/mutualinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Mutual Inductor

## 端口

R2025b 中未记录。

## 参数

### **Inductance L1** — 第一个电感的电感值 `1e-6 H`（默认）| 正标量

第一个电感的电感值，指定为以
`H`、`nH`、
`μH`、`mH` 为单位的正标量。

### **Inductance L2** — 第二个电感的电感值 `1e-6 H`（默认）| 正标量

第二个电感的电感值，指定为以
`H`、`nH`、
`μH`、`mH` 为单位的正标量。

### **Coefficient of coupling** — 互感的耦合系数 `0.9`（默认）| 标量

两个电感互感的耦合系数，
指定为从 0 到 1 的标量值。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

对用于电路包络分析的两个耦合电感进行建模

Mutual Inductor 模块在 RF Blockset™ 电路包络仿真环境中对电感进行建模。有关 RF
仿真的介绍，请参阅示例 Simulate High Frequency Components。

该模块实现以下关系

v1(t)=L1ddt[i1(t)]+Mddt[i2(t)]v2(t)=Mddt[i1(t)]+L2ddt[i2(t)]M=KL1L2

其中：

- *L*1 和
  *L*2 表示
  电感。
- *M* 表示具有耦合系数
  *K* 的互感。
- *v*1(*t*) 和
  *v*2(*t*)
  表示电感端子两端的电压，时间为
  *t*。
- *i*1(*t*) 和
  *i*2(*t*)
  表示在时间 *t* 流过电感的电流。
  该模块使用标准点标记来指示相对于正电压的正
  电流流动方向。

RF Blockset 电流和电压信号由 Configuration 模块中指定的每个频率 *fk* 处的同相
(*Ik*) 和正交 (*Qk*)
分量组成：

i(t)=∑{fk}(iIk(t)+j⋅iQk(t))ej(2πfk)tv(t)=∑{fk}(vIk(t)+j⋅vQk(t))ej(2πfk)t
