---
type: simulink-block
title: 'Constant Volume Chamber (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'constantvolumechamberil'
documentation_source_path: 'ref/constantvolumechamberil.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Volume Chamber (IL)

## 端口

### 守恒

### **A** — 腔室入口等温液体

与腔室入口关联的等温液体守恒端口。

## 参数

### **腔室体积** — 腔室内流体的体积 `0.001 m^3`（默认） | 正标量

腔室内流体的体积。该体积在仿真期间保持不变。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有一个端口且包含固定体积等温液体的腔室

Constant Volume Chamber (IL) 模块对包含固定体积等温液体的腔室中的质量积聚进行建模。该腔室有一个入口，标记为 **A**。

腔室可以与所连接的等温液体网络交换质量。腔室内部的压力基于流体体积的可压缩性变化。

质量守恒将质量流量与表示流体体积的内部节点压力关联起来：

dρmixdpIp˙IV=m˙A,

其中：

- m˙A 是端口 **A** 处的质量流量。与端口关联的流量在流入模块时为正。
- *p*I 是腔室内部的压力。端口 **A** 与腔室内部之间没有流动阻力，因此，假定端口 **A** 处的压力等于该压力，*p*A = *p*I。
- *V* 是腔室内流体的体积。
- *ρ*mix 是流体混合物密度。

流体可以是纯液体和少量夹带空气的混合物，具体由连接到回路的 Isothermal Liquid Properties (IL) 模块指定。用于计算 *ρ*mix 的方程取决于所选的等温液体模型。有关详细信息，请参阅等温液体建模选项。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。

### 假设和限制

- 腔室壁完全刚性。
- 端口 **A** 与腔室内部之间没有流动阻力。
