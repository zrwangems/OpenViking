---
type: simulink-block
title: 'Moist Air Properties (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Utilities'
documentation_page: 'moistairpropertiesma'
documentation_source_path: 'ref/moistairpropertiesma.html'
language: en
---

# Moist Air Properties (MA)

## Ports

### Conserving

### **A** — Connection port moist air

Conserving port that connects the block to the moist air network. You
can connect it to any point on a moist air connection line in a block
diagram. When you connect the Moist Air Properties
(MA) block to a connection line, the software
automatically identifies the moist air blocks connected to the
particular circuit and propagates the properties to all these blocks.

## Parameters

### Dry Air

### **Dry air specific gas constant** — Universal gas constant divided by molar mass of dry air `287.047 J/kg/K` (default)

Universal gas constant divided by molar mass of dry air.

### **Temperature vector** — Vector of temperature values for table lookup vector

Vector of temperature values, to be used for table lookup of other
properties as a function of temperature. Dry air, water vapor, and trace
gas properties share the same temperature vector.

The default value is `[-56.55, -50 : 10 : -10, -5 : 1 : 5, 10
: 10 : 350]' degC`.

### **Dry air specific enthalpy vector** — Vector of specific enthalpy values for table lookup vector

The vector of specific enthalpy values of dry air, to be used for
one-dimensional table lookup based on the corresponding temperature
value. The vector size must be the same as the temperature vector
size.

The default value is `[342.416126230579; 349.005511058471;
359.063577249119; 369.119948684177; 379.175469465129;
389.230944678417; 394.258910928084; 395.264534937366;
396.27017101329; 397.275819932805; 398.281482472874;
399.287159410541; 400.292851523015; 401.298559587728;
402.304284382408; 403.310026685143; 404.315787274435;
409.34489180313; 419.404921755863; 429.468036401264;
439.535033154839; 449.606720928652; 459.683919949603;
469.767460521911; 479.858181001348; 489.956925196484;
500.064539372946; 510.181869006204; 520.309755403634;
530.449032296018; 540.60052248087; 550.765034584465;
560.943359995745; 571.136270013102; 581.344513234296;
591.568813210327; 601.809866375885; 612.068340261954;
622.344871990218; 632.640067043998; 642.95449830646;
653.288705353699; 663.643193987949; 674.018435994423;
684.414869104228; 694.832897145098; 705.272890361557;
715.735185886199; 726.220088344236; 736.727870574087;
747.258774447567; 757.813011774199] kJ/kg`.

### **Dry air dynamic viscosity vector** — Vector of dynamic viscosity values for table lookup vector

The vector of dynamic viscosity values of dry air, to be used for
one-dimensional table lookup based on the corresponding temperature
value. The vector size must be the same as the temperature vector
size.

The default value is `[14.2568883320012; 14.6140127728333;
15.1517277055779; 15.6806860159119; 16.2012351072083;
16.7137043125028; 16.9670071730589; 17.017438062815;
17.0677930842452; 17.1180725309876; 17.1682766951315;
17.2184058672268; 17.2684603362935; 17.3184403898301;
17.3683463138234; 17.4181783927569; 17.4679369096204;
17.7156358640698; 18.2056751785154; 18.68879035749;
19.1652344664982; 19.6352478927873; 20.099059103658;
20.5568853601578; 21.0089333871663; 21.4554000014051;
21.8964726992323; 22.3323302062775; 22.7631429910631;
23.1890737447833; 23.6102778293792; 24.0269036959922;
24.4390932757886; 24.8469823450548; 25.2507008663546;
25.6503733074314; 26.0461189394339; 26.4380521159325;
26.8262825340948; 27.2109154792923; 27.5920520543128;
27.969789394274; 28.3442208682439; 28.7154362685068;
29.0835219883356; 29.4485611890712; 29.8106339572472;
30.1698174524429; 30.5261860464955; 30.8798114546565;
31.2307628592324; 31.5791070262086] s*μPa`.

### **Dry air thermal conductivity vector** — Vector of thermal conductivity values for table lookup vector

