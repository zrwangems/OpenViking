---
type: simulink-block
title: 'Vehicle Path Planner System'
family: 'mpc'
product_id: 'mpc'
product_name: 'Model Predictive Control Toolbox'
documentation_release: R2025b
official_category: 'Automated Driving'
documentation_page: 'vehiclepathplannersystem'
documentation_source_path: 'ref/vehiclepathplannersystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Path Planner System

## 端口

### 输入

### **Pose** — 初始车辆位姿三元行向量

将初始车辆位姿指定为向量信号
[*x*0
*y*0
*θ*0]，其中：

- (*x*0,
  *y*0) 是车辆后轴中心的初始位置。
- *θ*0 是初始车辆偏航角。

### **Target Pose** — 目标车辆位姿三元行向量

将目标车辆位姿指定为向量信号
[*xt*
*yt*
*θt*]，其中：

- (*xt*,
  *yt*) 是车辆后轴中心的目标位置。
- *θt* 是初始车辆偏航角。

### **Enable** — 启用规划逻辑标量

要使用当前位姿、目标位姿和障碍物规划路径，请将此信号设置为正值以启用路径规划器。

规划完成后，将启用信号设置为零，这将重置非线性 MPC 控制器。

路径规划器模块启用的时间必须：

- 长于规划器的最坏情况执行时间。为保证最坏情况执行时间，请通过选择 **Use suboptimal solution** 参数，将规划控制器配置为在指定的最大迭代次数后应用次优解。
- 短于控制器的采样时间，如使用 **Sample time** 参数所指定。

### **Obstacles** — 障碍物列表五列矩阵

将障碍物信息指定为具有 *N* 行的矩阵，其中
*N* 等于 **Number of obstacles**
参数。每行按顺序
[*X*
*Y*
*Φ*
*L*
*W*] 包含障碍物的以下信息：

- (*X*, *Y*) — 位置，以米为单位指定
- *Φ* — 偏航角，以弧度为单位指定
- *L* — 长度，以米为单位指定
- *W* — 宽度，以米为单位指定

#### 依赖

要启用此端口，请选择对应的 **Use external
source** 参数。

### **Velocity range** — 速度范围二元向量

车辆速度范围，以米每秒为单位，指定为二元行向量
[*Vmin*
*Vmax*]，其中：

- *Vmin* 是最小车辆速度。
- *Vmax* 是最大车辆速度。

#### 依赖

要启用此端口，请选择对应的 **Use external
source** 参数。

### **Steering angle range** — 前轮转向角范围二元向量

前轮转向角范围，以弧度为单位，指定为二元行向量
[*ψmin*
*ψmax*]，其中：

- *ψmin* 是最小转向角。
- *ψmax* 是最大转向角。

前轮转向角是前轮与车辆纵轴之间的夹角。转向角朝向自车正横向轴方向为正。

#### 依赖

要启用此端口，请选择对应的 **Use external
source** 参数。
### 输出

### **Path** — 规划车辆路径三列矩阵

规划车辆路径，输出为三列矩阵。每行包含沿车辆路径的一个车辆位姿 [*x*
*y*
*θ*]，其中：

- (*x*, *y*) 是车辆后轴中心的位置。
- *θ* 是车辆偏航角。

### **Exitflag** — 优化状态整数

非线性 MPC 控制器的优化状态，输出为整数，如下所示：

- 正值 — 找到最优解
- `0` — 达到最大优化迭代次数，解可能不是最优的
- 负值 — 不可行的优化问题

#### 依赖

要启用此端口，请选择 **Optimization status**
参数。

## 参数

#### 参数选项卡

### **Length** — 车辆长度 `4.7`（默认）| 非负标量

车辆长度，以米为单位指定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `egoLength` |
| **类型：** string, character vector |
| **默认：** `"4.7"` |

### **Width** — 车辆宽度 `1.8`（默认）| 非负标量

车辆宽度，以米为单位指定。

#### 编程用法

|  |
| --- |
| **模块参数：** `egoWidth` |
| **类型：** string, character vector |
| **默认值：** `"1.8"` |

### **Wheelbase** — 前后轴之间的距离 `2.8`（默认）| 非负标量

前后轴之间的距离，以米为单位指定。

#### 编程用法

|  |
| --- |
| **模块参数：** `wheelbase` |
| **类型：** string, character vector |
| **默认值：** `"2.8"` |

### **Center to rear axle** — 从车辆中心到后轴的距离 `1.4`（默认）| 非负标量

从车辆中心到后轴的纵向距离，以米为单位指定。

#### 编程用法

|  |
| --- |
| **模块参数：** `dist2Center` |
| **类型：** string, character vector |
| **默认值：** `"1.4"` |

### **Number of obstacles** — 环境中的障碍物数量 `0`（默认）| 非负整数

环境中的障碍物数量。

#### 编程用法

|  |
| --- |
| **模块参数：** `numObs` |
| **类型：** string, character vector |
| **默认值：** `"0"` |

### **Obstacle list** — 环境中的障碍物 `zeros(1,5)`（默认）| 五列矩阵

将障碍物信息指定为一个包含 *N* 行的矩阵，其中
*N* 等于 **Number of obstacles**
参数。每一行按以下顺序包含某个障碍物的信息
[*X*
*Y*
*Φ*
*L*
*W*]：

- (*X*, *Y*) — 位置，以
  米为单位指定
