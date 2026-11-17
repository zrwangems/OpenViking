---
type: simulink-block
title: 'Velocity Profiler'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'velocityprofiler'
documentation_source_path: 'ref/velocityprofiler.html'
language: zh-CN
chinese_source: worker-translation
---

# Velocity Profiler

## 端口
```yaml
ports:
- name: Directions
  summary: 沿路径的行驶方向 *M*×1 向量，元素为 1（前进运动）和 –1（倒车运动）
  direction: input
- name: CumLengths
  summary: 累积路径长度 *M*×1 向量，元素为单调递增的实数值
  direction: input
- name: Curvatures
  summary: 沿路径的带符号路径曲率 *M*×1 实数值向量
  direction: input
- name: StartVelocity
  summary: 车辆在路径起点处的纵向速度 实数标量
  direction: input
- name: EndVelocity
  summary: 车辆在路径终点处的纵向速度 实数标量
  direction: input
- name: Velocities
  summary: 沿路径的速度剖面 *M*×1 实数值向量
  direction: output
- name: Times
  summary: 速度剖面的车辆到达时间 *M*×1 实数值向量
  direction: output
```

### 输入

### **Directions** — 沿路径的行驶方向 *M*×1 向量，元素为 1（前进运动）和 –1（倒车运动）

车辆沿路径长度的行驶方向，指定为 *M*×1 向量，元素为 1（前进运动）和 –1（倒车运动）。每个向量元素表示车辆在 **CumLengths** 输入端口指定的对应累积路径长度处的行驶方向。*M* 是行驶方向的数量，必须等于 **CumLengths** 和 **Curvatures** 输入的长度。

您可以从 Path Smoother Spline 模块的输出获取 **Directions**。

### **CumLengths** — 累积路径长度 *M*×1 向量，元素为单调递增的实数值

累积路径长度，以米为单位，指定为 *M*×1 向量，元素为单调递增的实数值。每个向量元素表示路径上的一个点。*M* 是累积路径长度的数量，必须等于 **Directions** 和 **Curvatures** 输入的长度。

您可以从 Path Smoother Spline 模块的输出获取 **CumLengths**。

### **Curvatures** — 沿路径的带符号路径曲率 *M*×1 实数值向量

沿路径长度的带符号路径曲率，以弧度每米为单位，指定为 *M*×1 实数值向量。每个向量元素表示路径在 **CumLengths** 输入端口指定的对应累积路径长度处的曲率。*M* 是曲率的数量，必须等于 **Directions** 和 **CumLengths** 输入的长度。

您可以从 Path Smoother Spline 模块的输出获取 **Curvatures**。

### **StartVelocity** — 车辆在路径起点处的纵向速度 实数标量

车辆在路径起点处的纵向速度，以米每秒为单位，指定为实数标量。

### **EndVelocity** — 车辆在路径终点处的纵向速度 实数标量

车辆在路径终点处的纵向速度，以米每秒为单位，指定为实数标量。
### 输出

### **Velocities** — 沿路径的速度剖面 *M*×1 实数值向量

沿路径长度的速度剖面，以米每秒为单位，以 *M*×1 实数值列向量形式返回。每个向量元素表示车辆在 **CumLengths** 输入端口指定的对应累积路径长度处的参考纵向速度。*M* 是速度的数量，等于 **CumLengths** 的长度。

输出速度值满足 Velocity Profiler 模块参数中指定的速度、加速度和加加速度约束。您可以将此输出用作车辆控制器的参考速度。

**Velocities** 是可变大小输出，其限制如 Variable-Size Signal Limitations (Simulink) 中所述。

### **Times** — 速度剖面的车辆到达时间 *M*×1 实数值向量

**Velocities** 中指定的速度剖面的车辆到达时间，以 *M*×1 实数值向量形式返回。*M* 是车辆到达时间的数量，等于 **Velocities** 的长度。单位为秒。

每个向量元素表示以速度 *v* 行驶的车辆到达累积路径长度 *p* 的时间，其中：

- *v* 是 **Velocities** 输出端口返回的对应速度。
- *p* 是 **CumLengths** 输入端口指定的对应累积路径长度。

使用 **Times** 可视化速度剖面随时间的变化，如 Velocity Profile of Straight Path 和 Velocity Profile of Path with Curve and Direction Change 示例所示。

**Times** 是可变大小输出，其限制如 Variable-Size Signal Limitations (Simulink) 中所述。

#### 依赖关系