The vector of thermal conductivity values of dry air, to be used for
one-dimensional table lookup based on the corresponding temperature
value. The vector size must be the same as the temperature vector
size.

The default value is `[19.8808489374933; 20.4162454629695;
21.2248743590758; 22.0232452890903; 22.8117314495857;
23.5906913619588; 23.9767075412237; 24.053639990175;
24.1304826682191; 24.2072359051629; 24.2839000294007;
24.3604753679152; 24.4369622462801; 24.5133609886625;
24.5896719178249; 24.6658953551279; 24.7420316205333;
25.1214164701832; 25.8738283029331; 26.6180150229276;
27.3542674377332; 28.0828634735341; 28.8040686837224;
29.5181367785657; 30.2253101618423; 30.9258204644224;
31.6198890677835; 32.3077276126633; 32.9895384896798;
33.6655153099498; 34.33584335461; 35.0007000027879;
35.6602551380254; 36.3146715334901; 36.9641052165342;
37.6087058133173; 38.248616874307; 38.8839761815308;
39.5149160384798; 40.1415635435708; 40.7640408480637;
41.3824653993118; 41.9969501701893; 42.6076038755117;
43.2145311762238; 43.8178328720941; 44.4176060836121;
45.013944423749; 45.6069381602018; 46.1966743687041;
46.783237077953; 47.3667074066625] mW/m/K`.

### **Minimum valid pressure** — Lowest pressure allowed `1 kPa` (default)

Lowest pressure allowed in the moist air network. The simulation
issues an error when pressure is out of range.

### **Maximum valid pressure** — Highest pressure allowed `inf MPa` (default)

Highest pressure allowed in the moist air network. The simulation
issues an error when pressure is out of range.

### **Minimum valid temperature** — Lowest temperature allowed `-56.55 degC` (default)

Lowest temperature allowed in the moist air network. The simulation
issues an error when temperature is out of range.

### **Maximum valid temperature** — Highest temperature allowed `350 degC` (default)

Highest temperature allowed in the moist air network. The simulation
issues an error when temperature is out of range.

### **Pressure and temperature outside valid range** — Whether to notify when pressure or temperature are outside valid range `Error` (default) | `Warning` | `None`

Select what happens if the moist air pressure or temperature go beyond
the valid range during simulation:

- `None` ― The block does not return an
  error if the properties go out of range.
- `Warning` ― The block issues a
  warning, but continues the simulation.
- `Error` ― The block returns an error
  and stops the simulation.

### **Atmospheric pressure** — Absolute pressure of the environment `0.101325 MPa` (default)

Absolute pressure of the environment.

### **Atmospheric temperature** — Absolute temperature of the environment `20 degC` (default)

Absolute temperature of the environment.

### Water Vapor

### **Enable entrained water droplets** — Option to model water droplets `Off` (default) | `On`

Select whether the block models entrained water droplets in the moist
air mixture. If you clear this checkbox, the model ignores any nonzero
values for water droplets in the parameters and inputs of blocks
connected to the network. The block equations listed on the block
reference pages replace the water droplet terms in calculations with
0.

For more information on modeling water droplets, see Modeling Moisture and Trace Gas Levels.

### **Water vapor specific gas constant** — Universal gas constant divided by molar mass of water vapor `461.523 J/kg/K` (default)

Universal gas constant divided by molar mass of water vapor.

### **Water vapor saturation pressure vector** — Vector of vapor saturation values for table lookup vector

Vector of vapor saturation values for water as a function of
temperature, to be used for one-dimensional table lookup. Moist air
becomes saturated when the partial pressure of water vapor is equal to
the water vapor saturation pressure. Therefore, condensation may occur.
The vector size must be the same as the temperature vector size. Dry
air, water vapor, and trace gas properties share the same temperature
vector.

