# Holographic Envelopes — گزارش تحقیقاتی کامل و اجرایی

**پروژه:** Holographic Envelope  
**تاریخ:** 2026-09-23  
**وضعیت:** تحقیق فعال — هیچ پانل، کوپن یا نتیجه آزمایشگاهی ادعا نمی‌شود  

---

## ۱. چکیده اجرایی

این گزارش چهار جهت تحقیقاتی پروژه Holographic Envelope را از سطح نظری تا سطح اجرایی گسترش می‌دهد:

1. **TFE** (Temporal Facade Entropy) — کمیت اطلاعاتی برای اندازه‌گیری پوسته‌های هوشمند  
2. **H_facade** (Architectural Ising Hamiltonian) — مدل اسپین‌گلس برای بهینه‌سازی چندهدفه  
3. **BIR** (Boundary Information Ratio) — نسبت هولوگرافیک مرز به درون  
4. **D03 / جایگزین‌ها** — مسیر مواد عملگر (spore / wood / SMA / cellulose 4D)

---

## ۲. بازار — اعداد واقعی

**NON-CORE.** Market / TAM / CAGR text was moved (not deleted) to [`DOWNSTREAM/commercialization/holographic-envelope-market-notes.md`](../DOWNSTREAM/commercialization/holographic-envelope-market-notes.md). Activate only when the three commercialization gates in `CHARTER.md` are met.

---

## ۳. TFE — Temporal Facade Entropy

```
TFE(i, t) = H_space(t) × H_time(i)

H_space(t) = -sum_k p_k(t) * log2(p_k(t))     [bits]
H_time(i)  = -sum_tau q_tau(i) * log2(q_tau(i)) [bits]

دامنه: TFE ∈ [0, log2(N) × log2(T)]
TFE = 0  iff  نمای استاتیک (اثبات‌شده)
```

**شرط ابطال:**
اگر TFE_optimised ≤ TFE_rule-based در ۳ اجرای مستقل Wallacei با seed مختلف،
مدل بهینه‌سازی یا H_facade به‌درستی فرمول‌بندی نشده.

---

## ۴. H_facade — Architectural Ising Hamiltonian

```
H_facade(σ) = -sum_{i<j} J^arch_ij * σ_i * σ_j  -  sum_i h_i * σ_i  + λ*P(σ)

σ ∈ [-1,+1]^6:
  σ_1 = depth
  σ_2 = aperture
  σ_3 = rotation
  σ_4 = hysteresis ε
  σ_5 = max_step Δs
  σ_6 = rad_weight wr
```

**مثلث ناکام:**
```
sign(J_{ε,Δs}) × sign(J_{Δs,wr}) × sign(J_{wr,ε}) = -1
→ چند کمینه محلی → RSB (Replica Symmetry Breaking)
```

**پروتکل تشخیص RSB:**
```
1. ۱۰ اجرای Wallacei با seed مختلف، هر بار 5000 نسل
2. استخراج ژن‌های Pareto frontier
3. محاسبه فاصله زوجی: d_{ab} = ||σ_Pareto_a - σ_Pareto_b||_2
4. Hartigan Dip Test روی P_arch(d)

شرط RSB: p < 0.05  AND  K ≥ 2
شرط ابطال: p > 0.1 (توزیع تک-حالتی)
```

---

## ۵. BIR — Boundary Information Ratio

```
BIR(t) = H_boundary(t) / H_interior(t)

H_boundary(t) = H_space(t)
H_interior(t) = Shannon entropy (occupancy + zone temp + activity)

BIR ∈ [0, 1]
BIR = 0: پوسته کور
BIR → 1: پوسته هولوگرافیک

آنالوگ: S_BH = A / (4 * l_p²)
[BIR از AdS/CFT مشتق نمی‌شود — آنالوگ ماکروسکوپی است]
```

---

## ۶. مواد عملگر — داده واقعی

