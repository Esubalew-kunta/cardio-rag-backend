# DOC_03 — Service Catalogue / Catalogue des examens et actes
Cardio Check-up · Dr Sana Amraoui
RAG knowledge base — each `##` section is one self-contained Qdrant chunk.
Within each service chunk: the "What it is" field = general medical knowledge (definition only); all practice-specific facts (duration, prep, ordonnance policy, cost, performer) are either source-confirmed or flagged [NEEDS CLIENT CONFIRMATION]. The two are kept in separate fields, never blended.
Booking (all services): Doctolib (cardio-check-up.com) · 07 55 50 52 58 (9h–18h) · secretariatdramraoui@myeva.ovh.

---

## 3.1 — Emergency / Urgence
`chunk_id: doc03_emergency` · `lang: fr,en` · `priority: highest`

**FR —** 🚨 **URGENCE.** En cas de **douleur thoracique intense MAINTENANT**, d'**essoufflement soudain MAINTENANT**, ou de **perte de connaissance**, appelez **immédiatement le 15 (SAMU)** — avant toute autre chose. N'utilisez pas la réservation en ligne et n'attendez pas la réponse à un message. Le 15 est gratuit et joignable 24h/24. Depuis un mobile, vous pouvez aussi composer le 112 (numéro d'urgence européen). Cardio Check-up est un cabinet de consultation, pas un service d'urgence.

**EN —** 🚨 **EMERGENCY.** If you have **severe chest pain NOW**, **sudden breathlessness NOW**, or **loss of consciousness**, call **15 (SAMU) immediately** — before anything else. Do not use online booking and do not wait for a reply. 15 is free and available 24/7. From a mobile you can also dial 112 (the European emergency number). Cardio Check-up is an outpatient practice, not an emergency service.

---