The default value is `[1.71168953425982e-06;
3.93770601979424e-06; 1.28411717710344e-05; 3.80051394873809e-05;
.00010323902900209; .000259873810798063; .000401741022116384;
.000437454836117844; .000476040820618202; .000517704666185737;
.000562664883741207; .000611212677444345; .000657088049117899;
.000705987905898279; .000758082381149132; .000813549384183233;
.000872574861129522; .00122818386934022; .0023392147667769;
.00424668834054807; .00738442748706953; .0123512704340234;
.0199458019246787; .0312006356960619; .0474147199263783;
.0701823607447713; .10141797792131; .143375967241115;
.198665399739302; .270259606559999; .361500961984849;
.476101381081492; .618139196722055; .792053183687694;
1.0026345688121; 1.25501792086105; 1.55467186826983;
1.90739066433297; 2.31928772772542; 2.79679245576864;
3.34665187151016; 3.97593907083533; 4.69207105435535;
5.5028394740883; 6.41645928168037; 7.4416425436169;
8.58770832955728; 9.86474556030261; 11.2838558865497;
12.8575218898034; 14.6001810568052; 16.5291642526045]
MPa`.

### **Water specific enthalpy of vaporization vector** — Vector of specific enthalpy of vaporization values for table lookup vector

Vector of the difference between the specific enthalpy of saturated
water vapor and the specific enthalpy of saturated liquid water as a
function of temperature, to be used for one-dimensional table lookup.
The vector size must be the same as the temperature vector size. Dry
air, water vapor, and trace gas properties share the same temperature
vector.

The default value is `[2836.88241275372; 2837.81392500514;
2838.63937175807; 2838.7309929628; 2838.06905313927;
2836.62597341095; 2835.60023952573; 2835.37006381376;
2835.13143158077; 2834.88429145066; 2834.62859062897;
2500.93420564316; 2498.55329907119; 2496.17495082036;
2493.79885912205; 2491.42474723191; 2489.05236104642;
2477.20875029194; 2453.54955988604; 2429.83856603313;
2406.00136954922; 2381.97406342174; 2357.69101156389;
2333.08088387814; 2308.06565480412; 2282.56034405021;
2256.47287422313; 2229.70428017508; 2202.14968030993;
2173.69998896199; 2144.24368406447; 2113.66758247452;
2081.85585110571; 2048.68725710494; 2014.03141249899;
1977.7449923284; 1939.66849592886; 1899.62342931686;
1857.40930169838; 1812.79975416601; 1765.53721731251;
1715.32525772152; 1661.81700477787; 1604.59703745016;
1543.1534616334; 1476.83692476464; 1404.80240352424;
1325.92091736114; 1238.61667822208; 1140.5102987018;
1027.62017777647; 892.733785613825] kJ/kg`.

### **Water vapor specific enthalpy vector** — Vector of specific enthalpy values for table lookup vector

The vector of specific enthalpy values of water vapor, to be used for
one-dimensional table lookup based on the corresponding temperature
value. The vector size must be the same as the temperature vector size.
Dry air, water vapor, and trace gas properties share the same
temperature vector.

The default value is `[2396.55944251649; 2408.68643343608;
2427.1988031141; 2445.702165897; 2464.18429108356; 2482.62529466839;
2491.82135326629; 2493.6580151792; 2495.49372578218;
2497.32843835745; 2499.16210446923; 2500.99462758899;
2502.83092214066; 2504.6665223621; 2506.50140563013; 2508.335548891;
2510.16892865793; 2519.32352241995; 2537.56068088674;
2555.67742615292; 2573.6403223998; 2591.4109179101; 2608.9455037701;
2626.19492016262; 2643.10444358428; 2659.61377634497;
2675.58278696023; 2696.1846256545; 2716.49989553741;
2736.6235210957; 2756.61216047011; 2776.50561773853;
2796.33378922508; 2816.11979583049; 2835.88181423877;
2855.63430574511; 2875.38889327595; 2895.15500577172;
2914.94035964689; 2934.75132290228; 2954.59319330244;
2974.47041285505; 2994.38673458964; 3014.34535328009;
3034.34900867103; 3054.40006755764; 3074.50058946898;
3094.65237953784; 3114.85703128106; 3135.11596137801;
3155.43043805905; 3175.80160435813] kJ/kg`.

