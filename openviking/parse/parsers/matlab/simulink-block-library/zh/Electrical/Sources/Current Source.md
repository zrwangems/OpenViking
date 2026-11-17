---
type: simulink-block
title: 'Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'currentsource'
documentation_source_path: 'ref/currentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Source

## 端口

### 守恒端口

### **+** — 正极端口电气

与电流源正极端子关联的电气守恒端口

### **-** — 负极端口电气

与电流源负极端子关联的电气守恒端口

## 参数

### 直流与交流分量

### **DC current** — 直流电流 `0` `A`（默认值）

输出电流的直流分量。指定非零值以向电流源添加直流分量。

### **AC current peak amplitude** — 交流电流幅值 `0` `A`（默认值）

输出电流的交流分量幅值。指定非零值以向电流源添加交流分量。

### **AC current phase shift** — 交流电流相位偏移 `0` `rad`（默认值）

输出电流的交流分量相位偏移。

### **AC current frequency** — 交流电流频率 `60` `Hz`（默认值）

输出电流的交流分量频率。

### 噪声

### **Noise mode** — 噪声选项 `Disabled`（默认值） | `Enabled`

选择噪声选项：

- `Disabled` — 电流源不产生噪声。此为默认值。
- `Enabled` — 电流源产生热噪声，相关参数将在 **Noise** 选项卡上显示。

### **Power spectral density** — 功率谱密度 `0` `A^2/Hz`（默认值）

单边频谱噪声功率。严格来说，这是电流平方的密度函数，通常被认为是进入 1 欧姆负载的功率，因此单位为 A^2/Hz。为避免此单位歧义，一些数据手册将噪声电流表示为噪声密度，单位为 A/√Hz。在这种情况下，您应将数据手册中给出的噪声密度的平方作为参数值输入。

### **Repeatability** — 噪声控制选项 `Not repeatable`（默认值） | `Repeatable` | `Specify seed`

选择噪声控制选项：

- `Not repeatable` — 用于噪声生成的随机序列不可重复。此为默认值。
- `Repeatable` — 用于噪声生成的随机序列可重复，使用系统生成的种子。
- `Specify seed` — 用于噪声生成的随机序列可重复，您可以通过 **Seed** 参数控制种子。

### **Auto-generated seed used for repeatable option** — 自动生成的随机数种子 `3241354618`（默认值）

存储在模块内部的随机数种子，用于使随机序列可重复。该参数值使用 MATLAB 随机数生成器命令自动生成。您可以修改此参数值，但如果您将模块复制到模型中的另一个模块，它将被新的随机值覆盖。因此，如果您想控制随机序列的种子，请对 **Repeatability** 参数使用 `Specify seed` 选项，并使用 **Seed** 参数指定所需的种子值。

#### 依赖关系

此参数仅在您为 **Repeatability** 参数选择 `Repeatable` 时可见。

### **Seed** — 随机数种子 `0`（默认值）

噪声随机数生成器使用的随机数种子。

#### 依赖关系

此参数仅在您为 **Repeatability** 参数选择 `Specify seed` 时可见。

### **Sample time** — 采样时间 `1e-3` `s`（默认值）

定义噪声源的采样速率。选择该值以反映模型中感兴趣的频率。将采样时间设置得过小会不必要地减慢仿真速度。

## 所属库

Simscape / Electrical / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

具有可选直流、交流和噪声分量的电流源

Current Source 模块实现了一个具有直流、交流和噪声分量的电流源。从 **–** 端子流向 **+** 端子的电流由下式给出：

i=iDC+iACsin(2πft+ϕ)+iN

其中：

- *i*DC 是稳态直流电流分量。
- *i*AC 是交流电流分量的幅值。
- *f* 是交流分量的频率。
- *ϕ* 是交流分量的相位偏移。
- *i*N 是噪声电流。

您可以将电源配置为仅直流、仅交流或两者的组合。默认情况下，交流和直流分量均设置为 0。在将模块放入模型后，通过指定非零参数值来定义交流/直流电流。

噪声分量也是可选的。如果您将 **Noise mode** 参数设置为 `Enabled`，则添加的噪声电流由下式给出：

iN=Pi/2N(0,1)h

其中：

- *P*i 是 1 欧姆负载的单边噪声功率谱密度，单位为 A^2/Hz。
- *N* 是均值为零、标准差为一的高斯随机数。
- *h* 是采样间隔。

默认情况下，**Noise mode** 参数设置为 `Disabled`，电流源不产生热噪声。

### 噪声选项

该模块使用 Simscape™ Foundation 库中的 PS Random Number 源生成高斯噪声。您可以通过设置 **Repeatability** 参数来控制随机数种子：

- `Not repeatable` — 每次仿真模型时，模块使用 MATLAB® 随机数生成器重置随机种子：

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — 模块自动生成一个种子值并将其存储在模块内部，以始终使用相同的随机数开始仿真。此自动生成的种子值在您从模块库向模型中添加 Current Source 模块时设置。当您从模型中的现有 Current Source 模块创建新副本时，会生成新的种子值。模块使用上面显示的 MATLAB 随机数生成器命令设置该值。
- `Specify seed` — 如果您选择此选项，额外的 **Seed** 参数允许您直接指定随机数种子值。