要启用此端口，请选择 **Show Times output port** 参数。
## 参数
```yaml
parameters:
- name: Maximum longitudinal acceleration (m/s^2)
  summary: 车辆最大纵向加速度 3（默认值）| 正实数标量
  group: ''
- name: Maximum longitudinal deceleration (m/s^2)
  summary: 车辆最大纵向减速度 6（默认值）| 正实数标量
  group: ''
- name: Maximum allowable speed (m/s)
  summary: 沿路径的最大允许速度 10（默认值）| 正实数标量
  group: ''
- name: Maximum longitudinal jerk (m/s^3)
  summary: 最大纵向加加速度 1（默认值）| 正实数标量
  group: ''
- name: Maximum lateral acceleration (m/s^2)
  summary: 最大横向加速度 1（默认值）| 正实数标量
  group: ''
- name: Show Times output port
  summary: 输出速度剖面的到达时间 off（默认值）| on
  group: ''
- name: Sample time
  summary: 模块采样时间 -1（默认值）| 正实数标量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Code Generation（默认值）| Interpreted Execution
  group: ''
```

### **Maximum longitudinal acceleration (m/s^2)** — 车辆最大纵向加速度 `3`（默认值）| 正实数标量

车辆最大纵向加速度，以米每二次方秒为单位，指定为正实数标量。

在开发纵向控制器时，此参数必须等于 Longitudinal Controller Stanley 模块中的对应参数。否则，车辆无法运行生成的速度剖面。

### **Maximum longitudinal deceleration (m/s^2)** — 车辆最大纵向减速度 `6`（默认值）| 正实数标量

车辆最大纵向减速度，以米每二次方秒为单位，指定为正实数标量。

在开发纵向控制器时，此参数必须等于 Longitudinal Controller Stanley 模块中的对应参数。否则，车辆无法运行生成的速度剖面。

### **Maximum allowable speed (m/s)** — 沿路径的最大允许速度 `10`（默认值）| 正实数标量

车辆沿路径的最大允许速度，以米每秒为单位，指定为正实数标量。使用此参数可根据乘客舒适度或限速要求约束车辆速度。

当路径长度太短，车辆无法达到此最大速度时，模块会计算满足路径长度约束的较小最大速度。

在输出速度剖面中，车辆速度被约束在 [–*V*max, *V*max] 范围内，其中 *V*max 是此参数的值。

### **Maximum longitudinal jerk (m/s^3)** — 最大纵向加加速度 `1`（默认值）| 正实数标量

车辆沿路径的最大纵向加加速度，以米每三次方秒为单位，指定为正实数标量。

在输出速度剖面中，车辆的纵向加加速度被约束在 [–*J*max, *J*max] 范围内，其中 *J*max 是此参数的值。

### **Maximum lateral acceleration (m/s^2)** — 最大横向加速度 `1`（默认值）| 正实数标量

车辆沿路径的最大横向加速度，以米每二次方秒为单位，指定为正实数标量。

在输出速度剖面中，车辆的横向加速度被约束在 [–*A*max, *A*max] 范围内，其中 *A*max 是此参数的值。

### **Show Times output port** — 输出速度剖面的到达时间 `off`（默认值）| `on`

选择此参数以启用 **Times** 输出端口。

### **Sample time** — 模块采样时间 `-1`（默认值）| 正实数标量

模块的采样时间，以秒为单位，指定为 `-1` 或正实数标量。默认值 `-1` 表示模块从上游模块继承其采样时间。

由于 Velocity Profiler 模块输出可变大小信号，模块的采样时间必须为离散（非零）。如果模块从上游模块继承其采样时间，则这些模块也必须具有离散采样时间。

### **Simulate using** — 要运行的仿真类型 `Code Generation`（默认值）| `Interpreted Execution`

- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C/C++ 代码。只要模型不更改，C 代码就会在后续仿真中重用。此选项需要额外的启动时间。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
## 所属库

Automated Driving Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

在给定运动学约束的情况下生成车辆路径的速度剖面

Velocity Profiler 模块生成满足以下指定运动学约束集的行驶路径速度剖面：

- 车辆的最大允许速度
- 车辆的最大纵向加速度和减速度
- 车辆的最大纵向加加速度
- 车辆的最大横向加速度

指定沿路径的累积长度以及路径上每个点处的行驶方向和曲率。您可以从 Path Smoother Spline 模块的输出获取这些值。还需指定车辆在路径起点和终点处的纵向速度。

将生成的速度剖面用作纵向控制器的输入参考速度，如 Automated Parking Valet in Simulink 示例所示。
