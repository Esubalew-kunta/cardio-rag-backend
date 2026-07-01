# DOC_10 — Patient Question Bank (bilingual) / Banque de questions patients
Cardio Check-up · Dr Sana Amraoui
RAG knowledge base — each `##` section is one self-contained Qdrant chunk.
PURPOSE: boost retrieval with the SAME embedding model by putting real patient phrasings into the knowledge base. Each topic has a French chunk and an English chunk (kept short so the model embeds them fully). Each chunk LEADS with the words a patient actually types, then gives a short, safe answer: what it is, which doctor/exam, booking by phone, a non-diagnostic close, and an emergency note where relevant. Booking channel for this version = phone 07 55 50 52 58 (9h-18h) and e-mail. Cross-references: exams → DOC_03 · routing → DOC_04 · pathologies → DOC_08 · risk factors → DOC_09.

---

## 10.1 (FR) Douleur thoracique
`chunk_id: doc10_chest_fr` · `lang: fr`

Questions de patients : j'ai mal a la poitrine, j'ai une douleur dans le thorax, ca serre dans ma poitrine, j'ai une oppression thoracique, une gene au coeur a l'effort, une douleur qui va vers le bras ou la machoire, mal au sternum.
Reponse : une douleur thoracique non urgente merite une consultation de cardiologie (Dr Amraoui ou Dr Sofiane), parfois avec un ECG, une echographie du coeur ou une epreuve d'effort. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (du lundi au vendredi, de 9h a 18h) ou ecrivez a secretariatdramraoui@myeva.ovh. Le medecin evaluera votre situation lors de la consultation.
Attention : une douleur intense maintenant, au repos, avec sueurs ou essoufflement, est une urgence, appelez le 15 (SAMU) immediatement, ne prenez pas rendez-vous.

---

## 10.1 (EN) Chest pain
`chunk_id: doc10_chest_en` · `lang: en`

Patient questions: I have chest pain, my chest hurts, I feel tightness in my chest, pressure on my chest, discomfort in my heart on exertion, pain spreading to my arm or jaw, pain in my breastbone.
Answer: non-urgent chest pain should be seen in a cardiology consultation (Dr Amraoui or Dr Sofiane), sometimes with an ECG, a heart ultrasound or an exercise stress test. To book, call 07 55 50 52 58 (Monday to Friday, 9h to 18h) or e-mail secretariatdramraoui@myeva.ovh. The doctor will assess your situation during the consultation.
Warning: severe pain now, at rest, with sweating or breathlessness, is an emergency, call 15 (SAMU) immediately, do not book an appointment.

---

## 10.2 (FR) Palpitations et coeur irregulier
`chunk_id: doc10_palpitations_fr` · `lang: fr`

Questions de patients : j'ai des palpitations, mon coeur bat vite, mon coeur bat de facon irreguliere, j'ai des a-coups dans la poitrine, mon coeur s'emballe, je sens des ratés, mon coeur saute des battements, tachycardie.
Reponse : les palpitations et un coeur irregulier relevent d'une consultation de rythmologie avec le Dr Amraoui, souvent avec un Holter cardiaque (enregistrement du rythme sur 24h ou plus). Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.
Attention : des palpitations avec douleur thoracique, malaise ou essoufflement severe, appelez le 15 (SAMU).

---

## 10.2 (EN) Palpitations and irregular heartbeat
`chunk_id: doc10_palpitations_en` · `lang: en`

Patient questions: I have palpitations, my heart is racing, my heartbeat is irregular, I feel fluttering in my chest, my heart skips beats, pounding heart, my heart runs fast, tachycardia.
Answer: palpitations and an irregular heartbeat are handled in a rhythm (electrophysiology) consultation with Dr Amraoui, often with a cardiac Holter (recording your rhythm over 24h or more). To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.
Warning: palpitations with chest pain, faintness or severe breathlessness, call 15 (SAMU).

---

## 10.3 (FR) Essoufflement
`chunk_id: doc10_breathless_fr` · `lang: fr`

