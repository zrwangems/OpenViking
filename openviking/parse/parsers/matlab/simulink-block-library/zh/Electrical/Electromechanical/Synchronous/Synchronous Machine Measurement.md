---
type: simulink-block
title: 'Synchronous Machine Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'synchronousmachinemeasurement'
documentation_source_path: 'ref/synchronousmachinemeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Machine Measurement

## 端口

### 输入

### **pu** — 来自所连接同步电机物理量的标幺值测量

与来自所连接同步电机的标幺值测量相关联的物理信号向量端口。向量元素为：

- `pu_fd_Efd`
- `pu_fd_Ifd`
- `pu_torque`
- `pu_velocity`
- `pu_ed`
- `pu_eq`
- `pu_e0`
- `pu_id`
- `pu_iq`
- `pu_i0`
### 输出

### **o** — 标幺值测量输出端口物理量

与标幺值测量相关联的物理信号输出端口。

## 参数

### **Output** — 来自同步电机的标幺值测量 `Field voltage (field circuit base, Efd)`（默认）| `Field current (field circuit base, Ifd)` | `Electrical torque` | `Rotor velocity` | `Stator d-axis voltage` | `Stator q-axis voltage` | `Stator zero-sequence voltage` | `Stator d-axis current` | `Stator q-axis current` | `Stator zero-sequence current` | `Apparent power` | `Real power` | `Reactive power` | `Terminal voltage` | `Terminal current` | `Power factor angle` | `Power factor` | `Load angle` | `Rotor electrical angle`

来自同步电机的标幺值测量。默认值为 `Field voltage (field circuit base, Efd)`。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

来自同步电机的标幺值测量

Synchronous Machine Measurement 模块输出与所连接的 Synchronous Machine Round Rotor 或 Synchronous Machine Salient Pole 模块相关联的标幺值测量。Synchronous Machine Measurement 模块的输入连接到同步电机模块的 `pu` 输出端口。

将 **Output** 参数设置为与同步电机相关联的标幺值测量。根据您选择的值，Synchronous Machine Measurement 模块会：

- 直接输出输入信号向量中某个元素的值
- 通过在数学表达式中使用输入信号向量中元素的值来计算标幺值测量

Synchronous Machine Measurement 模块根据表中的输出值表达式输出同步电机的标幺值测量。例如，当您将 **Output** 设置为 `Stator d-axis voltage` 时，模块直接输出输入信号向量中 `pu_ed` 元素的值。然而，当您将 **Output** 设置为 `Reactive power` 时，模块会根据 `pu_ed`、`pu_eq`、`pu_id` 和 `pu_iq` 元素计算该值。

| 输出参数设置 | 输出值表达式 |
| --- | --- |
| Field voltage (field circuit base, Efd) | `pu_fd_Efd` |
| Field current (field circuit base, Ifd) | `pu_fd_Ifd` |
| Electrical torque | `pu_torque` |
| Rotor velocity | `pu_velocity` |
| Stator d-axis voltage | `pu_ed` |
| Stator q-axis voltage | `pu_eq` |
| Stator zero-sequence voltage | `pu_e0` |
| Stator d-axis current | `pu_id` |
| Stator q-axis current | `pu_iq` |
| Stator zero-sequence current | `pu_i0` |
| Apparent power | pu\_Pt2+pu\_Qt2 |
| Real power | `pu_Pt = (pu_ed*pu_id) + (pu_eq*pu_iq) + 2(pu_e0*pu_i0)` |
| Reactive power | `pu_Qt = (pu_eq*pu_id) – (pu_ed*pu_iq)` |
| Terminal voltage | (pu\_ed2+​pu\_eq2) |
| Terminal current | (pu\_id2+pu\_iq2) |
| Power factor angle (rad) | `power_factor_angle = atan2(pu_Qt, pu_Pt)` |
| Power factor | `cos(power_factor_angle)` |
| Load angle (rad) | `load_angle(rad) = atan2(pu_ed, pu_eq)` |
| Rotor electrical angle | `y = pi+2*atan(tan((u-pi)/2))` |