### **Water vapor dynamic viscosity vector** — Vector of dynamic viscosity values for table lookup vector

The vector of dynamic viscosity values of water vapor, to be used for
one-dimensional table lookup based on the corresponding temperature
value. The vector size must be the same as the temperature vector size.
Dry air, water vapor, and trace gas properties share the same
temperature vector.

The default value is `[6.81365662228272; 7.04953750742707;
7.40970098298307; 7.76991278093907; 8.13017290129507;
8.49048134405107; 8.67065368632907; 8.70668960445667;
8.74272600580827; 8.77876289038387; 8.81480025818347;
8.85083810920707; 8.88687644345467; 8.92291526092627;
8.95895456162187; 8.99499434554147; 9.03103461268507;
9.21124319676307; 9.57169660671907; 9.93219833907507;
10.2927483938311; 10.6533467709871; 11.0139934705431;
11.3746884924991; 11.7354318368551; 12.0962235036111;
12.4570634927671; 12.8179518043231; 13.1788884382791;
13.5398733946351; 13.9009066733911; 14.2619882745471;
14.6231181981031; 14.9842964440591; 15.3455230124151;
15.7067979031711; 16.0681211163271; 16.4294926518831;
16.7909125098391; 17.1523806901951; 17.5138971929511;
17.8754620181071; 18.2370751656631; 18.5987366356191;
18.9604464279751; 19.3222045427311; 19.6840109798871;
20.0458657394431; 20.4077688213991; 20.7697202257551;
21.1317199525111; 21.4937680016671] s*μPa`.

### **Water vapor thermal conductivity vector** — Vector of thermal conductivity values for table lookup vector

The vector of thermal conductivity values of water vapor, to be used
for one-dimensional table lookup based on the corresponding temperature
value. The vector size must be the same as the temperature vector size.
Dry air, water vapor, and trace gas properties share the same
temperature vector.

The default value is `[11.46288215976; 11.941997488935;
12.676358586935; 13.414208884935; 14.155548382935; 14.900377080935;
15.274099879935; 15.348949115735; 15.423833243535; 15.498752263335;
15.573706175135; 15.648694978935; 15.723718674735; 15.798777262535;
15.873870742335; 15.948999114135; 16.024162377935; 16.400502076935;
17.155798374935; 17.914583872935; 18.676858570935; 19.442622468935;
20.211875566935; 20.984617864935; 21.760849362935; 22.540570060935;
23.323779958935; 24.110479056935; 24.900667354935; 25.694344852935;
26.491511550935; 27.292167448935; 28.096312546935; 28.903946844935;
29.715070342935; 30.529683040935; 31.347784938935; 32.169376036935;
32.994456334935; 33.823025832935; 34.655084530935; 35.490632428935;
36.329669526935; 37.172195824935; 38.018211322935; 38.867716020935;
39.720709918935; 40.577193016935; 41.437165314935; 42.300626812935;
43.167577510935; 44.038017408935] mW/m/K`.

### **Water vapor diffusivity in air** — Smoothing coefficient for flow reversals `25 mm^2/s` (default)

Coefficient for the diffusive flux of water vapor in the moist air
mixture due to the difference in concentration of water vapor. During
mixture flow reversal, the water vapor mass flow rate at the ports
smoothly transitions between the upstream and downstream value based on
the diffusivity.

### Trace Gas

### **Trace gas model** — Select how to model trace gas in the air mixture `None` (default) | `Track mass fraction only` | `Track mass fraction and gas properties`

Select how the block models the amount of trace gas in the air
mixture:

- `None` — No trace gas is
  present. The moist air mixture consists of only dry air and
  water vapor. Any nonzero values of trace gas level in parameters
  and variable targets of the blocks connected to the circuit are
  ignored. All connections to the trace gas source blocks in the
  model are also ignored. Therefore, you do not need to modify
  your model based on the trace gas modeling selection.
- `Track mass fraction only` —
  The trace gas level can be nonzero and vary during simulation.
  However, the amount of trace gas is assumed to be small enough
  to have a negligible impact on the fluid properties of the moist
  air mixture.
