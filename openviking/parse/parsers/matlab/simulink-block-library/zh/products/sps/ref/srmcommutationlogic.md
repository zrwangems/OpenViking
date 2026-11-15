---
type: simulink-block
title: 'SRM Commutation Logic'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SRM Control\u200b'
documentation_page: 'srmcommutationlogic'
documentation_source_path: 'ref/srmcommutationlogic.html'
language: zh-CN
chinese_source: worker-translation
---

# SRM Commutation Logic

## 端口

### 输入

### **theta** — 相位角标量

相位角，*θph*，位于
区间 [0, *β* ] 内。

**数据类型：** `single` | `double`

### **thetaON** — 开通角标量

用于接通开关的下阈值。

**数据类型：** `single` | `double`

### **thetaOFF** — 关断角标量

用于关断开关的上阈值。

**数据类型：** `single` | `double`
### 输出

### **abcOnOff** — 换相信号向量

每相的换相信号：开通条件为 `1`，关断条件为
`0`

**数据类型：** `single` | `double`

## 参数

### **转矩能力角 (rad)** — 转矩角 `pi/2`（默认）

一个转子磁极的转矩产生能力，以弧度为单位。

### **采样时间 (-1 表示继承)** — 模块采样时间 `-1`（默认） | 正标量

连续模块执行之间的时间，以 s 为单位。在
执行期间，模块产生输出，并在适当情况下更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请通过将此参数设置为 `-1` 来继承
采样时间。如果此模块位于
连续变步长模型中，请使用正
标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / SRM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

开关磁阻电机的换相逻辑

SRM Commutation Logic 模块为
Switched Reluctance
Machine (SRM) 模块提供逻辑信号。该信号指示何时接通和断开
每相的电源。

每相的换相信号为：

- 如果 *θon* ≤
  *θph* ≤
  *θoff*，则为 `1`。
- 如果 *θph* <
  *θon*，则为 `0`。
- 如果 *θph* >
  *θoff*，则为 `0`。

其中：

- *θph* 是位于
  区间 [0,*β* ] 内的相位角。
- *β* 是转矩能力角。
- *θon* 是开通
  角。
- *θoff* 是关断
  角。
