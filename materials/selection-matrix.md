# Material Selection Matrix

## Status: Step 5 — Complete

Five candidate material families evaluated against eight criteria for a 1:5 prototype in an Australian research context.

Scoring: 3 = strong, 2 = moderate, 1 = weak, 0 = unsuitable

---

## Scoring table

| Criterion | PCM | SMA | SMP | Hygromorphic | Mech. Metamaterial |
|---|---|---|---|---|---|
| Trigger clarity | 3 | 3 | 2 | 2 | 3 |
| Geometric response | 0 | 3 | 3 | 2 | 3 |
| Desk-scale fabrication | 3 | 2 | 3 | 3 | 3 |
| Reversible cycles (100+) | 3 | 2 | 1 | 2 | 3 |
| Sourcing in Australia | 3 | 2 | 2 | 3 | 3 |
| Fire / safety class | 2 | 3 | 1 | 2 | 3 |
| Fail-safe default | 3 | 1 | 1 | 3 | 3 |
| Fabrication complexity | 3 | 1 | 2 | 2 | 2 |
| **Total / 24** | **20** | **17** | **15** | **19** | **23** |

---

## Recommendation

**Primary: Mechanical metamaterial (auxetic or deployable lattice, CNC-cut or 3D-printed)**

Reason: highest total score. Geometry-driven response requires no external power for shape logic. Fabrication is feasible with desktop FDM printer or CNC sheet cutter available in most architecture schools. Fail-safe by default (no actuator = no movement). Behaviour is fully deterministic and reproducible. Directly validates the spin-glass optimisation analogy in Step 8 because the geometry of the lattice IS the optimisation variable.

Supported by: 4D-printed mechanical metamaterials review (Taylor & Francis, 2026, DOI 10.1080/19475411.2026.2714783) and active metamaterials critical review (Swansea University, 2024).

**Fallback: Hygromorphic wood bilayer (passive humidity response)**

Reason: no motor, no power, directly demonstrable with laser-cut wood bilayer strips. Nature Communications (2024, DOI 10.1038/s41467-024-54808-8) validated biobased cellulosic hygromorphic bilayers at architectural scale for weather-responsive shading. Limitation: response time is minutes to hours, not seconds.

**PCM note:** PCM scores well on thermal performance but produces no geometric movement visible in prototype. Best suited as a supplementary layer for thermal buffering, not as the primary adaptive mechanism for this facade demonstrator.

---

## Prototype specification (1:5 scale)

- Panel count: 5 panels minimum
- Panel size: 150mm x 300mm each
- Material: TPU or PLA auxetic lattice (FDM printed) OR 3mm plywood bilayer
- Actuation: passive (hygromorphic) OR servo-driven aperture (mechanical metamaterial)
- Sensor: LDR light sensor or DS18B20 temperature sensor per panel cluster
- Controller: Arduino Nano or Raspberry Pi Pico
- Manual override: physical toggle switch, wired in hardware not software
- Safe default: panels close when power is removed (spring return or gravity)
- Documentation: photo at each stage, actuation range measured with protractor, cycle count log
