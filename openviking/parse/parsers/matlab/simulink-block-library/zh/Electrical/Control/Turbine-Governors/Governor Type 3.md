---
type: simulink-block
title: 'Governor Type 3'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Turbine-Governors'
documentation_page: 'governortype3'
documentation_source_path: 'ref/governortype3.html'
language: zh-CN
chinese_source: worker-translation
---

# Governor Type 3

## 端口
```yaml
ports:
- name: speed_pu
  summary: 涡轮转速标量
  direction: input
  data_types: single | double
- name: Pref
  summary: 转速参考偏置标量
  direction: input
  data_types: single | double
- name: Pmech
  summary: 机械功率标量
  direction: output
  data_types: single | double
```

### 输入

### **speed\_pu** — 涡轮转速标量

涡轮转速，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **Pref** — 转速参考偏置标量

转速负载参考的偏置，指定为标量。将此端口连接到涡轮负载控制器模块（例如 Controller LCFB1 模块）的 **Pref** 输出端口。

**数据类型：** `single` | `double`
### 输出

### **Pmech** — 机械功率标量

机械功率，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Speed reference (pu)
  summary: 转速参考 1（默认）| 标量
  group: 常规
- name: Initial torque (pu)
  summary: 初始转矩 0.45（默认）| 标量
  group: 常规
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: 常规
- name: Gate servomotor time constant, T_g (s)
  summary: 闸门伺服电机时间常数 0.52（默认）| 标量
  group: 调速器
- name: Pilot value time constant, T_p (s)
  summary: 导阀值时间常数 0.07（默认）| 标量
  group: 调速器
- name: Opening gate rate limit, U_o (pu/s)
  summary: 开启闸门速率限值 0.15（默认）| 标量
  group: 调速器
- name: Closing gate rate limit, U_c (pu/s)
  summary: 关闭闸门速率限值 -0.15（默认）| 标量
  group: 调速器
- name: Maximum gate position, on MVA capability, P_max (pu)
  summary: 闸门最大位置 0.75（默认）| 标量
  group: 调速器
- name: Minimum gate position, on MVA capability, P_min (pu)
  summary: 闸门最小位置 0（默认）| 标量
  group: 调速器
- name: Permanent speed droop coefficient, R_perm (pu)
  summary: 永态转速下降系数 0.05（默认）| 标量
  group: 调速器
- name: Transient speed droop coefficient, R_temp (pu)
  summary: 暂态转速下降系数 0.6（默认）| 标量
  group: 调速器
- name: Governor time constant, T_r (s)
  summary: 调速器时间常数 25（默认）| 标量
  group: 调速器
- name: Water starting time constant, T_w (s)
  summary: 水流启动时间常数 5（默认）| 标量
  group: 调速器
- name: Penstock coefficient, a_11
  summary: 压力管道动态系数 0.75（默认）| 标量
  group: 调速器
- name: Penstock coefficient, a_13
  summary: 压力管道动态系数 0.75（默认）| 标量
  group: 调速器
- name: Penstock coefficient, a_21
  summary: 压力管道动态系数 0.75（默认）| 标量
  group: 调速器
- name: Penstock coefficient, a_23
  summary: 压力管道动态系数 0.75（默认）| 标量
  group: 调速器
```

### 常规

### **Speed reference (pu)** — 转速参考 `1`（默认）| 标量

标幺转速参考。

### **Initial torque (pu)** — 初始转矩 `0.45`（默认）| 标量

仿真开始时的标幺初始转矩。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### 调速器

### **Gate servomotor time constant, T\_g (s)** — 闸门伺服电机时间常数 `0.52`（默认）| 标量

闸门伺服电机的时间常数，以秒为单位。

### **Pilot value time constant, T\_p (s)** — 导阀值时间常数 `0.07`（默认）| 标量

导阀值的时间常数，以秒为单位。此参数与图中标记为“Low-Pass Filter”的模块相关联。

### **Opening gate rate limit, U\_o (pu/s)** — 开启闸门速率限值 `0.15`（默认）| 标量

开启闸门速率的标幺限值。此参数与图中标记为“Low-Pass Filter”的模块相关联。

### **Closing gate rate limit, U\_c (pu/s)** — 关闭闸门速率限值 `-0.15`（默认）| 标量

关闭闸门速率的标幺限值。此参数与图中标记为“Low-Pass Filter”的模块相关联。

### **Maximum gate position, on MVA capability, P\_max (pu)** — 闸门最大位置 `0.75`（默认）| 标量

基于 MVA 能力的闸门最大标幺位置。

### **Minimum gate position, on MVA capability, P\_min (pu)** — 闸门最小位置 `0`（默认）| 标量

基于 MVA 能力的闸门最小标幺位置。

### **Permanent speed droop coefficient, R\_perm (pu)** — 永态转速下降系数 `0.05`（默认）| 标量

标幺永态转速下降系数。

### **Transient speed droop coefficient, R\_temp (pu)** — 暂态转速下降系数 `0.6`（默认）| 标量

标幺暂态转速下降系数。此参数与图中标记为“Filtered Derivative”的模块相关联。

### **Governor time constant, T\_r (s)** — 调速器时间常数 `25`（默认）| 标量

调速器的时间常数。此参数与图中标记为“Filtered Derivative”的模块相关联。

### **Water starting time constant, T\_w (s)** — 水流启动时间常数 `5`（默认）| 标量

水惯性时间常数。此参数与图中标记为“Lead-Lag”的模块相关联。

### **Penstock coefficient, a\_11** — 压力管道动态系数 `0.75`（默认）| 标量

压力管道动态的系数。此参数与图中标记为“Lead-Lag”的模块相关联。

### **Penstock coefficient, a\_13** — 压力管道动态系数 `0.75`（默认）| 标量

压力管道动态的系数。此参数与图中标记为“Lead-Lag”的模块相关联。

### **Penstock coefficient, a\_21** — 压力管道动态系数 `0.75`（默认）| 标量

压力管道动态的系数。此参数与图中标记为“Lead-Lag”的模块相关联。

### **Penstock coefficient, a\_23** — 压力管道动态系数 `0.75`（默认）| 标量

压力管道动态的系数。此参数与图中标记为“Lead-Lag”的模块相关联。
## 所属库

Simscape / Electrical / Control / Turbine-Governors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

IEEE 3 型线性化调速水轮机模型

Governor Type 3 模块对具有压力管道动态的 IEEEG3 水轮机调速器进行建模。

此模块具有比 Governor Type 1 模块更详细的调速器模型，并使用水轮机（或水柱）模型的线性化模型以及压力管道动态。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将调速器配置为连续时间，请将 **Sample time (-1 for inherited)** 属性设置为 `0`。要将调速器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正非零值，或设置为 `-1` 以从上游模块继承采样时间。

此图说明了模块的整体结构：
