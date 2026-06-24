# Client Confirmation Checklist / Liste de vérification client
Cardio Check-up RAG — every open `[NEEDS CLIENT CONFIRMATION]` flag across DOC_01–07, consolidated for one client review.
Once answered, these fill the flagged chunks before Qdrant ingestion. Grouped by theme; each item lists the documents it unblocks.

---

## A. Hours & availability / Horaires et disponibilités
1. **Opening hours per site** — Paris 17 (29 rue Bayen) and Neuilly (Hôpital Américain). *(DOC_01 1.3)*
2. **Same-day appointments** — are they available? *(DOC_05 5.2/5.6, DOC_06 Q25)*
3. **Typical wait time** to get an appointment. *(DOC_06 Q25)*
4. **Cancellation notice** — minimum delay required to cancel/reschedule. *(DOC_05 5.6, DOC_06 Q22)*

## B. The team / L'équipe
5. **Languages spoken** by Pr Doguet, Dr Taha, Dr Hakem Rabiaa. *(DOC_02 2.4/2.6/2.7, DOC_01 1.7, DOC_06 Q5)*
6. **English** available with other team members and the secretariat? *(DOC_01 1.7, DOC_06 Q5)*
7. **Consulting days/presence at Cardio Check-up** for Dr Berdah Sadaoui, Dr Taha, Dr Hakem Rabiaa. *(DOC_02 2.5/2.6/2.7)*
8. **Full profiles for Dr Adam Taha and Dr Hakem Rabiaa** — detailed specialties, procedures, and credentials/training (only name + role received so far). *(DOC_02 2.6/2.7)*
9. **Dr Berdah Sadaoui** — any other titles/hospital affiliations beyond AP-HP Cochin Port-Royal. *(DOC_02 2.5)*

## C. Routing boundaries / Frontières d'orientation
10. **Surgical vs non-surgical vascular split** — for each condition (aneurysm, arterial disease/claudication, carotid stenosis, varicose veins, venous insufficiency, thromboembolic follow-up), who takes it: Dr Taha (surgical) or Dr Hakem (medical)? *(DOC_04 4.5/4.6)*
11. **Aorta boundary** — thoracic aorta/aortic root (Pr Doguet) vs abdominal aorta (Dr Taha): confirm the dividing line. *(DOC_04 4.4/4.5)*

## D. Examinations / Examens
12. **Polygraphie nocturne** — who performs it, and the exam details (at home or on site, sensor fitting, what happens). The source sheet is image-based and unreadable. *(DOC_03 3.7, DOC_04 4.8, DOC_06 Q11)*
13. **Durations** of the consultation, ECG, ETT, polygraphy, bilan, and the interventional procedures (only Holter & MAPA fitting ~10 min are confirmed). *(DOC_03, DOC_05 5.6)*
14. **Preparation instructions** specific to the practice for ECG, ETT, consultation, bilan (e.g. fasting, what to wear). *(DOC_03 3.2/3.3/3.6/3.8, DOC_06 Q9)*
15. **Doppler ultrasound** (Dr Hakem) — does it require an ordonnance? *(DOC_04 4.6)*
16. **Interventional procedure logistics** — where ablation, pacemaker, defibrillator, and implantable Holter are performed, and how a patient is scheduled. *(DOC_03 3.9–3.12)*

## E. Prescriptions & reimbursement / Ordonnance et remboursement
17. **Booking without an ordonnance** — does the practice accept exam patients who have no prescription? *(DOC_03 3.3–3.8, DOC_05 5.2, DOC_06 Q12)*
18. **GP referral** — is a referral from the médecin traitant needed? *(DOC_06 Q13)*
19. **Parcours de soins** — is a patient reimbursed normally if they come without going through their médecin traitant first? *(DOC_06 Q15)*

## F. Fees & payment / Tarifs et paiement
20. **Exact fees** per consultation and per examination (and the Secteur 2 supplements). *(DOC_01 1.8b, DOC_05 5.4, DOC_06 Q19)*
21. **Carte Vitale** — is it accepted? *(DOC_05 5.4, DOC_06 Q18)*
22. **Tiers payant** — is direct billing (no upfront payment) offered? *(DOC_05 5.4, DOC_06 Q20)*

## G. Access / Accès
23. **Parking and how to get to the practice** (access, public transport). *(DOC_06 Q24)*
24. **Any other document** the practice requires patients to bring. *(DOC_05 5.3)*

---

### Consistency item to resolve with the Architect (not a client question)
- **DOC_01 §1.5** was approved *before* the team was known; it still says "5 cardiologists" with the other four flagged. The team is now confirmed as **multidisciplinary** (rythmologue + cardiac surgeon + GP + vascular surgeon + vascular physician), and four names are known. DOC_01 1.5 and 1.6 wording should be reconciled with DOC_02 so the bot never calls Pr Doguet/Dr Taha/Dr Hakem "cardiologists." Recommend a small DOC_01 revision pass after DOC_07 sign-off.