Questions de patients : je suis essouffle, j'ai du mal a respirer a l'effort, je manque d'air quand je monte les escaliers, je suis vite fatigue en marchant, je me reveille la nuit en manque d'air, je dois dormir assis.
Reponse : un essoufflement non urgent merite une consultation de cardiologie (Dr Amraoui ou Dr Sofiane), parfois avec un ECG, une echographie du coeur ou une epreuve d'effort, pour rechercher une cause cardiaque. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.
Attention : un essoufflement soudain et severe maintenant, appelez le 15 (SAMU).

---

## 10.3 (EN) Breathlessness
`chunk_id: doc10_breathless_en` · `lang: en`

Patient questions: I am short of breath, I struggle to breathe on exertion, I get breathless climbing stairs, I tire quickly when walking, I wake up at night gasping for air, I have to sleep sitting up.
Answer: non-urgent breathlessness should be seen in a cardiology consultation (Dr Amraoui or Dr Sofiane), sometimes with an ECG, a heart ultrasound or an exercise test, to look for a cardiac cause. To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.
Warning: sudden, severe breathlessness now, call 15 (SAMU).

---

## 10.4 (FR) Ronflements et apnee du sommeil
`chunk_id: doc10_sleep_fr` · `lang: fr`

Questions de patients : je ronfle beaucoup, je suis tres fatigue dans la journee, je somnole tout le temps, on m'a dit que je fais des pauses respiratoires la nuit, je me reveille avec mal a la tete, est-ce que j'ai de l'apnee du sommeil, mon sommeil n'est pas reparateur.
Reponse : ces signes peuvent evoquer un syndrome d'apnee du sommeil, frequemment lie au coeur et a la tension. Nous proposons une polygraphie ventilatoire nocturne, realisee par le Dr Amraoui, pour depister les apnees. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.

---

## 10.4 (EN) Snoring and sleep apnoea
`chunk_id: doc10_sleep_en` · `lang: en`

Patient questions: I snore a lot, I am very tired during the day, I feel sleepy all the time, I have been told I stop breathing at night, I wake up with headaches, do I have sleep apnoea, my sleep is not refreshing.
Answer: these signs can point to sleep apnoea syndrome, which is often linked to the heart and blood pressure. We offer a nocturnal ventilatory polygraphy, performed by Dr Amraoui, to screen for apnoeas. To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.

---

## 10.5 (FR) Douleurs aux jambes a la marche
`chunk_id: doc10_leg_pain_fr` · `lang: fr`

Questions de patients : j'ai mal aux jambes quand je marche, la douleur s'arrete quand je m'arrete, j'ai des crampes dans les mollets en marchant, mes jambes me font mal a l'effort, je ne peux marcher que quelques metres.
Reponse : une douleur des jambes a la marche qui cede au repos peut evoquer une atteinte des arteres des jambes. Le Dr Hakem realise une echographie Doppler des arteres des membres inferieurs pour l'explorer. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.
Attention : une jambe brutalement froide, pale et tres douloureuse, appelez le 15 (SAMU).

---

## 10.5 (EN) Leg pain when walking
`chunk_id: doc10_leg_pain_en` · `lang: en`

Patient questions: my legs hurt when I walk, the pain stops when I stop, I get calf cramps while walking, my legs ache on exertion, I can only walk a few metres.
Answer: leg pain on walking that eases with rest can point to a problem with the leg arteries. Dr Hakem performs a lower-limb arterial Doppler ultrasound to investigate it. To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.
Warning: a suddenly cold, pale, very painful leg, call 15 (SAMU).

---

## 10.6 (FR) Jambes gonflees et lourdes, varices
`chunk_id: doc10_legs_swelling_fr` · `lang: fr`

Questions de patients : mes jambes gonflent, j'ai les chevilles gonflees, j'ai les jambes lourdes le soir, j'ai des varices, j'ai des veines apparentes, j'ai les jambes qui tirent.
Reponse : des jambes lourdes, gonflees ou des varices relevent d'un bilan veineux. Le Dr Hakem realise une echographie Doppler veineuse des membres inferieurs ; si une chirurgie est envisagee, le Dr Taha (chirurgien vasculaire) prend le relais. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.
Attention : une jambe soudain gonflee et douloureuse avec essoufflement, appelez le 15 (SAMU).

