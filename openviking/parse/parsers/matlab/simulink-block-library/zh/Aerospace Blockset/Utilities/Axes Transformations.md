---
type: simulink-block
title: 'Axes Transformations'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'axes-transformations-1'
documentation_source_path: 'axes-transformations-1.html'
language: zh-CN
chinese_source: worker-translation
---

# Axes Transformations

Axes Transformations

将坐标系的轴变换为不同类型，例如将欧拉角变换为四元数

将坐标系的轴变换为不同类型，例如将欧拉角变换为四元数

## 模块

### 机体/风轴变换

|  |  |
| --- | --- |
| Direction Cosine Matrix Body to Wind | 将迎角和侧滑角转换为方向余弦矩阵 |
| Direction Cosine Matrix Body to Wind to Alpha and Beta | 将方向余弦矩阵转换为迎角和侧滑角 |
| Direction Cosine Matrix to Quaternions | 将方向余弦矩阵转换为四元数向量 |
| Direction Cosine Matrix to Rodrigues | 将方向余弦矩阵转换为 Euler-Rodrigues 向量 |
| Direction Cosine Matrix to Rotation Angles | 将方向余弦矩阵转换为旋转角 |
| Direction Cosine Matrix to Wind Angles | 将方向余弦矩阵转换为风角 |
| Quaternions to Direction Cosine Matrix | 将四元数向量转换为方向余弦矩阵 |
| Quaternions to Rodrigues | 将四元数转换为 Euler-Rodrigues 向量 |
| Quaternions to Rotation Angles | 从四元数确定旋转向量 |
| Rodrigues to Direction Cosine Matrix | 将 Euler-Rodrigues 向量转换为方向余弦矩阵 |
| Rodrigues to Quaternions | 将 Euler-Rodrigues 向量转换为四元数 |
| Rodrigues to Rotation Angles | 将 Euler-Rodrigues 向量转换为旋转角 |
| Rotation Angles to Direction Cosine Matrix | 将旋转角转换为方向余弦矩阵 |
| Rotation Angles to Quaternions | 从旋转角计算四元数 |
| Rotation Angles to Rodrigues | 将旋转角转换为 Euler-Rodrigues 向量 |
| Wind Angles to Direction Cosine Matrix | 将风角转换为方向余弦矩阵 |

### 大地坐标变换

|  |  |
| --- | --- |
| Direction Cosine Matrix ECEF to NED | 将大地纬度和经度转换为方向余弦矩阵 |
| Direction Cosine Matrix ECEF to NED to Latitude and Longitude | 将方向余弦矩阵转换为大地纬度和经度 |
| Direction Cosine Matrix ECI to ECEF | 将地心惯性（ECI）坐标转换为地心地球固连（ECEF）坐标 |
| ECEF Position to LLA | 从地心地球固连（ECEF）位置计算大地纬度、经度和行星椭球上的高度 |
| ECI Position to AER | 将地心惯性（ECI）坐标转换为方位坐标 |
| ECI Position to LLA | 将地心惯性（ECI）坐标转换为大地纬度、经度、高度（LLA）坐标 |
| Flat Earth to LLA | 从平面地球位置估计大地纬度、经度和高度 |
| Geodetic to Geocentric Latitude | 将大地纬度转换为地心纬度 |
| Geocentric to Geodetic Latitude | 将地心纬度转换为大地纬度 |
| LLA to ECEF Position | 从大地纬度、经度和行星椭球上的高度计算地心地球固连（ECEF）位置 |
| LLA to ECI Position | 将纬度、经度、高度（LLA）坐标转换为地心惯性（ECI）坐标 |
| LLA to Flat Earth | 从大地纬度、经度和高度估计平面地球位置 |

### 参考系变换

|  |  |
| --- | --- |
| Besselian Epoch to Julian Epoch | 将位置和速度分量从已停用的标准贝塞尔历元（B1950）变换为标准儒略历元（J2000） |
| Julian Epoch to Besselian Epoch | 将位置和速度分量从标准儒略历元（J2000）变换为已停用的标准贝塞尔历元（B1950） |

### 变换工具

|  |  |
| --- | --- |
| Delta UT1 | 根据国际天文学联合会（IAU）2000A 参考系统计算主世界时（UT1）与协调世界时（UTC）之间的差值 |

## 主题

### 关于航空航天坐标系

- **基本坐标系概念**

  在使用 Aerospace Blockset™ 软件时定义坐标系。

  - **用于建模的坐标系**
  - **用于导航的坐标系**
  - **用于显示的坐标系**

### 太阳时

- **计算 UT1 到 UTC 的值**
  根据国际地球自转服务（IERS）计算主世界时（UT1）与协调世界时（UTC）之间的差值。

## MATLAB 命令

您点击的链接对应于以下 MATLAB 命令：

请在 MATLAB 命令行窗口中输入该命令以运行它。
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

Select a Web Site

选择一个网站，以便在可提供翻译内容的地方获取翻译内容，并查看本地活动和优惠。根据您的位置，我们建议您选择：。

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择一个网站

**How to Get Best Site Performance**

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
