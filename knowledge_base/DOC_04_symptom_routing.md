# DOC_04 — Symptom Routing Table / Table d'orientation des symptômes
Cardio Check-up · Dr Sana Amraoui
RAG knowledge base — each `##` section is one self-contained Qdrant chunk, chunked by symptom domain.
This document is the routing brain: it maps a patient's symptom to a doctor, an exam, an urgency level, and the clarifying question to ask. Cross-references: doctor details → DOC_02 · exam details → DOC_03.

**Urgency legend (used in every chunk):**
🚨 EMERGENCY — call 15 (SAMU) now, do NOT book · ⚡ URGENT — contact the secretariat the same day or next day · 📅 ROUTINE — standard booking by phone (07 55 50 52 58).
**Légende d'urgence :** 🚨 URGENCE — appelez le 15 (SAMU) maintenant, ne pas réserver · ⚡ URGENT — contactez le secrétariat le jour même ou le lendemain · 📅 COURANT — réservation standard par téléphone (07 55 50 52 58).

---

## 4.1 — Emergency / Urgence
`chunk_id: doc04_emergency` · `lang: fr,en` · `priority: highest`

This chunk never routes to a doctor or to booking. Any of these signs **now** = call 15 (SAMU) immediately. From a mobile you may also dial 112.

### FR
| Signe d'alerte (maintenant) | Question de clarification | Conduite à tenir | Urgence |
|---|---|---|---|
| Douleur thoracique intense, oppressante, qui irradie au bras ou à la mâchoire, avec sueurs/nausées | Aucune — n'attendez pas | Appelez le **15 (SAMU)** immédiatement. Ne réservez pas en ligne. | 🚨 URGENCE |
| Essoufflement soudain et important, au repos | Aucune — n'attendez pas | Appelez le **15**. | 🚨 URGENCE |
| Perte de connaissance, ou malaise avec perte de connaissance en cours | Aucune — n'attendez pas | Appelez le **15**. | 🚨 URGENCE |
| Palpitations accompagnées de douleur thoracique, de malaise ou d'essoufflement sévère | Aucune — n'attendez pas | Appelez le **15**. | 🚨 URGENCE |
| Signes d'AVC : déformation du visage, faiblesse d'un bras, trouble de la parole | Aucune — n'attendez pas | Appelez le **15**. | 🚨 URGENCE |
| Défibrillateur (DAI) ayant délivré un ou plusieurs chocs avec malaise, ou chocs répétés | Aucune — n'attendez pas | Appelez le **15**. | 🚨 URGENCE |

### EN
| Red-flag sign (now) | Clarifying question | What to do | Urgency |
|---|---|---|---|
| Severe, crushing chest pain spreading to the arm or jaw, with sweating/nausea | None — do not wait | Call **15 (SAMU)** immediately. Do not book online. | 🚨 EMERGENCY |
| Sudden, severe breathlessness at rest | None — do not wait | Call **15**. | 🚨 EMERGENCY |
| Loss of consciousness, or fainting with loss of consciousness happening now | None — do not wait | Call **15**. | 🚨 EMERGENCY |
| Palpitations together with chest pain, faintness, or severe breathlessness | None — do not wait | Call **15**. | 🚨 EMERGENCY |
| Signs of stroke: face drooping, arm weakness, speech difficulty | None — do not wait | Call **15**. | 🚨 EMERGENCY |
| Defibrillator (ICD) has delivered a shock with feeling unwell, or repeated shocks | None — do not wait | Call **15**. | 🚨 EMERGENCY |

> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 4.2 — Cardiac rhythm symptoms / Symptômes du rythme cardiaque
`chunk_id: doc04_rhythm` · `lang: fr,en`

All rhythm routing goes to **Dr Sana Amraoui** (cardiologue-rythmologue). The first row is an emergency safeguard.

