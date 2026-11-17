---
type: simulink-block
title: 'Translational Velocity Noise Source'
family: 'sources'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'translationalvelocitynoisesource'
documentation_source_path: 'ref/translationalvelocitynoisesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Velocity Noise Source

## 端口

### 输入

### **P** — 单边噪声功率谱密度物理信号

噪声的功率谱密度 (*PSD*) 是每单位带宽的平均噪声功率，单位为 (m/s)2/Hz。
### 守恒

### **B** — 基座接口机械平移

与基座接口关联的机械平移守恒端口。

### **F** — 从动接口机械平移

与从动接口关联的机械平移守恒端口。

## 参数

### **Sample time** — 时间步长周期和偏移 `1e-3` `s`（默认） | `[step, offset]` `s`

时间 *step* 周期和初始时间 *offset* 的值。如果为 *step* 指定标量值，则该模块假定 *offset* 值为 `0`。要为初始时间偏移指定非零值，请使用向量 `[step, offset]` 指定参数值。*offset* 值必须小于 *step* 值且大于或等于零。

### **Repeatability** — 随机数种子控制 `Not repeatable`（默认） | `Repeatable` | `Specify seed`

随机数种子是用于初始化随机数生成器的数字。种子为 `0` 或正整数。要控制随机数种子，请将此参数设置为：

- `Not repeatable` — 每次仿真模型时种子都会变化。该模块使用以下 MATLAB® 随机数生成器命令重置随机种子：

      seed = randi(2^32-1);

- `Repeatable` — 在每次仿真开始时，种子都是相同的随机数。该模块使用与 `Not repeatable` 参数相同的 MATLAB 随机数生成器命令来设置该值。

  当您从 Sources 库向模型中添加 Translational Velocity Noise Source 模块时，该模块会为重复种子生成并存储一个随机值。当您从模型中的现有模块复制 Translational Velocity Noise Source 模块时，副本会为重复种子生成新的随机值。
- `Specify seed` — 种子是您使用 **Seed** 参数指定的数字。仅当您为 **Repeatability** 参数选择 `Specify seed` 时，**Seed** 参数才可用。

### **Seed** — 随机数生成种子值 `0`（默认）

种子必须为 `0` 或正整数。仅当您为 **Repeatability** 参数选择 `Specify seed` 时，此参数才可用。

## 所属库

Simscape / Driveline / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

生成零均值正态（高斯）分布的平移速度

Translational Velocity Noise Source 模块使用 Simscape™ Foundation 库中的 PS Random Number 源生成零均值正态（高斯）分布的平移速度。该模块生成的平移速度取决于两个因素：

- 输入到模块的噪声功率谱密度
- 使用 **Repeatability** 参数以及（如适用）**Seed** 参数控制的随机数种子

该模块生成的平移速度的定义方程为

v=PSD/2N(0,1)h,

其中：

- *v* 是输出平移速度。
- *PSD* 是单边噪声功率谱密度。
- *N* 是均值为零、标准差为 1 的高斯随机数。
- *h* 是采样间隔。
