---
type: simulink-block
title: 'Vector Field Histogram'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Control Algorithms'
documentation_page: 'vectorfieldhistogram'
documentation_source_path: 'ref/vectorfieldhistogram.html'
language: zh-CN
chinese_source: worker-translation
---

# Vector Field Histogram

## 端口
```yaml
ports:
- name: Ranges
  summary: 来自扫描数据的距离值，标量向量
  direction: input
- name: Angles
  summary: 来自扫描数据的角度值，标量向量
  direction: input
- name: TargetDir
  summary: 车辆的目标方向，标量
  direction: input
- name: SteerDir
  summary: 车辆的转向方向，标量
  direction: output
```

### 输入

### **Ranges** — 来自扫描数据的距离值，标量向量

来自扫描数据的距离值，指定为以米为单位的标量向量。这些距离值是在指定角度处距传感器的距离。该向量的长度必须与对应的 **Angles** 向量相同。

### **Angles** — 来自扫描数据的角度值，标量向量

来自扫描数据的角度值，指定为以弧度表示的标量向量。这些角度值是所指定距离对应的具体角度。该向量的长度必须与对应的 **Ranges** 向量相同。

### **TargetDir** — 车辆的目标方向，标量

车辆的目标方向，指定为以弧度表示的标量。车辆的前进方向视为零弧度，正角度按逆时针方向测量。当根据一组路点生成控制量时，可以使用 Pure Pursuit 模块的 **TargetDir** 输出。

### 输出

### **SteerDir** — 车辆的转向方向，标量

车辆的转向方向，指定为以弧度表示的标量。该无障碍方向基于 VFH+ 算法计算。车辆的前进方向视为零弧度，正角度按逆时针方向测量。
## 参数
```yaml
parameters:
- name: Number of angular sectors
  summary: 用于创建直方图的分箱数量 180（默认）| 标量
  group: ''
- name: Range distance limits (m)
  summary: 距离读数的限值 [0.05 2]（默认）| 由标量组成的二元素向量
  group: ''
- name: Histogram thresholds
  summary: 用于计算二值直方图的阈值 [3 10]（默认）| 由标量组成的二元素向量
  group: ''
- name: vehicle radius (m)
  summary: 车辆的半径 0.1（默认）| 标量
  group: ''
- name: Safety distance (m)
  summary: 车辆周围的安全距离 0.1（默认）| 标量
  group: ''
- name: Minimum turning radius (m)
  summary: 当前速度下的最小转弯半径 0.1（默认）| 标量
  group: ''
- name: Simulate using
  summary: 指定要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
- name: Target direction weight
  summary: 目标方向的代价函数权重 5（默认）| 标量
  group: ''
- name: Current direction weight
  summary: 当前方向的代价函数权重 2（默认）| 标量
  group: ''
- name: Previous direction weight
  summary: 前一方向的代价函数权重 2（默认）| 标量
  group: ''
```

#### 主

### **Number of angular sectors** — 用于创建直方图的分箱数量 `180`（默认）| 标量

用于创建直方图的分箱数量，指定为标量。此参数不可调。只能在对象初始化时设置此参数。

### **Range distance limits (m)** — 距离读数的限值 `[0.05 2]`（默认）| 由标量组成的二元素向量

距离读数的限值，以米为单位，指定为由标量组成的二元素向量。仅当距离读数落在距离限值内时才会被考虑。使用较低距离限值可忽略因传感器在较近距离处性能不佳而产生的误报。使用上限可忽略距离车辆过远的障碍物。

### **Histogram thresholds** — 用于计算二值直方图的阈值 `[3 10]`（默认）| 由标量组成的二元素向量

用于计算二值直方图的阈值，指定为由标量组成的二元素向量。该算法使用这些阈值根据极坐标障碍物密度计算二值直方图。高于上限阈值的极坐标障碍物密度值在二值直方图中表示为占用空间 (1)。小于下限阈值的值表示为自由空间 (0)。介于限值之间的值，如果先前迭代中存在已计算的二值直方图，则设置为该先前计算的二值直方图的值。如果不存在先前的直方图，则该值设置为自由空间 (0)。

### **vehicle radius (m)** — 车辆的半径 `0.1`（默认）| 标量

车辆的半径，指定为以米为单位的标量。此尺寸定义了可以外接车辆的最小圆。在计算无障碍方向时，车辆半径用于考虑车辆大小。

### **Safety distance (m)** — 车辆周围的安全距离 `0.1`（默认）| 标量

除 **vehicle radius** 之外，在车辆位置周围保留的安全距离，指定为以米为单位的标量。车辆半径和安全距离用于计算无障碍方向。

### **Minimum turning radius (m)** — 当前速度下的最小转弯半径 `0.1`（默认）| 标量

车辆以其当前速度行驶时的最小转弯半径，指定为以米为单位的标量。

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真将复用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。

**Tunable:** No

#### Cost Function Weights

### **Target direction weight** — 目标方向的代价函数权重 `5`（默认）| 标量

朝目标方向移动的代价函数权重，指定为标量。要跟随目标方向，请将此权重设置为高于 **Current direction weight** 与 **Previous direction weight** 之和。要忽略目标方向代价，请将此权重设置为 `0`。

### **Current direction weight** — 当前方向的代价函数权重 `2`（默认）| 标量

使车辆沿当前航向方向移动的代价函数权重，指定为标量。此权重值越高，生成的路径越高效。要忽略当前方向代价，请将此权重设置为 `0`。

### **Previous direction weight** — 前一方向的代价函数权重 `2`（默认）| 标量

沿先前选定的转向方向移动的代价函数权重，指定为标量。此权重值越高，生成的路径越平滑。要忽略前一方向代价，请将此权重设置为 `0`。
## 所属库

Navigation Toolbox / Control Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用向量场直方图避障

Vector Field Histogram (VFH) 模块使您的车辆能够基于距离传感器数据避开障碍物。给定以距离和角度表示的距离传感器读数，以及要驶向的目标方向，VFH 控制器会计算无碰撞的转向方向。

有关算法细节的更多信息，请参阅 Algorithms 下的 Vector Field Histogram。
