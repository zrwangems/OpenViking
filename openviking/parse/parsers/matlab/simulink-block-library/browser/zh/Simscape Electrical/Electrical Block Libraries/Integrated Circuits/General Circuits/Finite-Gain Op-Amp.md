---
type: simulink-block
title: 'Finite-Gain Op-Amp'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Integrated Circuits / General Circuits'
documentation_page: 'finitegainopamp'
documentation_source_path: 'ref/finitegainopamp.html'
language: zh-CN
chinese_source: worker-translation
---

# Finite-Gain Op-Amp

## 端口

### 守恒

### **+** — 正电气电压 electrical

与运放同相输入端关联的电气守恒端口。

### **-** — 负电气电压 electrical

与运放反相输入端关联的电气守恒端口。

### **out** — 输出电压 electrical

与运放输出端关联的电气守恒端口。端口名称在模块图标上隐藏，但您可以在仿真数据日志中看到它。

## 参数

### 主要

### **Gain, A** — 开环增益 1000（默认）

运算放大器的开环增益。

### **Input resistance, Rin** — 模块输入端的电阻 1e6 Ohm（默认）

运算放大器输入端的电阻，模块使用该电阻计算输入电流。

### **Output resistance, Rout** — 模块输出端的电阻 100 Ohm（默认）

运算放大器输出端的电阻，模块使用该电阻计算由输出电流引起的输出电压降。

### **Minimum output, Vmin** — 输出电压下限 -15 V（默认）

运算放大器输出电压的下限。

### **Maximum output, Vmax** — 输出电压上限 15 V（默认）

运算放大器输出电压的上限。

### 噪声

### **Noise mode** — 选择运放是否生成热噪声 `Disabled`（默认） | `Enabled`

选择是否对热噪声效应建模：

- `Disabled` — 运放不生成热噪声。
- `Enabled` — 运放生成热噪声电压和电流，相关参数将在 **噪声** 部分中可见。

### **Input noise voltage density** — 电压噪声密度 30e-9 V/Hz^0.5（默认）

施加到同相输入端的电压噪声的单边频谱幅度密度。

#### 依赖项

当 **Noise mode** 参数设置为 `Enabled` 时启用。

### **Noise current parameterization** — 选择两个输入的噪声电流密度是不同的还是相同的 `Apply same density function to both inputs`（默认） | `Apply different density function to each input`

选择施加到模块输入的电流密度值是不同的还是相同的。

#### 依赖项

当 **Noise mode** 参数设置为 `Enabled` 时启用。

### **Input noise current density** — 两个输入端的电流噪声 0.5e-12 A/Hz^0.5（默认）

施加到两个输入端的电流噪声的单边频谱幅度密度。请注意，即使两个输入的密度函数相同，实际噪声电流也取决于随机数种子。如果用于随机数生成的种子不同，则输入端的实际噪声电流也不同。

#### 依赖项

当 **Noise current parameterization** 参数设置为 `Apply same density function to both inputs` 时启用。

### **Noninverting input noise current density** — 同相输入端的电流噪声 0.5e-12 A/Hz^0.5（默认）

施加到同相输入端的电流噪声的单边频谱幅度密度。

#### 依赖项

当 **Noise current parameterization** 参数设置为 `Apply different density function to each input` 时启用。

### **Inverting input noise current density** — 反相输入端的电流噪声 0.5e-12 A/Hz^0.5（默认）

施加到反相输入端的电流噪声的单边频谱幅度密度。

#### 依赖项

当 **Noise current parameterization** 参数设置为 `Apply different density function to each input` 时启用。

### **Sample time** — 噪声源的采样速率 1e-3 s（默认）

定义噪声源的采样速率。选择该速率以反映模型中感兴趣的频率。将采样时间设置得太小会不必要地减慢仿真速度。

#### 依赖项

当 **Noise mode** 参数设置为 `Enabled` 时启用。

### **Repeatability** — 选择噪声控制选项 `Not repeatable`（默认） | `Repeatable` | `Specify seed`

选择噪声控制选项：

- `Not repeatable` — 用于噪声生成的随机序列不可重复。
- `Repeatable` — 用于噪声生成的随机序列可重复，并使用系统生成的种子。
- `Specify seed` — 用于噪声生成的随机序列可重复，并且您通过种子参数控制种子。您分别为输入噪声电压、同相输入噪声电流和反相输入噪声电流指定种子值。

#### 依赖项

当 **Noise mode** 参数设置为 `Enabled` 时启用。

### **Input noise voltage auto-generated seed used for repeatable option** — 用于电压噪声的自动生成随机数种子 random real number

