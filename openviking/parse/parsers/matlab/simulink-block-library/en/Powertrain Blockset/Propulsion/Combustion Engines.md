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
language: en
---

# Propulsion

Propulsion

Internal combustion engines, electric motors, and controllers

Propulsion systems in powertrains include internal combustion spark-ignition (SI) engines, compression-ignition (CI) engines, and electric motors. Use the propulsion blocks to assemble engine subsystems and controllers for hardware-in-the-loop (HIL) engine control design, vehicle-level fuel economy, and performance simulations.

## Blocks

### Internal Combustion Engines, Components, and Controllers

#### Engines and Controllers

|  |  |
| --- | --- |
| Mapped CI Engine | Compression-ignition engine model using lookup tables |
| Mapped SI Engine | Spark-ignition engine model using lookup tables |
| Simple Engine | Simplified engine model using lookup tables *(Since R2021b)* |
| CI Controller | Compression-ignition controller that includes air mass flow, torque, and EGR estimation |
| SI Controller | Spark-ignition engine controller that uses the driver torque request |

#### Components

|  |  |
| --- | --- |
| CI Core Engine | Compression-ignition engine from intake to exhaust port |
| SI Core Engine | Spark-ignition engine from intake to exhaust port |
| Mapped Core Engine | Steady-state core engine model using lookup tables |
| Boost Drive Shaft | Boost drive shaft speed |
| Compressor | Compressor for boosted engines |
| Control Volume System | Constant volume open thermodynamic system with heat transfer |
| Flow Boundary | Flow boundary for ambient temperature and pressure |
| Flow Restriction | Isentropic ideal gas flow through an orifice |
| Heat Exchanger | Intercooler or exhaust gas recirculation (EGR) cooler |
| Turbine | Turbine for boosted engines |

### Electric Motors, Inverters, and Controllers

#### Motors and Inverters

|  |  |
| --- | --- |
| Flux-Based PMSM | Flux-based permanent magnet synchronous motor |
| Induction Motor | Three-phase induction motor |
| Interior PMSM | Three-phase interior permanent magnet synchronous motor with sinusoidal back electromotive force |
| Mapped Motor | Mapped motor and drive electronics operating in torque-control mode |
| Surface Mount PMSM | Three-phase exterior permanent magnet synchronous motor with sinusoidal back electromotive force |
| Three-Phase Voltage Source Inverter | Three-phase voltage source inverter |

#### Controllers

|  |  |
| --- | --- |
| Equivalent Consumption Minimization Strategy | Energy management controller for P0–P4 hybrid electric vehicles |
| Flux-Based PM Controller | Controller for a flux-based permanent magnet synchronous motor |
| IM Controller | Internal torque-based, field-oriented controller for an induction motor with an optional outer-loop speed controller |
| Interior PM Controller | Torque-based, field-oriented controller for an internal permanent magnet synchronous motor |
| Surface Mount PM Controller | Torque-based, field-oriented controller for a surface mount permanent magnet synchronous motor |

## Topics

### Engines

- **Calibrate and Resize Engines and Electric Motors**
  Use reference applications and virtual vehicle composer to calibrate and resize
  engines and electric motors.
- **Calibrate, Validate, and Optimize CI Engine with Dynamometer Test Harness**
  Simulate a compression-ignition (CI) engine and controller under a dynamometer
  test harness using the CI engine dynamometer reference application.
- **Calibrate, Validate, and Optimize SI Engine with Dynamometer Test Harness**
  Simulate a spark-ignition (SI) engine and controller under a dynamometer test
  harness using the SI engine dynamometer reference application.
- **Calibrate, Validate, and Optimize SI H2 Engine with Dynamometer Test Harness**
  Simulate a hydrogen-fueled spark-ignition (SI) engine and controller under a
  dynamometer test harness using the SI H2 engine dynamometer reference
  application.
- **Calibrate ECMS Block for Objective Hybrid Vehicle Fuel Economy Assessment**
  Calibrate the Equivalent Consumption Minimization Strategy block in
  the HEV P2 reference application.

### Electric Motors

- **Develop, Resize, and Calibrate Motors with Dynamometer Test Harness**
  Develop a control test bench, resize e-motors, and calibrate controllers using the
  motor dynamometer reference application.
- **Generate Optimal Current Controller Calibration Tables for Permanent Magnet Synchronous Motors**

  Generate optimized current controller and flux parameters for permanent magnet
  synchronous motor (PMSM) blocks.

  - STEP 1: **Generate Current Controller Parameters**
  - STEP 2: **Generate Feed-Forward Flux Parameters**
  - STEP 3: **Generate Parameters for Flux-Based PMSM Block**

## Related Information

- **Engine Calibration Maps**
- **Estimate Motor Parameters Using Motor Control Blockset Parameter Estimation Tool (Motor Control Blockset)**

## Featured Examples

Build Conventional Vehicle Model

### Build Conventional Vehicle Model

Build a vehicle with an internal combustion engine using the conventional vehicle
reference application.

Calibrate Mapped Electric Motors Using Data

### Calibrate Mapped Electric Motors Using Data

Use the Virtual Vehicle Composer to calibrate mapped electric motors
from imported data.

Calibrate Mapped CI Engine Using Data

### Calibrate Mapped CI Engine Using Data

Use the Virtual Vehicle Composer to calibrate mapped CI engines from
imported data.

Calibrate Mapped SI Engine Using Data

### Calibrate Mapped SI Engine Using Data

Use the Virtual Vehicle Composer to calibrate mapped SI engines from
imported data.

Detect Misfires Using On-Board Diagnostics

### Detect Misfires Using On-Board Diagnostics

Implement onboard-diagnostics (OBD) to detect and report engine misfires.

- Open Model

Resize CI Engines

### Resize CI Engines

Resize compression-ignition (CI) engines using the dynamometer reference
application.

Resize SI Engines

### Resize SI Engines

Resize the spark-ignition (SI) engines using the dynamometer reference
application.

Resize Electric Motors

### Resize Electric Motors

Resize motors using the dynamometer reference application.

Read and Write Block Parameters to Excel

### Read and Write Block Parameters to Excel

Read data and write Mapped SI Engine block parameters to an Excel® data file.

- Open Live Script

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

Select a Web Site

Choose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select: .

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

You can also select a web site from the following list

**How to Get Best Site Performance**

Select the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.

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