---

## 10.6 (EN) Swollen heavy legs and varicose veins
`chunk_id: doc10_legs_swelling_en` · `lang: en`

Patient questions: my legs swell, my ankles are swollen, my legs feel heavy in the evening, I have varicose veins, I have visible veins, my legs feel tight.
Answer: heavy, swollen legs or varicose veins call for a venous assessment. Dr Hakem performs a lower-limb venous Doppler ultrasound; if surgery is considered, Dr Taha (vascular surgeon) takes over. To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.
Warning: a suddenly swollen, painful leg with breathlessness, call 15 (SAMU).

---

## 10.7 (FR) Malaise et perte de connaissance
`chunk_id: doc10_syncope_fr` · `lang: fr`

Questions de patients : j'ai fait un malaise, je me suis evanoui, j'ai perdu connaissance, j'ai eu un voile noir, je me sens partir, j'ai failli tomber dans les pommes.
Reponse : un malaise avec perte de connaissance (aujourd'hui stable) merite une consultation de rythmologie avec le Dr Amraoui, souvent avec un Holter cardiaque, parfois un Holter implantable. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.
Attention : une perte de connaissance en cours ou un malaise avec douleur thoracique, appelez le 15 (SAMU).

---

## 10.7 (EN) Fainting and loss of consciousness
`chunk_id: doc10_syncope_en` · `lang: en`

Patient questions: I fainted, I passed out, I lost consciousness, I had a blackout, I feel like I am going to faint, I nearly collapsed.
Answer: fainting with loss of consciousness (stable today) should be seen in a rhythm consultation with Dr Amraoui, often with a cardiac Holter and sometimes an implantable Holter. To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.
Warning: an ongoing loss of consciousness, or fainting with chest pain, call 15 (SAMU).

---

## 10.8 (FR) Tension arterielle elevee
`chunk_id: doc10_hypertension_fr` · `lang: fr`

Questions de patients : j'ai de la tension, ma tension est trop haute, je fais de l'hypertension, ma tension monte, je dois surveiller ma tension, mon medecin dit que j'ai trop de tension.
Reponse : pour confirmer et suivre une hypertension, le Dr Amraoui propose un holter tensionnel (MAPA) qui mesure la tension sur 24 heures. La prise en charge associe hygiene de vie et, si besoin, traitement. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.
Attention : une tension tres elevee avec un mal de tete brutal, appelez le 15 (SAMU).

---

## 10.8 (EN) High blood pressure
`chunk_id: doc10_hypertension_en` · `lang: en`

Patient questions: I have high blood pressure, my blood pressure is too high, I am hypertensive, my blood pressure keeps rising, I need to monitor my blood pressure, my doctor says my pressure is too high.
Answer: to confirm and follow high blood pressure, Dr Amraoui offers a blood-pressure Holter (MAPA) that measures your pressure over 24 hours. Management combines lifestyle and, if needed, treatment. To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.
Warning: very high blood pressure with a sudden severe headache, call 15 (SAMU).

---

## 10.9 (FR) Cholesterol, diabete et facteurs de risque
`chunk_id: doc10_risk_fr` · `lang: fr`

Questions de patients : j'ai du cholesterol, j'ai trop de cholesterol, j'ai du diabete, je fume et je veux arreter, je suis en surpoids, j'ai des antecedents familiaux de coeur, comment reduire mon risque cardiaque.
Reponse : ces facteurs de risque se prennent en charge en prevention, avec le Dr Berdah Sadaoui (mode de vie, nutrition) ou un cardiologue (Dr Amraoui ou Dr Sofiane) pour un bilan cardiovasculaire. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.

---

## 10.9 (EN) Cholesterol, diabetes and risk factors
`chunk_id: doc10_risk_en` · `lang: en`

Patient questions: I have high cholesterol, my cholesterol is too high, I have diabetes, I smoke and want to quit, I am overweight, I have a family history of heart disease, how do I lower my heart risk.
Answer: these risk factors are managed in prevention, with Dr Berdah Sadaoui (lifestyle, nutrition) or a cardiologist (Dr Amraoui or Dr Sofiane) for a cardiovascular check-up. To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.

---

## 10.10 (FR) Fibrillation atriale
`chunk_id: doc10_afib_fr` · `lang: fr`

Questions de patients : c'est quoi la fibrillation atriale, on m'a trouve une fibrillation atriale, j'ai de l'arythmie, ma montre a detecte un rythme irregulier, je dois suivre ma fibrillation, faut-il une ablation.
Reponse : la fibrillation atriale est le trouble du rythme le plus frequent ; elle se prend en charge en rythmologie avec le Dr Amraoui, qui evalue le risque et propose le traitement adapte, y compris l'ablation quand elle est indiquee. Toute alerte de montre connectee doit etre confirmee par un medecin. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.

---

## 10.10 (EN) Atrial fibrillation
`chunk_id: doc10_afib_en` · `lang: en`

Patient questions: what is atrial fibrillation, I was found to have atrial fibrillation, I have an arrhythmia, my watch detected an irregular rhythm, I need follow-up for my atrial fibrillation, do I need an ablation.
Answer: atrial fibrillation is the most common rhythm disorder; it is managed in rhythmology with Dr Amraoui, who assesses the risk and proposes the right treatment, including ablation when indicated. Any smartwatch alert should be confirmed by a doctor. To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.

---

## 10.11 (FR) Electrocardiogramme (ECG)
`chunk_id: doc10_ecg_fr` · `lang: fr`

Questions de patients : c'est quoi un ECG, on m'a prescrit un electrocardiogramme, je dois faire un ECG, comment se passe un electrocardiogramme, est-ce que l'ECG fait mal.
Reponse : l'ECG est un examen rapide et indolore qui enregistre l'activite electrique du coeur avec des electrodes sur la peau. Il est realise au cabinet par un cardiologue. Une ordonnance est necessaire pour cet examen. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h).