存储在模块内部以使随机序列可重复的随机数种子。参数值使用 MATLAB 随机数生成器命令自动生成。您可以修改此参数值，但如果将模块复制到模型中的另一个模块，它会被新的随机值覆盖。因此，如果要控制随机序列的种子，请对 **Repeatability** 参数使用 `Specify seed` 选项，并使用 **Input noise voltage seed** 参数指定所需的种子值。

#### 依赖项

当 **Repeatability** 参数设置为 `Repeatable` 时启用。

### **Noninverting input noise current auto-generated seed used for repeatable option** — 用于同相输入端电流噪声的自动生成随机数种子 random real number

存储在模块内部以使随机序列可重复的随机数种子。参数值使用 MATLAB 随机数生成器命令自动生成。您可以修改此参数值，但如果将模块复制到模型中的另一个模块，它会被新的随机值覆盖。因此，如果要控制随机序列的种子，请对 **Repeatability** 参数使用 `Specify seed` 选项，并使用 **Noninverting input noise current seed** 参数指定所需的种子值。

#### 依赖项

当 **Repeatability** 参数设置为 `Repeatable` 时启用。

### **Inverting input noise current auto-generated seed used for repeatable option** — 用于反相输入端电流噪声的自动生成随机数种子 random real number

存储在模块内部以使随机序列可重复的随机数种子。参数值使用 MATLAB 随机数生成器命令自动生成。您可以修改此参数值，但如果将模块复制到模型中的另一个模块，它会被新的随机值覆盖。因此，如果要控制随机序列的种子，请对 **Repeatability** 参数使用 `Specify seed` 选项，并使用 **Inverting input noise current seed** 参数指定所需的种子值。

#### 依赖项

当 **Repeatability** 参数设置为 `Repeatable` 时启用。

### **Input noise voltage seed** — 电压噪声的随机数种子 0（默认）

噪声随机数生成器使用的种子。

#### 依赖项

当 **Repeatability** 参数设置为 `Specify seed` 时启用。

### **Noninverting input noise current seed** — 同相输入端电流噪声的随机数种子 0（默认）

噪声随机数生成器使用的种子。

#### 依赖项

当 **Repeatability** 参数设置为 `Specify seed` 时启用。

### **Inverting input noise current seed** — 反相输入端电流噪声的随机数种子 0（默认）

噪声随机数生成器使用的种子。

#### 依赖项

当 **Repeatability** 参数设置为 `Specify seed` 时启用。

## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008b 中引入**

## 描述

带可选噪声的增益受限运算放大器模型

Finite-Gain Op-Amp 模块对增益受限运算放大器建模。如果正端口和负端口的电压分别为 *V*p 和 *V*m，则输出电压为：

Vout = A(Vp-Vm)−Iout\*Rout

其中：

- *A* 是增益。
- *R*out 是输出电阻。
- *I*out 是输出电流。

输入电流为：

Vp-VmRin

其中 *R*in 是输入电阻。

输出电压受您在模块对话框中指定的最小和最大输出值限制。

### 热噪声

Finite-Gain Op-Amp 模块可以生成热噪声。如果将 **Noise mode** 参数设置为 `Enabled`，则模块的等效电路包括连接到每个输入端的噪声电流源，以及连接到同相输入端的噪声电压源。这三个噪声源相互独立且不相关。

模块根据以下公式生成噪声电压和电流：

vnoise=vdensity2hN(0,1)

inoise=idensity2hN(0,1)

其中：

- *v*noise 是噪声电压。
- *v*density 是电压噪声的单边频谱幅度密度。
- *i*noise 是输入端的噪声电流。
- *i*density 是施加到该输入端的电流噪声的单边频谱幅度密度。
- *h* 是采样时间。
- *N* 是均值为零、标准差为一的高斯随机数。

模块使用 Simscape™ Foundation 库中的 PS Random Number 源生成高斯噪声。您可以通过设置 **Repeatability** 参数来控制随机数种子：

- `Not repeatable` — 每次您对模型进行仿真时，模块都会使用 MATLAB® 随机数生成器重置随机种子：

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — 模块自动生成一个种子值并将其存储在模块内部，以便始终以相同的随机数开始仿真。当您从模块库向模型添加 Finite-Gain Op-Amp 模块时，会设置此自动生成的种子值。当您从模型中的现有模块创建 Finite-Gain Op-Amp 模块的新副本时，会生成新的种子值。模块使用上面显示的 MATLAB 随机数生成器命令设置该值。
- `Specify seed` — 如果选择此选项，其他参数允许您直接为输入电压、同相输入端电流和反相输入端电流指定随机数种子值。