| معیار | Spore | Wood | SMA | Cellulose 4D |
|-------|-------|------|-----|-------------|
| زمان پاسخ | <3 min (latex) | 20-30 min | ثانیه-دقیقه | 30 min |
| چرخه‌های آزمون | 10 (latex Birch 2021) | 1 سال outdoor | مقاوم (با کاوت) | 170 + 13 ماه |
| مقیاس معماری | 1×2 cm + prototype | HygroSkin | louver 1:1 | 424 ماژول livMatS |
| trigger | رطوبت | رطوبت | دما/تابش | رطوبت+دما |
| germination مشکل | بله | خیر | خیر | خیر |
| cork dependency | بله (آزمایش‌نشده) | خیر | خیر | خیر |
| آزمون برای HE | خیر | خیر | خیر | خیر |

---

## ۷. کشف‌های اجرایی با علت و دلیل

### کشف ۱: شکاف بازار Smart Adaptive (CAGR 17.8%)

**NON-CORE.** Market-gap note moved (not deleted) to [`DOWNSTREAM/commercialization/holographic-envelope-market-notes.md`](../DOWNSTREAM/commercialization/holographic-envelope-market-notes.md).

### کشف ۲: Cellulose 4D Print = اجرایی‌ترین مسیر کوتاه‌مدت

علت:
- Cheng 2024: 424 ماژول، 13 ماه outdoor، بدون برق، بدون germination
- تنها جایگزینی که شواهد facade-scale دارد

ریسک: فیلامان cellulose/PK سفارشی است. proxy (wood PLA) باید برچسب‌گذاری شود.

### کشف ۳: RSB در Wallacei = کشف اصیل بالقوه

علت: هیچ کار منتشرشده‌ای RSB را در GA معماری اندازه نگرفته.
شرط اثبات: Hartigan Dip Test روی ۱۰ اجرای مستقل → p < 0.05 و K ≥ 2
ارزش: قابل انتشار ACADIA 2027 + پایه ابزار تجاری

### کشف ۴: Spore + Energy Harvesting = مدل کسب‌وکار جدید

**NON-CORE.** Business-model note moved (not deleted) to [`DOWNSTREAM/commercialization/holographic-envelope-market-notes.md`](../DOWNSTREAM/commercialization/holographic-envelope-market-notes.md).

---

## ۸. دیدگاه بُعد چهارم و سوم‌شخص انسان

انسان به‌عنوان ناظر بیرونی (سوم‌شخص):
- در t=0: TFE = 0 → نمای خاموش
- با گذر زمان (بُعد چهارم): TFE > 0 → کروگرافی اطلاعاتی
- پوسته به‌عنوان فیلم اطلاعاتی درون

```
zone پر (H_interior بالا) → H_space بالا → BIR → 1
ساختمان خالی (H_interior پایین) → H_space پایین → BIR → 0
                                                   (efficient, نه bad)
```

H_time(i) آنتروپی تاریخ پانل i در طول زمان:
- H_time = 0: پانل مرده (همیشه یک حالت)
- H_time = log2(T): پانل تصادفی (نویز)
- هدف: H_time متناسب با ریتم محیطی (شبانه‌روز، فصلی)

---

## ۹. ترتیب اجرا

```
فاز ۱ (0-6 هفته): Wallacei RSB detection
  - ساخت H_facade در Grasshopper
  - 10 اجرا با seed مختلف
  - Hartigan Dip Test

فاز ۲ (6-12 هفته): Track A spore + Track C cellulose
  - کوپن‌های 1×2 cm latex
  - n_layers: {1,2,3,4,5}
  - پرینت cellulose/PK proxy

فاز ۳ (12-24 هفته): BIR اندازه‌گیری
  - PIR + thermocouple + دوربین
  - BIR روزانه

فاز ۴ (24+ هفته):
  - ارسال ACADIA 2027
  - Dezeen press summary
```

---

## ۱۰. آنچه این گزارش ادعا نمی‌کند

- هیچ پانل HE ساخته نشده
- هیچ BIR، TFE، theta_max اندازه‌گیری نشده
- RSB تایید نشده — پیش‌بینی است
- اسپور روی cork آزمایش نشده
- BIR از AdS/CFT مشتق نمی‌شود
- energy harvesting در facade ثابت نشده

---

*منابع بازار: moved to `DOWNSTREAM/commercialization/holographic-envelope-market-notes.md` (NON-CORE).*  
*منابع آزمایشگاهی: Chen 2014/2015، Birch 2021/2024، Holstov 2015/2017، Cheng 2024، Stelzmann 2024*