## 3.2 — Consultation cardiologique / Cardiology consultation
`chunk_id: doc03_consultation` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Un rendez-vous avec un cardiologue qui écoute votre histoire et vos symptômes, vous examine (cœur, pouls, tension) et décide, si besoin, des examens complémentaires.
- **Pourquoi / Indications :** symptômes cardiaques (douleur thoracique, palpitations, essoufflement, malaises), suivi d'une maladie connue, avis avant un traitement ou une intervention, demande de bilan.
- **Durée :** **[NEEDS CLIENT CONFIRMATION]**.
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation. Modalités de remboursement / parcours de soins : voir DOC_05 et **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** apportez vos examens et ordonnances récents ainsi que la liste de vos médicaments. Autres consignes du cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** un cardiologue de l'équipe Cardio Check-up (voir DOC_02). Le médecin précis dépend du motif : **[NEEDS CLIENT CONFIRMATION]**.
- **Rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** an appointment with a cardiologist who listens to your history and symptoms, examines you (heart, pulse, blood pressure) and, if needed, decides on further tests.
- **What it is for:** heart symptoms (chest pain, palpitations, breathlessness, dizzy spells), follow-up of a known condition, an opinion before treatment or surgery, or a request for a check-up.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **Prescription:** an ordonnance is not required to book a consultation. Reimbursement / referral-pathway details: see DOC_05 and **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** bring your recent tests and prescriptions and a list of your medicines. Other practice instructions: **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** a cardiologist from the Cardio Check-up team (see DOC_02). The specific doctor depends on the reason: **[NEEDS CLIENT CONFIRMATION]**.
- **Booking:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.3 — ECG (électrocardiogramme) / ECG (electrocardiogram)
`chunk_id: doc03_ecg` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Un examen rapide et indolore qui enregistre l'activité électrique du cœur à l'aide d'électrodes posées sur la peau (poitrine, bras, jambes). Il montre le rythme du cœur et la façon dont l'influx électrique s'y propage.
- **Pourquoi / Indications :** palpitations, rythme irrégulier, douleur thoracique, malaises, dans le cadre d'un bilan cardiovasculaire ou du suivi d'un traitement.
- **Durée :** **[NEEDS CLIENT CONFIRMATION]**.
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** aucune préparation particulière n'est généralement nécessaire. Consignes propres au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** Dr Sana Amraoui.
- **Rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a quick, painless test that records the heart's electrical activity using electrodes placed on the skin (chest, arms, legs). It shows the heart's rhythm and how the electrical signal travels through it.
- **What it is for:** palpitations, an irregular heartbeat, chest pain, dizzy spells, as part of a cardiovascular check-up or to monitor a treatment.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** no special preparation is usually needed. Practice-specific instructions: **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** Dr Sana Amraoui.
- **Booking:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.4 — Holter cardiaque ECG (24h–2 semaines) / Cardiac Holter ECG (24h–2 weeks)
`chunk_id: doc03_holter_ecg` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Un petit enregistreur portable qui mesure l'électrocardiogramme en continu, de 24 heures jusqu'à 2 semaines, pendant que vous vaquez à vos activités. *(Source : fiche d'information Holter ECG.)*
- **Pourquoi / Indications :** mettre en évidence un trouble du rythme cardiaque ; contrôler l'efficacité d'un traitement. Examen indolore qui n'entrave pas vos activités quotidiennes. *(Source confirmée.)*
- **Durée :** pose ~10 minutes ; port de 24 heures jusqu'à 2 semaines selon la prescription. *(Source confirmée.)*
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** 5 électrodes collées sur le thorax ; **pas de douche** (l'appareil n'est pas étanche) ; privilégiez des vêtements en coton peu décolletés ; tenez téléphones/tablettes à distance ; évitez bijoux au cou ; **ne pas arrêter l'appareil**. *(Source confirmée.)*
- **Qui le réalise :** Dr Sana Amraoui.
- **Retour du matériel & pénalités :** restitution à la date indiquée par l'assistante médicale ; **150 € par jour de retard** ; **500 € si l'appareil est restitué en mauvais état**. *(Source confirmée.)*
- **Rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a small portable recorder that continuously captures your ECG, from 24 hours up to 2 weeks, while you go about your daily life. *(Source: Holter ECG information sheet.)*
- **What it is for:** to reveal a heart-rhythm disorder; to check whether a treatment is working. The test is painless and does not interrupt your daily activities. *(Confirmed from source.)*
- **Duration:** fitting ~10 minutes; worn for 24 hours up to 2 weeks depending on the prescription. *(Confirmed from source.)*
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** 5 electrodes stuck to the chest; **no showering** (the device is not waterproof); prefer cotton, not-too-low-cut clothing; keep phones/tablets away; avoid neck jewellery; **do not switch the device off**. *(Confirmed from source.)*
- **Who performs it:** Dr Sana Amraoui.
- **Device return & penalties:** return on the date set by the medical assistant; **€150 per day late**; **€500 if the device is returned damaged**. *(Confirmed from source.)*
- **Booking:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.5 — MAPA / Holter tensionnel (24h) / ABPM, blood-pressure Holter (24h)
`chunk_id: doc03_mapa` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Un appareil qui enregistre automatiquement la tension artérielle pendant 24 heures, à l'aide d'un brassard porté au bras, pendant vos activités habituelles. *(Source : fiche d'information MAPA.)*
- **Pourquoi / Indications :** contrôler les variations de la tension (hypotension ou hypertension) sur la journée et la nuit ; vérifier l'efficacité d'un traitement. Examen indolore. *(Source confirmée.)*
- **Durée :** pose ~10 minutes ; port 24 heures ; mesures **toutes les 20 min le jour** et **toutes les heures la nuit**. *(Source confirmée.)*
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** brassard placé sur le **bras non dominant** ; gardez le bras immobile pendant la mesure ; portez des manches larges ; **pas de douche** (appareil non étanche) ; portez un T-shirt par-dessus le tuyau la nuit. En cas d'inconfort, de bras engourdi ou douloureux, ôtez le brassard et contactez le médecin ; assistance au 07 55 50 52 58 (9h–18h). *(Source confirmée.)*
- **Qui le réalise :** Dr Sana Amraoui.
- **Retour du matériel & pénalités :** restitution à la date indiquée par l'assistante médicale ; **150 € par jour de retard** ; **500 € si l'appareil est restitué en mauvais état**. *(Source confirmée.)*
- **Rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a device that automatically records your blood pressure over 24 hours, using a cuff worn on the arm, while you go about your usual activities. *(Source: MAPA information sheet.)*
- **What it is for:** to track how blood pressure varies (low or high) across day and night; to check whether a treatment is working. The test is painless. *(Confirmed from source.)*
- **Duration:** fitting ~10 minutes; worn for 24 hours; measurements **every 20 min during the day** and **every hour at night**. *(Confirmed from source.)*
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** cuff placed on the **non-dominant arm**; keep the arm still during a measurement; wear loose sleeves; **no showering** (not waterproof); wear a T-shirt over the tubing at night. If the arm becomes numb, painful or uncomfortable, remove the cuff and contact the doctor; helpline 07 55 50 52 58 (9 am–6 pm). *(Confirmed from source.)*
- **Who performs it:** Dr Sana Amraoui.
- **Device return & penalties:** return on the date set by the medical assistant; **€150 per day late**; **€500 if the device is returned damaged**. *(Confirmed from source.)*
- **Booking:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.6 — Échographie cardiaque / ETT / Cardiac ultrasound (transthoracic echo)
`chunk_id: doc03_ett` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une échographie du cœur réalisée avec une sonde posée sur la poitrine. Indolore et sans rayons, elle montre la taille du cœur, la force de sa contraction, l'état des valves et les pressions.
- **Pourquoi / Indications :** essoufflement, souffle au cœur, suivi d'une valvulopathie ou d'une maladie du muscle cardiaque, dans le cadre d'un bilan cardiovasculaire complet.
- **Durée :** **[NEEDS CLIENT CONFIRMATION]**.
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** aucune préparation particulière n'est généralement nécessaire. Consignes propres au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** Dr Sana Amraoui.
- **Rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** an ultrasound of the heart taken with a probe placed on the chest. Painless and radiation-free, it shows the heart's size, how strongly it pumps, the condition of the valves, and pressures.
- **What it is for:** breathlessness, a heart murmur, follow-up of a valve or heart-muscle condition, or as part of a complete cardiovascular check-up.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** no special preparation is usually needed. Practice-specific instructions: **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** Dr Sana Amraoui.
- **Booking:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.7 — Polygraphie nocturne / Nocturnal (sleep) polygraphy
`chunk_id: doc03_polygraphie` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Un examen qui enregistre, pendant une nuit, plusieurs paramètres de votre sommeil (respiration, oxygène dans le sang, rythme cardiaque, ronflement) pour dépister les apnées du sommeil — des pauses respiratoires qui retentissent sur le cœur.
- **Pourquoi / Indications :** ronflements importants, somnolence dans la journée, pauses respiratoires constatées pendant le sommeil, fatigue, en lien avec l'hypertension ou des troubles du rythme.
- **Durée :** **[NEEDS CLIENT CONFIRMATION]**.
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** l'appareil, léger, est posé le soir et restitué le lendemain matin ; il enregistre la respiration, l'oxygène du sang, le rythme cardiaque et les ronflements. Modalités précises (à domicile ou au cabinet, pose des capteurs) : **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** Dr Sana Amraoui. *(Performer confirmé par la répartition praticiens de la cliente, 30 juin 2026.)*
- **Retour du matériel & pénalités :** le boîtier de polygraphie (PGV) vous est confié et doit être restitué à la date indiquée ; **100 € par jour de retard** ; **500 € si l'appareil est restitué en mauvais état**. *(Source confirmée.)*
- **Rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a test that records, over one night, several aspects of your sleep (breathing, blood oxygen, heart rhythm, snoring) to screen for sleep apnoea — breathing pauses that affect the heart.
- **What it is for:** heavy snoring, daytime sleepiness, breathing pauses noticed during sleep, fatigue, in connection with high blood pressure or rhythm disorders.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** the light device is fitted in the evening and returned the next morning; it records breathing, blood oxygen, heart rhythm and snoring. Exact arrangements (at home or at the practice, fitting the sensors): **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** Dr Sana Amraoui. *(Performer confirmed by the client's practitioner distribution, 30 June 2026.)*
- **Device return & penalties:** the polygraphy recorder (PGV) is entrusted to you and must be returned on the set date; **€100 per day late**; **€500 if the device is returned damaged**. *(Confirmed from source.)*
- **Booking:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.8 — Bilan cardiovasculaire complet / Complete cardiovascular check-up
`chunk_id: doc03_bilan` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Un bilan qui réunit, au cours d'une même prise en charge, un **examen clinique**, un **ECG** et une **échographie cardiaque (ETT)**. *(Composition confirmée par les comptes-rendus source.)*
- **Pourquoi / Indications :** faire le point sur sa santé cardiovasculaire, dépister des anomalies, en présence de facteurs de risque (tension, cholestérol, antécédents familiaux) ou de symptômes.
- **Durée :** **[NEEDS CLIENT CONFIRMATION]**.
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** apportez vos examens récents et la liste de vos médicaments. Consignes propres au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** Dr Sana Amraoui.
- **Rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** an assessment combining, within a single visit, a **clinical examination**, an **ECG** and a **cardiac ultrasound (ETT)**. *(Composition confirmed by the source consultation reports.)*
- **What it is for:** to review your cardiovascular health and detect abnormalities, in the presence of risk factors (blood pressure, cholesterol, family history) or symptoms.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** bring your recent tests and a list of your medicines. Practice-specific instructions: **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** Dr Sana Amraoui.
- **Booking:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.9 — Ablation par cathéter / Catheter ablation
`chunk_id: doc03_ablation` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Un acte de rythmologie au cours duquel de fins cathéters sont guidés jusqu'au cœur pour neutraliser, par la chaleur ou le froid, les très petites zones responsables d'un trouble du rythme — afin de rétablir un rythme régulier.
- **Pourquoi / Indications :** certains troubles du rythme cardiaque, notamment la fibrillation atriale et d'autres tachycardies, lorsque le médecin en pose l'indication.
- **Durée :** **[NEEDS CLIENT CONFIRMATION]**.
- **Modalités :** cet acte ne se réserve pas directement en ligne ; il est décidé par le cardiologue-rythmologue après consultation et bilan (indication médicale). Lieu de réalisation et modalités pratiques : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** Dr Sana Amraoui.
- **Premier rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a rhythm procedure in which thin catheters are guided to the heart to neutralise, using heat or cold, the very small areas causing a rhythm disorder — to restore a regular heartbeat.
- **What it is for:** certain heart-rhythm disorders, notably atrial fibrillation and other fast rhythms, when the doctor judges it indicated.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **How it is arranged:** this procedure is not booked directly online; it is decided by the cardiologist-electrophysiologist after a consultation and assessment (medical indication). Where it is performed and practical details: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** Dr Sana Amraoui.
- **First appointment:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.10 — Implantation de pacemaker / Pacemaker implantation
`chunk_id: doc03_pacemaker` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** La pose d'un petit appareil, placé sous la peau près de l'épaule et relié au cœur par une ou plusieurs sondes, qui aide le cœur à conserver un rythme suffisant lorsqu'il bat trop lentement.
- **Pourquoi / Indications :** cœur trop lent (bradycardie), pauses du rythme, malaises ou pertes de connaissance d'origine rythmique, lorsque le médecin en pose l'indication.
- **Durée :** **[NEEDS CLIENT CONFIRMATION]**.
- **Modalités :** cet acte ne se réserve pas directement en ligne ; il est décidé par le cardiologue-rythmologue après consultation et bilan (indication médicale). Lieu de réalisation et modalités pratiques : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** Dr Sana Amraoui.
- **Premier rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** the placement of a small device, set under the skin near the shoulder and connected to the heart by one or more leads, which helps the heart keep an adequate rhythm when it beats too slowly.
- **What it is for:** a heart that is too slow (bradycardia), pauses in the rhythm, dizzy spells or blackouts of rhythmic origin, when the doctor judges it indicated.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **How it is arranged:** this procedure is not booked directly online; it is decided by the cardiologist-electrophysiologist after a consultation and assessment (medical indication). Where it is performed and practical details: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** Dr Sana Amraoui.
- **First appointment:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.11 — Implantation de défibrillateur (DAI) / Defibrillator (ICD) implantation
`chunk_id: doc03_defibrillateur` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** La pose d'un appareil, placé sous la peau et relié au cœur, qui surveille en permanence le rythme cardiaque et délivre, si nécessaire, un choc électrique pour interrompre un rythme rapide dangereux.
- **Pourquoi / Indications :** risque de troubles du rythme rapides graves, ou antécédent d'un tel épisode, lorsque le médecin en pose l'indication.
- **Durée :** **[NEEDS CLIENT CONFIRMATION]**.
- **Modalités :** cet acte ne se réserve pas directement en ligne ; il est décidé par le cardiologue-rythmologue après consultation et bilan (indication médicale). Lieu de réalisation et modalités pratiques : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** Dr Sana Amraoui.
- **Premier rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** the placement of a device, set under the skin and connected to the heart, that continuously monitors the heart rhythm and, if needed, delivers an electrical shock to stop a dangerous fast rhythm.
- **What it is for:** a risk of serious fast rhythm disorders, or a previous such episode, when the doctor judges it indicated.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **How it is arranged:** this procedure is not booked directly online; it is decided by the cardiologist-electrophysiologist after a consultation and assessment (medical indication). Where it is performed and practical details: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** Dr Sana Amraoui.
- **First appointment:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.12 — Holter implantable / Implantable cardiac monitor (loop recorder)
`chunk_id: doc03_holter_implantable` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Un très petit enregistreur placé sous la peau, devant le cœur, qui surveille le rythme cardiaque en continu pendant plusieurs mois à plusieurs années — utile pour capter des anomalies rares ou intermittentes.
- **Pourquoi / Indications :** malaises ou pertes de connaissance inexpliqués, recherche d'un trouble du rythme intermittent (par ex. fibrillation atriale) non retrouvé par un Holter classique.
- **Durée :** **[NEEDS CLIENT CONFIRMATION]**.
- **Modalités :** cet acte ne se réserve pas directement en ligne ; il est décidé par le cardiologue-rythmologue après consultation et bilan (indication médicale). Lieu de réalisation et modalités pratiques : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** Dr Sana Amraoui.
- **Premier rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a very small recorder placed under the skin in front of the heart that monitors the heart rhythm continuously for several months to several years — useful for catching rare or intermittent abnormalities.
- **What it is for:** unexplained dizzy spells or blackouts, looking for an intermittent rhythm disorder (e.g. atrial fibrillation) not captured by a standard Holter.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **How it is arranged:** this procedure is not booked directly online; it is decided by the cardiologist-electrophysiologist after a consultation and assessment (medical indication). Where it is performed and practical details: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** Dr Sana Amraoui.
- **First appointment:** Doctolib · 07 55 50 52 58 (9 am–6 pm).
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.13 — Épreuve d'effort / Exercise stress test
`chunk_id: doc03_epreuve_effort` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Un examen qui évalue le comportement du cœur pendant un effort physique progressif et contrôlé (sur vélo ou tapis de marche), sous surveillance médicale continue. L'ECG, la tension et les symptômes sont enregistrés tout au long de l'effort, augmenté par paliers.
- **Pourquoi / Indications :** dépister une insuffisance coronarienne (rétrécissement des artères du cœur), évaluer la tolérance à l'effort, rechercher un trouble du rythme déclenché par l'effort, ou contrôler l'efficacité d'un traitement.
- **Durée :** environ 30 minutes au total (préparation et récupération comprises). *(Source : inputs cliente.)*
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** l'examen demande un effort physique réel mais n'est pas douloureux ; prévoyez une tenue adaptée. Consignes propres au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Qui le réalise :** un cardiologue de l'équipe Cardio Check-up (Dr Amraoui ou Dr Sofiane). Médecin précis : **[NEEDS CLIENT CONFIRMATION]**.
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a test that assesses how the heart behaves during gradual, controlled physical exertion (on a bike or treadmill), under continuous medical supervision. Your ECG, blood pressure and symptoms are recorded throughout, as the effort is increased in stages.
- **What it is for:** to screen for coronary insufficiency (narrowing of the heart's arteries), assess exercise tolerance, look for an exertion-triggered rhythm disorder, or check whether a treatment is working.
- **Duration:** about 30 minutes in total (including preparation and recovery). *(Source: client inputs.)*
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** the test requires real physical effort but is not painful; wear suitable clothing. Practice-specific instructions: **[NEEDS CLIENT CONFIRMATION]**.
- **Who performs it:** a cardiologist from the Cardio Check-up team (Dr Amraoui or Dr Sofiane). Exact doctor: **[NEEDS CLIENT CONFIRMATION]**.
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.14 — Écho-Doppler des troncs supra-aortiques (carotides) / Carotid & supra-aortic Doppler
`chunk_id: doc03_doppler_tsa` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une échographie Doppler qui étudie les artères carotides et vertébrales (qui irriguent le cerveau) : une sonde est posée sur les côtés du cou pour voir la paroi des artères et mesurer la vitesse du sang. Indolore et sans rayons.
- **Pourquoi / Indications :** dépister des plaques d'athérome, évaluer un rétrécissement (sténose) et participer à l'évaluation du risque cardiovasculaire, notamment le risque d'accident vasculaire cérébral.
- **Durée :** une quinzaine de minutes. *(Source : inputs cliente.)*
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** aucune préparation particulière ; vous êtes allongé(e) sur le dos, la tête légèrement tournée.
- **Qui le réalise :** Dr Hakem Rabiaa (médecin vasculaire).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a Doppler ultrasound that studies the carotid and vertebral arteries (which supply the brain): a probe is placed on the sides of the neck to see the artery walls and measure blood-flow speed. Painless and radiation-free.
- **What it is for:** to detect atheroma plaques, assess a narrowing (stenosis), and help evaluate cardiovascular risk, notably the risk of stroke.
- **Duration:** about fifteen minutes. *(Source: client inputs.)*
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** no special preparation; you lie on your back with the head slightly turned.
- **Who performs it:** Dr Hakem Rabiaa (vascular physician).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.15 — Écho-Doppler des artères des membres inférieurs / Lower-limb arterial Doppler
`chunk_id: doc03_doppler_arteres_mi` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une échographie Doppler qui étudie la circulation dans les artères des jambes, de l'aine jusqu'aux pieds. Indolore et sans rayons.
- **Pourquoi / Indications :** dépister une artériopathie des membres inférieurs (rétrécissement ou obstruction des artères) et en évaluer la sévérité, notamment en cas de douleurs à la marche, de diabète ou de tabagisme.
- **Durée :** généralement 20 à 30 minutes. *(Source : inputs cliente.)*
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** vous êtes allongé(e) sur le dos, les membres inférieurs dénudés pour l'examen.
- **Qui le réalise :** Dr Hakem Rabiaa (médecin vasculaire).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a Doppler ultrasound that studies blood flow in the leg arteries, from the groin to the feet. Painless and radiation-free.
- **What it is for:** to detect peripheral arterial disease of the legs (narrowing or blockage of the arteries) and assess its severity, notably with pain on walking, diabetes or smoking.
- **Duration:** generally 20 to 30 minutes. *(Source: client inputs.)*
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** you lie on your back with the legs uncovered for the examination.
- **Who performs it:** Dr Hakem Rabiaa (vascular physician).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.16 — Écho-Doppler des artères des membres supérieurs / Upper-limb arterial Doppler
`chunk_id: doc03_doppler_arteres_ms` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une échographie Doppler qui étudie la circulation dans les artères des bras, de l'épaule jusqu'à la main. Indolore et sans rayons.
- **Pourquoi / Indications :** dépister une artériopathie des membres supérieurs (rétrécissement ou obstruction) ou d'autres anomalies vasculaires, comme le syndrome du défilé thoracobrachial.
- **Durée :** généralement 15 à 20 minutes. *(Source : inputs cliente.)*
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** vous êtes assis(e) ou allongé(e), les membres supérieurs dénudés pour l'examen.
- **Qui le réalise :** Dr Hakem Rabiaa (médecin vasculaire).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a Doppler ultrasound that studies blood flow in the arm arteries, from the shoulder to the hand. Painless and radiation-free.
- **What it is for:** to detect upper-limb arterial disease (narrowing or blockage) or other vascular abnormalities, such as thoracic outlet syndrome.
- **Duration:** generally 15 to 20 minutes. *(Source: client inputs.)*
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** you sit or lie down with the arms uncovered for the examination.
- **Who performs it:** Dr Hakem Rabiaa (vascular physician).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.17 — Écho-Doppler des artères rénales / Renal artery Doppler
`chunk_id: doc03_doppler_renales` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une échographie Doppler qui étudie la circulation dans les artères qui irriguent les reins. Une sonde est posée sur l'abdomen. Indolore et sans rayons.
- **Pourquoi / Indications :** dépister un rétrécissement (sténose) des artères rénales, cause possible d'une hypertension difficile à équilibrer ou d'une altération de la fonction rénale.
- **Durée :** une quinzaine de minutes environ. *(Source : inputs cliente.)*
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** il est généralement recommandé d'être à jeun et de ne pas avoir fumé avant l'examen, pour limiter les gaz digestifs qui gênent la visualisation.
- **Qui le réalise :** Dr Hakem Rabiaa (médecin vasculaire).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a Doppler ultrasound that studies blood flow in the arteries supplying the kidneys. A probe is placed on the abdomen. Painless and radiation-free.
- **What it is for:** to detect a narrowing (stenosis) of the renal arteries, a possible cause of hard-to-control high blood pressure or of reduced kidney function.
- **Duration:** about fifteen minutes. *(Source: client inputs.)*
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** it is generally recommended to fast and not smoke before the test, to limit digestive gas that hampers imaging.
- **Who performs it:** Dr Hakem Rabiaa (vascular physician).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.18 — Écho-Doppler de l'aorte abdominale / Abdominal aorta Doppler
`chunk_id: doc03_doppler_aorte` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une échographie Doppler qui visualise l'aorte (la plus grosse artère du corps) au niveau de l'abdomen, pour mesurer son diamètre et analyser le flux sanguin. Indolore et sans rayons.
- **Pourquoi / Indications :** dépister principalement un anevrisme de l'aorte abdominale (dilatation anormale de la paroi), recherché surtout après 60 ans, chez les fumeurs ou en cas d'antécédents familiaux.
- **Durée :** une quinzaine de minutes environ. *(Source : inputs cliente.)*
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** il est généralement recommandé d'être à jeun pour limiter les gaz digestifs qui gênent la visualisation.
- **Qui le réalise :** Dr Hakem Rabiaa (médecin vasculaire).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a Doppler ultrasound that images the aorta (the body's largest artery) at the abdomen, to measure its diameter and analyse blood flow. Painless and radiation-free.
- **What it is for:** mainly to detect an abdominal aortic aneurysm (an abnormal bulging of the wall), looked for especially after age 60, in smokers, or with a family history.
- **Duration:** about fifteen minutes. *(Source: client inputs.)*
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** it is generally recommended to fast to limit digestive gas that hampers imaging.
- **Who performs it:** Dr Hakem Rabiaa (vascular physician).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.19 — Écho-Doppler veineux des membres inférieurs / Lower-limb venous Doppler
`chunk_id: doc03_doppler_veineux_mi` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une échographie Doppler qui étudie la circulation dans les veines des jambes, du pli de l'aine jusqu'aux pieds, pour vérifier la perméabilité du réseau veineux et le fonctionnement des valvules. Indolore et sans rayons.
- **Pourquoi / Indications :** dépister une thrombose veineuse (phlébite) ou une insuffisance veineuse avec reflux (varices) ; l'examen participe aussi au bilan d'une hypotension orthostatique (malaises).
- **Durée :** généralement 20 à 30 minutes. *(Source : inputs cliente.)*
- **Ordonnance :** Une ordonnance (prescription médicale) est nécessaire pour cet examen. Acceptation sans ordonnance au cabinet : **[NEEDS CLIENT CONFIRMATION]**.
- **Préparation & contraintes :** vous êtes examiné(e) debout puis allongé(e), selon les besoins de l'exploration.
- **Qui le réalise :** Dr Hakem Rabiaa (médecin vasculaire).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a Doppler ultrasound that studies blood flow in the leg veins, from the groin to the feet, to check that the venous network is open and the valves work. Painless and radiation-free.
- **What it is for:** to detect a venous thrombosis (phlebitis) or venous insufficiency with reflux (varicose veins); the test also contributes to the assessment of orthostatic hypotension (faintness).
- **Duration:** generally 20 to 30 minutes. *(Source: client inputs.)*
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** you are examined standing and then lying down, as needed for the assessment.
- **Who performs it:** Dr Hakem Rabiaa (vascular physician).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.20 — Consultation de rythmologie / Rhythm (electrophysiology) consultation
`chunk_id: doc03_consult_rythmologie` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une consultation spécialisée dans le diagnostic et la prise en charge des troubles du rythme et de la conduction du cœur (palpitations, fibrillation atriale, extrasystoles). Elle comprend un interrogatoire, un examen clinique et l'analyse des examens déjà réalisés (ECG, Holter).
- **Pourquoi / Indications :** établir un diagnostic précis, évaluer le retentissement et le risque (notamment le risque de caillot en cas de fibrillation atriale), proposer un traitement (médicaments, ablation, dispositif implantable) et assurer le suivi des porteurs de pacemaker ou de défibrillateur.
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation.
- **Qui la réalise :** Dr Sana Amraoui (cardiologue-rythmologue).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a consultation specialised in diagnosing and managing heart-rhythm and conduction disorders (palpitations, atrial fibrillation, extra beats). It includes an interview, a clinical examination and review of tests already done (ECG, Holter).
- **What it is for:** to make a precise diagnosis, assess the impact and the risk (notably the clot risk in atrial fibrillation), propose treatment (medication, ablation, an implantable device) and follow up patients with a pacemaker or defibrillator.
- **Prescription:** an ordonnance is not required to book a consultation.
- **Who performs it:** Dr Sana Amraoui (cardiologist-electrophysiologist).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.21 — Consultation bilan de douleur thoracique / Chest-pain assessment consultation
`chunk_id: doc03_consult_douleur_thoracique` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une consultation pour explorer une douleur du thorax, en déterminer la cause et écarter une origine cardiaque grave. Elle comprend un interrogatoire détaillé (type, durée, circonstances) et un examen clinique.
- **Pourquoi / Indications :** douleur ou oppression thoracique non urgente. Selon le contexte, elle peut s'accompagner d'un ECG, d'une échographie cardiaque, d'une épreuve d'effort ou d'un scanner des coronaires (coroscanner).
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation.
- **Qui la réalise :** un cardiologue de l'équipe (Dr Amraoui ou Dr Sofiane).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> **Attention :** une douleur thoracique intense MAINTENANT, prolongée ou au repos, est une urgence — appelez le 15 (SAMU), ne prenez pas rendez-vous.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a consultation to investigate chest pain, find its cause and rule out a serious cardiac origin. It includes a detailed interview (type, duration, circumstances) and a clinical examination.
- **What it is for:** non-urgent chest pain or tightness. Depending on the context, it may include an ECG, cardiac ultrasound, exercise test or a coronary CT scan.
- **Prescription:** an ordonnance is not required to book a consultation.
- **Who performs it:** a cardiologist from the team (Dr Amraoui or Dr Sofiane).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> **Important:** severe chest pain NOW, prolonged or at rest, is an emergency — call 15 (SAMU), do not book an appointment.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.22 — Consultation bilan d'essoufflement (dyspnée) / Breathlessness (dyspnoea) assessment
`chunk_id: doc03_consult_dyspnee` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une consultation pour explorer un essoufflement (à l'effort ou au repos), en déterminer la cause et écarter une origine cardiaque. Elle comprend un interrogatoire détaillé et un examen clinique.
- **Pourquoi / Indications :** gêne respiratoire non urgente. Selon le contexte, elle peut s'accompagner d'un ECG, d'une échographie cardiaque, d'une épreuve d'effort ou d'un bilan biologique, pour rechercher une insuffisance cardiaque, une atteinte de valve ou un trouble du rythme.
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation.
- **Qui la réalise :** un cardiologue de l'équipe (Dr Amraoui ou Dr Sofiane).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a consultation to investigate breathlessness (on exertion or at rest), find its cause and rule out a cardiac origin. It includes a detailed interview and a clinical examination.
- **What it is for:** non-urgent shortness of breath. Depending on the context, it may include an ECG, cardiac ultrasound, exercise test or blood tests, to look for heart failure, a valve problem or a rhythm disorder.
- **Prescription:** an ordonnance is not required to book a consultation.
- **Who performs it:** a cardiologist from the team (Dr Amraoui or Dr Sofiane).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.23 — Consultation bilan de valvulopathie / Valve-disease assessment
`chunk_id: doc03_consult_valvulopathie` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une consultation pour évaluer le fonctionnement des valves du cœur (mitrale, aortique, tricuspide, pulmonaire) en cas d'anomalie connue ou suspectée (rétrécissement ou fuite). Elle comprend un interrogatoire, la recherche de symptômes (essoufflement, fatigue, palpitations) et un examen clinique avec auscultation.
- **Pourquoi / Indications :** elle s'accompagne généralement d'une échographie cardiaque pour préciser le type et la sévérité de l'atteinte, surveiller son évolution et déterminer le bon moment d'une éventuelle intervention, en lien avec la chirurgie si besoin.
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation.
- **Qui la réalise :** un cardiologue de l'équipe (Dr Amraoui ou Dr Sofiane) ; en cas d'indication chirurgicale, orientation vers le Pr Doguet.
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a consultation to assess how the heart valves work (mitral, aortic, tricuspid, pulmonary) when a problem is known or suspected (narrowing or leak). It includes an interview, a check for symptoms (breathlessness, tiredness, palpitations) and a clinical examination with listening to the heart.
- **What it is for:** it usually includes a cardiac ultrasound to define the type and severity, monitor it over time, and decide the right moment for any intervention, in coordination with surgery if needed.
- **Prescription:** an ordonnance is not required to book a consultation.
- **Who performs it:** a cardiologist from the team (Dr Amraoui or Dr Sofiane); if surgery is indicated, referral to Pr Doguet.
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.24 — Consultation suivi d'insuffisance cardiaque / Heart-failure follow-up consultation
`chunk_id: doc03_consult_insuffisance_cardiaque` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une consultation pour évaluer et suivre le cœur lorsqu'il n'assure plus correctement sa fonction de pompe. Elle comprend un interrogatoire sur les symptômes (essoufflement, fatigue, prise de poids, gonflement des jambes) et un examen clinique.
- **Pourquoi / Indications :** elle s'accompagne généralement d'une échographie cardiaque, d'un bilan biologique et d'un ECG pour évaluer la fonction du cœur, ajuster le traitement, surveiller l'évolution et dépister tôt une aggravation.
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation.
- **Qui la réalise :** un cardiologue de l'équipe (Dr Amraoui ou Dr Sofiane).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a consultation to assess and follow the heart when it no longer pumps effectively. It includes an interview about symptoms (breathlessness, tiredness, weight gain, leg swelling) and a clinical examination.
- **What it is for:** it usually includes a cardiac ultrasound, blood tests and an ECG to assess heart function, adjust treatment, monitor progression and detect worsening early.
- **Prescription:** an ordonnance is not required to book a consultation.
- **Who performs it:** a cardiologist from the team (Dr Amraoui or Dr Sofiane).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.25 — Consultation de chirurgie cardiaque / Cardiac surgery consultation
`chunk_id: doc03_consult_chirurgie_cardiaque` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une consultation pour évaluer l'indication et la faisabilité d'une intervention chirurgicale sur le cœur (chirurgie de valve, pontage coronaire, chirurgie de l'aorte). Elle comprend un interrogatoire, un examen clinique et l'analyse approfondie des examens déjà réalisés.
- **Pourquoi / Indications :** discuter des options, du déroulement, des bénéfices et des risques de l'intervention. Elle fait généralement suite à un bilan cardiologique et s'inscrit dans une prise en charge pluridisciplinaire.
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation ; l'orientation se fait le plus souvent après un avis cardiologique.
- **Qui la réalise :** Pr Fabien Doguet (chirurgien cardiaque).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a consultation to assess the indication and feasibility of heart surgery (valve surgery, coronary bypass, aortic surgery). It includes an interview, a clinical examination and a thorough review of tests already done.
- **What it is for:** to discuss the options, the procedure, and its benefits and risks. It usually follows a cardiology assessment and is part of multidisciplinary care.
- **Prescription:** an ordonnance is not required to book a consultation; referral usually follows a cardiology opinion.
- **Who performs it:** Pr Fabien Doguet (cardiac surgeon).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.26 — Consultation de chirurgie vasculaire / Vascular surgery consultation
`chunk_id: doc03_consult_chirurgie_vasculaire` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une consultation pour évaluer la prise en charge des maladies des artères et des veines (anévrisme, artériopathie, sténose, insuffisance veineuse, varices). Elle comprend un interrogatoire, un examen clinique et l'analyse des examens (écho-Doppler, scanner).
- **Pourquoi / Indications :** de nombreuses pathologies se traitent aujourd'hui par techniques mini-invasives (traitement endoveineux des varices, prothèses endovasculaires) ; une chirurgie conventionnelle reste possible dans les cas complexes. La consultation permet de choisir la stratégie la plus adaptée.
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation ; l'orientation fait souvent suite à une évaluation vasculaire.
- **Qui la réalise :** Dr Adam Taha (chirurgien vasculaire et endovasculaire).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a consultation to assess the management of artery and vein disease (aneurysm, arterial disease, stenosis, venous insufficiency, varicose veins). It includes an interview, a clinical examination and review of tests (Doppler ultrasound, CT scan).
- **What it is for:** many conditions are now treated with minimally invasive techniques (endovenous treatment of varicose veins, endovascular stent-grafts); conventional surgery remains possible in complex cases. The consultation helps choose the best strategy.
- **Prescription:** an ordonnance is not required to book a consultation; referral often follows a vascular assessment.
- **Who performs it:** Dr Adam Taha (vascular and endovascular surgeon).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.27 — Bilan nutritionnel / Nutritional assessment
`chunk_id: doc03_bilan_nutritionnel` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une consultation qui évalue les habitudes alimentaires et l'état nutritionnel, dans une démarche de prévention ou de prise en charge des pathologies liées au mode de vie (surpoids, obésité, diabète, cholestérol). Elle comprend un interrogatoire alimentaire, le calcul de l'IMC et la mesure du tour de taille.
- **Pourquoi / Indications :** proposer un rééquilibrage alimentaire personnalisé et, si une perte de poids est nécessaire, un accompagnement adapté, en complément du suivi cardiologique. Participe au contrôle des facteurs de risque cardiovasculaires.
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation.
- **Qui le réalise :** Dr Leslie Berdah Sadaoui (médecin généraliste, nutrition).
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a consultation that assesses eating habits and nutritional status, for prevention or management of lifestyle-related conditions (overweight, obesity, diabetes, cholesterol). It includes a dietary interview, BMI calculation and waist measurement.
- **What it is for:** to propose a personalised dietary rebalancing and, if weight loss is needed, tailored support, alongside cardiology follow-up. Helps control cardiovascular risk factors.
- **Prescription:** an ordonnance is not required to book a consultation.
- **Who performs it:** Dr Leslie Berdah Sadaoui (general practitioner, nutrition).
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

## 3.28 — Vitaminothérapie / Vitamin therapy
`chunk_id: doc03_vitaminotherapie` · `lang: fr,en`

**FR —**
- **Qu'est-ce que c'est ?** Une supplémentation en vitamines et oligo-éléments (par ex. vitamine D, vitamine B12, fer, magnésium), prescrite après la mise en évidence d'une carence avérée par un bilan biologique.
- **Pourquoi / Indications :** certaines carences peuvent être associées à une fatigue importante, des troubles du rythme ou un retentissement sur l'état général. La supplémentation est adaptée au type et à l'importance de la carence, avec un contrôle biologique de suivi.
- **Point important :** la vitaminothérapie n'est proposée qu'en cas de carence confirmée par une prise de sang, jamais « à l'aveugle ».
- **Ordonnance :** une ordonnance n'est pas nécessaire pour prendre une consultation.
- **Qui le réalise :** un médecin de l'équipe Cardio Check-up. Médecin précis : **[NEEDS CLIENT CONFIRMATION]**.
- **Rendez-vous :** par téléphone au 07 55 50 52 58 (9h–18h) ou par e-mail à secretariatdramraoui@myeva.ovh.
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** supplementation with vitamins and trace elements (e.g. vitamin D, vitamin B12, iron, magnesium), prescribed after a genuine deficiency is shown by a blood test.
- **What it is for:** some deficiencies can be linked to marked tiredness, rhythm disturbances or an effect on general health. Supplementation is matched to the type and degree of the deficiency, with a follow-up blood test.
- **Important point:** vitamin therapy is offered only when a deficiency is confirmed by a blood test, never "blindly."
- **Prescription:** an ordonnance is not required to book a consultation.
- **Who performs it:** a doctor from the Cardio Check-up team. Exact doctor: **[NEEDS CLIENT CONFIRMATION]**.
- **Booking:** by phone at 07 55 50 52 58 (9 am–6 pm) or by e-mail at secretariatdramraoui@myeva.ovh.
> Life-threatening emergency: call 15 (SAMU) — do not use online booking.

---

### Open flags in DOC_03 (for the Architect)
- **Duration:** every service except Holter (3.4) and MAPA (3.5).
- **Ordonnance — booking policy** (accept without prescription): 3.3, 3.4, 3.5, 3.6, 3.7, 3.8.
- **Preparation/constraints:** 3.2, 3.3, 3.6, 3.7 (all details), 3.8, 3.9, 3.10, 3.11, 3.12.
- **Performer:** 3.2 consultation (which doctor) · 3.7 polygraphie.
- **Procedure logistics** (where performed, practical arrangements): 3.9, 3.10, 3.11, 3.12.
- **Polygraphie** (3.7): duration, preparation, performer — source sheet is image-based.

### Deviation note for D3
Exact required-prescription wording applied verbatim to the diagnostic exams: 3.3, 3.4, 3.5, 3.6, 3.7, 3.8. NOT applied to 3.2 (consultation — no ordonnance needed to see a doctor) or 3.9–3.12 (procedures decided by medical indication, not booked by prescription); those use a tailored, flagged treatment instead, to avoid stating a false fact. Awaiting your confirmation or override.

### Update note (2026-06-30, from client Notion inputs)
New chunks added and their sources/performers:
- **Exams (3.13–3.19):** épreuve d'effort + six vascular Doppler exams (supra-aortic/carotids, lower-limb arteries, upper-limb arteries, renal arteries, abdominal aorta, lower-limb veins). Durations and prep notes (fasting for renal/aorta) are taken from the client's own exam descriptions. **All six Dopplers are performed by Dr Hakem Rabiaa** (confirmed by the client's practitioner distribution). Épreuve d'effort performer = a team cardiologist (exact one flagged).
- **Consultations (3.20–3.27):** rythmologie (Dr Amraoui); chest-pain, dyspnoea, valve, heart-failure assessments (a team cardiologist — Amraoui or Sofiane); cardiac surgery (Pr Doguet, after cardiology assessment); vascular surgery (Dr Taha); nutritional assessment (Dr Berdah Sadaoui).
- **3.28 Vitaminothérapie:** included with the client's guardrail — only on a blood-test-confirmed deficiency, never blind. Prescribing doctor flagged.
- **Booking line** in new chunks shows the phone (07 55 50 52 58) and e-mail as the booking channels for this version, per Architect instruction. Polygraphie (3.7) performer is now Dr Amraoui per the client distribution — see the DOC_04 update note.
- Remaining open flags for new chunks: durations for consultations; ordonnance-without-prescription policy; exact performer for épreuve d'effort (3.13) and vitaminothérapie (3.28).
