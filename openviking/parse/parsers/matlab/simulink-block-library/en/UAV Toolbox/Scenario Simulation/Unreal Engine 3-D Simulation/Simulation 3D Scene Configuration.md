---
type: simulink-block
title: 'Simulation 3D Scene Configuration'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine 3-D Simulation'
documentation_page: 'simulation3dsceneconfiguration'
documentation_source_path: 'ref/simulation3dsceneconfiguration.html'
language: en
---

# Simulation 3D Scene Configuration

## Ports

Not documented in R2025b.

## Parameters

### Scene

#### Scene Selection

### **Scene source** — Source of scene `Default Scenes` (default) | `RoadRunner` | `Unreal Executable` | `Unreal Editor`

Source of the scene in which to simulate, specified as one of the options in the
table.

| Option | Description |
| --- | --- |
| `Default Scenes` | Simulate in one of the default, prebuilt scenes specified in the **Scene name** parameter. |
| `RoadRunner` | Simulate in a RoadRunner scene. To import the RoadRunner scene, specify the corresponding file in the **Project** parameter.  You can use these file formats.  - Filmbox (`.fbx`) file. - Universal Scene Description (`.usd`, `.usdc`, and   `.usda`) file. - RoadRunner scene or scenario (`.rrscene` or   `.rrscenario`) files. |
| `Unreal Executable` | Simulate in a scene that is part of an Unreal Engine executable file. Specify the executable file in the **Project name** parameter. Specify the scene in the **Scene** parameter.  Select this option to simulate in custom scenes that have been packaged into an executable for faster simulation. |
| `Unreal Editor` | Simulate in a scene that is part of an Unreal Engine project (`.uproject`) file and is open in the Unreal® Editor. Specify the project file in the **Project** parameter.  Select this option when developing custom scenes. By clicking **Open Unreal Editor**, you can co-simulate within Simulink and the Unreal Editor and modify your scenes based on the simulation results. |

### **Scene name** — Name of prebuilt 3D scene `US city block` | `Suburban scene`

Name of the prebuilt 3D scene in which to simulate, specified as one of these
options. For details about a scene, see its listed corresponding reference
page.

- `US city block` – US City Block
- `Suburban scene` – Suburban scene

#### Dependencies

To enable this parameter, set **Scene source** to
`Default Scenes`.

### **Project name** — Name of Unreal Engine executable file `VehicleSimulation.exe` (default) | valid executable file name

Name of the Unreal Engine executable file, specified as a valid executable project file name. You
can either browse for the file or specify the full path to the project file, using
backslashes. To specify a scene from this file to simulate in, use the
**Scene** parameter.

By default, **Project name** is set to
`VehicleSimulation.exe`, which is on the MATLAB® search path.

**Note**

If you select a custom Unreal executable file built with a version of Unreal Engine that is not compatible with the current version of MATLAB, you receive one of these error messages:

- `"Incompatible version of 3D Simulation engine:
  Undefined"`: For Unreal executable built for a MATLAB release prior to R2023b
- `"Incompatible version of 3D Simulation engine: 23.2.0"`:
  For Unreal executable built for MATLAB R2023b or later

To resolve these errors, you must migrate the Unreal project and rebuild the executable with the latest support package
installed. For more information, see Migrate Projects Developed Using Prior Support Packages.

**Example:** `C:\Local\WindowsNoEditor\AutoVrtlEnv.exe`

#### Dependencies

To enable this parameter, set **Scene source** to
`Unreal Executable`.

### **Project** — Name of Unreal Engine project file or RoadRunner file valid project file name

Name of the Unreal Engine project file or RoadRunner file, specified as a valid project file name. You can either browse for
the file or specify the full path to the file, using backslashes. The file name must
contain no spaces.

To simulate scenes from Unreal Engine project file in the Unreal Editor, click **Open Unreal Editor**. If you have an
Unreal Editor session open already, then this button is disabled.

To run the simulation, in Simulink, click **Run**. Before you click **Play** in
the Unreal Editor, wait until the Diagnostic Viewer window displays this confirmation
message:

```
In the Simulation 3D Scene Configuration block, you set the scene source to 'Unreal Editor'.
In Unreal Editor, select 'Play' to view the scene.
```

