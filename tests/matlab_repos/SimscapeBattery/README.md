# Simscape physical-network fixture

These unmodified files come from MathWorks' public `Battery-Pack-Model-Simscape` repository (`master` branch):

- `Libraries/demoDetailedThermalDataTransfer/detailedThermalModel_demo.slx`
- `Libraries/+batteryModule/batteryCellHeatConvection.ssc`

Upstream: https://github.com/mathworks/Battery-Pack-Model-Simscape

The SLX is a real ZIP/XML model with eight `lconn` / `rconn` connections. It tests that physical conserving networks are not converted into directed Simulink signal flows. The SSC source tests the distinction between conserving `nodes` and physical-signal `inputs` / `outputs`.
