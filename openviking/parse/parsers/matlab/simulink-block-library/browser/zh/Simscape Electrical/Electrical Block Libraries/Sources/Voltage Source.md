---
type: simulink-block
title: 'Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sources'
documentation_page: 'voltagesource'
documentation_source_path: 'ref/voltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Voltage Source

## 端口

### 守恒

### **+** — 正端口电气

与电压源正端子关联的电气守恒端口

### **-** — 负端口电气

与电压源负端子关联的电气守恒端口

## 参数

### DC 与 AC 分量

### **DC voltage** — 直流输出电压 `0` `V` (默认)

输出电压的 DC 分量。指定非零值可向电压源添加 DC 分量。

### **AC voltage peak amplitude** — AC 电压幅值 `0` `V` (默认)

输出电压的 AC 分量的幅值。指定非零值可向电压源添加 AC 分量。

### **AC voltage phase shift** — AC 电压相位偏移 `0` `rad` (默认)

输出电压的 AC 分量的相位偏移。

### **AC voltage frequency** — AC 电压频率 `60` `Hz` (默认)

输出电压的 AC 分量的频率，以 Hz 为单位。

### 噪声

### **Noise mode** — 噪声选项 `Disabled` (默认) | `Enabled`

选择噪声选项：

- `Disabled` — 电压源不产生噪声。
- `Enabled` — 电压源生成热噪声，并且相关参数会在 **Noise** 选项卡上可见。

### **Power spectral density** — 功率谱密度 `0` `V^2/Hz` (默认)

单边频谱噪声功率。严格来说，这是电压平方的密度函数，通常被视为进入 1 ohm 负载的功率，因此单位为 V^2/Hz。为避免这种单位歧义，一些数据手册将噪声电压表示为噪声密度，单位为 V/√Hz。在这种情况下，应将数据手册中给出的噪声密度的平方作为参数值输入。

### **Repeatability** — 噪声控制选项 `Not repeatable` (默认) | `Repeatable` | `Specify seed`

选择噪声控制选项：

- `Not repeatable` — 用于噪声生成的随机序列不可重复。
- `Repeatable` — 用于噪声生成的随机序列可重复，并使用系统生成的种子。
- `Specify seed` — 用于噪声生成的随机序列可重复，并且您通过 **Seed** 参数控制种子。

### **Auto-generated seed used for repeatable option** — 自动生成的随机数种子 `1964622691` (默认)

存储在模块内部的随机数种子，用于使随机序列可重复。该参数值使用 MATLAB 随机数生成器命令自动生成。您可以修改此参数值，但如果将模块复制到模型中的另一个模块，它会被新的随机值覆盖。因此，如果要控制随机序列的种子，请为 **Repeatability** 参数使用 `Specify seed` 选项，并使用 **Seed** 参数指定所需的种子值。

#### 依赖关系

仅当您为 **Repeatability** 参数选择 `Repeatable` 时，此参数才可见。

### **Seed** — 随机数种子 `0` (默认)

噪声随机数生成器使用的随机数种子。

#### 依赖关系

仅当您为 **Repeatability** 参数选择 `Specify seed` 时，此参数才可见。

### **Sample time** — 采样时间 `1e-3` `s` (默认)

定义噪声源的采样速率。选择该值时，应反映模型中关注的频率。将采样时间设置得过小会不必要地减慢仿真速度。

## 所属库

Simscape / Electrical / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

具有可选 DC、AC 和噪声分量的电压源

Voltage Source 模块实现具有 DC、AC 和噪声分量的电压源。**+** 和 **–** 端子之间的电压由下式给出：

v=vDC+vACsin(2πft+ϕ)+vN

其中：

- *vDC* 是稳态 DC 电压分量。
- *vAC* 是 AC 电压分量的幅值。
- *f* 是 AC 分量的频率。
- *ϕ* 是 AC 分量的相位偏移。
- *vN* 是噪声电压。

您可以将电源配置为仅 DC、仅 AC 或两者组合。默认情况下，AC 和 DC 分量都设置为 0。将模块放入模型后，通过指定非零参数值来定义 AC/DC 电压。

噪声分量也是可选的。如果将 **Noise mode** 参数设置为 `Enabled`，则添加的噪声电压由下式给出：

vN=Pv/2N(0,1)h

其中：

- *Pv* 是 1 ohm 负载的单边噪声功率谱密度，单位为 V^2/Hz。
- *N* 是均值为零、标准差为 1 的高斯随机数。
- *h* 是采样间隔。

默认情况下，**Noise mode** 参数设置为 `Disabled`，电压源不生成热噪声。

### 噪声选项

该模块通过使用 Simscape™ Foundation 库中的 PS Random Number 源生成高斯噪声。您可以通过设置 **Repeatability** 参数来控制随机数种子：

- `Not repeatable` — 每次仿真模型时，该模块都会使用 MATLAB® 随机数生成器重置随机种子：

  ```
  seed = randi(2^32-1);
  ```

- `Repeatable` — 该模块会自动生成一个种子值并将其存储在模块内部，以便始终使用相同的随机数开始仿真。当您从模块库向模型添加 Voltage Source 模块时，会设置此自动生成的种子值。当您从模型中的现有 Voltage Source 模块创建新副本时，会生成新的种子值。该模块使用上面显示的 MATLAB 随机数生成器命令设置该值。
- `Specify seed` — 如果选择此选项，则附加的 **Seed** 参数允许您直接指定随机数种子值。
