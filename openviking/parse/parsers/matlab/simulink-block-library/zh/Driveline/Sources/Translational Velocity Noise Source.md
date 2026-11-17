---
type: simulink-block
title: 'Translational Velocity Noise Source'
family: 'sdl'
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
```yaml
ports:
- name: P
  summary: 单边噪声功率谱密度物理信号
  direction: input
- name: B
  summary: 基座接口机械平移
  direction: input
- name: F
  summary: 从动接口机械平移
  direction: input
```

### 输入

### **P** — 单边噪声功率谱密度物理信号

噪声的功率谱密度（*PSD*）是每单位带宽的平均噪声功率，单位为
(m/s)2/Hz。
### 守恒

### **B** — 基座接口机械平移

与基座接口关联的机械平移守恒端口。

### **F** — 从动接口机械平移

与从动接口关联的机械平移守恒端口。
## 参数
```yaml
parameters:
- name: Sample time
  summary: 时间步周期和偏移量 1e-3 s（默认）| [step, offset] s
  group: ''
- name: Repeatability
  summary: 随机数种子控制 Not repeatable（默认）| Repeatable | Specify seed
  group: ''
- name: Seed
  summary: 随机数生成种子值 0（默认）
  group: ''
```

### **Sample time** — 时间步周期和偏移量 `1e-3` `s`（默认）| `[step, offset]` `s`

时间*步长*周期和初始时间*偏移量*的值。如果为
*step* 指定标量值，则该模块假定 *offset*
值为 `0`。要指定非零的初始
时间偏移量，请使用向量
`[step,
offset]` 指定参数值。*offset*
值必须小于 *step* 值且大于
或等于零。

### **Repeatability** — 随机数种子控制 `Not repeatable`（默认）| `Repeatable` | `Specify seed`

随机数种子是用于初始化随机数
生成器的数字。种子为 `0` 或正整数。要
控制随机数种子，请将此参数设置为：

- `Not repeatable` — 每次仿真模型时种子
  都会变化。该模块使用 MATLAB® 随机数生成器命令重置
  随机种子：

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — 种子在每次仿真开始时
  都是相同的随机数。该模块
  使用与 `Not repeatable` 参数相同的 MATLAB 随机数生成器命令
  设置该值。

  当您从 Sources 库向模型中添加 Translational Velocity Noise
  Source 模块时，
  该模块会为重复种子生成并存储一个随机值。当您从模型中的
  现有模块复制 Translational Velocity
  Noise Source 模块时，副本会为重复
  种子生成一个新的随机值。
- `Specify seed` — 种子是您使用 **Seed**
  参数指定的数字。**Seed** 参数仅在您为
  **Repeatability** 参数选择 `Specify
  seed` 时
  可用。

### **Seed** — 随机数生成种子值 `0`（默认）

种子必须为 `0` 或正整数。此
参数仅在您为 **Repeatability**
参数选择 `Specify
seed` 时可用。
## 所属库

Simscape / Driveline / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

生成零均值正态（高斯）分布平移速度

Translational Velocity Noise Source 模块使用 Simscape™ Foundation 库中的 PS Random Number 源生成零均值
正态（高斯）分布平移速度。该模块生成的平移速度
取决于两个因素：

- 输入到该模块的噪声功率谱密度
- 您使用 **Repeatability** 以及适用的
  **Seed** 参数控制的随机数种子

该模块生成的平移速度的定义方程为

v=PSD/2N(0,1)h，

其中：

- *v* 是输出平移速度。
- *PSD* 是单边噪声功率谱
  密度。
- *N* 是均值为零且
  标准差为一的高斯随机数。
- *h* 是采样间隔。