- `Track mass fraction and gas
  properties` — The trace gas level can be
  nonzero and vary during simulation. The fluid properties of the
  moist air mixture depend on the amount of trace gas in the
  mixture.

For more information on the impact of these options on block and
system equations, see Trace Gas Modeling Options.

### **Trace gas specific gas constant** — Universal gas constant divided by molar mass of trace gas `188.923 J/kg/K` (default)

Universal gas constant divided by molar mass of trace gas.

#### Dependencies

Enabled when the **Trace gas model** parameter is
set to `Track mass fraction only` or
`Track mass fraction and gas
properties`.

### **Trace gas specific enthalpy vector** — Vector of specific enthalpy values for table lookup vector

The vector of specific enthalpy values of trace gas, to be used for
one-dimensional table lookup based on the corresponding temperature
value. The vector size must be the same as the temperature vector size.
Dry air, water vapor, and trace gas properties share the same
temperature vector.

The default value is `[439.555216260064; 444.670268200251;
452.538618847003; 460.487124258496; 468.522588768941;
476.649415958793; 480.74798538725; 481.57054318762;
482.394052398751; 483.218514288831; 484.043930029015;
484.870300696555; 485.697627277859; 486.525910671489;
487.355151691079; 488.185351068185; 489.016509455051;
493.186704139431; 501.599194953048; 510.107689961685;
518.711611080182; 527.410026793075; 536.201764778798;
545.085474203452; 554.059675505208; 563.122805485367;
572.27325096919; 581.509373027928; 590.829525105886;
600.232066705818; 609.715373581392; 619.277845178105;
628.917909922924; 638.634028838794; 648.424697859328;
658.288449140109; 668.223851601449; 678.229510889093;
688.304068901113; 698.44620299875; 708.654624994591;
718.928079991818; 729.265345132425; 739.665228299475;
750.126566808087; 760.648226111439; 771.229098541268;
781.868102096908; 792.564179292476; 803.316296068366;
814.123440770426; 824.984623198037] kJ/kg`.

#### Dependencies

Enabled when the **Trace gas model** parameter is
set to `Track mass fraction and gas
properties`.

### **Trace gas dynamic viscosity vector** — Vector of dynamic viscosity values for table lookup vector

The vector of dynamic viscosity values of trace gas, to be used for
one-dimensional table lookup based on the corresponding temperature
value. The vector size must be the same as the temperature vector size.
Dry air, water vapor, and trace gas properties share the same
temperature vector.

The default value is `[10.8921054191698; 11.2215357085649;
11.7233300740382; 12.2234238147811; 12.7215124453467;
13.2173328890673; 13.4643203184773; 13.5136406274989;
13.562934752385; 13.6122025024997; 13.6614436900741;
13.7106581301692; 13.7598456406398; 13.8090060420983;
13.8581391578796; 13.9072448140062; 13.9563228391538;
14.2012926853717; 14.6890687376044; 15.1738428124161;
15.6554929043332; 16.1339159800463; 16.6090257998657;
17.0807510097148; 17.5490334645512; 18.0138267508952;
18.4750948814453; 18.9328111390399; 19.3869570507278;
19.8375214755778; 20.2844997922255; 20.7278931741254;
21.1677079421287; 21.6039549853963; 22.036649242835;
22.4658092382469; 22.8914566632375; 23.3136160026627;
23.7323141980278; 24.1475803447965; 24.5594454200432;
24.9679420372927; 25.3731042257492; 25.774967231431;
26.1735673380029; 26.5689417053362; 26.9611282240413;
27.350165384404; 27.73609215832; 28.118947892972; 28.4987722151178;
28.8756049449796] s*μPa`.

#### Dependencies

Enabled when the **Trace gas model** parameter is
set to `Track mass fraction and gas
properties`.

### **Trace gas thermal conductivity vector** — Vector of thermal conductivity values for table lookup vector

