from dataclasses import dataclass
from typing import Dict, List

@dataclass
class AirlineConfig:
    airline_code: str
    airline_name: str
    airline_display_name: str
    primary_color: str
    secondary_color: str
    logo_url: str
    headquarters_location: str
    fleet_size: int
    daily_flights_avg: int

AIRLINES: Dict[str, AirlineConfig] = {
    "PIA": AirlineConfig(
        airline_code="PIA",
        airline_name="Pakistan International Airlines",
        airline_display_name="PIA - Pakistan's National Carrier",
        primary_color="#1E3A5F",
        secondary_color="#E8A500",
        logo_url="https://upload.wikimedia.org/wikipedia/en/thumb/2/23/PIA_Logo.svg/300px-PIA_Logo.svg.png",
        headquarters_location="Karachi, Pakistan",
        fleet_size=28,
        daily_flights_avg=80,
    ),
    "AIRBLUE": AirlineConfig(
        airline_code="AIRBLUE",
        airline_name="AirBlue",
        airline_display_name="AirBlue - Excellence in Service",
        primary_color="#003DA5",
        secondary_color="#FF6B35",
        logo_url="https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/AirBlue_Logo.svg/300px-AirBlue_Logo.svg.png",
        headquarters_location="Karachi, Pakistan",
        fleet_size=15,
        daily_flights_avg=45,
    ),
    "SEREAIR": AirlineConfig(
        airline_code="SEREAIR",
        airline_name="SereneAir",
        airline_display_name="SereneAir - Comfort & Convenience",
        primary_color="#00A651",
        secondary_color="#FFD700",
        logo_url="https://upload.wikimedia.org/wikipedia/en/a/a9/Serene_Air_logo.png",
        headquarters_location="Islamabad, Pakistan",
        fleet_size=10,
        daily_flights_avg=30,
    ),
}

def get_airline_config(airline_code: str) -> AirlineConfig:
    if airline_code not in AIRLINES:
        raise ValueError(f"Airline '{airline_code}' not found")
    return AIRLINES[airline_code]

def list_airlines() -> List[str]:
    return list(AIRLINES.keys())
```

4. Click **"Commit changes"**

---

## ✅ STEP 6: Create .streamlit/config.toml Folder & File

1. Click **"Add file"** → **"Create new file"**
2. Filename: `.streamlit/config.toml`
3. Paste this:
```
[theme]
primaryColor = "#1E3A5F"
backgroundColor = "#F5F7FA"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#1A1A1A"
font = "sans serif"

[client]
showErrorDetails = false
maxUploadSize = 200

[logger]
level = "info"

[server]
port = 8501
headless = true
runOnSave = true
maxUploadSize = 200
enableXsrfProtection = true
```

4. Click **"Commit changes"**

---

## ✅ STEP 7: Create .env.template File

1. Click **"Add file"** → **"Create new file"**
2. Filename: `.env.template`
3. Paste this:
```
ENVIRONMENT=dev
DEFAULT_AIRLINE=PIA
LOG_LEVEL=INFO

PIA_SUPABASE_URL=https://your-project.supabase.co
PIA_SUPABASE_KEY=your-public-anon-key

