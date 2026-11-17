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
chinese_source: official
---

# Axes Transformations

Axes Transformations

Transform axes of coordinate systems to different types, such as Euler angles to
quaternions

Transform axes of coordinate systems to different types, such as Euler angles to
quaternions

## Blocks

### Body/Wind Axis Transformations

|  |  |
| --- | --- |
| Direction Cosine Matrix Body to Wind | Convert angle of attack and sideslip angle to direction cosine matrix |
| Direction Cosine Matrix Body to Wind to Alpha and Beta | Convert direction cosine matrix to angle of attack and sideslip angle |
| Direction Cosine Matrix to Quaternions | Convert direction cosine matrix to quaternion vector |
| Direction Cosine Matrix to Rodrigues | Convert direction cosine matrix to Euler-Rodrigues vector |
| Direction Cosine Matrix to Rotation Angles | Convert direction cosine matrix to rotation angles |
| Direction Cosine Matrix to Wind Angles | Convert direction cosine matrix to wind angles |
| Quaternions to Direction Cosine Matrix | Convert quaternion vector to direction cosine matrix |
| Quaternions to Rodrigues | Convert quaternion to Euler-Rodrigues vector |
| Quaternions to Rotation Angles | Determine rotation vector from quaternion |
| Rodrigues to Direction Cosine Matrix | Convert Euler-Rodrigues vector to direction cosine matrix |
| Rodrigues to Quaternions | Convert Euler-Rodrigues vector to quaternion |
| Rodrigues to Rotation Angles | Convert Euler-Rodrigues vector to rotation angles |
| Rotation Angles to Direction Cosine Matrix | Convert rotation angles to direction cosine matrix |
| Rotation Angles to Quaternions | Calculate quaternion from rotation angles |
| Rotation Angles to Rodrigues | Convert rotation angles to Euler-Rodrigues vector |
| Wind Angles to Direction Cosine Matrix | Convert wind angles to direction cosine matrix |

### Geodetic Transformations

|  |  |
| --- | --- |
| Direction Cosine Matrix ECEF to NED | Convert geodetic latitude and longitude to direction cosine matrix |
| Direction Cosine Matrix ECEF to NED to Latitude and Longitude | Convert direction cosine matrix to geodetic latitude and longitude |
| Direction Cosine Matrix ECI to ECEF | Convert Earth-centered inertial (ECI) to Earth-centered Earth-fixed (ECEF) coordinates |
| ECEF Position to LLA | Calculate geodetic latitude, longitude, and altitude above planetary ellipsoid from Earth-centered Earth-fixed (ECEF) position |
| ECI Position to AER | Convert Earth-centered inertial (ECI) coordinates to azimuth coordinates |
| ECI Position to LLA | Convert Earth-centered inertial (ECI) coordinates to geodetic latitude, longitude, altitude (LLA) coordinates |
| Flat Earth to LLA | Estimate geodetic latitude, longitude, and altitude from flat Earth position |
| Geodetic to Geocentric Latitude | Convert geodetic latitude to geocentric latitude |
| Geocentric to Geodetic Latitude | Convert geocentric latitude to geodetic latitude |
| LLA to ECEF Position | Calculate Earth-centered Earth-fixed (ECEF) position from geodetic latitude, longitude, and altitude above planetary ellipsoid |
| LLA to ECI Position | Convert latitude, longitude, altitude (LLA) coordinates to Earth-centered inertial (ECI) coordinates |
| LLA to Flat Earth | Estimate flat Earth position from geodetic latitude, longitude, and altitude |

### Reference System Transformations

|  |  |
| --- | --- |
| Besselian Epoch to Julian Epoch | Transform position and velocity components from discontinued Standard Besselian Epoch (B1950) to Standard Julian Epoch (J2000) |
| Julian Epoch to Besselian Epoch | Transform position and velocity components from Standard Julian Epoch (J2000) to discontinued Standard Besselian Epoch (B1950) |

### Transformation Utilities

|  |  |
| --- | --- |
| Delta UT1 | Calculate difference between principal Universal Time (UT1) and Coordinated Universal Time (UTC) according to International Astronomical Union (IAU) 2000A reference system |

## Topics

### About Aerospace Coordinate Systems

- **Fundamental Coordinate System Concepts**

  Define coordinate systems when working with the Aerospace Blockset™ software.

  - **Coordinate Systems for Modeling**
  - **Coordinate Systems for Navigation**
  - **Coordinate Systems for Display**

### Solar Time

- **Calculate UT1 to UTC Values**
  Calculate difference between principal Universal Time (UT1) and Coordinated
  Universal Time (UTC) according to International Earth Rotation Service
  (IERS).

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

选择网站

选择网站以获取翻译的可用内容，以及查看当地活动和优惠。根据您的位置，我们建议您选择：。

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择网站：

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站并未针对您所在位置的访问进行优化。

美洲

- América Latina (Español)
- Canada (English)
- United States (English)

欧洲

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

亚太

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
