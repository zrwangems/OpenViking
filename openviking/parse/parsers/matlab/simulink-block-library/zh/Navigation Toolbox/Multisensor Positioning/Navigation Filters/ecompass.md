---
type: simulink-block
title: 'ecompass'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Navigation Filters'
documentation_page: 'ecompassblock'
documentation_source_path: 'ref/ecompassblock.html'
language: zh-CN
chinese_source: worker-translation
---

# ecompass

## 端口
```yaml
ports:
- name: Accel
  summary: 加速度计读数 *N*×3 的实数标量矩阵
  direction: input
  data_types: single | double
- name: Mag
  summary: 磁力计读数 *N*×3 的实数标量矩阵
  direction: input
  data_types: single | double
- name: Orientation
  summary: 将量从全局坐标系旋转到传感器机体坐标系的姿态 *N*×4 的四元数矩阵（默认）| 3×3×*N* 的数组
  direction: output
  data_types: single | double
```

### 输入

### **Accel** — 加速度计读数 *N*×3 的实数标量矩阵

传感器机体坐标系下的加速度计读数，单位为 m/s2，指定为 *N*×3 的实数标量矩阵。矩阵的列对应于传感器机体的 *x* 轴、*y* 轴和 *z* 轴。矩阵中的行 *N* 对应于各个采样点。

**数据类型：** `single` | `double`

### **Mag** — 磁力计读数 *N*×3 的实数标量矩阵

传感器机体坐标系下的磁力计读数，单位为 µT，指定为 *N*×3 的矩阵。矩阵的列对应于传感器机体的 *x* 轴、*y* 轴和 *z* 轴。矩阵中的行 *N* 对应于各个采样点。

**数据类型：** `single` | `double`

### 输出

### **Orientation** — 将量从全局坐标系旋转到传感器机体坐标系的姿态 *N*×4 的四元数矩阵（默认）| 3×3×*N* 的数组

可将量从全局坐标系旋转到传感器机体坐标系的姿态，返回为 *N*×4 的四元数矩阵或 3×3×*N* 的旋转矩阵数组。*N* 表示采样点数。姿态是将量从局部导航坐标系变换到机体坐标系的旋转。

- 如果 **Orientation format** 指定为 `quaternion`，模块返回姿态为 *N*×4 的四元数矩阵。
- 如果 **Orientation format** 指定为 `Rotation matrix`，模块返回姿态为 3×3×*N* 的旋转矩阵数组。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Reference frame
  summary: 导航参考坐标系 NED（默认）| ENU
  group: ''
- name: Orientation format
  summary: 用于描述姿态的格式 quaternion（默认）| Rotation matrix
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Reference frame** — 导航参考坐标系 `NED`（默认）| `ENU`

导航参考坐标系，指定为 `NED`（北-东-地坐标系）或 `ENU`（东-北-天坐标系）。

### **Orientation format** — 用于描述姿态的格式 `quaternion`（默认）| `Rotation matrix`

用于描述姿态的格式，指定为 `'quaternion'` 或 `'Rotation matrix'`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。如果模型未更改，C 代码将在后续仿真中重用。此选项需要额外的启动时间。
## 所属库

Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Navigation Filters Navigation Toolbox / Multisensor Positioning / Navigation Filters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

根据加速度计和磁力计读数计算姿态

ecompass Simulink® 模块使用加速度计和磁力计读数计算姿态。您可以使用计算得到的姿态将量从全局坐标系旋转到传感器机体坐标系。