OPENAI_API_KEY=sk-
```

4. Click **"Commit changes"**

---

## ✅ STEP 8: Create .gitignore File

1. Click **"Add file"** → **"Create new file"**
2. Filename: `.gitignore`
3. Paste this:
```
.env
__pycache__/
*.pyc
.DS_Store
.streamlit/secrets.toml
```

4. Click **"Commit changes"**

---

## ✅ STEP 9: Deploy to Streamlit Cloud (THE MAGIC!)

1. Go to: **https://share.streamlit.io**
2. Click **"Sign in with GitHub"**
3. Click **"New app"**
4. Select your username
5. Select repository: `airops-pro`
6. Branch: `main`
7. Main file path: `app.py`
8. Click **"Deploy!"**

**Wait 3-5 minutes... ⏳**

---

## 🎉 YOUR APP IS LIVE!

You'll get a URL like:
```
https://share.streamlit.io/yourname/airops-pro
```

---

## 📸 HERE'S WHAT IT LOOKS LIKE

### **Dashboard Page:**
```
┌─────────────────────────────────────────────────────┐
│ 🛫 Pakistan International Airlines                  │
│ Operational Dashboard                              │
├─────────────────────────────────────────────────────┤
│ On-Time % │ Fleet Util. │ Delays │ Revenue ($M)   │
│  87.3%    │   78.9%     │  156   │    $12.4M      │
│  +2.1%    │   +3.2%     │  -12   │    +$0.45      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [📊 On-Time Performance Chart]  [✈️ Fleet Chart] │
│                                                     │
├─────────────────────────────────────────────────────┤
│ 🚨 Recent Alerts                                   │
│ 🔴 Aircraft N-4567 requires maintenance   2h ago  │
│ 🟠 Flight delayed by 1h 15min (weather)  1h ago  │
│ 🟡 Crew scheduling optimization noted   30m ago  │
│ 🟢 On-time exceeded target              10m ago  │
└─────────────────────────────────────────────────────┘
```

### **Flights Page:**
```
┌─────────────────────────────────────────────────────┐
│ ✈️ Flight Operations                               │
│ [Live Flights] [Routes] [Delays]                  │
├─────────────────────────────────────────────────────┤
│ Flight │ Route  │ Aircraft │ Status    │ Time      │
│ PK-001 │ KHI-ISB│ A320     │ Departed  │ 06:00     │
│ PK-002 │ KHI-LHE│ B777     │ On Time   │ 07:30     │
│ PK-003 │ ISB-KHI│ A320     │ Delayed   │ 08:15     │
│ PK-004 │ LHE-KHI│ B737     │ Cancelled │ 09:00     │
│ PK-005 │ KHI-DXB│ A320     │ Scheduled │ 10:30     │
└─────────────────────────────────────────────────────┘
```

### **Maintenance Page:**
```
┌─────────────────────────────────────────────────────┐
│ 🔧 Maintenance Management                          │
│ [Scheduled] [Alerts] [Predictive]                 │
├─────────────────────────────────────────────────────┤
│ Aircraft │ Type        │ Next Due   │ Duration   │
│ N-1001   │ C-Check     │ 2024-02-15 │ 48 hours   │
│ N-1002   │ A-Check     │ 2024-01-28 │ 12 hours   │
│ N-1003   │ Heavy Maint │ 2024-03-10 │ 200 hours  │
│ N-1004   │ B-Check     │ 2024-02-05 │ 24 hours   │
├─────────────────────────────────────────────────────┤
│ 🚨 ALERTS:                                         │
│ 🔴 N-4567: Engine vibration - Immediate action   │
│ 🟠 N-2345: Hydraulic pressure - Schedule 48h     │
│ 🟡 N-3456: Cabin pressure - Review next check    │
└─────────────────────────────────────────────────────┘
```

### **Revenue Page:**
```
┌─────────────────────────────────────────────────────┐
│ 💰 Revenue Management                              │
│ Monthly Revenue: $12.4M | Load Factor: 82.1%      │
├─────────────────────────────────────────────────────┤
│ Route    │ Current │ Recommended │ Revenue Impact │
│ KHI-ISB  │ $120    │ $125        │ +$2.1K        │
│ KHI-LHE  │ $95     │ $100        │ +$1.8K        │
│ ISB-KHI  │ $115    │ $118        │ +$2.5K        │
│ LHE-KHI  │ $90     │ $95         │ +$1.2K        │
│ KHI-DXB  │ $280    │ $290        │ +$3.5K        │
└─────────────────────────────────────────────────────┘
```

### **AI Insights Page:**
```
┌─────────────────────────────────────────────────────┐
│ 🤖 AI-Powered Insights                             │
│ [Summary] [Predictions] [Optimization]            │
├─────────────────────────────────────────────────────┤
│ MONTHLY REPORT SUMMARY                             │
│ • On-Time Performance: 87.3% (↑ 2.1%)             │
│ • Fleet Utilization: 78.9%                        │
│ • Maintenance Efficiency: 94.2%                   │
│ • Cost Per Seat: $0.082 (↓ 1.2%)                 │
│ • Revenue Per Hour: $2,847 (↑ $145)               │
│                                                     │
│ 🔮 DELAY PREDICTION                               │
│ Predicted Rate: 12.5% | Confidence: 87%          │
│ High Risk Routes: KHI-LHE, ISB-DXB               │
│                                                     │
│ 💡 COST OPTIMIZATION                              │
│ Potential Savings: $280K/month (+6.7%)            │
│ • Fuel Efficiency: $120K/month                    │
│ • Crew Scheduling: $85K/month                     │
│ • Maintenance: $45K/month                         │
│ • Operations: $30K/month                          │
└─────────────────────────────────────────────────────┘