---

## 10.11 (EN) Electrocardiogram (ECG)
`chunk_id: doc10_ecg_en` · `lang: en`

Patient questions: what is an ECG, I was prescribed an electrocardiogram, I need an ECG, how is an electrocardiogram done, does an ECG hurt.
Answer: an ECG is a quick, painless test that records the heart's electrical activity using electrodes on the skin. It is done at the practice by a cardiologist. A prescription is required for this test. To book, call 07 55 50 52 58 (9h to 18h).

---

## 10.12 (FR) Holter cardiaque (enregistrement du rythme)
`chunk_id: doc10_holter_fr` · `lang: fr`

Questions de patients : c'est quoi un holter, on m'a prescrit un holter cardiaque, je dois porter un holter, comment se passe un holter ECG, combien de temps garder l'appareil.
Reponse : le Holter cardiaque enregistre le rythme du coeur en continu, de 24 heures a plusieurs jours, pour reperer un trouble du rythme. La pose dure environ 10 minutes ; pas de douche pendant le port. Il faut restituer l'appareil a la date prevue (penalites en cas de retard ou de dommage). Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h).

---

## 10.12 (EN) Cardiac Holter (rhythm recording)
`chunk_id: doc10_holter_en` · `lang: en`

Patient questions: what is a Holter, I was prescribed a cardiac Holter, I have to wear a Holter, how does a Holter ECG work, how long do I keep the device.
Answer: the cardiac Holter records your heart rhythm continuously, from 24 hours to several days, to catch a rhythm disorder. Fitting takes about 10 minutes; no showering while wearing it. The device must be returned on the set date (penalties apply for lateness or damage). To book, call 07 55 50 52 58 (9h to 18h).

---

## 10.13 (FR) Holter tensionnel (MAPA)
`chunk_id: doc10_mapa_fr` · `lang: fr`

Questions de patients : c'est quoi une MAPA, on m'a prescrit un holter tensionnel, je dois mesurer ma tension sur 24h, comment se passe le holter de tension, l'appareil de tension sur 24 heures.
Reponse : la MAPA mesure automatiquement la tension pendant 24 heures avec un brassard, dans vos conditions de vie habituelles. La pose dure environ 10 minutes ; brassard au bras non dominant, pas de douche. Il faut restituer l'appareil a la date prevue. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h).

