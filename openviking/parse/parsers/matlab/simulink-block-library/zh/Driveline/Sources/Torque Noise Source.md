---
type: simulink-block
title: 'Torque Noise Source'
family: 'sources'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'torquenoisesource'
documentation_source_path: 'ref/torquenoisesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Torque Noise Source

## 端口

### 输入

### **P** — 单边噪声功率谱密度物理信号

噪声的功率谱密度（*PSD*）是每单位带宽的平均噪声功率，单位为 (N\*m)2/Hz。
### 守恒

### **B** — 基础接口机械旋转

与基础接口关联的机械旋转守恒端口。

### **F** — 从动接口机械旋转

与从动接口关联的机械旋转守恒端口。

## 参数

### **Sample time** — 时间步周期和偏移 `1e-3` `s`（默认） | `[step, offset]` `s`

时间 *step* 周期和初始时间 *offset* 的值。如果为 *step* 指定标量值，则该模块假定 *offset* 值为 `0`。要指定初始时间偏移的非零值，请使用向量 `[step, offset]` 指定参数值。*offset* 值必须小于 *step* 值且大于或等于零。

### **Repeatability** — 随机数种子控制 `Not repeatable`（默认） | `Repeatable` | `Specify seed`

随机数种子是用于初始化随机数生成器的数字。种子为 `0` 或正整数。要控制随机数种子，请将此项参数设置为：

- `Not repeatable` — 每次仿真模型时，种子都会变化。该模块使用 MATLAB® 随机数生成器命令重置随机种子：

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — 每次仿真开始时，种子都是相同的随机数。该模块使用与 `Not repeatable` 参数相同的 MATLAB 随机数生成器命令来设置该值。

  当您从 Sources 库向模型添加 Torque Noise Source 模块时，该模块会为重复种子生成并存储一个随机值。当您从模型中的现有模块复制 Torque Noise Source 模块时，副本会为重复种子生成一个新的随机值。
- `Specify seed` — 种子是您使用 **Seed** 参数指定的数字。仅当您为 **Repeatability** 参数选择 `Specify seed` 时，**Seed** 参数才可用。

### **Seed** — 随机数生成种子值 `0`（默认）

种子必须为 `0` 或正整数。仅当您为 **Repeatability** 参数选择 `Specify seed` 时，此参数才可用。

## 所属库

Simscape / Driveline / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

对零均值正态（高斯）分布扭矩建模

Torque Noise Source 模块使用 Simscape™ Foundation 库中的 PS Random Number 源生成零均值正态（高斯）分布扭矩。该模块产生的扭矩取决于两个因素：

- 输入到该模块的噪声功率谱密度
- 使用 **Repeatability** 以及（若适用）**Seed** 参数控制的随机数种子

该模块所生成扭矩的定义方程为

T=PSD/2N(0,1)h,

其中：

- *T* 是输出扭矩。
- *PSD* 是单边噪声功率谱密度。
- *N* 是均值为零且标准差为 1 的高斯随机数。
- *h* 是采样间隔。