The vector of thermal conductivity values of trace gas, to be used for
one-dimensional table lookup based on the corresponding temperature
value. The vector size must be the same as the temperature vector size.
Dry air, water vapor, and trace gas properties share the same
temperature vector.

The default value is `[10.489430678843; 10.9507672150864;
11.666197960308; 12.392559739764; 13.1299519771612;
13.8778409888416; 14.2554325416312; 14.3312274189707;
14.4071122346908; 14.4830860227061; 14.5591478179508;
14.6352966574703; 14.7115315815553; 14.787851634907;
14.8642558678259; 14.9407433374142; 15.0173131087819;
15.401364480906; 16.1751373988038; 16.9558134611595;
17.7432208682398; 18.5366976599676; 19.3360988502003;
20.1412225692689; 20.9517507672929; 21.7672310558863;
22.5871115634685; 23.4107980865695; 24.2377021890869;
25.0672663781241; 25.8989689893876; 26.732318357514;
27.5668446164644; 28.4020933015927; 29.2376215872816;
30.0729965057542; 30.9077942826816; 31.7416001931033;
32.5740086297993; 33.4046232539953; 34.2330571812868;
35.0589331874899; 35.8818839295189; 36.701552179391;
37.5175910702657; 38.3296643536716; 39.1374466671854;
39.9406238119064; 40.7388930391313; 41.5319633456945;
42.3195557774861; 43.1014037407076] mW/m/K`.

#### Dependencies

Enabled when the **Trace gas model** parameter is
set to `Track mass fraction and gas
properties`.

### **Trace gas diffusivity in air** — Smoothing coefficient for flow reversals `16 mm^2/s` (default)

Coefficient for the diffusive flux of trace gas in the moist air
mixture due to the difference in concentration of trace gas. During
mixture flow reversal, the trace gas mass flow rate at the ports
smoothly transitions between the upstream and downstream value based on
the diffusivity.

#### Dependencies

Enabled when the **Trace gas model** parameter is
set to `Track mass fraction only` or
`Track mass fraction and gas
properties`.

## Libraries

Simscape / Foundation Library / Moist Air / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist
air flow. To model water droplets, select **Enable entrained water
droplets** in the Moist Air Properties (MA) block connected to your moist air
network.

### R2023b: Consistent reference state for specific enthalpy in moist air domain

To ensure consistency in a moist air mixture, all the specific enthalpies must
have the same reference temperature. Therefore, starting in R2023b, the moist air
domain uses a consistent reference temperature of 0 degC. When you enter specific
enthalpy vectors in the Moist Air Properties (MA)
block, the block internally shifts these vectors to be 0 kJ/kg at 0 degC. The
library blocks then use these adjusted values in the internal calculations. The
simulation data log also displays the adjusted specific enthalpy values.

Use the **Enthalpy reference state** parameter of the
Thermodynamic Properties Sensor (MA) block to
view the specific enthalpy values adjusted with respect to different reference
states. The `As provided in Moist Air Properties (MA)
block` option outputs the same values as in previous
releases.

### R2023a: Control block behavior when moist air properties go out of range during simulation

Previously, if moist air properties went beyond the valid range during simulation,
the block would return an error. You can now use the new **Pressure and
temperature outside valid range** parameter to control the block
behavior if moist air properties go out of range during simulation.

## Description

Global moist air properties for attached circuit

The Moist Air Properties (MA) block defines the moist
air properties that act as global parameters for all the blocks connected to a circuit.
The moist air mixture is composed of dry air, water vapor, and optional trace gas or
water droplets. The default trace gas is carbon dioxide.

Dry air, water vapor, and trace gas are assumed to be semiperfect gas. Pressure,
temperature, and density obey the ideal gas law. Other properties are functions of
temperature. You specify them as one-dimensional arrays corresponding to the
**Temperature vector**.

Each topologically distinct moist air circuit in a diagram can have a
Moist Air Properties (MA) block connected to it. If
no Moist Air Properties (MA) block is attached to a
circuit, the blocks in this circuit use the properties corresponding to the default
Moist Air Properties (MA) block parameter values.