This
message confirms that Simulink has instantiated the scene actors, including the vehicles and cameras, in the
Unreal Engine 3D environment. If you click **Play** before the Diagnostic
Viewer window displays this confirmation message, Simulink might not instantiate the actors in the Unreal Editor.

To simulate a RoadRunner scene, you can import files in Filmbox (`.fbx`), Universal Scene Description (USD), RoadRunner scene (`.rrscene`), or RoadRunner scenario (`.rrscenario`) formats.

- To simulate scenes in Filmbox (`.fbx`) format, browse for the folder containing
  the exported RoadRunner scene files and specify the `.fbx` file. You can export a RoadRunner scene using the option **CARLA**
  **Filmbox** in Export Using CARLA Filmbox (RoadRunner). This
  option exports these three files to a folder:

  - Filmbox (`.fbx`) file
  - ASAM OpenDrive (`.xodr`) file
  - XML (`.rrdata.xml`) file
- To simulate scenes in Universal Scene Description (USD) format, browse for the folder containing the exported RoadRunner scene files, and select the `.usd`,
  `.usdc`, or `.usda` files. The actors
  imported from USD files are not compatible with collision detection. To export a RoadRunner scene in USD format, see Export to USD (RoadRunner).
- To simulate scenes in RoadRunner scene or scenario (`.rrscene` or
  `.rrscenario`) formats, browse for the folder containing the
  RoadRunner files, and select the corresponding file. Before simulation, you
  must configure RoadRunner integration with MATLAB using the `roadrunnerSetup` (RoadRunner) function.

  - Enter the `roadrunnerSetup` function in the
    MATLAB Command Window.
  - The RoadRunner Setup dialog box opens.
  - Specify the **RoadRunner Project Folder** and
    **RoadRunner Installation Folder** locations.

For more information on exporting and simulating RoadRunner scenes, see Simulate in RoadRunner Scene.

**Note**

USD and RoadRunner scene or scenario (`.rrscene` or
`.rrscenario`) file import are not supported on Linux®.

#### Dependencies

To enable this parameter, set
**Scene source** to `Unreal Editor` or
`RoadRunner`.

#### Scene Parameters

### **Scene view** — Placement of virtual camera that displays scene `Scene Origin` (default) | `Custom` | vehicle name | `sim3d` actor name | viewpoint name

Configure the placement of the virtual camera to set the viewpoint that displays
the scene during simulation. The **Scene view** parameter list is
populated with all the **Name** parameter values of the vehicle and
actor blocks in your model, along with any additional custom viewpoints you have
created. If you add a Simulation 3D Scene Configuration block to your
model, the virtual camera remains positioned at the scene origin. To reposition the
camera to a custom viewpoint or to follow a vehicle, or actor, update this
parameter.

The table lists the **Scene view** parameter options if your
model contains no vehicle blocks, actor blocks, or custom viewpoints.

| Option | Description |
| --- | --- |
| `Custom` | - Create a custom viewpoint. This option enables these parameters.  - **Name**   - **Translation**   - **Rotation** - Click **Save Viewpoint** to create the   viewpoint. - View the scene in free camera mode. The camera movement uses the   world coordinate system. |
| `Scene Origin` | - Set the viewpoint at the scene origin. - View the scene in free camera mode. The camera movement uses the   world coordinate system. |

The table lists the additional options if your model contains vehicle blocks,
actor blocks, or custom viewpoints.

| Option | Description |
| --- | --- |
| Vehicle name | - Attach the virtual camera to the selected vehicle block in your   model. - You can only change the location of the camera around the   vehicle. |
| `sim3d` actor name | - Attach the virtual camera to the selected Simulation 3D   Actor block in your model. - This option enables these parameters to set the location of the   camera relative to the actor origin.  - **Viewer relative translation [X, Y, Z]     (m)**   - **Viewer relative rotation [Roll, Pitch, Yaw]     (deg)** |
| Viewpoint name | - Set the viewpoint to the selected viewpoint name. This option also   enables these parameters.  - **Name**   - **Translation**   - **Rotation** - Click **Save Viewpoint** to update the   viewpoint. - Click **Delete Viewpoint** to remove it. - View the scene in free camera mode. The camera movement uses the   world coordinate system. |

