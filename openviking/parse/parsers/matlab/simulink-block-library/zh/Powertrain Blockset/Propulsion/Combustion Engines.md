---
type: simulink-block
title: 'Propulsion'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion'
documentation_page: 'propulsion'
documentation_source_path: 'propulsion.html'
language: zh-CN
chinese_source: worker-translation
---

# Propulsion

Propulsion

内燃机、电动机和控制器

动力总成中的推进系统包括内燃机火花点火（SI）发动机、压缩点火（CI）发动机和电动机。使用推进模块来组装发动机子系统和控制器，用于硬件在环（HIL）发动机控制设计、整车级燃油经济性和性能仿真。

## 模块

### 内燃机、组件和控制器

#### 发动机和控制器

|  |  |
| --- | --- |
| Mapped CI Engine | 使用查找表的压缩点火发动机模型 |
| Mapped SI Engine | 使用查找表的火花点火发动机模型 |
| Simple Engine | 使用查找表的简化发动机模型 *(自 R2021b 起)* |
| CI Controller | 包含空气质量流量、扭矩和 EGR 估计的压缩点火控制器 |
| SI Controller | 使用驾驶员扭矩请求的火花点火发动机控制器 |

#### 组件

|  |  |
| --- | --- |
| CI Core Engine | 从进气口到排气口的压缩点火发动机 |
| SI Core Engine | 从进气口到排气口的火花点火发动机 |
| Mapped Core Engine | 使用查找表的稳态核心发动机模型 |
| Boost Drive Shaft | 增压驱动轴转速 |
| Compressor | 增压发动机的压缩机 |
| Control Volume System | 带传热的定容开放热力学系统 |
| Flow Boundary | 环境温度和压力的流动边界 |
| Flow Restriction | 通过孔口的等熵理想气体流动 |
| Heat Exchanger | 中冷器或废气再循环（EGR）冷却器 |
| Turbine | 增压发动机的涡轮 |

### 电动机、逆变器和控制器

#### 电动机和逆变器

|  |  |
| --- | --- |
| Flux-Based PMSM | 基于磁链的永磁同步电机 |
| Induction Motor | 三相感应电机 |
| Interior PMSM | 具有正弦反电动势的三相内置式永磁同步电机 |
| Mapped Motor | 在扭矩控制模式下运行的映射电机和驱动电子设备 |
| Surface Mount PMSM | 具有正弦反电动势的三相表贴式永磁同步电机 |
| Three-Phase Voltage Source Inverter | 三相电压源逆变器 |

#### 控制器

|  |  |
| --- | --- |
| Equivalent Consumption Minimization Strategy | 用于 P0–P4 混合动力电动汽车的能量管理控制器 |
| Flux-Based PM Controller | 用于基于磁链的永磁同步电机的控制器 |
| IM Controller | 用于感应电机的基于内部扭矩的磁场定向控制器，带有可选的外环速度控制器 |
| Interior PM Controller | 用于内置式永磁同步电机的基于扭矩的磁场定向控制器 |
| Surface Mount PM Controller | 用于表贴式永磁同步电机的基于扭矩的磁场定向控制器 |

## 主题

### Engines

- **Calibrate and Resize Engines and Electric Motors**
  使用参考应用和虚拟车辆 composer 来校准和调整发动机与电动机的尺寸。
- **使用测功机测试台架校准、验证和优化 CI 发动机**
  使用 CI 发动机测功机参考应用，在测功机测试 harness 下仿真压缩点火（CI）发动机和控制器。
- **使用测功机测试台架校准、验证和优化 SI 发动机**
  使用 SI 发动机测功机参考应用，在测功机测试 harness 下仿真火花点火（SI）发动机和控制器。
- **使用测功机测试台架校准、验证和优化 SI H2 发动机**
  使用 SI H2 发动机测功机参考应用，在测功机测试 harness 下仿真氢燃料火花点火（SI）发动机和控制器。
- **为客观的混合动力车辆燃油经济性评估校准 ECMS 模块**
  在 HEV P2 参考应用中校准等效消耗最小化策略模块。

### Electric Motors

- **使用测功机测试台架开发、调整尺寸和校准电机**
  使用电机测功机参考应用开发控制测试台、调整 e-motors 尺寸并校准控制器。
- **为永磁同步电机生成最优电流控制器校准表**

  为永磁同步电机（PMSM）模块生成优化的电流控制器和磁通参数。

  - STEP 1: **Generate Current Controller Parameters**
  - STEP 2: **Generate Feed-Forward Flux Parameters**
  - 步骤 3：**为基于磁链的 PMSM 模块生成参数**

## Related Information

- **Engine Calibration Maps**
- **使用电机控制模块集参数估计工具估计电机参数（电机控制模块集）**

## Featured Examples

Build Conventional Vehicle Model

### Build Conventional Vehicle Model

使用传统车辆参考应用构建带有内燃机的车辆。

使用数据校准映射电机

### 使用数据校准映射电机

使用 Virtual Vehicle Composer 根据导入的数据校准映射电动机。

使用数据校准映射 CI 发动机

### 使用数据校准映射 CI 发动机

使用 Virtual Vehicle Composer 根据导入的数据校准映射 CI 发动机。

使用数据校准映射 SI 发动机

### 使用数据校准映射 SI 发动机

使用 Virtual Vehicle Composer 根据导入的数据校准映射 SI 发动机。

Detect Misfires Using On-Board Diagnostics

### Detect Misfires Using On-Board Diagnostics

实现车载诊断（OBD）以检测并报告发动机失火。

- Open Model

Resize CI Engines

### Resize CI Engines

使用测功机参考应用调整压缩点火（CI）发动机的尺寸。

Resize SI Engines

### Resize SI Engines

使用测功机参考应用调整火花点火（SI）发动机的尺寸。

Resize Electric Motors

### Resize Electric Motors

使用测功机参考应用调整电机尺寸。

读取和写入模块参数到 Excel

### 读取和写入模块参数到 Excel

读取数据并将 Mapped SI Engine 模块参数写入 Excel® 数据文件。

- Open Live Script

## MATLAB 命令

您点击了一个对应于以下 MATLAB 命令的链接：

在 MATLAB Command Window 中输入该命令以运行它。
Web 浏览器不支持 MATLAB 命令。

Close

MathWorks
MathWorks

Select a Web Site

选择一个网站以获取可用的翻译内容并查看本地活动和优惠。根据您的位置，我们建议您选择：

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择一个网站

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站未针对您所在位置的访问进行优化。

Americas

- América Latina (Español)
- Canada (English)
- United States (English)

Europe

- Belgium (English)
- Denmark (English)
- Deutschland (Deutsch)
- España (Español)
- Finland (English)
- France (Français)
- Ireland (English)
- Italia (Italiano)
- Luxembourg (English)

- Netherlands (English)
- Norway (English)
- Österreich (Deutsch)
- Portugal (English)
- Sweden (English)
- Switzerland
  - Deutsch
  - English
  - Français
- United Kingdom (English)

Asia Pacific

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

Contact your local office
