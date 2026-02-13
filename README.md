Core Components
1. Ranger Inputs (Sidebar)
- Animal ID: 
- Date picker
- 4 Threat sliders (0-10): Habitat Loss, Predation, Competition, Disease  
- Shannon Diversity (0.5-3.0): Healthy=1.8+
- Pathogen Load % (0-50)
- Reference image guide
2. Risk Algorithm 
total_threat = Σ(threat_weight × intensity/10)
raw_score = total_threat + (pathogens × 0.5) - (shannon × 10)
risk_score = min(100, max(0, raw_score / 2.25))  # 0-100 scale
Thresholds:
HIGH (>70) = Emergency quarantine 🔴
MEDIUM (40-70) = Enhanced monitoring 🟡
LOW (<40) = Routine patrols 🟢
Weights: Habitat(65) > Predation(55) > Competition(45) > Disease(35)
3. Web3 Integration (No Tokens!)
python
@st.cache_data
def generate_ipfs_hash(risk_data):
    json_str → SHA256 → "Qm" + hash[:44] = IPFS CID