**Scene Controls**

When **Scene view** is set to `Scene Origin` or
`Custom`, you can change the location of the camera to navigate in
the scene during simulation using keyboard and mouse control. You can also change the
camera location when the simulation is paused.

To navigate in the 3D environment, use these keyboard
shortcuts.

| Keyboard Shortcut | Camera Control |
| --- | --- |
| **W** | Move forward. |
| **Shift+W** | Move faster in the forward direction. |
| **S** | Move backward. |
| **Shift+S** | Move faster in reverse direction. |
| **A** | Move left. |
| **Shift+A** | Move faster toward left. |
| **D** | Move right. |
| **Shift+D** | Move faster toward right. |
| **E** | Move up. |
| **Shift+E** | Move faster in the upward direction. |
| **Q** | Move down. |
| **Shift+Q** | Move faster in the downward direction. |
| Mouse scroll wheel | Control the camera distance from the cursor point. |
| **Shift**+mouse scroll wheel | Camera moves faster. |
| Mouse right-click and drag | Orbit around the cursor point. |
| **O** | Attach camera to actor under the cursor point. |
| Mouse left-click and drag | Orbit around the actor after camera attaches to the actor. |
| **P** | Detach camera from the actor. |
| **L** | Record the current viewpoint and display `Location saved` on the scene. |
| **1 to 9** | Access the stored viewpoints, if available. |
| **Tab** | Cycle the view between all vehicles in the scene and the viewpoint at the start of the simulation, in the forward direction. |
| **Shift+Tab** | Cycle the view between all vehicles in the scene and the viewpoint at the start of the simulation, in the reverse direction. |
| **I** | Toggle the display of keyboard shortcuts on the screen. Press once to show and again to hide. |

**Vehicle Views**

When **Scene view** is set to a vehicle name, during simulation,
you can change the location of the camera around the vehicle. You can also set the
view to a vehicle during simulation by pressing **Tab**.

To smoothly change the camera views, use these keyboard
shortcuts.

| Keyboard Shortcut | Camera View | |
| --- | --- | --- |
| **1** | Back left | A diagram shows numbered key commands corresponding to camera views     View Animated GIF  Animated gif of camera views |
| **2** | Back |
| **3** | Back right |
| **4** | Left |
| **5** | Internal |
| **6** | Right |
| **7** | Front left |
| **8** | Front |
| **9** | Front right |
| **0** | Overhead |

For additional camera controls, use these keyboard shortcuts.

| Keyboard Shortcut | Camera Control |
| --- | --- |
| **Tab** | Cycle the view between all vehicles in the scene.   View Animated GIF  Animated gif of cycling views between all vehicles in scene |
| Mouse scroll wheel | Control the camera distance from the vehicle.   View Animated GIF  Animated gif of camera distance control |
| **L** | Toggle a camera lag effect on or off. When you enable the lag effect, the camera view includes:  - Position lag, based on the vehicle translational   acceleration - Rotation lag, based on the vehicle rotational   velocity  This lag improves visualization of overall vehicle acceleration and rotation.   View Animated GIF  Animated gif of camera lag effect |
| **F** | Toggle the free camera mode on or off. When you enable the free camera mode, you can use the mouse to change the pitch and yaw of the camera. This mode allows you to orbit the camera around the vehicle.   View Animated GIF  Animated gif of free camera mode |

### **Name** — Name of custom viewpoint `custom` (default) | character array | string scalar

*Since R2025a*

Specify the name of the custom viewpoint as a character array or string
scalar.

**Example:** `View1`

#### Dependencies

To enable this parameter, set **Scene view** to
`Custom`.

**Data Types:** `char` | `string`

### **Translation** — Viewpoint translation `[0 0 0]` (default) | real 1-by-3 vector

*Since R2025a*

Specify the viewpoint translation
(*x*,*y*,*z*) as a real 1-by-3
vector, in m.

#### Dependencies

To enable this parameter, set **Scene view** to
`Custom`.

**Data Types:** `double`

### **Rotation** — Viewpoint rotation `[0 0 0]` (default) | real 1-by-3 vector

