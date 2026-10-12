# Multiphase Vertical Flow Calculator (Modified Hagedorn–Brown)

A web app that estimates the **pressure drop in a vertical well** carrying gas and liquid, using the modified Hagedorn–Brown method. Built with Python and Django.

## Method
1. **Superficial velocities:** Vsl and Vsg from the in-situ flow rates and the tubing diameter.
2. **Flow regime:** the Orkiszewski bubble/slug boundary,
   L_B = 1.071 − 0.2218·Vm²/D (minimum 0.13). The flow is **bubble** if Vsg/Vm < L_B; otherwise it is **slug**.
3. **Bubble flow → Griffith correlation:** liquid holdup from a slip velocity of 0.8 ft/s, then the hydrostatic and friction gradients.
4. **Slug flow → Hagedorn–Brown correlation:**
   - dimensionless numbers N_L, N_vl, N_vg and N_d
   - the C_NL, H_L/ψ and ψ chart fits, giving liquid holdup H_L
   - the two-phase Reynolds number, Re = 2.2×10⁻² m / (D·μL^HL·μG^(1−HL))
5. **Friction factor:** the explicit Chen (1979) equation (Fanning).
6. **Pressure drop:** Δp = [ρ̄ + f·m² / (7.413×10¹⁰·D⁵·ρ̄)] · ΔL / 144.

The chart fits and equations follow Economides et al., *Petroleum Production Systems*. The correlations are in [`calc/HB.py`](calc/HB.py), [`calc/grifth.py`](calc/grifth.py), [`calc/regime.py`](calc/regime.py) and [`calc/base.py`](calc/base.py).

## Inputs (field units)
| Input | Unit |
|---|---|
| Liquid and gas flow rates (at flowing conditions) | ft³/s |
| Tubing inner diameter | ft |
| Densities | lb/ft³ |
| Viscosities | cP |
| Interfacial tension | dyne/cm |
| Pressure | psia |
| Relative roughness (ε/D) | — |
| Pipe length | ft |

The calculation is for a single segment at average conditions. For long wells, split the well into segments and update the fluid properties in each one.

## Run locally
```bash
pip install -r requirements.txt
python manage.py runserver
```

## Author
Kwaku Appenteng Wiredu, BSc Petroleum Engineering, KNUST (2025)
