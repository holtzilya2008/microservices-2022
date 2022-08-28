## Use-cases

```plantuml
@startuml
!define ThemePath https://azuker.github.io/sw-design/puml/theme
!includeurl ThemePath//idesign.puml

title Register new devices

|#1ba1e2|m1|Devices Entities Manager
|#fa6800|e1|Devices Entities Engine
|#60a917|a1|Connected Devices Accessor

|m1|
start
    :Register device;
    |e1|
    :Set required params
    and call devices accessor;
    |a1|
    :Add new device to DB;
    |m1|
    :Device id and initial props;
stop
@enduml
```

```plantuml
@startuml
!define ThemePath https://azuker.github.io/sw-design/puml/theme
!includeurl ThemePath//idesign.puml

title Update device properties / state

|#1ba1e2|m1|Device State Manager
|#fa6800|e1|Device State Engine
|#60a917|a1|Device State Accessor

|m1|
start
    :Update device state;
    |e1|
    :Set required params
    and call device state accessor;
    |a1|
    :Set required device state;
    |m1|
    :Props of the updated device;
stop
@enduml
```

```plantuml
@startuml
!define ThemePath https://azuker.github.io/sw-design/puml/theme
!includeurl ThemePath//idesign.puml

title Devices should be able to send telemetry

|#1ba1e2|m1|Device Telemetry Manager
|#fa6800|e1|Device Telemetry Engine
|#60a917|a1|Raw Telemetry Accessor

|m1|
start
    :Handle incoming message
    from IOT device;
    |e1|
    :Set required params
    and call telemetry accessor;
    |a1|
    :Save raw telemetry data;
    |m1|
    :Notify Telemetry Manager
    (via some message bus)
    to start analyzing and
    processing raw data;
stop
@enduml
```