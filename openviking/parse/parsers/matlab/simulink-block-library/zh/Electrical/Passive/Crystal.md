---
type: simulink-block
title: 'Crystal'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'crystal'
documentation_source_path: 'ref/crystal.html'
language: zh-CN
chinese_source: worker-translation
---

# Crystal

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: unspecified
- name: '-'
  summary: 负极端子电气
  direction: unspecified
```

### 守恒

### **+** — 正极端子电气

与晶体正电压相关联的电气守恒端口。

### **-** — 负极端子电气

与晶体负电压相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Parameterization
  summary: 模块参数化 Series resonance data（默认）| Parallel resonance data | Equivalent circuit parameters
  group: ''
- name: Series resonance, fs
  summary: 晶体串联谐振频率 32.764 kHz（默认）
  group: ''
- name: Parallel resonance, fa
  summary: 晶体并联谐振频率 32.768 kHz（默认）
  group: ''
- name: Motional inductance, L1
  summary: 动态电感 6742 H（默认）
  group: ''
- name: R1 parameterization
  summary: 串联电阻参数化 Equivalent series resistance R1（默认）| Quality factor Q
  group: ''
- name: Quality factor, Q
  summary: 晶体品质因数 90000（默认）
  group: ''
- name: Equivalent series resistance, R1
  summary: 动态阻尼 15 kOhm（默认）
  group: ''
- name: Motional capacitance, C1
  summary: 动态电容 0.0035 pF（默认）
  group: ''
- name: Load capacitance, CL
  summary: 负载电容 12.5 pF（默认）
  group: ''
- name: Shunt capacitance, C0
  summary: 并联电容 1.6 pF（默认）| 正标量
  group: ''
- name: Initial voltage
  summary: 初始输出电压 0 V（默认）
  group: ''
```

### **Parameterization** — 模块参数化 `Series resonance data`（默认）| `Parallel resonance data` | `Equivalent circuit parameters`

选择以下方法之一进行模块参数化：

- `Series resonance data` —
  提供晶体的串联谐振频率和电容数据。此方法为默认方法。
- `Parallel resonance data` —
  提供晶体的并联谐振频率和电容数据。
- `Equivalent circuit parameters`
  — 提供晶体等效电路模型的电气参数。

### **Series resonance, fs** — 晶体串联谐振频率 `32.764` `kHz`（默认）

晶体串联谐振频率。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Series
resonance data` 时，此参数才可见。

### **Parallel resonance, fa** — 晶体并联谐振频率 `32.768` `kHz`（默认）

晶体并联谐振频率，对应于由 **Load capacitance,
CL** 参数指定的并联负载电容下的工作状态。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Parallel
resonance data` 时，此参数才可见。

### **Motional inductance, L1** — 动态电感 `6742` `H`（默认）

表示晶体机械质量的电感。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Equivalent
circuit parameters` 时，此参数才可见。

### **R1 parameterization** — 串联电阻参数化 `Equivalent series resistance R1`（默认）| `Quality factor Q`

选择以下方法之一进行串联电阻参数化：

- `Equivalent series resistance R1`
  — 直接提供电阻值。此为默认方法。
- `Quality factor Q` — 提供
  模块用于计算电阻值的品质因数。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Series
resonance data` 或 `Parallel resonance
data` 时，此参数才可见。

### **Quality factor, Q** — 晶体品质因数 `90000`（默认）

晶体品质因数。仅当进行以下选择之一时，此参数才可见：

- 为 **Parameterization** 参数选择 `Series resonance data`，并为
  **R1 parameterization** 参数选择
  `Quality factor Q`
- 为 **Parameterization** 参数选择 `Parallel resonance data`，并为
  **R1 parameterization** 参数选择
  `Quality factor Q`

#### 依赖关系

仅当选择以下内容时，此参数才可见：

- 为 **Parameterization** 参数选择 `Series resonance data`，并为
  **R1 parameterization**
  参数选择 `Quality factor Q`
- 为 **Parameterization** 参数选择 `Parallel resonance data`，并为
  **R1 parameterization**
  参数选择 `Quality factor Q`

### **Equivalent series resistance, R1** — 动态阻尼 `15` `kOhm`（默认）

动态阻尼项。仅当进行以下选择之一时，此参数才可见：

- 为 **Parameterization** 参数选择 `Series resonance data`，并为
  **R1 parameterization**
  参数选择 `Equivalent series resistance R1`
- 为 **Parameterization** 参数选择 `Parallel resonance data`，并为
  **R1 parameterization**
  参数选择 `Equivalent series resistance R1`
- 为 **Parameterization** 参数选择 `Equivalent circuit parameters`

#### 依赖关系

仅当选择以下内容时，此参数才可见：

- 为 **Parameterization** 参数选择 `Series resonance data`，并为
  **R1
  parameterization** 参数选择 `Equivalent series resistance
  R1`
- 为 **Parameterization** 参数选择 `Parallel resonance data`，并为
  **R1
  parameterization** 参数选择 `Equivalent series resistance
  R1`
- 为 **Parameterization**
  参数选择 `Equivalent circuit parameters`

### **Motional capacitance, C1** — 动态电容 `0.0035` `pF`（默认）

表示负载下晶体机械刚度的电容。

### **Load capacitance, CL** — 负载电容 `12.5` `pF`（默认）

与 **Parallel resonance,
fa** 参数值对应的负载电容。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Parallel
resonance data` 时，此参数才可见。

### **Shunt capacitance, C0** — 并联电容 `1.6` `pF`（默认）| 正标量

两个晶体电气连接之间的电气电容。

### **Initial voltage** — 初始输出电压 `0` `V`（默认）

当输出电流为零时，仿真开始时的输出电压。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

稳定谐振器

Crystal 模块表示晶体的电气特性。下图显示了 Crystal 模块的等效电路模型。

当您将 **Parameterization** 参数设置为 `Equivalent circuit
parameters` 时，您需要为该模型指定等效电路参数。

- 电容 *C0* 对应于您在 **Shunt capacitance, C0** 参数中指定的电容。
- 电容 *C1* 对应于您在 **Motional capacitance, C1**
  参数中指定的电容。
- 电感 *L1* 对应于您在 **Motional inductance, L1**
  参数中指定的电感。
- 电阻 *R1* 对应于您在 **Equivalent series resistance, R1**
  参数中指定的电阻。

大多数数据手册指定的是晶体频率而非电感，因此该模块可选地接受频率数据。

- 当您将 **Parameterization** 参数设置为
  `Series resonance data` 时，模块使用以下关系从串联谐振频率计算 *L1*：

  fs=12πL1C1

  其中 *fs* 是
  **Series resonance, fs** 参数值。
- 当您将 **Parameterization** 参数设置为
  `Parallel resonance data` 时，模块使用以下关系从并联谐振频率计算 *L1*：

  fa=12πL1C1(C0+CL)/(C1+C0+CL)

  其中：

  - *fa* 是
    **Parallel resonance, fa** 参数值。
  - *CL* 是
    **Load capacitance, CL** 参数值。

某些数据手册指定的是品质因数而非等效串联电阻，因此该模块可选地接受品质因数数据。当您将 **R1
parameterization** 参数设置为 `Quality factor
Q` 时，模块使用以下关系从品质因数计算 *R1*：

Q=2πfL1R1

其中 *Q* 是 **Quality factor,
Q** 参数值。

**注意**

**R1 parameterization** 参数仅在为 **Parameterization**
参数选择 `Series resonance data` 或 `Parallel
resonance data` 时才可见。