*Since R2025a*

Specify the viewpoint rotation (*roll*, *pitch*,
*yaw*) as a real 1-by-3 vector, in deg.

#### Dependencies

To enable this parameter, set **Scene view** to
`Custom`.

**Data Types:** `double`

### **Viewer relative translation [X, Y, Z] (m)** — Viewpoint translation relative to actor `[0 0 0]` (default) | real 1-by-3 vector

*Since R2025a*

Specify the viewpoint translation
(*x*,*y*,*z*) relative to
`sim3d` actor origin as a real 1-by-3 vector, in m.

#### Dependencies

To enable this parameter, set **Scene view** to the
`sim3d` actor name.

**Data Types:** `double`

### **Viewer relative rotation [Roll, Pitch, Yaw] (deg)** — Viewpoint rotation relative to actor `[0 0 0]` (default) | real 1-by-3 vector

*Since R2025a*

Specify the viewpoint rotation (*roll*, *pitch*,
*yaw*) relative to `sim3d` actor origin as a real
1-by-3 vector, in deg.

#### Dependencies

To enable this parameter, set **Scene view** to the
`sim3d` actor name.

**Data Types:** `double`

### **Sample time** — Sample time of visualization engine `1/60` (default) | real positive scalar

Sample time, *Ts*, of the visualization
engine, specified as a real positive scalar. Units are in seconds.

The graphics frame rate of the visualization engine is the inverse of the sample
time. For example, if **Sample time** is
`1/60`, then the visualization engine solver tries to achieve a
frame rate of 60 frames per second. However, the real-time graphics frame rate is
often lower due to factors such as graphics card performance and model
complexity.

By default, blocks that receive data from the visualization engine inherit this
sample rate.

### **Display 3D simulation window** — Unreal Engine visualization `on` (default) | `off`

Select whether to run simulations in the 3D visualization environment without
visualizing the results, that is, in *headless mode*.

Consider running in headless mode in these cases:

- You want to run multiple 3D simulations in parallel to test models in
  different Unreal Engine scenarios.

#### Dependencies

To enable this parameter, set **Scene source** to
`Default Scenes` or `Unreal
Executable`.

### Weather

### **Override scene weather** — Option to control the scene weather and sun position `off` (default) | `on`

Select whether to control the scene weather and sun position during simulation.
Use the enabled parameters to change the sun position, clouds, fog, rain, and
snow.

This table summarizes sun position settings for specific times of day.

| Time of Day | Settings | Unreal Editor Environment |
| --- | --- | --- |
| Midnight | **Sun altitude**: -90  **Sun azimuth**: 180 | Road at midnight |
| Sunrise in the north | **Sun altitude**: 0  **Sun azimuth**: 180 | Road at sunrise |
| Noon | **Sun altitude**: 90  **Sun azimuth**: 180 | Road at noon |

This table summarizes settings for specific cloud conditions.

| Cloud Condition | Settings | Unreal Editor Environment |
| --- | --- | --- |
| Clear | **Cloud opacity**: 0 | Road with clear skies |
| Heavy | **Cloud opacity**: 85 | Road with cloudy skies |
| Heavy | **Enable Volumetric clouds**: Selected  **Cloud Coverage**: 50  **Cloud layer altitude**: 6 | Road with volumetric clouds |

This table summarizes settings for specific fog conditions.

| Fog Condition | Settings | Unreal Editor Environment |
| --- | --- | --- |
| None | **Fog density**: 0 | Road with no fog |
| Heavy | **Fog density**: 100 | Road with heavy fog |

This table summarizes settings for specific rain conditions.

| Rain Condition | Settings | Unreal Editor Environment |
| --- | --- | --- |
| Light | **Cloud opacity**: 10  **Rain density**: 25 | City scene with light rain |
| Heavy | **Cloud opacity**: 10  **Rain density**: 80 | City scene with heavy rain |

This table summarizes settings for specific snow conditions.

| Snow Condition | Settings | Unreal Editor Environment |
| --- | --- | --- |
| Heavy | **Snow density**: 50 | Road scene with heavy snow |

#### Sun

### **Sun azimuth** — Azimuth angle from south to horizontal projection of the sun ray `90` (default) | any value between `0` and `360`

