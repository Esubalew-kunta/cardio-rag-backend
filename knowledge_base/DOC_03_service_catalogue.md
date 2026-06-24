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
- **Préparation & contraintes :** modalités de l'examen (à domicile ou au cabinet, pose des capteurs, déroulement) : **[NEEDS CLIENT CONFIRMATION]** *(la fiche d'information source est sous forme d'image, non lisible).*
- **Qui le réalise :** **[NEEDS CLIENT CONFIRMATION]**.
- **Retour du matériel & pénalités :** le boîtier de polygraphie (PGV) vous est confié et doit être restitué à la date indiquée ; **100 € par jour de retard** ; **500 € si l'appareil est restitué en mauvais état**. *(Source confirmée.)*
- **Rendez-vous :** Doctolib · 07 55 50 52 58 (9h–18h).
> Urgence vitale : appelez le 15 (SAMU) — ne pas utiliser la réservation en ligne.

**EN —**
- **What it is:** a test that records, over one night, several aspects of your sleep (breathing, blood oxygen, heart rhythm, snoring) to screen for sleep apnoea — breathing pauses that affect the heart.
- **What it is for:** heavy snoring, daytime sleepiness, breathing pauses noticed during sleep, fatigue, in connection with high blood pressure or rhythm disorders.
- **Duration:** **[NEEDS CLIENT CONFIRMATION]**.
- **Prescription:** A medical prescription (ordonnance) is required for this examination. Whether the practice accepts patients without a prescription: **[NEEDS CLIENT CONFIRMATION]**.
- **Preparation & constraints:** how the test is done (at home or at the practice, fitting the sensors, what happens): **[NEEDS CLIENT CONFIRMATION]** *(the source information sheet is image-based and not machine-readable).*
- **Who performs it:** **[NEEDS CLIENT CONFIRMATION]**.
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

### Open flags in DOC_03 (for the Architect)
- **Duration:** every service except Holter (3.4) and MAPA (3.5).
- **Ordonnance — booking policy** (accept without prescription): 3.3, 3.4, 3.5, 3.6, 3.7, 3.8.
- **Preparation/constraints:** 3.2, 3.3, 3.6, 3.7 (all details), 3.8, 3.9, 3.10, 3.11, 3.12.
- **Performer:** 3.2 consultation (which doctor) · 3.7 polygraphie.
- **Procedure logistics** (where performed, practical arrangements): 3.9, 3.10, 3.11, 3.12.
- **Polygraphie** (3.7): duration, preparation, performer — source sheet is image-based.

### Deviation note for D3
Exact required-prescription wording applied verbatim to the diagnostic exams: 3.3, 3.4, 3.5, 3.6, 3.7, 3.8. NOT applied to 3.2 (consultation — no ordonnance needed to see a doctor) or 3.9–3.12 (procedures decided by medical indication, not booked by prescription); those use a tailored, flagged treatment instead, to avoid stating a false fact. Awaiting your confirmation or override.
