# Physical Prototype Log

## Status: Step 7 — Specification complete, build pending

---

## Minimum viable prototype (MVP)

### Configuration
- 5 panels arranged as a flat or curved strip (1:5 scale of a 3m x 6m facade bay)
- Each panel: 150mm x 300mm
- Material (Option A): TPU auxetic lattice, FDM printed, 20% infill, gyroid or re-entrant hexagon cell
- Material (Option B): 3mm plywood + 1mm maple veneer bilayer, laser cut, hygromorphic
- Actuation range: 0 to 75 degrees rotation OR 0 to 60% aperture opening

### Electronics (Option A — active)
- Arduino Nano or Raspberry Pi Pico
- 1x LDR per panel cluster
- 1x DS18B20 temperature sensor
- 5x SG90 servo motors (5V, 1.8kg/cm torque)
- Manual override toggle switch (hardware, not software)
- Power: USB 5V bench supply
- Safe default: servo returns to 0 degrees on power loss (spring or gravity assist)

### Electronics (Option B — passive hygromorphic)
- No electronics
- Humidity source: spray bottle or humid/dry room test
- Measurement: time-lapse camera, protractor overlay
- Cycle test: wet/dry/wet = 1 cycle, target 100 cycles minimum

---

## Build log template

| Stage | Description | Date | Notes |
|---|---|---|---|
| 1 | Panel geometry printed or cut | — | — |
| 2 | Sensor wiring complete | — | — |
| 3 | Controller code loaded | — | — |
| 4 | First actuation test | — | — |
| 5 | Sensor failure test | — | — |
| 6 | Manual override test | — | — |
| 7 | 100-cycle endurance test | — | — |
| 8 | Measurement of actuation range | — | — |

---

## Falsification criteria

- Panel must respond to sensor input within 5 seconds.
- Panel must return to safe (closed) position within 3 seconds of simulated sensor failure.
- Panel must complete 100 actuation cycles without structural failure or significant hysteresis drift (>10%).
- Manual override must function independently of software state.

---

## Key reference

Nature Communications (2024): biobased cellulosic hygromorphic bilayers validated at architectural scale for weather-responsive shading, energy-autonomous operation, and reversible actuation. DOI: 10.1038/s41467-024-54808-8.