### FR
| Symptôme / motif | Question de clarification | Médecin → Examen | Urgence |
|---|---|---|---|
| Palpitations AVEC douleur thoracique, malaise ou essoufflement sévère | Aucune — n'attendez pas | Appelez le **15 (SAMU)** | 🚨 URGENCE |
| Palpitations / cœur irrégulier (par ailleurs stable) | Depuis quand ? Régulier ou irrégulier ? Symptômes associés (douleur, essoufflement, malaise) ? | Dr Amraoui → Holter cardiaque | ⚡ URGENT |
| Tachycardie (cœur rapide, récidivant, stable) | Crises brèves ou prolongées ? Déclenchées par l'effort ? | Dr Amraoui → Holter cardiaque | ⚡ URGENT |
| Bradycardie (cœur lent) avec fatigue, vertiges | Vertiges, fatigue, malaises ? Sous traitement ralentissant le cœur ? | Dr Amraoui → Holter cardiaque | ⚡ URGENT |
| Extrasystoles ressenties (« ratés », « à-coups ») | Depuis quand ? Fréquence ? Symptômes associés ? | Dr Amraoui → Holter cardiaque | ⚡ URGENT |
| Syncope / malaise avec perte de connaissance (épisode passé, stable aujourd'hui) | Combien d'épisodes ? Prévenu ou brutal ? À l'effort ? | Dr Amraoui → Holter ± Holter implantable | ⚡ URGENT |
| Fibrillation atriale (FA) connue — suivi | Déjà diagnostiquée ? Sous anticoagulant ? Symptômes récents ? | Dr Amraoui → Consultation | 📅 COURANT |
| Suivi après pose de pacemaker | Date de pose ? Symptômes ? | Dr Amraoui → Consultation spécialisée | 📅 COURANT |
| Suivi après pose de défibrillateur (DAI) | Date de pose ? Choc reçu ? (si choc + malaise : 15) | Dr Amraoui → Consultation spécialisée | 📅 COURANT |
| Discussion d'une ablation (candidat potentiel) | Quel trouble du rythme ? Traitements déjà essayés ? | Dr Amraoui → Consultation | 📅 COURANT |

### EN
| Symptom / reason | Clarifying question | Doctor → Exam | Urgency |
|---|---|---|---|
| Palpitations WITH chest pain, faintness or severe breathlessness | None — do not wait | Call **15 (SAMU)** | 🚨 EMERGENCY |
| Palpitations / irregular heartbeat (otherwise stable) | Since when? Regular or irregular? Associated symptoms (pain, breathlessness, faintness)? | Dr Amraoui → cardiac Holter | ⚡ URGENT |
| Tachycardia (fast heartbeat, recurring, stable) | Brief or prolonged episodes? Triggered by exertion? | Dr Amraoui → cardiac Holter | ⚡ URGENT |
| Bradycardia (slow heartbeat) with fatigue, dizziness | Dizziness, fatigue, faintness? On heart-slowing medication? | Dr Amraoui → cardiac Holter | ⚡ URGENT |
| Felt extra/skipped beats ("flutters") | Since when? How often? Associated symptoms? | Dr Amraoui → cardiac Holter | ⚡ URGENT |
| Syncope / fainting with loss of consciousness (past episode, stable today) | How many episodes? Warning or sudden? During exertion? | Dr Amraoui → Holter ± implantable Holter | ⚡ URGENT |
| Known atrial fibrillation (AF) — follow-up | Already diagnosed? On a blood thinner? Recent symptoms? | Dr Amraoui → consultation | 📅 ROUTINE |
| Follow-up after pacemaker implantation | Date of implant? Symptoms? | Dr Amraoui → specialist consultation | 📅 ROUTINE |
| Follow-up after defibrillator (ICD) implantation | Date of implant? Any shock? (if shock + feeling unwell: 15) | Dr Amraoui → specialist consultation | 📅 ROUTINE |
| Discussing an ablation (possible candidate) | Which rhythm disorder? Treatments already tried? | Dr Amraoui → consultation | 📅 ROUTINE |

> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 4.3 — Chest symptoms (non-acute) / Symptômes thoraciques (non aigus)
`chunk_id: doc04_chest` · `lang: fr,en`

The first row is an emergency safeguard; acute chest pain is never routed to booking. **General (non-rhythm) cardiology consultations here may be with Dr Amraoui or Dr Sofiane** (both cardiologists); rhythm-specific problems go to Dr Amraoui (see 4.2).

### FR
| Symptôme / motif | Question de clarification | Médecin → Examen | Urgence |
|---|---|---|---|
| Douleur thoracique intense MAINTENANT, au repos, ou irradiant bras/mâchoire avec sueurs | Aucune — n'attendez pas | Appelez le **15 (SAMU)** | 🚨 URGENCE |
| Douleur thoracique non aiguë / essoufflement à l'effort | Depuis quand ? Au repos ou à l'effort ? D'autres symptômes associés ? | Dr Amraoui → Consultation ± ETT/bilan | ⚡ URGENT |
| Oppression thoracique intermittente (non aiguë) | À l'effort ou au repos ? Durée ? Soulagée par le repos ? | Dr Amraoui → Consultation ± ETT/bilan | ⚡ URGENT |
| Essoufflement progressif à l'effort (non aigu) | Depuis quand ? Pour quel niveau d'effort ? Gonflement des jambes ? | Dr Amraoui → Consultation ± ETT | ⚡ URGENT |
| Essoufflement la nuit / réveils en manque d'air (orthopnée) | Devez-vous dormir assis ? Gonflement des chevilles ? | Dr Amraoui → Consultation ± ETT | ⚡ URGENT |

### EN
| Symptom / reason | Clarifying question | Doctor → Exam | Urgency |
|---|---|---|---|
| Severe chest pain NOW, at rest, or spreading to arm/jaw with sweating | None — do not wait | Call **15 (SAMU)** | 🚨 EMERGENCY |
| Non-acute chest pain / breathlessness on exertion | Since when? At rest or during exertion? Any other symptoms? | Dr Amraoui → consultation ± ETT/bilan | ⚡ URGENT |
| Intermittent chest tightness (non-acute) | On exertion or at rest? How long? Relieved by rest? | Dr Amraoui → consultation ± ETT/bilan | ⚡ URGENT |
| Progressive breathlessness on exertion (non-acute) | Since when? At what level of effort? Leg swelling? | Dr Amraoui → consultation ± ETT | ⚡ URGENT |
| Breathlessness at night / waking short of breath (orthopnoea) | Do you need to sleep sitting up? Ankle swelling? | Dr Amraoui → consultation ± ETT | ⚡ URGENT |

> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 4.4 — Cardiac surgery indications / Indications de chirurgie cardiaque
`chunk_id: doc04_cardiac_surgery` · `lang: fr,en`

All rows route to **Pr Fabien Doguet** and **always after a cardiology assessment** — patients do not self-refer to cardiac surgery. The first contact is normally a cardiology consultation (Dr Amraoui), which then refers to surgery if needed.

### FR
| Symptôme / motif | Question de clarification | Médecin → Examen | Urgence |
|---|---|---|---|
| Maladie de valve / souffle au cœur — évaluation chirurgicale | Valve déjà diagnostiquée ? Échographie réalisée ? Essoufflement ? | D'abord Dr Amraoui (bilan cardiologique) → puis Pr Doguet **après bilan cardiologique** | 📅 COURANT |
| Candidat à un pontage coronaire | Coronaires déjà explorées ? Avis cardiologique en cours ? | Pr Doguet **après bilan cardiologique** | 📅 COURANT |
| Chirurgie de l'aorte (aorte thoracique / racine aortique) | Dilatation déjà connue ? Imagerie réalisée ? | Pr Doguet **après bilan cardiologique** — *(répartition exacte aorte thoracique vs abdominale entre Pr Doguet et Dr Taha : [NEEDS CLIENT CONFIRMATION])* | 📅 COURANT |

### EN
| Symptom / reason | Clarifying question | Doctor → Exam | Urgency |
|---|---|---|---|
| Valve disease / heart murmur — surgical evaluation | Valve already diagnosed? Ultrasound done? Breathlessness? | First Dr Amraoui (cardiology assessment) → then Pr Doguet **after cardiology assessment** | 📅 ROUTINE |
| Coronary bypass candidate | Coronary arteries already investigated? Cardiology opinion under way? | Pr Doguet **after cardiology assessment** | 📅 ROUTINE |
| Aortic surgery (thoracic aorta / aortic root) | Dilatation already known? Imaging done? | Pr Doguet **after cardiology assessment** — *(exact thoracic-vs-abdominal aorta split between Pr Doguet and Dr Taha: [NEEDS CLIENT CONFIRMATION])* | 📅 ROUTINE |

> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 4.5 — Vascular symptoms — surgical / Symptômes vasculaires — chirurgicaux
`chunk_id: doc04_vascular_surgical` · `lang: fr,en`

Domain target = **Dr Adam Taha** (chirurgien vasculaire). The exact surgical-vs-medical boundary with Dr Hakem Rabiaa is **[NEEDS CLIENT CONFIRMATION]** (their detailed profiles were not received); per-condition indications below are flagged. The first row is an acute-vascular safeguard.

### FR
| Symptôme / motif | Question de clarification | Médecin → Examen | Urgence |
|---|---|---|---|
| Jambe brutalement froide, pâle, douloureuse, insensible (ischémie aiguë) | Aucune — n'attendez pas | Appelez le **15 (SAMU)** | 🚨 URGENCE |
| Anévrisme de l'aorte (abdominale) — prise en charge chirurgicale | Déjà diagnostiqué ? Taille connue ? Surveillance ou chirurgie évoquée ? | Dr Taha *(indication chirurgicale précise : [NEEDS CLIENT CONFIRMATION])* | 📅 COURANT |
| Artériopathie des membres (douleur à la marche / claudication) | Doppler déjà réalisé ? Chirurgie évoquée ? | Dr Taha si chirurgical / Dr Hakem si évaluation d'abord *([NEEDS CLIENT CONFIRMATION])* | 📅 COURANT |
| Sténose carotidienne — évaluation chirurgicale | Déjà détectée à l'écho ? Symptômes neurologiques ? | Dr Taha **après évaluation vasculaire** *([NEEDS CLIENT CONFIRMATION])* | 📅 COURANT |
| Varices nécessitant une chirurgie | Doppler déjà réalisé ? Chirurgie déjà évoquée ? | Dr Taha (si chirurgie) **ou** Dr Hakem (évaluation/sclérothérapie) — voir 4.6 | 📅 COURANT |

### EN
| Symptom / reason | Clarifying question | Doctor → Exam | Urgency |
|---|---|---|---|
| Sudden cold, pale, painful, numb leg (acute limb ischaemia) | None — do not wait | Call **15 (SAMU)** | 🚨 EMERGENCY |
| Aortic aneurysm (abdominal) — surgical management | Already diagnosed? Size known? Surveillance or surgery mentioned? | Dr Taha *(precise surgical indication: [NEEDS CLIENT CONFIRMATION])* | 📅 ROUTINE |
| Peripheral arterial disease (pain on walking / claudication) | Doppler already done? Surgery mentioned? | Dr Taha if surgical / Dr Hakem if assessment first *([NEEDS CLIENT CONFIRMATION])* | 📅 ROUTINE |
| Carotid stenosis — surgical evaluation | Already found on ultrasound? Neurological symptoms? | Dr Taha **after vascular assessment** *([NEEDS CLIENT CONFIRMATION])* | 📅 ROUTINE |
| Varicose veins requiring surgery | Doppler already done? Surgery already mentioned? | Dr Taha (if surgery) **or** Dr Hakem (assessment/sclerotherapy) — see 4.6 | 📅 ROUTINE |

> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 4.6 — Vascular symptoms — non-surgical / Symptômes vasculaires — non chirurgicaux
`chunk_id: doc04_vascular_medical` · `lang: fr,en`

Domain target = **Dr Hakem Rabiaa** (médecin vasculaire / angiologue). Surgical-vs-medical boundary with Dr Taha is **[NEEDS CLIENT CONFIRMATION]**. The first row is an acute-vascular safeguard (suspected clot / pulmonary embolism).

### FR
| Symptôme / motif | Question de clarification | Médecin → Examen | Urgence |
|---|---|---|---|
| Jambe soudain gonflée, douloureuse + essoufflement ou douleur thoracique (suspicion de caillot / embolie) | Aucune — n'attendez pas | Appelez le **15 (SAMU)** | 🚨 URGENCE |
| Varices (évaluation médicale, Doppler, sclérothérapie) | Doppler déjà réalisé ? Chirurgie évoquée ? | Dr Hakem → écho-Doppler **ou** Dr Taha si chirurgie envisagée *([NEEDS CLIENT CONFIRMATION])* | 📅 COURANT |
| Bilan vasculaire par écho-Doppler (général) | Quelle zone (jambes, cou, abdomen) ? Sur prescription ? | Dr Hakem → écho-Doppler *([NEEDS CLIENT CONFIRMATION])* | 📅 COURANT |
| Insuffisance veineuse / jambes lourdes (non aiguë) | Depuis quand ? Gonflement ? Varices visibles ? | Dr Hakem *([NEEDS CLIENT CONFIRMATION])* | 📅 COURANT |
| Suivi de maladie thromboembolique (après phlébite / embolie traitée) | Épisode quand ? Sous anticoagulant ? Stable ? | Dr Hakem *([NEEDS CLIENT CONFIRMATION])* | 📅 COURANT |

### EN
| Symptom / reason | Clarifying question | Doctor → Exam | Urgency |
|---|---|---|---|
| Sudden swollen, painful leg + breathlessness or chest pain (suspected clot / embolism) | None — do not wait | Call **15 (SAMU)** | 🚨 EMERGENCY |
| Varicose veins (medical assessment, Doppler, sclerotherapy) | Doppler already done? Surgery mentioned? | Dr Hakem → Doppler ultrasound **or** Dr Taha if surgery considered *([NEEDS CLIENT CONFIRMATION])* | 📅 ROUTINE |
| Vascular assessment by Doppler ultrasound (general) | Which area (legs, neck, abdomen)? On prescription? | Dr Hakem → Doppler ultrasound *([NEEDS CLIENT CONFIRMATION])* | 📅 ROUTINE |
| Venous insufficiency / heavy legs (non-acute) | Since when? Swelling? Visible varicose veins? | Dr Hakem *([NEEDS CLIENT CONFIRMATION])* | 📅 ROUTINE |
| Thromboembolic disease follow-up (after treated clot / embolism) | When was the episode? On a blood thinner? Stable? | Dr Hakem *([NEEDS CLIENT CONFIRMATION])* | 📅 ROUTINE |

> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 4.7 — Prevention & general cardiovascular health / Prévention et santé cardiovasculaire
`chunk_id: doc04_prevention` · `lang: fr,en`

Domain target = **Dr Leslie Berdah Sadaoui** (médecin généraliste, nutrition/prévention), with documented overlaps where a cardiologist (**Dr Amraoui or Dr Sofiane**) is the right choice — the clarifying question disambiguates. Lifestyle/nutrition/weight → Berdah Sadaoui; a cardiovascular check-up or cardiac symptoms → a cardiologist.

### FR
| Symptôme / motif | Question de clarification | Médecin → Examen | Urgence |
|---|---|---|---|
| Bilan / check-up sans symptômes | S'agit-il d'un bilan hygiène de vie/prévention, ou avez-vous des symptômes cardiaques à explorer ? | Dr Berdah Sadaoui (check-up prévention) **ou** Dr Amraoui (bilan cardiovasculaire complet) | 📅 COURANT |
| Nutrition / surpoids / perte de poids | Objectif ? Antécédents médicaux ? | Dr Berdah Sadaoui → Consultation | 📅 COURANT |
| Facteurs de risque (cholestérol, tabac, sédentarité, diabète) | Lesquels ? Bilan sanguin récent ? | Dr Berdah Sadaoui → Consultation | 📅 COURANT |
| Tension artérielle élevée à surveiller | Mesures à domicile ? Sous traitement ? Tension actuellement > 180/110 ou maux de tête brutaux ou soudains ? → appelez le 15 (SAMU) immédiatement. Sinon, prenez rendez-vous par téléphone au 07 55 50 52 58 pour un suivi par MAPA. | Dr Amraoui → MAPA | 📅 COURANT |
| Antécédents familiaux de maladie cardiaque | Avez-vous des symptômes, ou est-ce un dépistage préventif ? | Dr Amraoui (si symptômes) **ou** Dr Berdah Sadaoui (si prévention/facteurs de risque) | 📅 COURANT |
| Aptitude au sport / reprise du sport, dépistage sportif | Sport d'intensité ? Symptômes à l'effort ? Plus de 40 ans ? | Dr Berdah Sadaoui (prévention) **ou** Dr Amraoui (évaluation cardiaque : ECG/ETT si besoin) | 📅 COURANT |

### EN
| Symptom / reason | Clarifying question | Doctor → Exam | Urgency |
|---|---|---|---|
| Check-up with no symptoms | Is this a lifestyle/prevention check-up, or do you have cardiac symptoms to investigate? | Dr Berdah Sadaoui (prevention check-up) **or** Dr Amraoui (complete cardiovascular bilan) | 📅 ROUTINE |
| Nutrition / overweight / weight loss | Goal? Medical history? | Dr Berdah Sadaoui → consultation | 📅 ROUTINE |
| Risk factors (cholesterol, smoking, inactivity, diabetes) | Which ones? Recent blood test? | Dr Berdah Sadaoui → consultation | 📅 ROUTINE |
| High blood pressure to monitor | Home readings? On treatment? Is your BP currently >180/110, or do you have a sudden severe headache? → call 15 (SAMU) immediately. Otherwise, book by phone at 07 55 50 52 58 for MAPA monitoring. | Dr Amraoui → MAPA | 📅 ROUTINE |
| Family history of heart disease | Do you have symptoms, or is this preventive screening? | Dr Amraoui (if symptoms) **or** Dr Berdah Sadaoui (if prevention/risk factors) | 📅 ROUTINE |
| Fitness for sport / return to sport, athlete screening | High-intensity sport? Symptoms on exertion? Over 40? | Dr Berdah Sadaoui (prevention) **or** Dr Amraoui (cardiac evaluation: ECG/ETT if needed) | 📅 ROUTINE |

> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 4.8 — Sleep & breathing symptoms / Sommeil et respiration
`chunk_id: doc04_sleep` · `lang: fr,en`

Sleep-apnoea screening → **polygraphie nocturne** (performed by **Dr Amraoui**, per the client's practitioner distribution). The first row is an emergency safeguard; nocturnal breathlessness can be cardiac.

### FR
| Symptôme / motif | Question de clarification | Médecin → Examen | Urgence |
|---|---|---|---|
| Essoufflement soudain et sévère MAINTENANT / réveil en suffocation avec douleur thoracique | Aucune — n'attendez pas | Appelez le **15 (SAMU)** | 🚨 URGENCE |
| Ronflements + somnolence diurne / pauses respiratoires constatées | Ronflements ? Pauses respiratoires constatées ? Somnolence dans la journée ? | Polygraphie nocturne (Dr Amraoui) | 📅 COURANT |
| Sommeil non réparateur, maux de tête au réveil + facteurs de risque | Fatigue au réveil ? Hypertension ? Surpoids ? | Polygraphie nocturne (Dr Amraoui) | 📅 COURANT |
| Dépistage d'apnée du sommeil (adressé) | Déjà évoqué par un médecin ? | Polygraphie nocturne (Dr Amraoui) | 📅 COURANT |
| Essoufflement la nuit, devoir dormir assis (possible origine cardiaque) | Gonflement des jambes ? Essoufflement à l'effort le jour ? | Dr Amraoui → Consultation ± ETT | ⚡ URGENT |

### EN
| Symptom / reason | Clarifying question | Doctor → Exam | Urgency |
|---|---|---|---|
| Sudden, severe breathlessness NOW / waking up choking with chest pain | None — do not wait | Call **15 (SAMU)** | 🚨 EMERGENCY |
| Snoring + daytime sleepiness / witnessed breathing pauses | Snoring? Witnessed breathing pauses? Daytime sleepiness? | Nocturnal polygraphy (Dr Amraoui) | 📅 ROUTINE |
| Unrefreshing sleep, morning headaches + risk factors | Tired on waking? High blood pressure? Overweight? | Nocturnal polygraphy (Dr Amraoui) | 📅 ROUTINE |
| Sleep-apnoea screening (referred) | Already raised by a doctor? | Nocturnal polygraphy (Dr Amraoui) | 📅 ROUTINE |
| Breathlessness at night, needing to sleep sitting up (possible cardiac cause) | Leg swelling? Breathlessness on exertion in the daytime? | Dr Amraoui → consultation ± ETT | ⚡ URGENT |

> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 4.9 — Choosing the vascular Doppler exam / Choix de l'examen Doppler vasculaire
`chunk_id: doc04_doppler_selection` · `lang: fr,en`

Domain target = **Dr Hakem Rabiaa** (médecin vasculaire), who performs the vascular Doppler ultrasounds. These are non-urgent explorations on prescription; the first row is an acute-vascular safeguard. If surgery is later indicated, referral to Dr Taha (see 4.5).

### FR
| Motif / zone | Question de clarification | Médecin → Examen | Urgence |
|---|---|---|---|
| Jambe brutalement froide, pâle, douloureuse OU jambe soudain gonflée + essoufflement | Aucune — n'attendez pas | Appelez le **15 (SAMU)** | 🚨 URGENCE |
| Douleurs/crampes des jambes à la marche (claudication) | Depuis quand ? Distance de marche ? Diabète, tabac ? | Dr Hakem → Doppler des artères des membres inférieurs | 📅 COURANT |
| Dépistage risque d'AVC / plaques carotidiennes | Facteurs de risque ? Déjà détecté à l'écho ? | Dr Hakem → Doppler des troncs supra-aortiques (carotides) | 📅 COURANT |
| Hypertension difficile à équilibrer (recherche cause rénale) | Sous plusieurs traitements ? Bilan rénal ? | Dr Hakem → Doppler des artères rénales | 📅 COURANT |
| Dépistage d'anévrisme de l'aorte abdominale | Plus de 60 ans, tabac, antécédents familiaux ? | Dr Hakem → Doppler de l'aorte abdominale | 📅 COURANT |
| Jambes lourdes, varices, suspicion de phlébite (non aiguë) | Gonflement ? Varices visibles ? Doppler déjà fait ? | Dr Hakem → Doppler veineux des membres inférieurs | 📅 COURANT |
| Symptômes vasculaires des bras / mains | Depuis quand ? Effort particulier ? | Dr Hakem → Doppler des artères des membres supérieurs | 📅 COURANT |

### EN
| Reason / area | Clarifying question | Doctor → Exam | Urgency |
|---|---|---|---|
| Sudden cold, pale, painful leg OR sudden swollen leg + breathlessness | None — do not wait | Call **15 (SAMU)** | 🚨 EMERGENCY |
| Leg pain/cramps when walking (claudication) | Since when? Walking distance? Diabetes, smoking? | Dr Hakem → lower-limb arterial Doppler | 📅 ROUTINE |
| Stroke-risk / carotid-plaque screening | Risk factors? Already found on ultrasound? | Dr Hakem → carotid & supra-aortic Doppler | 📅 ROUTINE |
| Hard-to-control high blood pressure (renal cause) | On several treatments? Kidney work-up? | Dr Hakem → renal artery Doppler | 📅 ROUTINE |
| Abdominal aortic aneurysm screening | Over 60, smoking, family history? | Dr Hakem → abdominal aorta Doppler | 📅 ROUTINE |
| Heavy legs, varicose veins, suspected phlebitis (non-acute) | Swelling? Visible varicose veins? Doppler already done? | Dr Hakem → lower-limb venous Doppler | 📅 ROUTINE |
| Arm / hand vascular symptoms | Since when? Particular exertion? | Dr Hakem → upper-limb arterial Doppler | 📅 ROUTINE |

> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

### Update note (2026-06-30, from client Notion inputs)
- **Dr Sofiane added as a second cardiologist**: general (non-rhythm) cardiology, chest-pain and prevention routing now reads "Dr Amraoui or Dr Sofiane" (4.3, 4.7). Rhythm problems stay with Dr Amraoui (4.2).
- **Polygraphie nocturne performer resolved → Dr Amraoui** (4.8).
- **New chunk 4.9** maps vascular symptoms to the specific Doppler exam, all performed by **Dr Hakem Rabiaa** — this resolves the "who does the Doppler" question. Surgical escalation still goes to Dr Taha (4.5).
- The Taha-vs-Hakem boundary is now clearer in principle (Hakem = Doppler / medical assessment; Taha = surgery), but per-condition surgical thresholds remain a clinical judgement — kept flagged below.

### Open flags in DOC_04 (for the Architect)
- **Taha vs Hakem split** (per condition: aneurysm, arterial disease, carotid, varices, Doppler, venous, thromboembolic) — surgical vs non-surgical boundary unconfirmed (4.5, 4.6).
- **Thoracic vs abdominal aorta** boundary between Pr Doguet (4.4) and Dr Taha (4.5).
- **Polygraphie performer** (4.8, all rows).
- **Doppler-on-prescription** detail (4.6) — whether Dr Hakem's Doppler needs an ordonnance.

### Safety additions beyond the mandated emergency rows (please confirm)
Per the cross-cutting safety rule ("ANY row where the symptom could be acute/life-threatening must carry the EMERGENCY level"), I added 🚨 emergency safeguard rows to **4.5 (acute limb ischaemia)** and **4.6 (suspected clot / pulmonary embolism)** in addition to the mandated 4.2 / 4.3 / 4.8. Tell me to keep or remove.

### Assertions made beyond the confirmed list (please confirm)
- **High blood pressure to monitor → Dr Amraoui · MAPA · ⚡ URGENT** (4.7) — derived from confirmed MAPA performer; flag if you'd rather route BP to prevention.
- **Nocturnal breathlessness / orthopnoea → Dr Amraoui · consultation ± ETT** (4.3, 4.8) — asserted as a cardiac red flag; confirm.
- **Athlete/sport screening → Berdah Sadaoui or Amraoui** (4.7) — presented as an overlap with clarifying question; confirm default.