---

## 10.13 (EN) Blood-pressure Holter (MAPA / ABPM)
`chunk_id: doc10_mapa_en` · `lang: en`

Patient questions: what is a MAPA, I was prescribed a blood-pressure Holter, I need to measure my blood pressure over 24h, how does the ABPM work, the 24-hour blood pressure device.
Answer: the MAPA automatically measures your blood pressure over 24 hours with a cuff, during your normal daily life. Fitting takes about 10 minutes; cuff on the non-dominant arm, no showering. The device must be returned on the set date. To book, call 07 55 50 52 58 (9h to 18h).

---

## 10.14 (FR) Echographie du coeur (echographie cardiaque)
`chunk_id: doc10_echo_fr` · `lang: fr`

Questions de patients : c'est quoi une echographie du coeur, on m'a prescrit une echocardiographie, je dois faire une echo cardiaque, une echographie cardiaque fait-elle mal, on m'a entendu un souffle au coeur.
Reponse : l'echographie cardiaque (ETT) regarde le coeur en mouvement avec une sonde sur la poitrine, sans rayons et sans douleur. Elle montre les cavites, la contraction et les valves. Elle est realisee au cabinet par un cardiologue. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h).

---

## 10.14 (EN) Heart ultrasound (echocardiogram)
`chunk_id: doc10_echo_en` · `lang: en`

Patient questions: what is a heart ultrasound, I was prescribed an echocardiogram, I need a cardiac echo, does a heart ultrasound hurt, a heart murmur was heard.
Answer: the heart ultrasound (echocardiogram) looks at the beating heart with a probe on the chest, with no radiation and no pain. It shows the chambers, the contraction and the valves. It is done at the practice by a cardiologist. To book, call 07 55 50 52 58 (9h to 18h).

---

## 10.15 (FR) Epreuve d'effort
`chunk_id: doc10_stress_fr` · `lang: fr`

Questions de patients : c'est quoi une epreuve d'effort, on m'a prescrit un test d'effort, je dois faire un effort sous surveillance, l'epreuve d'effort sur velo ou tapis, test cardiaque a l'effort.
Reponse : l'epreuve d'effort evalue le coeur pendant un effort progressif sur velo ou tapis, sous surveillance, pour depister une atteinte des arteres du coeur ou un trouble du rythme a l'effort. Elle dure environ 30 minutes et est realisee par un cardiologue. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h).

---

## 10.15 (EN) Exercise stress test
`chunk_id: doc10_stress_en` · `lang: en`

Patient questions: what is a stress test, I was prescribed an exercise test, I need a supervised exercise test, stress test on a bike or treadmill, cardiac test on exertion.
Answer: the exercise stress test assesses the heart during gradual effort on a bike or treadmill, under supervision, to screen for a heart-artery problem or an exertion-triggered rhythm disorder. It takes about 30 minutes and is done by a cardiologist. To book, call 07 55 50 52 58 (9h to 18h).

---

## 10.16 (FR) Echographie Doppler (arteres et veines)
`chunk_id: doc10_doppler_fr` · `lang: fr`