- *Φ* — 偏航角，以弧度为单位指定
- *L* — 长度，以米为单位指定
- *W* — 宽度，以米为单位指定

如果障碍物的位置和方向随时间变化，请通过选择 **Use
external source** 向模块添加
**Obstacles** 输入端口。

#### 依赖关系

要启用此参数，请将 **Number of obstacles**
参数设置为非零值。

#### 编程用法

|  |
| --- |
| **模块参数：** `obsMat` |
| **类型：** string, character vector |
| **默认值：** `"zeros(1,5)"` |

#### 编程用法：Use external source

|  |
| --- |
| **模块参数：** `obs_ext` |
| **类型：** string, character vector |
| **值：** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Minimum distance from ego vehicle to obstacles** — 车辆与任何障碍物之间的最小安全距离 `0.1`（默认）| 正标量

自车与环境中任何障碍物之间的最小安全距离，
以米为单位指定。

#### 依赖关系

要启用此参数，请将 **Number of obstacles**
参数设置为非零值。

#### 编程用法

|  |
| --- |
| **模块参数：** `minDist` |
| **类型：** string, character vector |
| **默认值：** `"0.1"` |

### **Sample time** — 控制器采样时间 `1`（默认）| 正标量

控制器采样时间，以秒为单位指定。

#### 编程用法

|  |
| --- |
| **模块参数：** `Ts` |
| **类型：** string, character vector |
| **默认值：** `"1"` |

### **Prediction horizon** — 预测时域 `20`（默认）| 正整数

用于规划的预测时域步数。总预测时间等于
采样时间与预测时域的乘积。

#### 编程用法

|  |
| --- |
| **模块参数：** `pPlanning` |
| **类型：** string, character vector |
| **默认值：** `"20"` |

### **Velocity range** — 速度范围 `[-6.5 6.5]`（默认）| 二元素行向量

车辆速度范围，以米每秒为单位，指定为二元素行向量
[*Vmin*
*Vmax*]，其中：

- *Vmin* 是最小车辆
  速度。
- *Vmax* 是最大车辆
  速度。

如果速度范围随时间变化，请通过选择 **Use external source**
向模块添加 **Velocity range**
输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `v_range` |
| **类型：** string, character vector |
| **默认值：** `"[-6.5,6.5]"` |

#### 编程用法：Use external source

|  |
| --- |
| **模块参数：** `v_ext` |
| **类型：** string, character vector |
| **值：** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Steering angle range** — 前轮转向角范围 `[-pi/4 pi/4]` | 二元素行向量

前轮转向角范围，以弧度为单位，指定为二元素行向量
[*ψmin*
*ψmax*]，其中：

- *ψmin* 是最小转向角。
- *ψmax* 是最大转向角。

前轮转向角是前轮相对于车辆纵轴的角度。转向角朝向自车正横向轴方向为正。

如果转向角范围随时间变化，请通过选择 **Use external source** 将 **Steering angle range** 输入端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`steer_range` |
| **类型**：string, character vector |
| **默认值**：`"[-pi/4,pi/4]"` |

#### Programmatic Use: Use external source

|  |
| --- |
| **模块参数**：`steer_ext` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

#### Block Tab

### **Use suboptimal solution** — 在指定迭代次数后应用次优解 `off`（默认）| `on`

将控制器配置为在指定的最大迭代次数后应用次优解，这保证了规划控制器的最坏情况执行时间。要设置最大迭代次数，请使用 **Maximum iteration number** 参数。

有关详细信息，请参阅 Suboptimal QP Solution。

#### 编程使用

|  |
| --- |
| **模块参数**：`suboptimal` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **Maximum iteration number** — 最大优化迭代次数 `200`（默认）| 正整数

最大优化迭代次数。

#### 依赖关系

要启用此参数，请选择 **Use suboptimal solution** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`maxIter` |
| **类型**：string, character vector |
| **默认值**：`"200"` |

### **Optimization status** — 添加优化状态输出端口 off（默认）| on

选择此参数可将 **Exitflag** 输出端口添加到模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`output_exitflag` |
| **类型**：string, character vector |
| **值**：`"off"` | `"on"` |
| **默认值**：`"off"` |

### **Create VPP subsystem** — 创建自定义规划器 按钮

生成自定义 VPP 子系统，您可以针对自己的应用进行修改。自定义控制器的配置数据将作为结构体导出到 MATLAB® 工作区。

## 所属库

Model Predictive Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 不支持单精度或定点计算的代码生成。
- 在“配置参数”对话框中，在 **Code Generation > Interface** 窗格上，必须选择以下参数。

  - **Support non-finite numbers** — 默认情况下已选中此参数。
  - **Support variable-size signals**（使用 Embedded Coder® 时）— 默认情况下未选中此参数。

## 版本历史

**在 R2022b 中引入**

## 描述

规划从初始位姿到目标位姿的无碰撞路径

Vehicle Path Planner System 模块模拟车辆路径规划器（VPP）系统，该系统使用多级非线性 MPC 控制器规划从初始位姿到目标位姿的无碰撞轨迹。您可以使用此模块为车辆规划路径，例如进出停车位的车辆或在仓库中移动的机器人。

规划路径后，您可以让车辆使用路径跟随控制系统跟踪该路径。

要自定义控制器，例如修改控制器代价函数或更改控制器初始条件，请点击 **Create VPP subsystem**。