Azimuth angle in the horizontal plane measured from the south to the horizontal
projection of the sun rays, in deg.

Diagram of sun altitude angle (vertical arrow) and sun azimuth angle (horizontal arrow

Use the **Sun altitude** and **Sun azimuth**
parameters to control the time of day in the scene. For example, to specify sunrise in
the north, set **Sun altitude** to 0 deg and **Sun
azimuth** to 180 deg.

#### Dependencies

To enable this parameter, select **Override scene weather**.

### **Sun altitude** — Altitude angle between sun and horizon `40` (default) | any value between `-90` and `90`

Altitude angle in a vertical plane between the sun's rays and the horizontal
projection of the rays, in deg.

Diagram of sun altitude angle (vertical arrow) and sun azimuth angle (horizontal arrow)

Use the **Sun altitude** and **Sun azimuth**
parameters to control the time of day in the scene. For example, to specify sunrise in
the north, set **Sun altitude** to 0 deg and **Sun
azimuth** to 180 deg.

#### Dependencies

To enable this parameter, select **Override scene weather**.

### **Enable geospatial sun** — Option to enable geospatial sun `off` (default) | `on`

Select this check box to enable geospatial sun. Enabling geospatial sun is useful
to simulate conditions near the poles or at locations with disproportionate lengths of
day versus night.

#### Dependencies

To enable this parameter, select **Override scene
weather**.

### **Latitude** — Latitude of geolocation on earth `0` (default) | scalar

Latitude of geolocation on earth, specified as a scalar, in deg.

#### Dependencies

To enable this parameter, select **Override scene weather** and
**Enable geospatial sun**.

### **Longitude** — Longitude of geolocation on earth 0 (default) | scalar

Longitude of geolocation on earth, specified as a scalar, in deg.

#### Dependencies

To enable this parameter, select **Override scene weather** and
**Enable geospatial sun**.

### **Date (YYYY-MM-DD)** — Date 2023-01-01 (default) | integer

Date, specified as an integer in the format `YYYY-MM-DD`.

#### Dependencies

To enable this parameter, select **Override scene weather** and
**Enable geospatial sun**.

### **Time (HH:MM:SS)** — Time `10:30:00` (default) | integer

Time, specified as an integer in the format `HH:MM:SS`.

#### Dependencies

To enable this parameter, select **Override scene weather** and
**Enable geospatial sun**.

### **Time zone** — Time zone `-5.0` (default) | any value between `-12.0` and `12.0`

Time zone specifies the number of hours offset from the Coordinated Universal Time
(UTC) or Greenwich Mean Time (GMT).

#### Dependencies

To enable this parameter, select **Override scene weather** and
**Enable geospatial sun**.

### **Daylight saving time** — Option to enable daylight saving time `off` (default) | `on`

Select this check box to enable daylight saving time.

#### Dependencies

To enable this parameter, select **Override scene weather** and
**Enable geospatial sun**.

#### Cloud

### **Cloud speed** — Unreal Editor Cloud Speed global actor target value `1` (default) | any value between `-100` and `100`

Parameter that corresponds to the Unreal Editor **Cloud Speed** global actor target value. The
clouds move from west to east for positive values and east to west for negative
values.

Cloud Opacity and Cloud Speed settings in Unreal Editor

Use the **Cloud opacity** and **Cloud speed**
parameters to control clouds in the scene.

#### Dependencies

To enable this parameter, select **Override scene weather**.

### **Cloud opacity** — Unreal Editor Cloud Opacity global actor target value `10` (default) | any value between `0` and `100`

Parameter that corresponds to the Unreal Editor **Cloud Opacity** global actor target value, in
percent. Zero is a cloudless scene.

Cloud Opacity and Cloud Speed settings in Unreal Editor

Use the **Cloud opacity** and **Cloud speed**
parameters to control clouds in the scene.

#### Dependencies

To enable this parameter, select **Override scene weather**.

### **Enable volumetric clouds** — Option to enable volumetric clouds `off` (default) | `on`

Select this check box to enable volumetric clouds.

#### Dependencies

To enable this parameter, select **Override scene weather**.

### **Cloud coverage** — Unreal Editor Cloud Density global target value `1.0` (default) | any value between `0` and `100`

Parameter that corresponds to the Unreal Editor **Cloud Density** global actor target value, in
percent.

Cloud coverage settings in Unreal Editor

Use the **Cloud coverage** parameter to control clouds in the
scene.

#### Dependencies

To enable this parameter, select **Override scene weather** and
**Enable volumetric clouds**.

### **Cloud layer altitude** — Unreal Editor Layer Bottom Altitude global actor target value `6` (default) | any value between `5` and `20`

Parameter that corresponds to the Unreal Editor **Layer Bottom
Altitude** global actor target value, in km.

Cloud altitude setting in Unreal Editor

#### Dependencies

To enable this parameter, select **Override scene weather** and
**Enable volumetric clouds**.

#### Fog

### **Fog density** — Unreal Editor Set Fog Density and Set Start Distance target values `0` (default) | any value between `0` and `100`

Parameter that corresponds to the Unreal Editor **Set Fog Density** and **Set Start
Distance** target values, in percent.

Set Fog Density setting in Unreal Editor

#### Dependencies

To enable this parameter, select **Override scene weather**.

#### Rain

### **Rain density** — Unreal Editor local actor controlling rain density, wetness, rain puddles, and ripples `0` (default) | any value between `0` and `100`

Parameter corresponding to the Unreal Editor local actor that controls rain density, wetness, rain puddles,
and ripples, in percent.

Unreal Editor settings to control rain density. The Get Components by Class on the left activates or deactivates the rain density settings. The rain effects on the right control settings such as wetness, rain puddles, and ripples.

Use the **Cloud opacity** and **Rain density**
parameters to control rain in the scene.

#### Dependencies

To enable this parameter, select **Override scene weather**.

### **Enable raindrops on camera lens** — Option to enable raindrops on camera lens `off` (default) | `on`

Select this check box to enable raindrops on the camera lens.

Cloud altitude setting in Unreal Editor

#### Dependencies

To enable this parameter, select **Override scene weather**.

#### Snow

### **Snow density** — Unreal Editor global actor controlling snow density `0` (default) | any value between `0` and `100`

This parameter corresponds to the Unreal Editor global actor that controls snow density, in percent.

Cloud altitude setting in Unreal Editor

#### Dependencies

To enable this parameter, select **Override scene weather**.

### Geospatial

### **Enable geospatial configuration** — Option to enable geospatial parameters and variant subsystem `off` (default) | `on`

Select this check box to enable geospatial parameters and a variant
subsystem.

### **Access token ID** — ID of stored token string representing ID of stored token

ID of stored token, specified as a string. To create this token, create a
Cesium Ion® account, then generate the token through this account. The
Authentication Manager stores the token from Cesium Ion. For more information, see Visualize with Cesium (Aerospace Blockset) and https://ion.cesium.com/.

#### Dependencies

To enable this parameter, select the **Enable geospatial
configuration** check box.

### **Use Earth center as origin (ECEF)** — Use Earth center as origin (ECEF) `off` (default) | on

Select this check box to position aerospace vehicles with respect to the Earth
center. Use this option with the ECEF coordinate frame selection in the pack
blocks.

### **Origin height (m)** — Height at georeference point on globe real scalar

Height at georeference point on the globe, specified as a real scalar. This
parameter represents the height above the 1984 World Geodetic System (WGS84) ellipsoid
model of the Earth at the latitude and longitude specified in **Origin
latitude** and **Origin longitude**.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Clear the **Use Earth center as origin (ECEF)** check
  box.

### **Origin latitude** — Latitude real scalar

Latitude, specified as a real scalar in decimal degrees.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Clear the **Use Earth center as origin (ECEF)** check
  box.

### **Origin longitude** — Longitude real scalar

Longitude, specified as a real scalar in decimal degrees.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Clear the **Use Earth center as origin (ECEF)** check
  box.

### **Map style** — Raster overlay type `Aerial` (default) | `Aerial with labels` | `Road`

Raster overlay type, specified as `Aerial`,
`Aerial with labels`, or
`Road`.

#### Dependencies

To enable this parameter, select the **Enable geospatial
configuration** check box.

### **Additional asset IDs** — Local dataset IDs `[]` (default) | array | vector

Local dataset IDs, specified as an array or vector.

#### Dependencies

To enable this parameter, select the **Enable geospatial
configuration** check box.

### **Use advanced Sun sky** — Georeferenced, location-accurate Sun Sky actor `off` (default) | on

Select this check box to add a georeferenced, location-accurate Sun Sky actor in
simulation.

#### Dependencies

To enable this parameter, select the **Enable geospatial
configuration** check box.

### **Solar time** — Current solar time `11` (default) | scalar real

Current solar time, specified as scalar hours from midnight.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **Time zone** — Time zone `11` (default) | scalar real

Time zone, specified as hours offset from Greenwich Mean Time (GMT). To specify
hours before GMT, use a minus sign (`-`).

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **Day** — Day `21` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

Day, specified as a scalar from `1` to
`31`.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **Month** — Month `9` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12`

Month, specified as a scalar from `1` to
`12`.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **Year** — Year `2022` (default) | scalar real

Year, specified as a scalar real.

### **Use daylight saving time (DST)** — Daylight saving time `off` (default) | on

Select this check box to enable daylight saving time.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **DST start day** — Start day of daylight saving time `10` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

Start day of daylight saving time, specified as a scalar from `1`
to `31`.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **DST start month** — Start month of daylight saving time `3` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12`

Start month of daylight saving time, specified as a scalar from
`1` to `12`.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **DST end day** — Last day of daylight saving time `3` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

Last day of daylight saving time, specified as a scalar from `1`
to `31`.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **DST end month** — Last month of daylight saving time `11` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12`

Last month of daylight saving time, specified as a scalar from
`1` to `12`.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **DST switch hour** — Hour when daylight saving time switches `2` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24`

Hour when daylight saving time switches, specified as a scalar from
`1` to `24`.

#### Dependencies

To enable this parameter:

- Select the **Enable geospatial configuration** check
  box.
- Select the **Use advanced Sun sky** check box.

### **Authentication manager** — Management of access tokens button

Click to manage access tokens, such as create, update, and delete tokens.

#### Dependencies

To enable this parameter, select the **Enable geospatial
configuration** check box.

### **TilesetSource** — Tileset Source `'Earth Terrain'` (default) | `'URL'` | `'None'`

Tileset source, specified as one of `'Earth Terrain'`,
`'URL'`, or `'None'`.

#### Dependencies

To enable this parameter, select the **Enable geospatial
configuration** check box.

**Data Types:** `string`

### **TilesetUrl** — File path of locally stored 3d tileset data string

File path of locally stored 3d tileset data, specified as a string.

#### Dependencies

To enable this parameter, select the **Enable geospatial
configuration** check box and set the
**TilesetSource** parameter to `URL`.

**Data Types:** `string`

## Libraries

Offroad Autonomy Library / Simulation 3D Aerospace Blockset / Animation / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Environment UAV Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

### R2025a: Simulation 3D Scene Configuration block has two new parameters

The UAV Toolbox now offers additional support for offline dataset loading in
Cesium® to allow Air-Gap use-cases. The Simulation 3D Scene
Configuration block has two new parameters `TilesetSource` and
`Url`.

You can use the `TilesetSource` parameter to select the value of the
`URL` parameter as the source, where you can specify the file path of
your offline tileset data.

### R2025a: Import USD and RoadRunner scene or scenario files into Unreal Engine Simulation Environment

You can import these RoadRunner scene files:

- Universal Scene Description (`.usd`, `.usdc`, and
  `.usda`) file
- RoadRunner scene or scenario (`.rrscene` or
  `.rrscenario`) files

To specify the source of scene, set the **Scene source**
parameter as `RoadRunner`. Then, in the **Project**
parameter, specify the corresponding RoadRunner scene file.

### R2025a: Create multiple views of 3D environment

You can create custom viewpoints using the `Custom` option from
the **Scene view** parameter. This option enables these parameters.

- **Name**
- **Translation**
- **Rotation**

You can save the viewpoint to populate the **Scene view**
parameter list with the viewpoint name. Select the viewpoint to set the view of the scene.
You can also edit or delete the viewpoint.

### R2025a: Set the scene view relative to `sim3d` actor

You can set the **Scene view** parameter to the
**Name** parameter of the Simulation 3D Actor block
contained in your model. This option enables these parameters to set the location of the
camera relative to the actor origin.

- **Viewer relative translation [X, Y, Z] (m)**
- **Viewer relative rotation [Roll, Pitch, Yaw] (deg)**

### R2025a: Install additional scenes

In addition to the default scenes, you can download and install any prebuilt 3D scenes
available in the Unreal Engine environment for 3D simulation.

To select and download a scene, click **Install**. MATLAB restarts after the scene is installed. You can now select the installed scene
from the **Scene view** parameter list.

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Scene Configuration block requires
Simulink
3D Animation.

### R2024a: New parameters available to simulate additional weather conditions

Use new weather parameters to simulate additional weather conditions.

| Weather | Parameters |
| --- | --- |
| **Sun** | - **Enable geospatial sun** - **Latitude** - **Longitude** - **Date** - **Time** - **Daylight saving time** |
| **Cloud** | - **Enable volumetric clouds** - **Cloud coverage** - **Cloud layer altitude** |
| **Rain** | - **Enable raindrops on camera lens** |
| **Snow** | - **Snow density** |

### R2023b: Import RoadRunner Scene into Unreal Engine Simulation Environment

Use the Simulation 3D Scene Configuration block to import a RoadRunner scene and simulate in the scene. To specify the source of scene, select the
**Scene source** parameter as `RoadRunner`. Then, in the
**Project** parameter, specify the Filmbox `(.fbx)` file
corresponding to the RoadRunner scene. For an example, see Import RoadRunner Scene into Unreal Engine Using Simulink (Simulink 3D Animation).

### R2023b: Camera View Improvements to View the Virtual World

Use the Simulation 3D Scene Configuration block to view the virtual world
from a camera positioned at a custom viewpoint. To set the custom viewpoint, select
**Scene view** as `Custom` and set the **Initial
viewer translation** and **Initial viewer rotation** values. You
can also use keyboard shortcuts and mouse controls to navigate in the virtual world
scene.

### R2023a: Cesium support for specifying geospatial coordinates

You can select the **Enable geospatial configuration** parameter to
enable the parameters of the **Geospatial** tab, such as **Access
token ID** and **Georeference parameters**. You can use the
parameters on the **Geospatial** tab to specify geospatial origin
coordinates using a Cesium access token ID.

## Description

Scene configuration for 3D simulation environment

**Note**

Simulating models with the Simulation 3D Scene Configuration block requires
Simulink®
3D Animation™.

The Simulation 3D Scene Configuration block implements a 3D simulation
environment that is rendered by using the Unreal Engine® from Epic Games®.
UAV Toolbox integrates the 3D simulation environment with Simulink so that you can query the world around the vehicle and virtually test
perception, control, and planning algorithms. Using this block, you can also control the
position of the sun and the weather conditions of a scene. For more details, see Sun Position and
Weather.

You can simulate from a set of prebuilt
scenes or from your own custom scenes. Scene customization requires the
UAV Toolbox Interface for Unreal Engine Projects support package. For more details, see Customize Unreal Engine Scenes for UAVs.

You can also simulate custom scenes
designed and built in RoadRunner. To do so, you must first export scenes from RoadRunner and specify the path to the exported scene artifacts in the
**Project** parameter of the Simulation 3D Scene
Configuration block.

**Tip**

The Simulation 3D Scene Configuration block must execute after blocks
that send data to the 3D environment and before blocks that receive data from the 3D
environment. To verify the execution order of such blocks, right-click the blocks and select
**Properties**. Then, on the **General** tab, confirm
these **Priority** settings:

- For blocks that send data to the 3D environment,
  **Priority** must be set to `-1` so the blocks
  can prepare their data before the 3D environment receives it.
- For the Simulation 3D Scene Configuration block in your model,
  **Priority** must be set to `0`.
- For blocks that receive data from the 3D environment,
  **Priority** must be set to `1` so the 3D
  environment can prepare the data before these blocks receive it.

For more information about execution order, see How Unreal Engine Simulation for UAVs Works.
