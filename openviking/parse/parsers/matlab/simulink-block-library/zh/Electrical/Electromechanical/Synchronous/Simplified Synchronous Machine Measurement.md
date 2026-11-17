---
type: simulink-block
title: 'Simplified Synchronous Machine Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'simplifiedsynchronousmachinemeasurement'
documentation_source_path: 'ref/simplifiedsynchronousmachinemeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Simplified Synchronous Machine Measurement

## 端口

### 输入

### **pu** — 来自所连接同步电机的标幺值测量值，物理信号向量

与来自所连接的 Simplified Synchronous Machine 的标幺值测量值相关联的物理信号，指定为：

- `pu_EMFa`
- `pu_EMFb`
- `pu_EMFc`
- `pu_torque`
- `pu_velocity`
- `pu_vd`
- `pu_vq`
- `pu_v0`
- `pu_id`
- `pu_iq`
- `pu_i0`
### 输出

### **o** — 标幺值测量输出端口，物理信号

与标幺值测量值相关联的物理信号输出端口，以物理信号形式返回。

## 参数

### **Output** — 来自同步电机的标幺值测量值 `EMF phase A`（默认）| `EMF phase B` | `EMF phase C` | `Electrical torque` | `Rotor velocity` | `Stator d-axis voltage` | `Stator q-axis voltage` | `Stator zero-sequence voltage` | `Stator d-axis current` | `Stator q-axis current` | `Stator zero-sequence current` | `Apparent power` | `Real power` | `Reactive power` | `Terminal voltage` | `Terminal current` | `Power factor angle` | `Power factor` | `Load angle` | `Rotor electrical angle`

来自简化同步电机的标幺值测量值。默认值为 `EMF phase A`。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

来自简化同步电机的标幺值测量值

Simplified Synchronous Machine Measurement 模块输出与所连接的 Simplified Synchronous Machine 模块相关联的标幺值测量值。Simplified Synchronous Machine Measurement 模块的输入连接到 Simplified Synchronous Machine 模块的 `pu` 输出端口。

将 **Output** 参数设置为与简化同步电机相关联的标幺值测量值。根据所选择的值，Simplified Synchronous Machine Measurement 模块会：

- 直接输出输入信号向量中某个元素的值
- 通过数学表达式使用输入信号向量中元素的值来计算标幺值测量值。

Simplified Synchronous Machine Measurement 模块根据表中的输出值表达式输出简化同步电机的标幺值测量值。例如，当将 **Output** 设置为 `Stator d-axis voltage` 时，模块直接输出输入信号向量中 `pu_ed` 元素的值。然而，当将 **Output** 设置为 `Reactive power` 时，模块根据 `pu_ed`、`pu_eq`、`pu_id` 和 `pu_iq` 元素计算该值。

| 输出参数设置 | 输出值表达式 |
| --- | --- |
| `EMF phase A` | `pu_EMFa` |
| `EMF phase B` | `pu_EMFb` |
| `EMF phase C` | `pu_EMFc` |
| `Electrical torque` | `pu_torque` |
| `Rotor velocity` | `pu_velocity` |
| `Stator d-axis voltage` | `pu_vd` |
| `Stator q-axis voltage` | `pu_vq` |
| `Stator zero-sequence voltage` | `pu_v0` |
| `Stator d-axis current` | `pu_id` |
| `Stator q-axis current` | `pu_iq` |
| `Stator zero-sequence current` | `pu_i0` |
| `Apparent power` | pu\_Pt2+pu\_Qt2 |
| `Real power` | `pu_Pt = (pu_vd*pu_id) + (pu_vq*pu_iq) + 2(pu_v0*pu_i0)` |
| `Reactive power` | `pu_Qt = (pu_vq*pu_id) – (pu_vd*pu_iq)` |
| `Terminal voltage` | (pu\_vd2+​pu\_vq2) |
| `Terminal current` | (pu\_id2+pu\_iq2) |
| `Power factor angle` | `power_factor_angle = atan2(pu_Qt, pu_Pt)` |
| `Power factor` | `cos(power_factor_angle)` |
| `Load angle` | `load_angle(rad) = atan2(pu_vd, pu_vq)` |
| `Rotor electrical angle` | θe(t)=Nθr(t) |