Questions de patients : c'est quoi un doppler, on m'a prescrit un echo doppler, doppler des carotides pour le risque d'AVC, doppler des jambes, doppler de l'aorte, doppler des arteres renales, examen des vaisseaux.
Reponse : les echographies Doppler vasculaires sont realisees par le Dr Hakem : carotides (risque d'AVC), arteres et veines des jambes, aorte abdominale, arteres renales, arteres des bras. Ce sont des examens indolores, sur ordonnance. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h).

---

## 10.16 (EN) Doppler ultrasound (arteries and veins)
`chunk_id: doc10_doppler_en` · `lang: en`

Patient questions: what is a Doppler, I was prescribed a Doppler ultrasound, carotid Doppler for stroke risk, leg Doppler, aorta Doppler, renal artery Doppler, blood-vessel scan.
Answer: vascular Doppler ultrasounds are performed by Dr Hakem: carotids (stroke risk), leg arteries and veins, abdominal aorta, renal arteries, arm arteries. They are painless tests, on prescription. To book, call 07 55 50 52 58 (9h to 18h).

---

## 10.17 (FR) Perte de poids et nutrition
`chunk_id: doc10_nutrition_fr` · `lang: fr`

Questions de patients : je veux perdre du poids, j'ai besoin d'un suivi nutritionnel, je veux revoir mon alimentation, aide pour maigrir, bilan nutritionnel, je suis en surpoids et je veux un accompagnement.
Reponse : le bilan nutritionnel est assure par le Dr Berdah Sadaoui (medecin generaliste, nutrition) : il propose un reequilibrage alimentaire personnalise et, si besoin, un accompagnement a la perte de poids, en prevention cardiovasculaire. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h). Le medecin evaluera votre situation lors de la consultation.

---

## 10.17 (EN) Weight loss and nutrition
`chunk_id: doc10_nutrition_en` · `lang: en`

Patient questions: I want to lose weight, I need nutrition follow-up, I want to review my diet, help with losing weight, nutritional assessment, I am overweight and want support.
Answer: the nutritional assessment is provided by Dr Berdah Sadaoui (GP, nutrition): a personalised dietary rebalancing and, if needed, support with weight loss, as part of cardiovascular prevention. To book, call 07 55 50 52 58 (9h to 18h). The doctor will assess your situation during the consultation.

---

## 10.18 (FR) Bilan cardiovasculaire et check-up
`chunk_id: doc10_checkup_fr` · `lang: fr`

Questions de patients : je veux faire un bilan du coeur, je veux un check-up cardiovasculaire, verifier mon coeur, bilan de prevention, je n'ai pas de symptome mais je veux controler mon coeur, bilan avant de reprendre le sport.
Reponse : un bilan cardiovasculaire complet reunit un examen clinique, un ECG et une echographie du coeur, avec un cardiologue (Dr Amraoui ou Dr Sofiane). Pour un bilan hygiene de vie et facteurs de risque, le Dr Berdah Sadaoui peut aussi vous recevoir. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h).

---

## 10.18 (EN) Cardiovascular check-up
`chunk_id: doc10_checkup_en` · `lang: en`

Patient questions: I want a heart check-up, I want a cardiovascular assessment, check my heart, a prevention check-up, I have no symptoms but want to check my heart, a check-up before returning to sport.
Answer: a complete cardiovascular check-up combines a clinical examination, an ECG and a heart ultrasound, with a cardiologist (Dr Amraoui or Dr Sofiane). For a lifestyle and risk-factor review, Dr Berdah Sadaoui can also see you. To book, call 07 55 50 52 58 (9h to 18h).

---

## 10.19 (FR) Prendre rendez-vous
`chunk_id: doc10_booking_fr` · `lang: fr`

Questions de patients : comment prendre rendez-vous, je veux un rendez-vous, comment vous contacter, quel numero appeler, comment reserver une consultation, je voudrais consulter.
Reponse : pour prendre rendez-vous, appelez le 07 55 50 52 58, du lundi au vendredi de 9h a 18h, ou ecrivez a secretariatdramraoui@myeva.ovh. Indiquez votre motif pour etre oriente vers le bon medecin et le bon examen. Une ordonnance n'est pas necessaire pour une consultation, mais la plupart des examens se font sur prescription.

---

## 10.19 (EN) Booking an appointment
`chunk_id: doc10_booking_en` · `lang: en`

Patient questions: how do I book, I want an appointment, how do I contact you, which number do I call, how do I book a consultation, I would like to see a doctor.
Answer: to book, call 07 55 50 52 58, Monday to Friday from 9h to 18h, or e-mail secretariatdramraoui@myeva.ovh. Tell us your reason so we can direct you to the right doctor and test. A prescription is not needed for a consultation, but most tests are done on prescription.

---

## 10.20 (FR) Que faut-il apporter
`chunk_id: doc10_bring_fr` · `lang: fr`

Questions de patients : que dois-je apporter, quels documents pour le rendez-vous, faut-il une ordonnance, dois-je apporter ma carte vitale, quoi prendre pour la consultation.
Reponse : apportez votre ordonnance, votre carte Vitale et votre carte de mutuelle, la liste de vos medicaments, et vos examens cardiaques recents (ECG, echographie, anciens Holter, resultats de laboratoire). Cela aide le medecin a evaluer votre situation. Pour toute question, appelez le 07 55 50 52 58 (9h a 18h).

---

## 10.20 (EN) What to bring
`chunk_id: doc10_bring_en` · `lang: en`

Patient questions: what should I bring, which documents for the appointment, do I need a prescription, should I bring my carte Vitale, what to take to the consultation.
Answer: bring your prescription, your carte Vitale and top-up insurance card, your list of medicines, and your recent cardiac tests (ECG, ultrasound, previous Holter, laboratory results). This helps the doctor assess your situation. For any question, call 07 55 50 52 58 (9h to 18h).

---

## 10.21 (FR) Tarifs et remboursement
`chunk_id: doc10_fees_fr` · `lang: fr`

Questions de patients : combien coute une consultation, quel est le prix d'une consultation, le tarif d'une consultation, une consultation ca coute combien, faut-il payer, est-ce que la consultation est remboursee, quels sont vos tarifs, y a-t-il un depassement d'honoraires, vous etes conventionne secteur 2.
Reponse : le prix exact d'une consultation ou d'un examen n'est pas indique ici, mais voici le principe : Cardio Check-up est conventionne en secteur 2. L'Assurance Maladie rembourse sur la base du tarif conventionnel, et la difference (le depassement d'honoraires) peut etre prise en charge, en tout ou partie, par votre mutuelle. Verifiez votre couverture avant le rendez-vous. Pour connaitre les montants precis, appelez le secretariat au 07 55 50 52 58 (9h a 18h) ou ecrivez a secretariatdramraoui@myeva.ovh.

---

## 10.21 (EN) Fees and reimbursement
`chunk_id: doc10_fees_en` · `lang: en`

Patient questions: how much is a consultation, what is the price of a consultation, the cost of a consultation, how much do I pay, is the consultation reimbursed, what are your fees, is there a fee supplement, are you secteur 2.
Answer: the exact price of a consultation or test is not listed here, but here is the principle: Cardio Check-up operates under the French secteur 2 convention. Public health insurance reimburses on the standard rate, and the difference (the fee supplement) may be covered, in full or in part, by your top-up insurance (mutuelle). Check your cover before the appointment. For exact amounts, call the secretariat at 07 55 50 52 58 (9h to 18h) or e-mail secretariatdramraoui@myeva.ovh.

---

## 10.22 (FR) Adresse, acces et horaires
`chunk_id: doc10_location_fr` · `lang: fr`

Questions de patients : ou etes-vous, quelle est votre adresse, comment venir, quels sont vos horaires, ou se trouve le cabinet, a quelle heure vous etes ouverts.
Reponse : Cardio Check-up se situe au 29 rue Bayen, 75017 Paris. Le secretariat repond au 07 55 50 52 58, du lundi au vendredi de 9h a 18h. Le Dr Amraoui consulte aussi a l'Hopital Americain de Paris (Neuilly-sur-Seine). Pour un rendez-vous, appelez le 07 55 50 52 58.

---

## 10.22 (EN) Address, access and hours
`chunk_id: doc10_location_en` · `lang: en`

Patient questions: where are you, what is your address, how do I get there, what are your hours, where is the practice, when are you open.
Answer: Cardio Check-up is at 29 rue Bayen, 75017 Paris. The secretariat answers on 07 55 50 52 58, Monday to Friday from 9h to 18h. Dr Amraoui also consults at the American Hospital of Paris (Neuilly-sur-Seine). To book, call 07 55 50 52 58.

---

## 10.23 (FR) Quel medecin pour quoi, l'equipe
`chunk_id: doc10_team_fr` · `lang: fr`

Questions de patients : quel medecin dois-je voir, qui fait la cardiologie generale, qui s'occupe du rythme, qui fait les doppler, qui fait la chirurgie, qui voir pour la nutrition, c'est qui les medecins.
Reponse : le Dr Amraoui (cardiologue et rythmologue) et le Dr Sofiane (cardiologue) assurent la cardiologie ; le Dr Hakem realise les echographies Doppler vasculaires ; le Dr Taha est chirurgien vasculaire ; le Pr Doguet est chirurgien cardiaque ; le Dr Berdah Sadaoui (medecin generaliste) s'occupe de la nutrition et de la prevention. Pour prendre rendez-vous, appelez le 07 55 50 52 58 (9h a 18h).

---

## 10.23 (EN) Which doctor for what, the team
`chunk_id: doc10_team_en` · `lang: en`

Patient questions: which doctor should I see, who does general cardiology, who handles rhythm problems, who does the Doppler scans, who does surgery, who to see for nutrition, who are the doctors.
Answer: Dr Amraoui (cardiologist and rhythm specialist) and Dr Sofiane (cardiologist) handle cardiology; Dr Hakem performs the vascular Doppler ultrasounds; Dr Taha is a vascular surgeon; Pr Doguet is a cardiac surgeon; Dr Berdah Sadaoui (GP) handles nutrition and prevention. To book, call 07 55 50 52 58 (9h to 18h).

---

## 10.24 (FR) Langues parlees
`chunk_id: doc10_languages_fr` · `lang: fr`

Questions de patients : parlez-vous anglais, est-ce qu'on peut consulter en anglais, quelles langues parlez-vous, je ne parle pas bien francais.
Reponse : le Dr Amraoui parle francais et anglais, et le Dr Berdah Sadaoui parle francais, anglais et espagnol. Pour organiser une consultation dans votre langue, appelez le 07 55 50 52 58 (9h a 18h) et le secretariat vous orientera.

---

## 10.24 (EN) Languages spoken
`chunk_id: doc10_languages_en` · `lang: en`

Patient questions: do you speak English, can I be seen in English, what languages do you speak, I do not speak French well.
Answer: Dr Amraoui speaks French and English, and Dr Berdah Sadaoui speaks French, English and Spanish. To arrange a consultation in your language, call 07 55 50 52 58 (9h to 18h) and the secretariat will help you.

---

## 10.25 (FR) Urgence, que faire
`chunk_id: doc10_emergency_fr` · `lang: fr`

Questions de patients : c'est une urgence, j'ai une forte douleur dans la poitrine maintenant, je n'arrive plus a respirer, quelqu'un a perdu connaissance, que faire en urgence, j'ai les signes d'un infarctus.
Reponse : en cas de douleur thoracique intense maintenant, d'essoufflement soudain, de perte de connaissance ou de signes d'AVC (visage deforme, bras faible, parole troublee), appelez immediatement le 15 (SAMU), avant toute autre chose. Depuis un mobile, vous pouvez aussi composer le 112. N'utilisez pas la reservation en ligne et n'attendez pas de reponse a un message.

---

## 10.25 (EN) Emergency, what to do
`chunk_id: doc10_emergency_en` · `lang: en`

Patient questions: this is an emergency, I have severe chest pain right now, I cannot breathe, someone has lost consciousness, what to do in an emergency, I have signs of a heart attack.
Answer: for severe chest pain now, sudden breathlessness, loss of consciousness, or signs of stroke (face drooping, arm weakness, speech difficulty), call 15 (SAMU) immediately, before anything else. From a mobile you can also dial 112. Do not use online booking and do not wait for a reply to a message.

---

### Provenance note (for the Architect)
- DOC_10 is a retrieval-booster built entirely from facts already confirmed in DOC_01-DOC_09 (no new claims). Its job is to carry the patient's own vocabulary (FR + EN) so the existing all-MiniLM-L6-v2 model retrieves the right topic. No architecture change.
- One topic = one FR chunk + one EN chunk, kept short (under the model's ~256-token window) so both languages embed fully.
- Answers are written in plain style (no Markdown bold, no em dashes) so they double as clean, safe model outputs consistent with DOC_07 §11.
