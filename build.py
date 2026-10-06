#!/usr/bin/env python3
"""Tiquet's site. One template, three languages (Spanish at the root, /en/, /ca/). Edit S, run, commit the HTML.
Same pattern as decksweep-site: static files, GitHub Pages, CNAME. Screenshots come from the app's sample data only
(invented household, invented companies): never a capture of anyone's real data."""
import os, sys, html
ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ["en", "es", "ca"]
CSS_VERSION = 10
# The App Store page, once Tiquet is live (Spain first): the hero's main button goes there.
# The App Store's own campaign link (pt: our provider token; ct: where the visit came from). Apple counts, in totals, how many
# reach the app's page and download it from each campaign; the site itself counts nothing and stores nothing.
APP_STORE = "https://apps.apple.com/es/app/tiquet/id6816756161?pt=587846&ct=web&mt=8"
# "?ct=linkedin" on our own address carries on to the download buttons, and to our other pages, so a post can be told apart.
CAMPAIGN = ('<script>(function(){var c=new URLSearchParams(location.search).get("ct");if(!c||!/^[a-z0-9-]{1,40}$/.test(c))return;'
            'document.querySelectorAll("a[href]").forEach(function(a){var u=new URL(a.href,location.href);'
            'if(u.hostname==="apps.apple.com"&&u.searchParams.has("ct")){u.searchParams.set("ct",c);a.href=u.toString()}'
            'else if(u.origin===location.origin&&u.pathname!==location.pathname&&!u.searchParams.has("ct")){u.searchParams.set("ct",c);a.href=u.toString()}})})()</script>')
EMAIL = "a.estevez@gmail.com"          # the same public contact as decksweep.securlabs.net; change here only
UPDATED = {"en": "6 October 2026", "es": "6 de octubre de 2026", "ca": "6 d’octubre de 2026"}

S = {
"en": dict(lang="en", name_lang="English",
  title="Tiquet — what your household is signed up to, what it costs, and what runs out",
  desc="Contracts, insurance, warranties and spending, kept on your iPhone and iPad. Read on the device, no account, no bank login, no trackers.",
  nav=[('#story', 'How it helps'), ('#pricing', 'Free and Plus'), ('#ai', 'Ask'), ('#privacy', 'Privacy')],
  h1a="Know what your home is ", h1b="signed up to.",
  sub="Insurance, subscriptions, utilities, warranties: what you have, what each one costs, how much you have paid so far, when it renews and who to call. Your spending is the context, not the chore.",
  cta="Coming to the App Store", note='iOS and iPadOS 27 or later · app in Spanish and English; Catalan coming soon',
  mission_k="What it's for", mission_h="Three questions every household has, answered from its own papers",
  mission_p="Most money apps start from your bank and end in a pie chart. Tiquet starts from what you agreed to pay, and keeps the paper that proves it.",
  pillars=[("What are we signed up to?","Every policy, subscription and bill as a card: number, price, period, renewal, last day to cancel, the phone to call, and the PDF attached.","c-green"),
           ("What does it really cost?","Paid so far, year by year, from your own bank statements. A rise from one year to the next is said in plain words, with the dates.","c-wine"),
           ("What is about to run out?","Renewals, last days to say no, return windows and warranties, on one time axis, with a reminder before each one costs you money.","c-sea")],
  feat_k="Features", feat_h="Everything it does, and nothing it doesn't need",
  feats=[('Scan a receipt, keep the facts',
  'Photograph it or share it from Mail. The on-device model reads shop, date, items, return policy and '
  'warranty. The photo stays as proof.',
  'c-clay'),
 ('Attach the policy, fill the card',
  'Drop a PDF or a photo of a policy: number, premium, what it covers, who is insured and the claims phone '
  'are read and checked against the paper.',
  'c-green'),
 ('Bank and card statements, by file',
  'Download them from your bank and open them with Tiquet: BBVA, Sabadell and more. No login, no connection. '
  'Card numbers are cut to their last four digits before anything is saved. Search any shop or word across '
  'all of them.',
  'c-sea'),
 ('Nothing counted twice',
  "A receipt, its bank line and the contract's premium are one payment. Where there are statements, the "
  "statements rule. Two policies with one insurer, yours and your partner's, are two cards with two prices.",
  'c-wine'),
 ('Contracts that stop charging',
  'If the bank stops showing a charge, Tiquet closes the contract on the last month it was seen, and says '
  'so.',
  'c-night'),
 ('Review: where to spend less',
  'Silent rises, protection that has cost more than the thing, a paid warranty the law already gives you, '
  'bank fees. Your numbers and the question to ask, with every charge behind each one; never a company, a '
  'cover or a cancellation.',
  'c-clay'),
 ('One kind of tag',
  'Every bank payment gets a tag by itself; one tap classifies the rest, past and future, one payee or many '
  'at once. A tag adds up its receipts, its contracts, its things and its bank payments, each counted once. '
  'Follow any tag month by month.',
  'c-green'),
 ('Places you ate',
  "Your regulars on a shelf, your trips found by themselves, home's towns at a glance; then each place with "
  'its own stars and notes, all its visits, what it has cost and the dishes worth coming back for. Search a '
  'name the bank knows and it becomes a place.',
  'c-sea'),
 ('Ask in your own words',
  '“How much on groceries this month?” or “When is the next payment?”. Answers come from saved records, with '
  'the payments behind them. Forecasts are distinguished from recorded charges; some questions require Apple '
  'Intelligence.',
  'c-wine'),
 ('Widgets, and a budget',
  'A policy at hand on the Lock Screen, the next charge, the month against one number you choose. One '
  'budget, not twenty.',
  'c-night'),
 ('iPhone and iPad, in step',
  'Your own iCloud keeps your devices the same, if you switch it on. For the family, one file by AirDrop '
  'with contracts and warranties: no receipts, no bank.',
  'c-clay'),
 ('Discreet mode',
  'One tap turns every amount into •••, for the train or the sofa. The app switcher shows a cover, not your '
  'figures.',
  'c-green'),
 ('Anything strange?',
  'A Bizum to someone new and far above your usual, a transfer to an account never seen, a charge abroad '
  'with no trip, a card being tried, a double charge. Tiquet asks if you recognise it, and if not, says what '
  'to do now. Worked out on your iPhone; it contacts no one.',
  'c-sea'),
 ('In and out',
  'What came in against what went out and what was kept, each month. Money moved between your own accounts '
  "is recognised and left out; refunds and a friend's Bizum are money given back, not earnings. Each account "
  'shows how far its statements go; only the bank and the last four digits are kept.',
  'c-sea'),
 ('Saving for something',
  'A trip, a car, a cushion: how much and by when. What you put aside and the transfers your bank shows fill '
  'the ring, with what is needed each month to arrive on time.',
  'c-sea'),
 ("Say it, and it's a receipt",
  '“Dinner at Can Pere, 42, yesterday” in the question bar becomes a receipt as it will be saved: check it, '
  'tap Save. Nothing exists until you do.',
  'c-sea'),
 ('What a bill will charge next',
  "Electricity, water, gas: the expected charge is the same month last year moved by this year's drift, "
  'never just the last receipt. The card says what is expected and why.',
  'c-wine'),
 ('Payments with an end, and free trials',
  'A phone in 24 instalments says “payment 7 of 24, until March 2027” and retires itself after the last one. '
  'A free trial counts down to the day it starts charging, with a reminder while saying no is still free.',
  'c-night'),
 ('Review the classification',
  'By merchant, by group, or let the on-device model point at what looks filed wrong. One tap fixes every '
  'payment of that merchant, past and future, on every device. Undo is one tap too.',
  'c-clay'),
 ('Many at once, everywhere',
  'Select contracts, things, bank payments, tags or places and act on all of them: tag, move, merge, cancel, '
  'delete. Every delete asks first and says what stays.',
  'c-sea'),
 ('A place is one card',
  'Where it is, its phone, its stars and your notes live on the place; every visit, scanned or from the '
  'bank, links to it. The next statement goes straight to the right place.',
  'c-clay'),
 ('What needs you, in whole sentences',
  'Returns, renewals and warranties as a stack you read at a glance; mark done, or be reminded tomorrow or '
  'on Monday, one by one or many at once.',
  'c-wine'),
 ('On a plane',
  'Your saved documents and local calculations remain available offline. Sync, map searches, logos and App '
  'Store operations need a connection.',
  'c-green')],
  fam_k="For the family", fam_h="If something happens to me",
  fam_p="The papers a household needs when one of its adults is not there to explain them. Made on the device, shared only by you.",
  fam=[("The household sheet","One PDF with everything the household is signed up to: insurance first, then subscriptions and bills. Company, policy number, who is insured, what it covers, the phone to report a claim, where the login is kept, when it renews. No prices unless asked for; never a password.","c-green"),
       ("Documents that expire","ID card, passport, driving licence, the car's inspection, health cards. Which, whose, until when; the number hidden in discreet mode and never on the sheet. Reminded 60 and 15 days before, on the widget and in The Month.","c-wine"),
       ("Everything of Marta's","The people of the household are tags: one tap on a contract says whose it is, and “everything of Marta's” is a screen.","c-sea")],
  cm_k="What's coming", cm_h="The next twelve months, one screen",
  cm_p="A bar per month, solid for fixed premiums and lighter for the bills that depend on consumption, green for what this month has already charged. Below, each charge on its day: the amount, and what it rests on when it is a forecast.",
  cm_l=["“Payment 8 of 24” for plans, “starts charging” for a trial's end","The same figures as Home, Horizon and the widget: one arithmetic for all","Tap a charge to open its contract"],
  wk_k="Week by week", wk_h="Sixteen bars, nothing to zoom",
  wk_p="Four weeks behind and twelve ahead. What was spent, then what is coming: your everyday pace, the fixed charges and the bills that go by consumption. The heaviest week is named on top, because that is the one that hurts.",
  wk_l=["Tap a bar or swipe the card to read the week, charge by charge","The same arithmetic as Horizon and What's coming","Turn the phone for the full time line"],
  month_k="The Month", month_h="Your household's own newspaper",
  month_p="On the 3rd, last month comes out as an issue: a cover, the money drawn day by day, a diary of what happened, where you ate and what you loved, the map, and the household's horoscope: what next month holds, read in your contracts, not in the stars.",
  month_l=["Written on the device from your own receipts, statements and ratings","Share it as a PDF, with or without figures","Every past issue on the shelf"],
  hz_k="Horizon", hz_h="Turn the phone: past, today, future",
  hz_p="One time axis. What you spent, where the month is heading with an honest band, and every charge that is coming. Switch a contract off to see the year without it.",
  hz_l=["Forecast from your own normal weeks, never from your income","Renewals, returns and warranties as deadlines on the same axis","Felt under the finger: a tick on each charge, a thud on month's end"],
  priv_k="Privacy", priv_h="Your data stays with you", priv_p="Your financial AI runs on your device. We receive neither your statements nor your amounts: there is no server of ours. Sync through your own iCloud only if you choose; Apple Maps gets an address or a place name when you look one up.",
  where_h="Where your data is", where=["On your device, in Tiquet's own storage","In your own iCloud private database, only if you switch it on","Read by Apple's on-device model; nothing is sent away to be read"],
  never_h="What Tiquet never does", never=["No account, and no password of yours is ever stored","No connection to your bank","No trackers, no ads, no analytics, no third-party code"],
  leaves_h='Features that use a connection', leaves=['Your private iCloud database, only if you enable sync',
 'Apple Maps: a place name, address or coordinate, including place questions',
 'A company’s website to download its logo, if logos are enabled',
 'App Store: checking, buying or restoring Plus and the trial',
 'Anything you choose to export or share, to your chosen destination'],
  how_k="How it starts", how_h="Useful in ten minutes",
  steps=[("Add what you're signed up to","Type a contract, or attach its PDF and let the card fill itself."),
         ("Bring a year of statements","Download them from your bank as files. Tiquet finds what repeats and offers it as contracts."),
         ("Scan what matters","The receipt of anything with a warranty or a return window. The rest is optional."),
         ("Let it remind you","A month before a yearly policy renews: time to compare. Then the last days to say no.")],
  faq_k="Questions", faq_h="Short answers",
  faqs=[('How much does it cost?',
  'Free includes receipts, warranties, contracts, reminders and 5 questions a day per device about free '
  'features. Plus has a €9.99 launch price in Spain, paid once with no subscription, and supports Family '
  'Sharing for the purchase. Try Plus free for 14 days with no automatic renewal.'),
 ('Does it connect to my bank?',
  'No, and it never will. You download statements as files and open them with Tiquet. It keeps no bank '
  'login.'),
 ('Where is my data?',
  'On your device. If you switch on iCloud sync, also in the private database of your own Apple Account, '
  "which the developer can't read."),
 ('What if Apple Intelligence is unavailable?',
  'You can save and view documents and use text recognition and rules. The local model needs a compatible '
  'device, Apple Intelligence enabled and the model downloaded and available in your language. Some '
  'questions and AI features will be unavailable.'),
 ('Does Family Sharing share my spending?',
  'No. It shares the Plus purchase, subject to Apple’s settings, with up to five family members. Each Apple '
  'Account keeps separate data. To share documents with someone else, explicitly choose to export the '
  'household file.'),
 ('Can I get everything out?',
  'Yes. One .zip with every receipt, photo, policy and movement, plus spreadsheets anyone can open.'),
 ('Does it give financial advice?',
  'No. It reports your own numbers and the question worth asking. It never recommends a company, a cover or '
  'a cancellation.'),
 ('What happens after the 14 days?',
  'You return to the free features with no automatic charge. Everything you saved stays. Plus features '
  'require a purchase; the trial is not shared through Family Sharing.')],
  f_privacy="Privacy", f_support="Support", f_terms="Terms", f_contact="Contact", home="Home",
  privacy_t="Tiquet privacy policy",
  privacy_b=[('Summary',
  'Tiquet stores and processes your documents and figures on your device. It does not send your statements '
  'or amounts to the developer for analysis. No Tiquet account is needed. Some features use external '
  'services, as explained below: optional iCloud sync, maps, logos and App Store purchases.'),
 ('What is stored, and where',
  'Receipts, contracts, policies, things under warranty, bank movements you import, photos, tags, your '
  "budget and your settings are stored on your device, in the app's own storage. If you switch on iCloud "
  'sync, the same data is kept in the private database of your own iCloud account, which only devices signed '
  'in with your Apple Account can read. The developer has no access to it.'),
 ('Reading on the device',
  'Text and speech recognition and Apple’s language model run on the device. We do not send documents or '
  'figures to a remote AI. Model availability depends on your device and Apple Intelligence settings. Place '
  'searches may query Apple Maps with a name, address or coordinate.'),
 ('Bank and card statements',
  'Statements are files you download from your bank and open with Tiquet. Tiquet never connects to a bank '
  'and never stores a bank login. Card numbers found in statements are reduced to their last four digits '
  'before anything is saved.'),
 ('Maps, logos and shared files',
  "Only, and only when a feature you use needs it: an address, a venue's name and town, or a coordinate sent "
  "to Apple Maps to place a receipt, draw a map or show a street picture; a request to a company's own "
  'website, once, to fetch its logo, if logos are on; and whatever you choose to share yourself (a backup, '
  'the household file, an issue of The Month), which goes only where you send it. None of the requests to '
  "Apple Maps or to a company's website carries an amount, your name or a line from your bank."),
 ('Purchases and Family Sharing',
  'Apple handles payments and restoration through the App Store. Tiquet checks your entitlement to Plus or '
  'the trial; it does not receive your card details. Family Sharing shares the Plus entitlement, not your '
  'documents or database.'),
 ('If you contact support',
  'We receive the email address and content you send, to answer your request. Do not attach financial '
  'documents or other people’s personal data: describe the issue with invented data.'),
 ('Permissions',
  'Camera and photos, to scan receipts and attach documents. Location, only if you ask Tiquet to place a '
  'receipt where you are, ask for your places near you, or use the nearby-places widget. Microphone and '
  'speech recognition, only if you ask by voice; recognition runs on the device. Notifications, for the '
  'reminders you see in Settings.'),
 ('No tracking', 'No analytics, no advertising, no third-party code.'),
 ('This website', 'No cookies, no analytics and no third-party code here either. The download buttons carry an App Store campaign label (such as “web” or “linkedin”): the App Store counts, in totals and without identifying you, how many downloads come through each one.'),
 ('Deleting your data',
  'Settings → Backup and restore → Delete everything. With iCloud sync on, it is deleted from your iCloud '
  'and your other devices too. Deleting the app removes what is on the device.'),
 ('Children', 'Tiquet is not directed at children. It includes no advertising or tracking.'),
 ('Contact', 'Questions about this policy: <a href="mailto:a.estevez@gmail.com">a.estevez@gmail.com</a>.')],
  support_t="Tiquet support",
  support_p=('<a href="mailto:a.estevez@gmail.com">a.estevez@gmail.com</a>. Include your device, iOS or iPadOS version '
 'and what you were doing. The app does not automatically send us your financial records. If you email us, '
 'we receive your email and the information you choose to include. Use invented examples; do not send '
 'statements, personal documents or screenshots with real data.'),
  support_h="Common questions",
  support_faq=[("My bank's file isn't read.",
  "Excel, CSV or the bank's PDF statement all work; before saving, “How Tiquet read this file” shows how it was understood. "
  "If it still isn't read, tap “Send us the file's shape”: it prepares an email with the file's layout only (every digit a 9, "
  'every word its length), which you read before sending. Never send the file itself.'),
 ('A charge is counted twice, or not at all.',
  "Open the contract and check the provider's name matches what the bank prints. Where statements cover a "
  "month, only the bank's lines count."),
 ("iPhone and iPad don't show the same.",
  'Both need iCloud sync on (Settings → iPhone and iPad, in step), the same Apple Account, and a few minutes '
  'the first time.'),
 ('A place is on the wrong spot of the map.',
  "Open its card and set the address, or tap “I'm here now” when you are there."),
 ('How do I move to a new phone?',
  'With iCloud sync on, just sign in. Without it: Settings → Backup and restore → Export everything, then '
  'Restore on the new phone.'),
 ('How do I restore Plus?',
  'Open the Tiquet Plus offer in Settings and tap Restore purchases. Use the Apple Account you bought with '
  'and an internet connection. If you receive Plus through Family Sharing, also check your group’s '
  'purchase-sharing settings.'),
 ('What happens after the 14 days?',
  'You return to the free features with no automatic charge. Everything you saved stays. Plus features '
  'require a purchase; the trial is not shared through Family Sharing.'),
 ('What if Apple Intelligence is unavailable?',
  'You can save and view documents and use text recognition and rules. The local model needs a compatible '
  'device, Apple Intelligence enabled and the model downloaded and available in your language. Some '
  'questions and AI features will be unavailable.'),
 ('Does Family Sharing share my spending?',
  'No. It shares the Plus purchase, subject to Apple’s settings, with up to five family members. Each Apple '
  'Account keeps separate data. To share documents with someone else, explicitly choose to export the '
  'household file.')],
  terms_t="Tiquet terms of use",
  terms_b=[("Licence","Tiquet is licensed under Apple's standard Licensed Application End User License Agreement (EULA): <a href=\"https://www.apple.com/legal/internet-services/itunes/dev/stdeula/\">apple.com/legal/internet-services/itunes/dev/stdeula</a>."),
           ("Not financial, legal or insurance advice","Tiquet reports figures from the documents and statements you give it, and points at questions worth asking. It does not recommend companies, products, covers or cancellations, and nothing in it is advice. Decisions about your contracts and your money are yours."),
           ("Accuracy","Text read from receipts, policies and statements can contain errors. Forecasts are estimates from your own past. Check the original document before acting on a date or an amount; reminders are a help, not a guarantee."),
           ("Your data","You are responsible for your backups. The developer cannot recover data, because the developer never has it."),
           ("Contact","<a href=\"mailto:%s\">%s</a>" % (EMAIL, EMAIL))]),

"es": dict(lang="es", name_lang="Español",
  title="Tiquet — lo que tu casa tiene contratado, lo que cuesta y lo que caduca",
  desc="Contratos, seguros, garantías y gastos, guardados en tu iPhone y tu iPad. Se lee en el dispositivo: sin cuenta, sin acceso a tu banco, sin rastreadores.",
  nav=[('#story', 'Cómo te ayuda'), ('#pricing', 'Gratis y Plus'), ('#ai', 'Pregunta'), ('#privacy', 'Privacidad')],
  h1a="Saber qué tiene tu casa ", h1b="contratado.",
  sub="Seguros, suscripciones, suministros, garantías: qué tienes, cuánto cuesta cada cosa, cuánto llevas pagado, cuándo renueva y a quién llamar. Tus gastos son el contexto, no una obligación.",
  cta="Próximamente en el App Store", note='iOS y iPadOS 27 o posterior · app en español e inglés; catalán próximamente',
  mission_k="Para qué sirve", mission_h="Tres preguntas que se hace cualquier casa, respondidas con sus propios papeles",
  mission_p="Casi todas las apps de dinero empiezan en tu banco y acaban en un gráfico de tarta. Tiquet empieza en lo que acordaste pagar, y guarda el papel que lo demuestra.",
  pillars=[("¿Qué tenemos contratado?","Cada póliza, suscripción y recibo como una ficha: número, precio, periodo, renovación, último día para dar de baja, el teléfono al que llamar y el PDF adjunto.","c-green"),
           ("¿Cuánto cuesta de verdad?","Lo pagado hasta hoy, año a año, según tus propios extractos. Una subida de un año a otro se dice con palabras claras y con fechas.","c-wine"),
           ("¿Qué está a punto de caducar?","Renovaciones, últimos días para decir que no, plazos de devolución y garantías, en un solo eje de tiempo, con un aviso antes de que te cueste dinero.","c-sea")],
  feat_k="Funciones", feat_h="Todo lo que hace, y nada que no necesite",
  feats=[('Escanea un tique, guarda los hechos',
  'Hazle una foto o compártelo desde Mail. El modelo del dispositivo lee tienda, fecha, artículos, política '
  'de devolución y garantía. La foto queda como prueba.',
  'c-clay'),
 ('Adjunta la póliza y la ficha se rellena',
  'Un PDF o una foto de la póliza: número, prima, qué cubre, quién está asegurado y el teléfono de '
  'siniestros se leen y se comprueban contra el papel.',
  'c-green'),
 ('Extractos de banco y de tarjeta, por archivo',
  'Los descargas de tu banco y los abres con Tiquet: BBVA, Sabadell y más. Sin contraseña, sin conexión. Los '
  'números de tarjeta se recortan a sus cuatro últimas cifras antes de guardar nada. Busca cualquier tienda '
  'o palabra en todos ellos.',
  'c-sea'),
 ('Nada se cuenta dos veces',
  'Un tique, su línea del banco y la cuota del contrato son un solo pago. Donde hay extracto, manda el '
  'extracto. Dos pólizas de una misma aseguradora, la tuya y la de tu pareja, son dos fichas con dos '
  'precios.',
  'c-wine'),
 ('Contratos que dejan de cobrarse',
  'Si el banco deja de mostrar un cargo, Tiquet cierra el contrato en el último mes en que se vio, y lo '
  'dice.',
  'c-night'),
 ('Revisión: dónde gastar menos',
  'Subidas silenciosas, protecciones que ya han costado más que la cosa, una garantía de pago que la ley ya '
  'te da, comisiones. Tus números y la pregunta que hacer, con cada cargo detrás de cada una; nunca una '
  'compañía, una cobertura ni una baja.',
  'c-clay'),
 ('Una sola clase de etiqueta',
  'Cada pago del banco recibe su etiqueta solo; un toque clasifica el resto, pasado y futuro, de un comercio '
  'o de muchos a la vez. Una etiqueta suma sus tiques, sus contratos, sus cosas y sus pagos del banco, cada '
  'uno contado una vez. Sigue cualquier etiqueta mes a mes.',
  'c-green'),
 ('Sitios donde comisteis',
  'Vuestros habituales en una estantería, los viajes detectados solos, las localidades de casa de un '
  'vistazo; y luego cada sitio con sus estrellas y notas, todas sus visitas, lo que ha costado y los platos '
  'para volver a pedir. Busca un nombre que tu banco conoce y pasa a ser un sitio.',
  'c-sea'),
 ('Pregunta con tus palabras',
  '«¿Cuánto llevo en compra este mes?» o «¿Cuándo toca el próximo pago?». Respuestas a partir de tus '
  'registros, con los pagos que las respaldan. Las previsiones se distinguen de los cobros ya registrados; '
  'algunas preguntas requieren Apple Intelligence.',
  'c-wine'),
 ('Widgets y un presupuesto',
  'Una póliza a mano en la pantalla de bloqueo, el próximo cargo, el mes frente a un número que eliges tú. '
  'Un presupuesto, no veinte.',
  'c-night'),
 ('iPhone y iPad, a la par',
  'Tu propio iCloud mantiene tus dispositivos iguales, si lo activas. Para la familia, un archivo por '
  'AirDrop con contratos y garantías: sin tiques, sin banco.',
  'c-clay'),
 ('Modo discreto',
  'Un toque convierte cada importe en •••, para el tren o el sofá. El selector de apps muestra una tapa, no '
  'tus cifras.',
  'c-green'),
 ('¿Algo raro?',
  'Un Bizum a alguien nuevo y muy por encima de lo habitual, una transferencia a una cuenta nunca vista, un '
  'cargo en el extranjero sin viaje, una tarjeta que están probando, un cobro doble. Tiquet te pregunta si '
  'lo reconoces y, si no, te dice qué hacer ya. Se calcula en tu iPhone y no contacta con nadie.',
  'c-sea'),
 ('Entra y sale',
  'Lo que entró frente a lo que salió y lo que quedó, cada mes. El dinero que mueves entre tus propias '
  'cuentas se reconoce y no cuenta; las devoluciones y el Bizum de un amigo son dinero que vuelve, no '
  'ganancias. Cada cuenta dice hasta dónde llegan sus extractos; solo se guardan el banco y las cuatro '
  'últimas cifras.',
  'c-sea'),
 ('Ahorrando para algo',
  'Un viaje, un coche, un colchón: cuánto y para cuándo. Lo que apartas y las transferencias que muestra tu '
  'banco llenan el anillo, con lo que hace falta cada mes para llegar a tiempo.',
  'c-sea'),
 ('Dilo, y ya es un tique',
  '«Cena Can Pere 42 ayer» en la barra de preguntas se convierte en un tique tal como se guardará: lo '
  'revisas y tocas Guardar. Nada existe hasta que lo haces.',
  'c-sea'),
 ('Lo que cobrará el próximo recibo',
  'Luz, agua, gas: el cargo previsto es el mismo mes del año pasado movido por la deriva de este año, nunca '
  'solo el último recibo. La ficha dice qué se espera y por qué.',
  'c-wine'),
 ('Pagos con final, y pruebas gratis',
  'Un móvil a 24 plazos dice «pago 7 de 24, hasta marzo de 2027» y se retira solo tras el último. Una prueba '
  'gratis cuenta los días hasta que empieza a cobrar, con un aviso mientras decir que no sigue siendo '
  'gratis.',
  'c-night'),
 ('Revisar la clasificación',
  'Por comercio, por grupo, o deja que el modelo del dispositivo señale lo que parece mal archivado. Un '
  'toque corrige cada pago de ese comercio, pasado y futuro, en todos tus dispositivos. Deshacer también es '
  'un toque.',
  'c-clay'),
 ('Muchos a la vez, en todas partes',
  'Selecciona contratos, cosas, pagos del banco, etiquetas o sitios y actúa sobre todos: etiquetar, mover, '
  'fusionar, dar de baja, borrar. Todo borrado pregunta antes y dice qué se queda.',
  'c-sea'),
 ('Un sitio, una ficha',
  'Dónde está, su teléfono, sus estrellas y tus notas viven en el sitio; cada visita, escaneada o del banco, '
  'se engancha a él. El siguiente extracto va directo al sitio correcto.',
  'c-clay'),
 ('Lo que te necesita, en frases enteras',
  'Devoluciones, renovaciones y garantías en una pila que se lee de un vistazo; márcalas como hechas o que '
  'te lo recuerde mañana o el lunes, de una en una o muchas a la vez.',
  'c-wine'),
 ('En el avión',
  'Tus documentos guardados y los cálculos locales siguen disponibles sin conexión. La sincronización, las '
  'búsquedas de mapas, los logos y las operaciones del App Store necesitan conexión.',
  'c-green')],
  fam_k="Para la familia", fam_h="Si me pasa algo",
  fam_p="Los papeles que una casa necesita cuando uno de sus adultos no está para explicarlos. Hechos en el dispositivo, compartidos solo por ti.",
  fam=[("La hoja de la casa","Un PDF con todo lo que la casa tiene contratado: seguros primero, luego suscripciones y recibos. Compañía, número de póliza, quién está asegurado, qué cubre, el teléfono para dar un parte, dónde se guarda el acceso, cuándo renueva. Sin precios salvo que los pidas; nunca una contraseña.","c-green"),
       ("Documentos que caducan","DNI, pasaporte, carné de conducir, la ITV, tarjetas sanitarias. Cuál, de quién, hasta cuándo; el número oculto en modo discreto y nunca en la hoja. Aviso 60 y 15 días antes, en el widget y en El Mes.","c-wine"),
       ("Todo lo de Marta","Las personas de la casa son etiquetas: un toque en un contrato dice de quién es, y «todo lo de Marta» es una pantalla.","c-sea")],
  cm_k="Lo que viene", cm_h="Los próximos doce meses, en una pantalla",
  cm_p="Una barra por mes, sólida para las cuotas fijas y más clara para los recibos que dependen del consumo, verde para lo que este mes ya ha cobrado. Debajo, cada cargo en su día: el importe, y en qué se apoya cuando es una previsión.",
  cm_l=["«Pago 8 de 24» en los planes, «empieza a cobrar» al acabar una prueba","Las mismas cifras que Inicio, Horizonte y el widget: una sola aritmética para todo","Toca un cargo para abrir su contrato"],
  wk_k="Semana a semana", wk_h="Dieciséis barras, nada que ampliar",
  wk_p="Cuatro semanas atrás y doce adelante. Lo gastado, y luego lo que viene: tu ritmo del día a día, los cargos fijos y los recibos que van por consumo. La semana más cargada se nombra arriba, porque es la que duele.",
  wk_l=["Toca una barra o desliza la tarjeta para leer la semana, cargo a cargo","La misma aritmética que Horizonte y Lo que viene","Gira el teléfono para la línea de tiempo completa"],
  month_k="El Mes", month_h="El periódico de tu casa",
  month_p="El día 3 sale el número del mes pasado: una portada, el dinero dibujado día a día, un diario de lo que pasó, dónde comisteis y qué os encantó, el mapa, y el horóscopo de la casa: lo que trae el mes que viene, leído en tus contratos y no en las estrellas.",
  month_l=["Escrito en el dispositivo con tus tiques, extractos y valoraciones","Compártelo en PDF, con cifras o sin ellas","Todos los números anteriores, en la hemeroteca"],
  hz_k="Horizonte", hz_h="Gira el teléfono: pasado, hoy, futuro",
  hz_p="Un solo eje de tiempo. Lo que gastaste, hacia dónde va el mes con una banda honesta, y cada cargo que viene. Apaga un contrato para ver el año sin él.",
  hz_l=["Previsión a partir de tus semanas normales, nunca de tus ingresos","Renovaciones, devoluciones y garantías como plazos en el mismo eje","Se nota bajo el dedo: un toque en cada cargo, un golpe al cerrar el mes"],
  priv_k="Privacidad", priv_h="Tus datos se quedan contigo", priv_p="Tu IA financiera funciona en tu dispositivo. No recibimos ni tus extractos ni tus importes: no hay ningún servidor nuestro. Sincroniza con tu propio iCloud solo si quieres; Apple Maps recibe una dirección o el nombre de un sitio cuando lo buscas.",
  where_h="Dónde están tus datos", where=["En tu dispositivo, en el almacenamiento propio de Tiquet","En la base de datos privada de tu iCloud, solo si lo activas","Los lee el modelo de Apple del dispositivo; nada se envía fuera para leerlo"],
  never_h="Lo que Tiquet no hace nunca", never=["Sin cuenta, y nunca se guarda una contraseña tuya","Sin conexión con tu banco","Sin rastreadores, sin anuncios, sin analítica, sin código de terceros"],
  leaves_h='Funciones que usan conexión', leaves=['Tu base de datos privada de iCloud, solo si activas la sincronización',
 'Apple Maps: nombre de un lugar, dirección o coordenada, también en preguntas sobre sitios',
 'La web de una empresa para descargar su logo, si los logos están activados',
 'App Store: consultar, comprar o restaurar Plus y la prueba',
 'Lo que decidas exportar o compartir, al destino que elijas'],
  how_k="Cómo se empieza", how_h="Útil en diez minutos",
  steps=[("Añade lo que tienes contratado","Escribe un contrato, o adjunta su PDF y deja que la ficha se rellene sola."),
         ("Trae un año de extractos","Descárgalos de tu banco como archivos. Tiquet encuentra lo que se repite y te lo ofrece como contratos."),
         ("Escanea lo que importa","El tique de cualquier cosa con garantía o plazo de devolución. El resto es opcional."),
         ("Deja que te avise","Un mes antes de que renueve una póliza anual: momento de comparar. Después, los últimos días para decir que no.")],
  faq_k="Preguntas", faq_h="Respuestas cortas",
  faqs=[('¿Cuánto cuesta?',
  'Gratis incluye tiques, garantías, contratos, recordatorios y 5 preguntas al día por dispositivo sobre '
  'funciones gratuitas. Plus tiene un precio de lanzamiento de 9,99 € en España, en un solo pago, sin '
  'suscripción, y permite compartir la compra con En Familia. Puedes probar Plus 14 días gratis, sin '
  'renovación automática.'),
 ('¿Se conecta a mi banco?',
  'No, y no lo hará nunca. Descargas los extractos como archivos y los abres con Tiquet. No guarda ningún '
  'acceso al banco.'),
 ('¿Dónde están mis datos?',
  'En tu dispositivo. Si activas la sincronización con iCloud, también en la base de datos privada de tu '
  'cuenta de Apple, que el desarrollador no puede leer.'),
 ('¿Y si Apple Intelligence no está disponible?',
  'Puedes guardar y consultar documentos y usar la lectura de texto y las reglas. El modelo local exige un '
  'dispositivo compatible, Apple Intelligence activado y el modelo descargado y disponible en tu idioma. '
  'Algunas preguntas y funciones de IA no estarán disponibles.'),
 ('¿En Familia comparte mis gastos?',
  'No. Comparte la compra de Plus, sujeto a los ajustes de Apple, con hasta cinco familiares. Los datos de '
  'cada cuenta de Apple siguen separados. Para compartir documentos con otra persona, elige expresamente la '
  'exportación del archivo de casa.'),
 ('¿Puedo sacar todo?',
  'Sí. Un .zip con cada tique, foto, póliza y movimiento, más hojas de cálculo que abre cualquiera.'),
 ('¿Da consejo financiero?',
  'No. Te da tus propios números y la pregunta que vale la pena hacer. Nunca recomienda una compañía, una '
  'cobertura ni una baja.'),
 ('¿Qué pasa al terminar los 14 días?',
  'Vuelves a las funciones gratuitas sin ningún cobro automático. Lo que hayas guardado se conserva. Las '
  'funciones de Plus requieren comprarlo; la prueba no se comparte por En Familia.')],
  f_privacy="Privacidad", f_support="Soporte", f_terms="Condiciones", f_contact="Contacto", home="Inicio",
  privacy_t="Política de privacidad de Tiquet",
  privacy_b=[('Resumen',
  'Tiquet guarda y procesa tus documentos y cifras en tu dispositivo. No envía tus extractos ni tus importes '
  'al desarrollador para analizarlos. No necesitas una cuenta de Tiquet. Algunas funciones usan servicios '
  'externos, como se explica a continuación: sincronización opcional con iCloud, mapas, logos y compras en '
  'el App Store.'),
 ('Qué se guarda y dónde',
  'Tiques, contratos, pólizas, cosas en garantía, movimientos bancarios que importes, fotos, etiquetas, tu '
  'presupuesto y tus ajustes se guardan en tu dispositivo, en el almacenamiento propio de la app. Si activas '
  'la sincronización con iCloud, los mismos datos se guardan en la base de datos privada de tu cuenta de '
  'iCloud, que solo pueden leer los dispositivos con tu cuenta de Apple. El desarrollador no tiene acceso.'),
 ('Lectura en el dispositivo',
  'El reconocimiento de texto y voz y el modelo de lenguaje de Apple se ejecutan en el dispositivo. No '
  'enviamos documentos ni cifras a una IA remota. La disponibilidad del modelo depende del dispositivo y de '
  'los ajustes de Apple Intelligence. Las búsquedas de lugares pueden consultar Apple Maps con un nombre, '
  'dirección o coordenada.'),
 ('Extractos de banco y de tarjeta',
  'Los extractos son archivos que descargas de tu banco y abres con Tiquet. Tiquet nunca se conecta a un '
  'banco ni guarda un acceso bancario. Los números de tarjeta que aparezcan se reducen a sus cuatro últimas '
  'cifras antes de guardar nada.'),
 ('Mapas, logos y archivos compartidos',
  'Solo, y solo cuando lo necesita una función que usas: una dirección, el nombre y la población de un '
  'local, o una coordenada, enviados a Apple Maps para situar un tique, dibujar un mapa o mostrar la foto de '
  'una calle; una petición a la web de una empresa, una vez, para obtener su logo, si los logos están '
  'activados; y lo que decidas compartir tú (una copia, el archivo de casa, un número de El Mes), que va '
  'solo a donde lo envíes. Ninguna petición a Apple Maps ni a la web de una empresa lleva un importe, tu '
  'nombre ni una línea de tu banco.'),
 ('Compras y En Familia',
  'Apple gestiona los pagos y la restauración mediante el App Store. Tiquet comprueba el derecho a usar Plus '
  'o la prueba; no recibe tus datos de tarjeta. En Familia comparte el derecho a Plus, no tus documentos ni '
  'tu base de datos.'),
 ('Si contactas con soporte',
  'Recibimos la dirección de correo y el contenido que tú envíes, para responder a tu consulta. No adjuntes '
  'documentos financieros ni datos personales de terceros: describe el problema con datos ficticios.'),
 ('Permisos',
  'Cámara y fotos, para escanear tiques y adjuntar documentos. Ubicación, solo si pides a Tiquet situar un '
  'tique donde estás, preguntas por tus sitios cercanos, o usas el widget de sitios cercanos. Micrófono y '
  'reconocimiento de voz, solo si preguntas hablando; el reconocimiento se hace en el dispositivo. '
  'Notificaciones, para los avisos que ves en Ajustes.'),
 ('Sin seguimiento', 'Sin analítica, sin publicidad, sin código de terceros.'),
 ('Esta web', 'Aquí tampoco hay cookies, analítica ni código de terceros. Los botones de descarga llevan una etiqueta de campaña del App Store (como «web» o «linkedin»): el App Store cuenta, en total y sin identificarte, cuántas descargas llegan por cada una.'),
 ('Borrar tus datos',
  'Ajustes → Copia y restauración → Borrar todo. Con la sincronización activada, se borra también de tu '
  'iCloud y de tus otros dispositivos. Borrar la app elimina lo que hay en el dispositivo.'),
 ('Menores', 'Tiquet no está dirigida a menores. No incluye publicidad ni seguimiento.'),
 ('Contacto', 'Dudas sobre esta política: <a href="mailto:a.estevez@gmail.com">a.estevez@gmail.com</a>.')],
  support_t="Soporte de Tiquet",
  support_p=('<a href="mailto:a.estevez@gmail.com">a.estevez@gmail.com</a>. Indica tu dispositivo, la versión de iOS o '
 'iPadOS y qué estabas haciendo. La app no nos envía automáticamente tus registros financieros. Si escribes, '
 'recibimos tu correo y la información que decidas incluir. Usa ejemplos ficticios; no envíes extractos, '
 'documentos personales ni capturas con datos reales.'),
  support_h="Preguntas frecuentes",
  support_faq=[('No lee el archivo de mi banco.',
  'Sirven Excel, CSV y el extracto en PDF del banco; antes de guardar, «Así ha leído Tiquet este archivo» enseña cómo lo ha '
  'entendido. Si aun así no se lee, toca «Envíanos la forma del archivo»: prepara un correo solo con la estructura del archivo '
  '(cada cifra, un 9; cada palabra, su longitud), que lees antes de enviarlo. No envíes nunca el archivo en sí.'),
 ('Un cargo se cuenta dos veces, o no se cuenta.',
  'Abre el contrato y comprueba que el nombre del proveedor coincide con el que imprime el banco. Donde un '
  'extracto cubre el mes, solo cuentan las líneas del banco.'),
 ('El iPhone y el iPad no muestran lo mismo.',
  'Los dos necesitan la sincronización activada (Ajustes → iPhone y iPad, a la par), la misma cuenta de '
  'Apple, y unos minutos la primera vez.'),
 ('Un sitio está mal situado en el mapa.',
  'Abre su ficha y pon la dirección, o toca «Estoy aquí ahora» cuando estés allí.'),
 ('¿Cómo paso a un teléfono nuevo?',
  'Con la sincronización activada, basta con iniciar sesión. Sin ella: Ajustes → Copia y restauración → '
  'Exportar todo, y luego Restaurar en el teléfono nuevo.'),
 ('¿Cómo restauro Plus?',
  'Abre la oferta de Tiquet Plus en Ajustes y toca Restaurar compras. Usa la cuenta de Apple con la que '
  'compraste y conexión a internet. Si recibes Plus por En Familia, comprueba también los ajustes de compras '
  'compartidas de tu grupo.'),
 ('¿Qué pasa al terminar los 14 días?',
  'Vuelves a las funciones gratuitas sin ningún cobro automático. Lo que hayas guardado se conserva. Las '
  'funciones de Plus requieren comprarlo; la prueba no se comparte por En Familia.'),
 ('¿Y si Apple Intelligence no está disponible?',
  'Puedes guardar y consultar documentos y usar la lectura de texto y las reglas. El modelo local exige un '
  'dispositivo compatible, Apple Intelligence activado y el modelo descargado y disponible en tu idioma. '
  'Algunas preguntas y funciones de IA no estarán disponibles.'),
 ('¿En Familia comparte mis gastos?',
  'No. Comparte la compra de Plus, sujeto a los ajustes de Apple, con hasta cinco familiares. Los datos de '
  'cada cuenta de Apple siguen separados. Para compartir documentos con otra persona, elige expresamente la '
  'exportación del archivo de casa.')],
  terms_t="Condiciones de uso de Tiquet",
  terms_b=[("Licencia","Tiquet se licencia bajo el acuerdo estándar de Apple para aplicaciones (EULA): <a href=\"https://www.apple.com/legal/internet-services/itunes/dev/stdeula/\">apple.com/legal/internet-services/itunes/dev/stdeula</a>."),
           ("No es asesoramiento financiero, legal ni de seguros","Tiquet muestra cifras de los documentos y extractos que le das, y señala preguntas que vale la pena hacer. No recomienda compañías, productos, coberturas ni bajas, y nada en ella es asesoramiento. Las decisiones sobre tus contratos y tu dinero son tuyas."),
           ("Exactitud","El texto leído de tiques, pólizas y extractos puede contener errores. Las previsiones son estimaciones a partir de tu propio pasado. Comprueba el documento original antes de actuar sobre una fecha o un importe; los avisos son una ayuda, no una garantía."),
           ("Tus datos","Tus copias de seguridad son responsabilidad tuya. El desarrollador no puede recuperar datos, porque nunca los tiene."),
           ("Contacto","<a href=\"mailto:%s\">%s</a>" % (EMAIL, EMAIL))]),

"ca": dict(lang="ca", name_lang="Català",
  title="Tiquet — què té contractat casa teva, què costa i què caduca",
  desc="Contractes, assegurances, garanties i despeses, guardats al teu iPhone i al teu iPad. Es llegeix al dispositiu: sense compte, sense accés al banc, sense rastrejadors.",
  nav=[('#story', 'Com t’ajuda'), ('#pricing', 'Gratis i Plus'), ('#ai', 'Pregunta'), ('#privacy', 'Privadesa')],
  h1a="Saber què té casa teva ", h1b="contractat.",
  sub="Assegurances, subscripcions, subministraments, garanties: què tens, què costa cada cosa, quant portes pagat, quan es renova i a qui trucar. Les despeses són el context, no una obligació.",
  cta="Aviat a l'App Store", note='iOS i iPadOS 27 o posterior · app en castellà i anglès; català aviat',
  mission_k="Per a què serveix", mission_h="Tres preguntes que es fa qualsevol casa, respostes amb els seus propis papers",
  mission_p="Gairebé totes les apps de diners comencen al teu banc i acaben en un gràfic de pastís. Tiquet comença en allò que vas acordar pagar, i guarda el paper que ho demostra.",
  pillars=[("Què tenim contractat?","Cada pòlissa, subscripció i rebut com una fitxa: número, preu, període, renovació, últim dia per donar-se de baixa, el telèfon on trucar i el PDF adjunt.","c-green"),
           ("Què costa de veritat?","El que has pagat fins avui, any a any, segons els teus propis extractes. Una pujada d'un any a l'altre es diu amb paraules clares i amb dates.","c-wine"),
           ("Què està a punt de caducar?","Renovacions, últims dies per dir que no, terminis de devolució i garanties, en un sol eix de temps, amb un avís abans que et costi diners.","c-sea")],
  feat_k="Funcions", feat_h="Tot el que fa, i res que no necessiti",
  feats=[('Escaneja un tiquet, guarda els fets',
  'Fes-li una foto o comparteix-lo des del Mail. El model del dispositiu llegeix botiga, data, articles, '
  'política de devolució i garantia. La foto queda com a prova.',
  'c-clay'),
 ("Adjunta la pòlissa i la fitxa s'omple",
  'Un PDF o una foto de la pòlissa: número, prima, què cobreix, qui està assegurat i el telèfon de sinistres '
  'es llegeixen i es comproven contra el paper.',
  'c-green'),
 ('Extractes de banc i de targeta, per fitxer',
  'Els descarregues del teu banc i els obres amb Tiquet: BBVA, Sabadell i més. Sense contrasenya, sense '
  'connexió. Els números de targeta es retallen a les quatre últimes xifres abans de guardar res. Busca '
  'qualsevol botiga o paraula en tots.',
  'c-sea'),
 ('Res es compta dues vegades',
  'Un tiquet, la seva línia del banc i la quota del contracte són un sol pagament. On hi ha extracte, mana '
  "l'extracte. Dues pòlisses d'una mateixa asseguradora, la teva i la de la teva parella, són dues fitxes "
  'amb dos preus.',
  'c-wine'),
 ('Contractes que deixen de cobrar-se',
  "Si el banc deixa de mostrar un càrrec, Tiquet tanca el contracte l'últim mes en què es va veure, i ho "
  'diu.',
  'c-night'),
 ('Revisió: on gastar menys',
  'Pujades silencioses, proteccions que ja han costat més que la cosa, una garantia de pagament que la llei '
  'ja et dona, comissions. Els teus números i la pregunta a fer, amb cada càrrec darrere de cadascuna; mai '
  'una companyia, una cobertura ni una baixa.',
  'c-clay'),
 ("Una sola mena d'etiqueta",
  "Cada pagament del banc rep la seva etiqueta tot sol; un toc classifica la resta, passat i futur, d'un "
  'comerç o de molts alhora. Una etiqueta suma els seus tiquets, contractes, coses i pagaments del banc, '
  'cadascun comptat un cop. Segueix qualsevol etiqueta mes a mes.',
  'c-green'),
 ('Llocs on vau menjar',
  "Els vostres habituals en un prestatge, els viatges detectats sols, les poblacions de casa d'un cop d'ull; "
  'i després cada lloc amb les seves estrelles i notes, totes les visites, el que ha costat i els plats per '
  'tornar a demanar. Busca un nom que el teu banc coneix i passa a ser un lloc.',
  'c-sea'),
 ('Pregunta amb les teves paraules',
  '«Quant porto en compra aquest mes?» o «Quan toca el proper pagament?». Respostes a partir dels registres, '
  'amb els pagaments que les sostenen. Les previsions es distingeixen dels càrrecs registrats; algunes '
  'preguntes requereixen Apple Intelligence.',
  'c-wine'),
 ('Widgets i un pressupost',
  "Una pòlissa a mà a la pantalla de bloqueig, el proper càrrec, el mes davant d'un número que tries tu. Un "
  'pressupost, no vint.',
  'c-night'),
 ('iPhone i iPad, a la par',
  "El teu propi iCloud manté els teus dispositius iguals, si l'actives. Per a la família, un fitxer per "
  'AirDrop amb contractes i garanties: sense tiquets, sense banc.',
  'c-clay'),
 ('Mode discret',
  "Un toc converteix cada import en •••, per al tren o el sofà. El selector d'apps mostra una tapa, no les "
  'teves xifres.',
  'c-green'),
 ('Alguna cosa estranya?',
  'Un Bizum a algú nou i molt per sobre del que és habitual, una transferència a un compte mai vist, un '
  "càrrec a l'estranger sense viatge, una targeta que estan provant, un cobrament doble. Tiquet et pregunta "
  'si ho reconeixes i, si no, et diu què fer ara. Es calcula al teu iPhone i no contacta amb ningú.',
  'c-sea'),
 ('Entra i surt',
  'El que va entrar davant del que va sortir i el que va quedar, cada mes. Els diners que mous entre els '
  "teus propis comptes es reconeixen i no compten; les devolucions i el Bizum d'un amic són diners que "
  'tornen, no guanys. Cada compte diu fins on arriben els seus extractes; només es guarden el banc i les '
  'quatre últimes xifres.',
  'c-sea'),
 ('Estalviant per a alguna cosa',
  'Un viatge, un cotxe, un coixí: quant i per a quan. El que aparties i les transferències que mostra el teu '
  "banc omplen l'anell, amb el que cal cada mes per arribar-hi a temps.",
  'c-sea'),
 ('Digues-ho, i ja és un tiquet',
  '«Sopar Can Pere 42 ahir» a la barra de preguntes es converteix en un tiquet tal com es desarà: el revises '
  'i toques Desa. Res no existeix fins que ho fas.',
  'c-sea'),
 ('El que cobrarà el proper rebut',
  "Llum, aigua, gas: el càrrec previst és el mateix mes de l'any passat mogut per la deriva d'enguany, mai "
  "només l'últim rebut. La fitxa diu què s'espera i per què.",
  'c-wine'),
 ('Pagaments amb final, i proves gratis',
  "Un mòbil a 24 terminis diu «pagament 7 de 24, fins al març de 2027» i es retira sol després de l'últim. "
  'Una prova gratis compta els dies fins que comença a cobrar, amb un avís mentre dir que no encara és '
  'gratis.',
  'c-night'),
 ('Revisar la classificació',
  'Per comerç, per grup, o deixa que el model del dispositiu assenyali el que sembla mal arxivat. Un toc '
  "corregeix cada pagament d'aquell comerç, passat i futur, a tots els teus dispositius. Desfer també és un "
  'toc.',
  'c-clay'),
 ('Molts alhora, a tot arreu',
  'Selecciona contractes, coses, pagaments del banc, etiquetes o llocs i actua sobre tots: etiquetar, moure, '
  'fusionar, donar de baixa, esborrar. Tot esborrat pregunta abans i diu què es queda.',
  'c-sea'),
 ('Un lloc, una fitxa',
  'On és, el seu telèfon, les seves estrelles i les teves notes viuen al lloc; cada visita, escanejada o del '
  "banc, s'hi enganxa. El següent extracte va directe al lloc correcte.",
  'c-clay'),
 ('El que et necessita, en frases senceres',
  "Devolucions, renovacions i garanties en una pila que es llegeix d'un cop d'ull; marca-les com a fetes o "
  "que t'ho recordi demà o dilluns, d'una en una o moltes alhora.",
  'c-wine'),
 ("A l'avió",
  'Els documents desats i els càlculs locals continuen disponibles sense connexió. La sincronització, les '
  'cerques de mapes, els logos i les operacions de l’App Store necessiten connexió.',
  'c-green')],
  fam_k="Per a la família", fam_h="Si em passa res",
  fam_p="Els papers que una casa necessita quan un dels seus adults no hi és per explicar-los. Fets al dispositiu, compartits només per tu.",
  fam=[("El full de la casa","Un PDF amb tot el que la casa té contractat: assegurances primer, després subscripcions i rebuts. Companyia, número de pòlissa, qui està assegurat, què cobreix, el telèfon per donar un part, on es guarda l'accés, quan es renova. Sense preus si no els demanes; mai una contrasenya.","c-green"),
       ("Documents que caduquen","DNI, passaport, carnet de conduir, la ITV, targetes sanitàries. Quin, de qui, fins quan; el número amagat en mode discret i mai al full. Avís 60 i 15 dies abans, al widget i a El Mes.","c-wine"),
       ("Tot el de la Marta","Les persones de la casa són etiquetes: un toc en un contracte diu de qui és, i «tot el de la Marta» és una pantalla.","c-sea")],
  cm_k="El que ve", cm_h="Els propers dotze mesos, en una pantalla",
  cm_p="Una barra per mes, sòlida per a les quotes fixes i més clara per als rebuts que depenen del consum, verda per al que aquest mes ja ha cobrat. A sota, cada càrrec al seu dia: l'import, i en què es basa quan és una previsió.",
  cm_l=["«Pagament 8 de 24» als plans, «comença a cobrar» en acabar una prova","Les mateixes xifres que Inici, Horitzó i el widget: una sola aritmètica per a tot","Toca un càrrec per obrir el seu contracte"],
  wk_k="Setmana a setmana", wk_h="Setze barres, res a ampliar",
  wk_p="Quatre setmanes enrere i dotze endavant. El que s'ha gastat, i després el que ve: el teu ritme del dia a dia, els càrrecs fixos i els rebuts que van per consum. La setmana més carregada s'anomena a dalt, perquè és la que fa mal.",
  wk_l=["Toca una barra o llisca la targeta per llegir la setmana, càrrec a càrrec","La mateixa aritmètica que Horitzó i El que ve","Gira el telèfon per a la línia de temps completa"],
  month_k="El Mes", month_h="El diari de casa teva",
  month_p="El dia 3 surt el número del mes passat: una portada, els diners dibuixats dia a dia, un dietari del que va passar, on vau menjar i què us va encantar, el mapa, i l'horòscop de la casa: el que porta el mes que ve, llegit als teus contractes i no a les estrelles.",
  month_l=["Escrit al dispositiu amb els teus tiquets, extractes i valoracions","Comparteix-lo en PDF, amb xifres o sense","Tots els números anteriors, a l'hemeroteca"],
  hz_k="Horitzó", hz_h="Gira el telèfon: passat, avui, futur",
  hz_p="Un sol eix de temps. El que vas gastar, cap on va el mes amb una banda honesta, i cada càrrec que ve. Apaga un contracte per veure l'any sense ell.",
  hz_l=["Previsió a partir de les teves setmanes normals, mai dels teus ingressos","Renovacions, devolucions i garanties com a terminis al mateix eix","Es nota sota el dit: un toc a cada càrrec, un cop en tancar el mes"],
  priv_k="Privadesa", priv_h="Les teves dades es queden amb tu", priv_p="La teva IA financera funciona al teu dispositiu. No rebem ni els teus extractes ni els teus imports: no hi ha cap servidor nostre. Sincronitza amb el teu propi iCloud només si vols; Apple Maps rep una adreça o el nom d'un lloc quan el cerques.",
  where_h="On són les teves dades", where=["Al teu dispositiu, a l'emmagatzematge propi de Tiquet","A la base de dades privada del teu iCloud, només si l'actives","Les llegeix el model d'Apple del dispositiu; res s'envia fora per llegir-ho"],
  never_h="El que Tiquet no fa mai", never=["Sense compte, i mai es guarda cap contrasenya teva","Sense connexió amb el teu banc","Sense rastrejadors, sense anuncis, sense analítica, sense codi de tercers"],
  leaves_h='Funcions que fan servir connexió', leaves=['La base de dades privada d’iCloud, només si actives la sincronització',
 'Apple Maps: nom d’un lloc, adreça o coordenada, també en preguntes sobre llocs',
 'El web d’una empresa per descarregar-ne el logo, si els logos estan activats',
 'App Store: consultar, comprar o restaurar Plus i la prova',
 'El que decideixis exportar o compartir, a la destinació que triïs'],
  how_k="Com es comença", how_h="Útil en deu minuts",
  steps=[("Afegeix el que tens contractat","Escriu un contracte, o adjunta'n el PDF i deixa que la fitxa s'ompli sola."),
         ("Porta un any d'extractes","Descarrega'ls del teu banc com a fitxers. Tiquet troba el que es repeteix i t'ho ofereix com a contractes."),
         ("Escaneja el que importa","El tiquet de qualsevol cosa amb garantia o termini de devolució. La resta és opcional."),
         ("Deixa que t'avisi","Un mes abans que es renovi una pòlissa anual: moment de comparar. Després, els últims dies per dir que no.")],
  faq_k="Preguntes", faq_h="Respostes curtes",
  faqs=[('Quant costa?',
  'Gratis inclou tiquets, garanties, contractes, recordatoris i 5 preguntes al dia per dispositiu sobre '
  'funcions gratuïtes. Plus té un preu de llançament de 9,99 € a Espanya, amb un sol pagament, sense '
  'subscripció, i permet compartir la compra amb En Família. Pots provar Plus 14 dies gratis, sense '
  'renovació automàtica.'),
 ('Es connecta al meu banc?',
  'No, i no ho farà mai. Descarregues els extractes com a fitxers i els obres amb Tiquet. No guarda cap '
  'accés al banc.'),
 ('On són les meves dades?',
  'Al teu dispositiu. Si actives la sincronització amb iCloud, també a la base de dades privada del teu '
  "compte d'Apple, que el desenvolupador no pot llegir."),
 ('I si Apple Intelligence no està disponible?',
  'Pots desar i consultar documents i fer servir el reconeixement de text i les regles. El model local '
  'necessita un dispositiu compatible, Apple Intelligence activat i el model descarregat i disponible en el '
  'teu idioma. Algunes preguntes i funcions d’IA no estaran disponibles.'),
 ('En Família comparteix les meves despeses?',
  'No. Comparteix la compra de Plus, segons els ajustos d’Apple, amb fins a cinc familiars. Les dades de '
  'cada compte d’Apple continuen separades. Per compartir documents amb una altra persona, tria expressament '
  'l’exportació del fitxer de casa.'),
 ('Puc treure-ho tot?',
  'Sí. Un .zip amb cada tiquet, foto, pòlissa i moviment, més fulls de càlcul que obre qualsevol.'),
 ('Dona consell financer?',
  'No. Et dona els teus propis números i la pregunta que val la pena fer. Mai recomana una companyia, una '
  'cobertura ni una baixa.'),
 ('Què passa quan s’acaben els 14 dies?',
  'Tornes a les funcions gratuïtes sense cap càrrec automàtic. El que hagis desat es conserva. Les funcions '
  'de Plus requereixen comprar-lo; la prova no es comparteix per En Família.')],
  f_privacy="Privadesa", f_support="Suport", f_terms="Condicions", f_contact="Contacte", home="Inici",
  privacy_t="Política de privadesa de Tiquet",
  privacy_b=[('Resum',
  'Tiquet desa i processa els teus documents i xifres al dispositiu. No envia els extractes ni els imports '
  'al desenvolupador per analitzar-los. No cal cap compte de Tiquet. Algunes funcions fan servir serveis '
  'externs, com s’explica a continuació: sincronització opcional amb iCloud, mapes, logos i compres a l’App '
  'Store.'),
 ('Què es guarda i on',
  'Tiquets, contractes, pòlisses, coses en garantia, moviments bancaris que importis, fotos, etiquetes, el '
  "teu pressupost i els teus ajustos es guarden al teu dispositiu, a l'emmagatzematge propi de l'app. Si "
  'actives la sincronització amb iCloud, les mateixes dades es guarden a la base de dades privada del teu '
  "compte d'iCloud, que només poden llegir els dispositius amb el teu compte d'Apple. El desenvolupador no "
  'hi té accés.'),
 ('Lectura al dispositiu',
  'El reconeixement de text i veu i el model de llenguatge d’Apple s’executen al dispositiu. No enviem '
  'documents ni xifres a una IA remota. La disponibilitat del model depèn del dispositiu i dels ajustos '
  'd’Apple Intelligence. Les cerques de llocs poden consultar Apple Maps amb un nom, adreça o coordenada.'),
 ('Extractes de banc i de targeta',
  'Els extractes són fitxers que descarregues del teu banc i obres amb Tiquet. Tiquet mai es connecta a un '
  'banc ni guarda un accés bancari. Els números de targeta que hi apareguin es redueixen a les quatre '
  'últimes xifres abans de guardar res.'),
 ('Mapes, logos i fitxers compartits',
  "Només, i només quan ho necessita una funció que fas servir: una adreça, el nom i la població d'un local, "
  "o una coordenada, enviats a Apple Maps per situar un tiquet, dibuixar un mapa o mostrar la foto d'un "
  "carrer; una petició al web d'una empresa, una vegada, per obtenir-ne el logo, si els logos estan "
  "activats; i el que decideixis compartir tu (una còpia, el fitxer de casa, un número d'El Mes), que va "
  "només on ho enviïs. Cap petició a Apple Maps ni al web d'una empresa porta un import, el teu nom ni una "
  'línia del teu banc.'),
 ('Compres i En Família',
  'Apple gestiona els pagaments i la restauració a través de l’App Store. Tiquet comprova el dret a fer '
  'servir Plus o la prova; no rep les dades de la targeta. En Família comparteix el dret a Plus, no els '
  'documents ni la base de dades.'),
 ('Si contactes amb suport',
  'Rebem l’adreça de correu i el contingut que enviïs, per respondre a la consulta. No adjuntis documents '
  'financers ni dades personals d’altres persones: descriu el problema amb dades fictícies.'),
 ('Permisos',
  'Càmera i fotos, per escanejar tiquets i adjuntar documents. Ubicació, només si demanes a Tiquet situar un '
  'tiquet on ets, preguntes pels teus llocs propers, o fas servir el widget de llocs propers. Micròfon i '
  'reconeixement de veu, només si preguntes parlant; el reconeixement es fa al dispositiu. Notificacions, '
  'pels avisos que veus a Ajustos.'),
 ('Sense seguiment', 'Sense analítica, sense publicitat, sense codi de tercers.'),
 ('Aquest web', 'Aquí tampoc no hi ha galetes, analítica ni codi de tercers. Els botons de descàrrega porten una etiqueta de campanya de l’App Store (com ara «web» o «linkedin»): l’App Store compta, en total i sense identificar-te, quantes descàrregues arriben per cadascuna.'),
 ('Esborrar les teves dades',
  "Ajustos → Còpia i restauració → Esborrar-ho tot. Amb la sincronització activada, s'esborra també del teu "
  "iCloud i dels teus altres dispositius. Esborrar l'app elimina el que hi ha al dispositiu."),
 ('Menors', 'Tiquet no està dirigida a menors. No inclou publicitat ni seguiment.'),
 ('Contacte', 'Dubtes sobre aquesta política: <a href="mailto:a.estevez@gmail.com">a.estevez@gmail.com</a>.')],
  support_t="Suport de Tiquet",
  support_p=('<a href="mailto:a.estevez@gmail.com">a.estevez@gmail.com</a>. Indica el dispositiu, la versió d’iOS o '
 'iPadOS i què estaves fent. L’app no ens envia automàticament els teus registres financers. Si ens escrius, '
 'rebem el correu i la informació que hi incloguis. Fes servir exemples ficticis; no enviïs extractes, '
 'documents personals ni captures amb dades reals.'),
  support_h="Preguntes freqüents",
  support_faq=[('No llegeix el fitxer del meu banc.',
  "Serveixen Excel, CSV i l'extracte en PDF del banc; abans de desar, «Así ha leído Tiquet este archivo» mostra com l'ha "
  "entès. Si tot i així no es llegeix, toca «Envíanos la forma del archivo»: prepara un correu només amb l'estructura del fitxer "
  "(cada xifra, un 9; cada paraula, la seva llargada), que llegeixes abans d'enviar-lo. No enviïs mai el fitxer en si."),
 ('Un càrrec es compta dues vegades, o no es compta.',
  'Obre el contracte i comprova que el nom del proveïdor coincideix amb el que imprimeix el banc. On un '
  'extracte cobreix el mes, només compten les línies del banc.'),
 ("L'iPhone i l'iPad no mostren el mateix.",
  'Tots dos necessiten la sincronització activada (Ajustos → iPhone i iPad, a la par), el mateix compte '
  "d'Apple, i uns minuts la primera vegada."),
 ('Un lloc està mal situat al mapa.',
  "Obre la seva fitxa i posa-hi l'adreça, o toca «Soc aquí ara» quan hi siguis."),
 ('Com passo a un telèfon nou?',
  "Amb la sincronització activada, n'hi ha prou d'iniciar sessió. Sense: Ajustos → Còpia i restauració → "
  'Exportar-ho tot, i després Restaurar al telèfon nou.'),
 ('Com restauro Plus?',
  'Obre l’oferta de Tiquet Plus a Configuració i toca Restaurar compres. Fes servir el compte d’Apple amb '
  'què vas comprar i connexió a internet. Si reps Plus per En Família, comprova també els ajustos de compres '
  'compartides del grup.'),
 ('Què passa quan s’acaben els 14 dies?',
  'Tornes a les funcions gratuïtes sense cap càrrec automàtic. El que hagis desat es conserva. Les funcions '
  'de Plus requereixen comprar-lo; la prova no es comparteix per En Família.'),
 ('I si Apple Intelligence no està disponible?',
  'Pots desar i consultar documents i fer servir el reconeixement de text i les regles. El model local '
  'necessita un dispositiu compatible, Apple Intelligence activat i el model descarregat i disponible en el '
  'teu idioma. Algunes preguntes i funcions d’IA no estaran disponibles.'),
 ('En Família comparteix les meves despeses?',
  'No. Comparteix la compra de Plus, segons els ajustos d’Apple, amb fins a cinc familiars. Les dades de '
  'cada compte d’Apple continuen separades. Per compartir documents amb una altra persona, tria expressament '
  'l’exportació del fitxer de casa.')],
  terms_t="Condicions d'ús de Tiquet",
  terms_b=[("Llicència","Tiquet es llicencia sota l'acord estàndard d'Apple per a aplicacions (EULA): <a href=\"https://www.apple.com/legal/internet-services/itunes/dev/stdeula/\">apple.com/legal/internet-services/itunes/dev/stdeula</a>."),
           ("No és assessorament financer, legal ni d'assegurances","Tiquet mostra xifres dels documents i extractes que li dones, i assenyala preguntes que val la pena fer. No recomana companyies, productes, cobertures ni baixes, i res del que conté és assessorament. Les decisions sobre els teus contractes i els teus diners són teves."),
           ("Exactitud","El text llegit de tiquets, pòlisses i extractes pot contenir errors. Les previsions són estimacions a partir del teu propi passat. Comprova el document original abans d'actuar sobre una data o un import; els avisos són una ajuda, no una garantia."),
           ("Les teves dades","Les teves còpies de seguretat són responsabilitat teva. El desenvolupador no pot recuperar dades, perquè mai les té."),
           ("Contacte","<a href=\"mailto:%s\">%s</a>" % (EMAIL, EMAIL))]),
}

# The landing: household benefits first, accurate privacy, one phone that changes as you scroll, and the
# rest of the features as a strip instead of a wall of cards. Screens in img/s are the app's sample household.
X = {
"en": dict(
  h1a='What you pay. What renews. ', h1b='What you want to remember.',
  sub=('Keep contracts, insurance and receipts together. Find the next payment, look up a warranty and get '
 'reminders before a deadline. On your iPhone and iPad, without connecting to your bank.'),
  badges=["On-device AI", "No account", "No servers of ours", "No trackers"],

  ai_k="Ask", ai_h='Ask about your spending. From your own records.',
  ai_p=('The app calculates figures from your saved records; Apple’s model explains them on the device. Check the '
 'source documents: readings can contain errors, and future charges are estimates. A question about places '
 'may query Apple Maps to locate a place, without sending your amounts or statements.'),
  chat=[("How much did we spend on restaurants this year?", "€724.68 in 7 payments. Mostly at El Celler (€210), La Taverna del Pla (€173) and Bar Ponent (€98)."),
        ("Where did I love the patatas bravas?", "La Taverna del Pla (Barcelona): ★★★★★, 9 Aug 2026."),
        ("And in Sant Cugat?", "No bravas in Sant Cugat in your receipts. Where you've had them: La Taverna del Pla.")],
  ai_net='Financial calculations', ai_model='AI', ai_model_v='On device',
  story_k="A tour", story_h='Three moments when it helps',
  priv_n=[('0', 'Tiquet accounts'),
 ('0', 'servers of ours'),
 ('0', 'trackers'),
 ('0', 'documents sent to a remote AI')],
  more_k="And also", more_h="%d more things it does", more_all="Read them all",
  primary_cta='Compare Free and Plus',
  ai_net_v='On your device',
  demo_note=('Conversation and screens use invented data. Answers depend on saved records and Apple Intelligence '
 'availability.'),
  tour=[('contracts',
  'Before your insurance renews',
  'The policy, price and last cancellation date in one card. A reminder gives you time to review the '
  'contract.'),
 ('coming',
  'Before the next charge',
  'See what is expected and when, based on contracts and previous payments. Forecasts explain what they are '
  'based on. Included in Plus.'),
 ('home',
  'When you need to return something',
  'Keep the receipt and look up the return window or warranty. Keep the original document and check the date '
  'that was read.')],
  price_k='Free and Plus',
  price_h='Start free. Upgrade when it helps.',
  free_h='Tiquet Free',
  free_price='€0',
  free_note='No time limit',
  free_items=['Receipts, warranties, contracts and reminders',
 'The household sheet and unusual-charge checks',
 'Backups and optional iCloud sync',
 '5 questions a day per device about free features'],
  plus_h='Tiquet Plus',
  plus_price='€9.99',
  plus_note='Launch price in Spain · one-time payment',
  plus_items=['Everything in Free',
 'Spending review, income, accounts and savings goals',
 'Upcoming charges for 12 months and The Month',
 'Places from your statements',
 'Ask without a daily limit',
 'Purchase supports Family Sharing'],
  trial_h='Try Plus free for 14 days',
  trial_p=('No automatic renewal or charge when it ends. Continue with Free and keep everything you saved. The trial '
 'is individual; buying Plus is optional.'),
  family_note=('Family Sharing shares the Plus purchase with up to five family members, subject to Apple’s '
 'purchase-sharing settings. Each person keeps their own data: statements, spending and documents are not '
 'shared automatically.'),
  compat_h='Check your device',
  compat_p=('Requires iOS or iPadOS 27 or later. Local model features need a compatible device with Apple Intelligence '
 'enabled and its model available in the chosen language. Without it, you can save and view documents and '
 'use text recognition and rules; some questions and AI features will be unavailable.')),
"es": dict(
  h1a='Lo que pagas. Lo que renueva. ', h1b='Lo que no quieres olvidar.',
  sub=('Reúne contratos, seguros y tiques. Encuentra el próximo pago, ten a mano una garantía y recibe avisos '
 'antes de que termine un plazo. En tu iPhone y tu iPad, sin conectar tu banco.'),
  badges=["IA en el dispositivo", "Sin cuenta", "Sin servidores nuestros", "Sin rastreadores"],

  ai_k="Pregunta", ai_h='Pregunta sobre tus gastos. Con tus propios datos.',
  ai_p=('La app calcula las cifras a partir de tus registros; el modelo de Apple las explica en el dispositivo. '
 'Comprueba los documentos leídos: pueden contener errores, y los cargos futuros son previsiones. Una '
 'pregunta sobre sitios puede consultar Apple Maps para localizar un lugar, sin enviar tus importes ni tus '
 'extractos.'),
  chat=[("¿Cuánto hemos gastado en restaurantes este año?", "724,68 € en 7 pagos. Sobre todo en El Celler (210 €), La Taverna del Pla (173 €) y Bar Ponent (98 €)."),
        ("¿Dónde me encantaron las bravas?", "La Taverna del Pla (Barcelona): ★★★★★, 9 ago 2026."),
        ("¿Y en Sant Cugat?", "No hay bravas en Sant Cugat en tus tiques. Donde sí las has tomado: La Taverna del Pla.")],
  ai_net='Cálculos financieros', ai_model='IA', ai_model_v='Local',
  story_k="Recorrido", story_h='Tres momentos en los que te ayuda',
  priv_n=[('0', 'cuentas de Tiquet'),
 ('0', 'servidores nuestros'),
 ('0', 'rastreadores'),
 ('0', 'documentos enviados a una IA remota')],
  more_k="Y además", more_h="%d cosas más que hace", more_all="Leerlas todas",
  primary_cta='Ver Gratis y Plus',
  ai_net_v='En tu dispositivo',
  demo_note=('Conversación y pantallas con datos ficticios. Las respuestas dependen de los datos guardados y de la '
 'disponibilidad de Apple Intelligence.'),
  tour=[('contracts',
  'Antes de que renueve el seguro',
  'La póliza, el precio y el último día para darlo de baja, en una ficha. Un aviso te da tiempo para revisar '
  'el contrato.'),
 ('coming',
  'Antes del próximo cargo',
  'Consulta qué se espera cobrar y cuándo, según tus contratos y pagos anteriores. Las previsiones indican '
  'en qué se apoyan. Incluido en Plus.'),
 ('home',
  'Cuando necesitas devolver algo',
  'Guarda el tique y consulta el plazo de devolución o la garantía. Conserva el documento original y revisa '
  'la fecha leída.')],
  price_k='Gratis y Plus',
  price_h='Empieza gratis. Amplía cuando te compense.',
  free_h='Tiquet Gratis',
  free_price='0 €',
  free_note='Sin límite de tiempo',
  free_items=['Tiques, garantías, contratos y sus recordatorios',
 'Hoja de la casa y detección de cargos inusuales',
 'Copias de seguridad e iCloud opcional',
 '5 preguntas al día por dispositivo sobre funciones gratuitas'],
  plus_h='Tiquet Plus',
  plus_price='9,99 €',
  plus_note='Precio de lanzamiento en España · pago único',
  plus_items=['Todo lo de Gratis',
 'Revisión de gastos, ingresos, cuentas y objetivos de ahorro',
 'Próximos cargos a 12 meses y El Mes',
 'Sitios a partir de tus extractos',
 'Preguntas sin límite diario',
 'Compra compatible con En Familia'],
  trial_h='Prueba Plus gratis durante 14 días',
  trial_p=('Sin renovación automática ni cargos al terminar. Después sigues con Gratis y conservas lo que hayas '
 'guardado. La prueba es individual; comprar Plus es opcional.'),
  family_note=('En Familia comparte la compra de Plus con hasta cinco familiares, según los ajustes de compras compartidas '
 'de Apple. Cada persona conserva sus propios datos: no se comparten automáticamente extractos, gastos ni '
 'documentos.'),
  compat_h='Comprueba tu dispositivo',
  compat_p=('Requiere iOS o iPadOS 27 o posterior. Las funciones del modelo local necesitan un dispositivo compatible '
 'con Apple Intelligence, con el servicio activado y el modelo disponible en el idioma elegido. Sin él, '
 'puedes guardar y consultar documentos y usar la lectura de texto y las reglas; algunas preguntas y '
 'funciones de IA no estarán disponibles.')),
"ca": dict(
  h1a='El que pagues. El que es renova. ', h1b='El que no vols oblidar.',
  sub=('Reuneix contractes, assegurances i tiquets. Troba el proper pagament, tingues una garantia a mà i rep '
 'avisos abans que s’acabi un termini. Al teu iPhone i iPad, sense connectar el banc.'),
  badges=["IA al dispositiu", "Sense compte", "Sense servidors nostres", "Sense rastrejadors"],

  ai_k="Pregunta", ai_h='Pregunta sobre les teves despeses. Amb les teves dades.',
  ai_p=('L’app calcula les xifres a partir dels teus registres; el model d’Apple les explica al dispositiu. '
 'Comprova els documents llegits: poden contenir errors, i els càrrecs futurs són previsions. Una pregunta '
 'sobre llocs pot consultar Apple Maps per situar un lloc, sense enviar els teus imports ni extractes.'),
  chat=[("Quant hem gastat en restaurants aquest any?", "724,68 € en 7 pagaments. Sobretot a El Celler (210 €), La Taverna del Pla (173 €) i Bar Ponent (98 €)."),
        ("On em van encantar les braves?", "La Taverna del Pla (Barcelona): ★★★★★, 9 d'ag. 2026."),
        ("I a Sant Cugat?", "No hi ha braves a Sant Cugat als teus tiquets. On sí que les has pres: La Taverna del Pla.")],
  ai_net='Càlculs financers', ai_model='IA', ai_model_v='Local',
  story_k="Recorregut", story_h='Tres moments en què t’ajuda',
  priv_n=[('0', 'comptes de Tiquet'),
 ('0', 'servidors nostres'),
 ('0', 'rastrejadors'),
 ('0', 'documents enviats a una IA remota')],
  more_k="I a més", more_h="%d coses més que fa", more_all="Llegir-les totes",
  primary_cta='Veure Gratis i Plus',
  ai_net_v='Al teu dispositiu',
  demo_note=('Conversa i pantalles amb dades fictícies. Les respostes depenen dels registres desats i de la '
 'disponibilitat d’Apple Intelligence.'),
  tour=[('contracts',
  'Abans que es renovi l’assegurança',
  'La pòlissa, el preu i l’últim dia per donar-la de baixa, en una fitxa. Un avís et dona temps per revisar '
  'el contracte.'),
 ('coming',
  'Abans del proper càrrec',
  'Consulta què es preveu cobrar i quan, segons els contractes i els pagaments anteriors. Les previsions '
  'indiquen en què es basen. Inclòs a Plus.'),
 ('home',
  'Quan necessites tornar alguna cosa',
  'Guarda el tiquet i consulta el termini de devolució o la garantia. Conserva el document original i revisa '
  'la data llegida.')],
  price_k='Gratis i Plus',
  price_h='Comença gratis. Amplia quan et compensi.',
  free_h='Tiquet Gratis',
  free_price='0 €',
  free_note='Sense límit de temps',
  free_items=['Tiquets, garanties, contractes i recordatoris',
 'Full de casa i detecció de càrrecs inusuals',
 'Còpies de seguretat i iCloud opcional',
 '5 preguntes al dia per dispositiu sobre funcions gratuïtes'],
  plus_h='Tiquet Plus',
  plus_price='9,99 €',
  plus_note='Preu de llançament a Espanya · pagament únic',
  plus_items=['Tot el de Gratis',
 'Revisió de despeses, ingressos, comptes i objectius d’estalvi',
 'Propers càrrecs a 12 mesos i El Mes',
 'Llocs a partir dels extractes',
 'Preguntes sense límit diari',
 'Compra compatible amb En Família'],
  trial_h='Prova Plus gratis durant 14 dies',
  trial_p=('Sense renovació automàtica ni càrrecs quan s’acaba. Després continues amb Gratis i conserves el que hagis '
 'desat. La prova és individual; comprar Plus és opcional.'),
  family_note=('En Família comparteix la compra de Plus amb fins a cinc familiars, segons els ajustos de compres '
 'compartides d’Apple. Cada persona conserva les seves dades: no es comparteixen automàticament extractes, '
 'despeses ni documents.'),
  compat_h='Comprova el teu dispositiu',
  compat_p=('Requereix iOS o iPadOS 27 o posterior. Les funcions del model local necessiten un dispositiu compatible '
 'amb Apple Intelligence, amb el servei activat i el model disponible en l’idioma triat. Sense això, pots '
 'desar i consultar documents i fer servir el reconeixement de text i les regles; algunes preguntes i '
 'funcions d’IA no estaran disponibles.')),
}
for _l in X: S[_l].update(X[_l])

# How things get in, and what sits on the Home Screen (owner, 2026-09-28: "do we explain the widgets and that you can
# send files from mail attachments or the phone to Tiquet?"). Drawn in HTML: a capture of the share sheet or of real
# widgets would show someone's data; these show the sample household's.
X3 = {
"es": dict(
  in_k="Cómo entra todo", in_h="Desde donde ya está: el correo, Archivos, Fotos",
  in_p="La póliza que te mandaron por correo, la factura en PDF, la foto de un tique, el extracto que bajas de tu banco: mantenlo pulsado, toca Compartir y elige Tiquet. Hasta 20 a la vez. Se lee en el dispositivo y ves lo que ha entendido antes de guardar nada.",
  sources=[("✉️","Mail","un adjunto"),("📁","Archivos","PDF, Excel, CSV"),("🖼️","Fotos","foto o captura"),("📷","Cámara","escanea un tique"),("🏦","Tu banco","el extracto, sin contraseña"),("📲","AirDrop","el archivo de casa")],
  steps3=["Mantén pulsado el adjunto","Toca Compartir","Elige Tiquet"], share_to="Compartir con",
  outs=[("Una póliza","su ficha: número, prima, qué cubre, a quién llamar"),("Un tique","el gasto, la devolución y la garantía"),("Un extracto","tus movimientos, cada pago una vez")],
  w_k="En la pantalla de inicio", w_h="Lo importante, sin abrir la app",
  w_p="Cinco widgets: el mes, el próximo cargo, tus seguros a mano el día que pasa algo, tus buenos sitios cerca y la lista de la compra, que tachas sin abrir la app. Un botón en el Centro de control para escanear un tique. Y Siri, que sabe cuándo se renueva cada contrato.",
  wg=dict(month="Este mes", month_v="2.291 €", month_s="≈ 2.440 € a fin de mes", next="Próximo cargo", next_v="9,99 €", next_s="Seguro móvil · 2 oct", week="Esta semana: 132 €",
          ins="Seguros a mano", ins_rows=[("Hogar","Póliza 1234-5678","900 000 000"),("Coche","Póliza 8765-4321","900 000 001")],
          near="Buenos sitios cerca", near_rows=[("La Taverna del Pla","★★★★★","350 m"),("Bar Ponent","★★★★★","1,2 km")],
          ctl="Añadir un tique", siri="«Oye Siri, ¿cuándo se renueva el seguro de hogar en Tiquet?»", demo="Datos de ejemplo")),
"ca": dict(
  in_k="Com hi entra tot", in_h="Des d'on ja és: el correu, Fitxers, Fotos",
  in_p="La pòlissa que et van enviar per correu, la factura en PDF, la foto d'un tiquet, l'extracte que baixes del teu banc: mantén-ho premut, toca Compartir i tria Tiquet. Fins a 20 alhora. Es llegeix al dispositiu i veus què ha entès abans de desar res.",
  sources=[("✉️","Mail","un adjunt"),("📁","Fitxers","PDF, Excel, CSV"),("🖼️","Fotos","foto o captura"),("📷","Càmera","escaneja un tiquet"),("🏦","El teu banc","l'extracte, sense contrasenya"),("📲","AirDrop","el fitxer de casa")],
  steps3=["Mantén premut l'adjunt","Toca Compartir","Tria Tiquet"], share_to="Compartir amb",
  outs=[("Una pòlissa","la seva fitxa: número, prima, què cobreix, a qui trucar"),("Un tiquet","la despesa, la devolució i la garantia"),("Un extracte","els teus moviments, cada pagament una vegada")],
  w_k="A la pantalla d'inici", w_h="El que importa, sense obrir l'app",
  w_p="Cinc ginys: el mes, el proper càrrec, les teves assegurances a mà el dia que passa alguna cosa, els teus bons llocs a prop i la llista de la compra, que ratlles sense obrir l’app. Un botó al Centre de control per escanejar un tiquet. I Siri, que sap quan es renova cada contracte.",
  wg=dict(month="Aquest mes", month_v="2.291 €", month_s="≈ 2.440 € a final de mes", next="Proper càrrec", next_v="9,99 €", next_s="Assegurança mòbil · 2 oct.", week="Aquesta setmana: 132 €",
          ins="Assegurances a mà", ins_rows=[("Llar","Pòlissa 1234-5678","900 000 000"),("Cotxe","Pòlissa 8765-4321","900 000 001")],
          near="Bons llocs a prop", near_rows=[("La Taverna del Pla","★★★★★","350 m"),("Bar Ponent","★★★★★","1,2 km")],
          ctl="Afegir un tiquet", siri="«Oye Siri, ¿cuándo se renueva el seguro de hogar en Tiquet?»", demo="Dades d'exemple")),
"en": dict(
  in_k="How things get in", in_h="From wherever it already is: Mail, Files, Photos",
  in_p="The policy they emailed you, the invoice as a PDF, a photo of a receipt, the statement you download from your bank: press and hold, tap Share and pick Tiquet. Up to 20 at once. It is read on the device, and you see what it understood before anything is saved.",
  sources=[("✉️","Mail","an attachment"),("📁","Files","PDF, Excel, CSV"),("🖼️","Photos","a photo or screenshot"),("📷","Camera","scan a receipt"),("🏦","Your bank","the statement, no password"),("📲","AirDrop","the household file")],
  steps3=["Press and hold the attachment","Tap Share","Pick Tiquet"], share_to="Share with",
  outs=[("A policy","its card: number, premium, what it covers, who to call"),("A receipt","the spending, the return and the warranty"),("A statement","your payments, each one once")],
  w_k="On your Home Screen", w_h="What matters, without opening the app",
  w_p="Five widgets: the month, the next charge, your insurance at hand the day something happens, your good places nearby, and the shopping list, ticked off without opening the app. A Control Centre button to scan a receipt. And Siri, which knows when each contract renews.",
  wg=dict(month="This month", month_v="€2,291", month_s="≈ €2,440 by month end", next="Next charge", next_v="€9.99", next_s="Phone insurance · 2 Oct", week="This week: €132",
          ins="Insurance at hand", ins_rows=[("Home","Policy 1234-5678","900 000 000"),("Car","Policy 8765-4321","900 000 001")],
          near="Good places near you", near_rows=[("La Taverna del Pla","★★★★★","350 m"),("Bar Ponent","★★★★★","1.2 km")],
          ctl="Add a receipt", siri="“Hey Siri, when does the home insurance renew in Tiquet?”", demo="Sample data")),
}
for _l in X3: S[_l].update(X3[_l])

# The basket and the shopping list (owner, 2026-10-03: "show the shopping list and how prices move"), and several
# files at once: bank statements are imported one after another, in the order sent.
X4 = {
"es": dict(
  bk_k="La cesta", bk_h="Lo que sube en tu súper, y la lista de lo que te toca comprar",
  bk_p="Cada tique del súper guarda sus artículos con su precio. Tiquet compara lo mismo en la misma tienda y te dice cuánto ha subido tu cesta habitual, qué producto sube más y dónde lo tienes más barato.",
  bk_l=["Tu cesta habitual, comparada con la de hace meses", "Precio por unidad, o por kilo si se pesa", "El mismo producto, más barato en tu otro súper",
        "Lista de la compra con lo que te toca reponer", "Escribe tres letras y te sugiere lo que ya compraste", "En el súper vas tachando y ves cuánto falta"],
  bk_alt1="La cesta: tu cesta habitual sube un 14,4 % y los productos que más suben", bk_alt2="Lista de la compra en forma de tique, con un artículo tachado",
  in_p="La póliza que te mandaron por correo, la factura en PDF, la foto de un tique, los extractos que bajas de tu banco: mantenlos pulsados, toca Compartir y elige Tiquet. Hasta 20 a la vez: los lee uno tras otro, en el orden en que los mandas. Todo se lee en el dispositivo.",
  faq_more=[("¿Puedo mandar varios archivos a la vez?", "Sí, hasta 20 en cada envío: fotos, PDF y extractos del banco en CSV o Excel. Al abrir Tiquet los lee en el orden en que los mandaste; los extractos, uno detrás de otro, y lo que ya estaba no se duplica. Si tu banco solo exporta un año cada vez, manda un archivo por año.")]),
"en": dict(
  bk_k="The basket", bk_h="What goes up at your supermarket, and the list of what you need",
  bk_p="Every supermarket receipt keeps its items and their prices. Tiquet compares the same thing at the same shop and tells you how much your usual basket has gone up, which product rises most and where it is cheaper.",
  bk_l=["Your usual basket, against months ago", "Price per unit, or per kilo when weighed", "The same product, cheaper at your other supermarket",
        "A shopping list with what is due again", "Type three letters and it suggests what you bought before", "In the shop, tick things off and see what is left"],
  bk_alt1="The basket: your usual basket is up 14.4 % and the products rising most", bk_alt2="Shopping list as a till receipt, one item ticked off",
  in_p="The policy you were emailed, the PDF invoice, a photo of a receipt, the statements you download from your bank: press and hold, tap Share and choose Tiquet. Up to 20 at once: it reads them one after another, in the order you sent them. Everything is read on the device.",
  faq_more=[("Can I send several files at once?", "Yes, up to 20 each time: photos, PDFs and bank statements in CSV or Excel. When you open Tiquet it reads them in the order you sent them; statements one after another, and nothing already there is added twice. If your bank exports one year at a time, send one file per year.")]),
"ca": dict(
  bk_k="La cistella", bk_h="El que puja al teu súper, i la llista del que t'has de comprar",
  bk_p="Cada tiquet del súper guarda els seus articles amb el preu. Tiquet compara el mateix a la mateixa botiga i et diu quant ha pujat la teva cistella habitual, quin producte puja més i on el tens més barat.",
  bk_l=["La teva cistella habitual, comparada amb la de fa mesos", "Preu per unitat, o per quilo si es pesa", "El mateix producte, més barat a l'altre súper",
        "Llista de la compra amb el que t'has de reposar", "Escriu tres lletres i et suggereix el que ja vas comprar", "Al súper vas ratllant i veus quant falta"],
  bk_alt1="La cistella: la teva cistella habitual puja un 14,4 % i els productes que més pugen", bk_alt2="Llista de la compra en forma de tiquet, amb un article ratllat",
  in_p="La pòlissa que et van enviar per correu, la factura en PDF, la foto d'un tiquet, els extractes que baixes del banc: mantén-los premuts, toca Comparteix i tria Tiquet. Fins a 20 alhora: els llegeix un rere l'altre, en l'ordre en què els envies. Tot es llegeix al dispositiu.",
  faq_more=[("Puc enviar diversos fitxers alhora?", "Sí, fins a 20 cada vegada: fotos, PDF i extractes del banc en CSV o Excel. Quan obres Tiquet els llegeix en l'ordre en què els vas enviar; els extractes, un rere l'altre, i el que ja hi era no es duplica. Si el banc només exporta un any cada vegada, envia un fitxer per any.")]),
}
for _l in X4:
    _faq = X4[_l].pop("faq_more")
    S[_l].update(X4[_l])
    S[_l]["faqs"] = S[_l]["faqs"] + _faq

# Live on the App Store (Spain first).
X5 = {"es": dict(store_cta="Descargar en el App Store", store_note="Gratis · App Store de España"),
      "en": dict(store_cta="Download on the App Store", store_note="Free · App Store in Spain"),
      "ca": dict(store_cta="Descarrega a l'App Store", store_note="Gratis · App Store d'Espanya")}
for _l in X5: S[_l].update(X5[_l])


# Spanish at the root: the App Store starts in Spain (owner, 2026-09-28). English at /en/, Catalan at /ca/.
# The guide: how each part works, one section per part (guide.py holds the words, per language).
sys.path.insert(0, ROOT)
try:
    from guide import GUIDE
except ImportError:
    GUIDE = {}
GUIDE_NAV = {"es": "Cómo funciona", "ca": "Com funciona", "en": "How it works"}

HOME = "es"
ORDER = ["es", "ca", "en"]                        # as the switcher shows them
def root(lang, depth): return "../" * (depth + (0 if lang == HOME else 1))
def page_url(lang, page=""): return "/" + ("" if lang == HOME else lang + "/") + (page + "/" if page else "")
def switcher(lang, page=""):
    """ES · CA · EN at the top of every page, the current one lit; each goes to the same page in that language."""
    there = lambda l: page if page != "guia" or l in GUIDE else ""      # the guide only where it is written
    return '<div class="langs">' + "".join('<a href="%s" lang="%s" hreflang="%s"%s>%s</a>' % (page_url(l, there(l)), l, l, ' class="on" aria-current="true"' if l == lang else "", l.upper()) for l in ORDER) + '</div>'

def head(t, lang, title, depth, page=""):
    r = root(lang, depth)
    alts = "".join('<link rel="alternate" hreflang="%s" href="https://tiquet.securlabs.net%s">' % (l, page_url(l, page)) for l in LANGS if page != "guia" or l in GUIDE)
    alts += '<link rel="alternate" hreflang="x-default" href="https://tiquet.securlabs.net%s">' % page_url(HOME, page)
    alts += '<link rel="canonical" href="https://tiquet.securlabs.net%s"><meta property="og:url" content="https://tiquet.securlabs.net%s">' % (page_url(lang, page), page_url(lang, page))
    return ('<!doctype html><html lang="%s"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><meta name="description" content="%s"><meta property="og:title" content="%s"><meta property="og:description" content="%s">'
            '<meta property="og:image" content="https://tiquet.securlabs.net/img/s/home-%s.jpg"><link rel="icon" href="%simg/icon.png">%s'
            '<link rel="stylesheet" href="%sstyle.css?v=%d"><script>document.documentElement.classList.add("js")</script></head><body>') % (lang, html.escape(title), html.escape(t["desc"]), html.escape(title), html.escape(t["desc"]), "en" if lang == "en" else "es", r, alts, r, CSS_VERSION)

def nav(t, lang, depth, landing, page=""):
    r = root(lang, depth); home = page_url(lang)
    links = "".join('<a class="opt" href="%s%s">%s</a>' % ("" if landing else home, a, html.escape(n)) for a, n in t["nav"])
    if lang in GUIDE: links += '<a class="opt%s" href="%s">%s</a>' % (" on" if page == "guia" else "", page_url(lang, "guia"), html.escape(GUIDE_NAV[lang]))
    return '<nav><div class="wrap"><a class="brand" href="%s"><img src="%simg/icon.png" alt="">Tiquet</a><div class="links">%s<a href="%s">%s</a></div>%s</div></nav>' % (home, r, links, page_url(lang, "support"), html.escape(t["f_support"]), switcher(lang, page))

def footer(t, lang, page=""):
    langs = "".join('<a href="%s">%s</a>' % (page_url(l, page if page != "guia" or l in GUIDE else ""), S[l]["name_lang"]) for l in LANGS if l != lang)
    guide = '<a href="%s">%s</a>' % (page_url(lang, "guia"), html.escape(GUIDE_NAV[lang])) if lang in GUIDE else ""
    return ('<footer><div class="wrap"><span>© 2026 Tiquet</span>' + guide + '<a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a><a href="mailto:%s">%s</a><span class="langs">%s</span></div></footer></body></html>'
            % (page_url(lang, "privacy"), t["f_privacy"], page_url(lang, "support"), t["f_support"], page_url(lang, "terms"), t["f_terms"], EMAIL, t["f_contact"], langs))

def cards(items): return '<div class="grid">' + "".join('<div class="card %s"><span class="tag"></span><h3>%s</h3><p>%s</p></div>' % (c, html.escape(h), html.escape(p)) for h, p, c in items) + '</div>'
def checks(items, cls="check"): return '<ul class="check %s">%s</ul>' % (cls if cls != "check" else "", "".join("<li>%s</li>" % html.escape(i) for i in items))

def landing(t, lang):
    r = root(lang, 0); e = html.escape; shot = lambda n: "%simg/s/%s-%s.jpg" % (r, n, "en" if lang == "en" else "es")
    out = head(t, lang, t["title"], 0) + nav(t, lang, 0, True)
    # Hero: the promise, the four refusals, and the phone with what it is doing right now.
    out += ('<header class="hero-x"><div class="wrap hero"><div class="reveal"><h1>%s<em>%s</em></h1><p class="sub">%s</p>'
            '<ul class="badges">%s</ul><div class="hero-actions">%s</div><p class="note">%s</p></div>'
            '<div class="stage reveal"><div class="shot phone"><img src="%s" alt="" loading="eager"></div>'
            '<div class="float f1"><span class="dot"></span>%s · <b>%s</b></div><div class="float f2">%s · <b>%s</b></div></div></div></header>'
            ) % (e(t["h1a"]), e(t["h1b"]), e(t["sub"]), "".join("<li>%s</li>" % e(b) for b in t["badges"]),
                 ('<a class="pill" href="%s">%s</a><a class="pill ghost" href="#pricing">%s</a><span class="release-note">%s</span>' % (e(APP_STORE), e(t["store_cta"]), e(t["primary_cta"]), e(t["store_note"])))
                 if APP_STORE else ('<a class="pill" href="#pricing">%s</a><span class="release-note">%s</span>' % (e(t["primary_cta"]), e(t["cta"]))), e(t["note"]),
                 shot("home"), e(t["ai_model"]), e(t["ai_model_v"]), e(t["ai_net"]), e(t["ai_net_v"]))
    # Ask: a conversation that writes itself when it comes into view; all figures are invented examples.
    chat = "".join('<div class="msg q">%s</div><div class="msg a"><span class="spark"></span><span class="txt">%s</span></div>' % (e(q), e(a)) for q, a in t["chat"])
    ask_section = ('<section id="ai"><div class="wrap split"><div class="reveal"><span class="kicker">%s</span><h2>%s</h2><p class="lead">%s</p>'
            '<div class="meters"><div><span>%s</span><b class="zero">%s</b></div><div><span>%s</span><b>%s</b></div></div></div>'
            '<div><div class="chat reveal" data-chat>%s</div><p class="note">%s</p></div></div></section>') % (e(t["ai_k"]), e(t["ai_h"]), e(t["ai_p"]), e(t["ai_net"]), e(t["ai_net_v"]), e(t["ai_model"]), e(t["ai_model_v"]), chat, e(t["demo_note"]))
    # A tour: one phone stays while the words scroll past it, and it changes screen with each one.
    f = t["feats"]
    steps = t["tour"]
    phones = "".join('<img src="%s" alt="" loading="lazy" data-i="%d"%s>' % (shot(n), i, ' class="on"' if i == 0 else "") for i, (n, _, _) in enumerate(steps))
    words = "".join('<div class="step%s" data-i="%d"><span class="num">%02d</span><h3>%s</h3><p>%s</p><img class="inline" src="%s" alt="" loading="lazy"></div>'
                    % (" on" if i == 0 else "", i, i + 1, e(h), e(p), shot(n)) for i, (n, h, p) in enumerate(steps))
    out += ('<section id="story"><div class="wrap"><span class="kicker reveal">%s</span><h2 class="reveal">%s</h2>'
            '<div class="tour"><div class="steps">%s</div><div class="pin"><div class="shot phone">%s</div></div></div></div></section>') % (e(t["story_k"]), e(t["story_h"]), words, phones)
    # The comparison is visible before the longer feature tour; no purchase CTA before release.
    out += ('<section id="pricing" class="glow"><div class="wrap"><span class="kicker">%s</span><h2>%s</h2>'
            '<div class="plans"><article class="plan"><h3>%s</h3><p class="price">%s</p><p class="plan-note">%s</p>%s</article>'
            '<article class="plan plus"><h3>%s</h3><p class="price">%s</p><p class="plan-note">%s</p>%s</article></div>'
            '<div class="trial"><h3>%s</h3><p>%s</p></div><p class="family-note">%s</p>'
            '<div class="compat"><h3>%s</h3><p>%s</p></div></div></section>') % (
                e(t["price_k"]), e(t["price_h"]), e(t["free_h"]), e(t["free_price"]), e(t["free_note"]), checks(t["free_items"]),
                e(t["plus_h"]), e(t["plus_price"]), e(t["plus_note"]), checks(t["plus_items"]),
                e(t["trial_h"]), e(t["trial_p"]), e(t["family_note"]), e(t["compat_h"]), e(t["compat_p"]))
    out += ask_section
    # How things get in: the sources flow into Tiquet; the share sheet in three steps; what each file becomes.
    src = "".join('<div class="src reveal"><span class="ico">%s</span><b>%s</b><small>%s</small></div>' % (i, e(n), e(d)) for i, n, d in t["sources"])
    sheet = ('<div class="sheet reveal"><div class="att"><span class="pdf">PDF</span><div><b>poliza-hogar.pdf</b><small>184 KB</small></div></div>'
             '<div class="to">%s</div><div class="apps"><span class="app">✉️</span><span class="app">💬</span><span class="app tq"><img src="%simg/icon.png" alt=""><i>Tiquet</i></span><span class="app">📁</span></div>'
             '<ol class="how3">%s</ol></div>') % (e(t["share_to"]), r, "".join("<li>%s</li>" % e(x) for x in t["steps3"]))
    outs = "".join('<div class="out reveal"><b>%s →</b> %s</div>' % (e(a), e(b)) for a, b in t["outs"])
    out += ('<section id="in"><div class="wrap"><span class="kicker reveal">%s</span><h2 class="reveal">%s</h2><p class="lead reveal">%s</p>'
            '<div class="flow"><div class="srcs">%s</div><div class="into"><span class="beam"></span><img src="%simg/icon.png" alt="Tiquet"><span class="beam b2"></span></div>%s</div>'
            '<div class="outs">%s</div></div></section>') % (e(t["in_k"]), e(t["in_h"]), e(t["in_p"]), src, r, sheet, outs)
    # The basket and the shopping list: two phones, the sample household's prices.
    out += ('<section id="basket"><div class="wrap split"><div class="reveal"><span class="kicker">%s</span><h2>%s</h2><p class="lead">%s</p>%s</div>'
            '<div class="duo reveal"><div class="shot phone"><img src="%s" alt="%s" loading="lazy"></div><div class="shot phone"><img src="%s" alt="%s" loading="lazy"></div></div></div></section>'
            ) % (e(t["bk_k"]), e(t["bk_h"]), e(t["bk_p"]), checks(t["bk_l"]), shot("basket"), e(t["bk_alt1"]), shot("list"), e(t["bk_alt2"]))
    # The Home Screen: the four widgets, the Control Centre button and Siri, drawn with the sample household's figures.
    w = t["wg"]
    widgets = ('<div class="home reveal"><span class="demo">%s</span>'
               '<div class="wd s"><small>%s</small><b>%s</b><i>%s</i><span class="ring"></span></div>'
               '<div class="wd s"><small>%s</small><b>%s</b><i>%s</i><i class="dim">%s</i></div>'
               '<div class="wd m"><small>%s</small>%s</div>'
               '<div class="wd m"><small>%s</small>%s</div>'
               '<div class="ctl"><span>📷</span><i>%s</i></div><div class="siri">%s</div></div>') % (
        e(w["demo"]), e(w["month"]), e(w["month_v"]), e(w["month_s"]), e(w["next"]), e(w["next_v"]), e(w["next_s"]), e(w["week"]),
        e(w["ins"]), "".join('<div class="row"><b>%s</b><span>%s</span><em>☎ %s</em></div>' % (e(a), e(b), e(c)) for a, b, c in w["ins_rows"]),
        e(w["near"]), "".join('<div class="row"><b>%s</b><span class="stars">%s</span><em>%s</em></div>' % (e(a), e(b), e(c)) for a, b, c in w["near_rows"]),
        e(w["ctl"]), e(w["siri"]))
    out += ('<section id="widgets"><div class="wrap split"><div class="reveal"><span class="kicker">%s</span><h2>%s</h2><p class="lead">%s</p></div>%s</div></section>'
            % (e(t["w_k"]), e(t["w_h"]), e(t["w_p"]), widgets))
    # Horizon: the phone turned, as wide as the page.
    out += ('<section id="horizon"><div class="wrap"><div class="reveal"><span class="kicker">%s</span><h2>%s</h2><p class="lead">%s</p></div>'
            '<div class="wide reveal"><img src="%s" alt="" loading="lazy"></div>%s</div></section>') % (e(t["hz_k"]), e(t["hz_h"]), e(t["hz_p"]), shot("horizon"), checks(t["hz_l"], "check row"))
    # Privacy: in numbers first, then where it is, what never happens, and the little that leaves.
    nums = "".join('<div class="n reveal"><b>%s</b><span>%s</span></div>' % (e(a), e(b)) for a, b in t["priv_n"])
    out += ('<section id="privacy" class="glow"><div class="wrap"><span class="kicker reveal">%s</span><h2 class="reveal">%s</h2><p class="lead reveal">%s</p><div class="nums">%s</div>'
            '<div class="cols"><div class="reveal"><h3>%s</h3>%s</div><div class="reveal"><h3>%s</h3>%s</div><div class="reveal"><h3>%s</h3>%s</div></div>'
            '<p class="note"><a href="%s">%s →</a></p></div></section>') % (e(t["priv_k"]), e(t["priv_h"]), e(t["priv_p"]), nums, e(t["where_h"]), checks(t["where"]),
                                                                    e(t["never_h"]), checks(t["never"], "never"), e(t["leaves_h"]), checks(t["leaves"]), page_url(lang, "privacy"), e(t["privacy_t"]))
    # The family's papers, as rows.
    out += ('<section id="family"><div class="wrap split"><div class="reveal"><span class="kicker">%s</span><h2>%s</h2><p class="lead">%s</p></div><div class="rows">%s</div></div></section>'
            % (e(t["fam_k"]), e(t["fam_h"]), e(t["fam_p"]), "".join('<div class="row reveal"><h3>%s</h3><p>%s</p></div>' % (e(h), e(p)) for h, p, _ in t["fam"])))
    # Everything else: a strip that moves, and the whole list one tap away.
    shown = [x for i, x in enumerate(f) if i not in (8, 9)]   # Ask and widgets have their own sections
    shown += [(t["wk_h"], t["wk_p"], "c-sea"), (t["month_h"], t["month_p"], "c-wine")]
    chips = "".join("<span>%s</span>" % e(h) for h, _, _ in shown)
    out += ('<section id="more"><div class="wrap"><span class="kicker reveal">%s</span><h2 class="reveal">%s</h2></div>'
            '<div class="marquee" aria-hidden="true"><div class="track">%s%s</div></div><div class="marquee rev" aria-hidden="true"><div class="track">%s%s</div></div>'
            '<div class="wrap"><details class="all"><summary>%s</summary><div class="list">%s</div></details></div></section>'
            ) % (e(t["more_k"]), e(t["more_h"] % len(shown)), chips, chips, chips[::1], chips, e(t["more_all"]),
                 "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(h), e(p)) for h, p, _ in shown))
    # How it starts: a line of four.
    more = ('<p class="guide-link reveal"><a class="pill ghost" href="%s">%s →</a></p>' % (page_url(lang, "guia"), e(GUIDE[lang]["cta"]))) if lang in GUIDE else ""
    out += ('<section id="start"><div class="wrap"><span class="kicker reveal">%s</span><h2 class="reveal">%s</h2><ol class="timeline">%s</ol>%s</div></section>'
            % (e(t["how_k"]), e(t["how_h"]), "".join('<li class="reveal"><h3>%s</h3><p>%s</p></li>' % (e(h), e(p)) for h, p in t["steps"]), more))
    out += '<section id="faq"><div class="wrap"><span class="kicker">%s</span><h2>%s</h2>%s</div></section>' % (e(t["faq_k"]), e(t["faq_h"]), "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in t["faqs"]))
    return out.replace("</body>", "") + footer(t, lang).replace("</body>", CAMPAIGN + '<script src="%ssite.js?v=%d" defer></script></body>' % (r, CSS_VERSION))

def doc(t, lang, page, title, body):
    return head(t, lang, title, 1, page) + nav(t, lang, 1, False, page) + '<div class="wrap doc"><h1>%s</h1><p class="date">%s</p>%s</div>' % (html.escape(title), UPDATED[lang], body) + footer(t, lang, page)

# The index lights the part being read.
GUIDE_SPY = ('<script>(function(){var l=document.querySelectorAll(".gtoc a"),m={};l.forEach(function(a){m[a.getAttribute("href").slice(1)]=a});'
             'if(!("IntersectionObserver" in window))return;var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&m[e.target.id]){'
             'l.forEach(function(a){a.classList.remove("on")});m[e.target.id].classList.add("on")}})},{rootMargin:"-30% 0px -60% 0px"});'
             'document.querySelectorAll(".gpart[id]").forEach(function(s){o.observe(s)})})()</script>')

def guide(t, lang):
    """How it works: an index, then each part as what it does for you, how, tips and questions, beside its screen."""
    g = GUIDE[lang]; e = html.escape; r = root(lang, 1)
    shot = lambda n: "%simg/s/%s-%s.jpg" % (r, n, "en" if lang == "en" else "es")
    badge = lambda s: '<span class="tier %s">%s</span>' % (s["tier"], e(g[s["tier"]])) + ('<span class="tier v11">%s</span>' % e(g["v11"]) if s.get("v11") else "")
    toc = "".join('<li><a href="#%s">%s</a></li>' % (s["id"], e(s["short"])) for s in g["sections"])
    parts = ""
    for s in g["sections"]:
        body = '<p class="hook">%s</p>' % e(s["hook"])
        if s.get("steps"): body += '<h3>%s</h3><ol class="howto">%s</ol>' % (e(g["steps_h"]), "".join("<li>%s</li>" % e(x) for x in s["steps"]))
        if s.get("tips"): body += '<h3>%s</h3>%s' % (e(g["tips_h"]), checks(s["tips"]))
        if s.get("faq"): body += '<h3>%s</h3>%s' % (e(g["faq_h"]), "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in s["faq"]))
        pic = '<div class="gshot"><div class="shot phone"><img src="%s" alt="" loading="lazy"></div></div>' % shot(s["shot"]) if s.get("shot") else ""
        parts += '<section class="gpart" id="%s"><div class="ghead">%s<h2>%s</h2></div><div class="gbody%s"><div class="gtext">%s</div>%s</div></section>' % (
            s["id"], badge(s), e(s["title"]), " has-shot" if pic else "", body, pic)
    store = '<a class="pill" href="%s">%s</a>' % (e(APP_STORE), e(t["store_cta"])) if APP_STORE else ""
    return (head(t, lang, g["title"], 1, "guia") + nav(t, lang, 1, False, "guia")
            + '<header class="wrap ghero"><span class="kicker">%s</span><h1>%s</h1><p class="lead">%s</p></header>' % (e(g["kicker"]), e(g["h1"]), e(g["intro"]))
            + '<div class="wrap guide"><aside class="gtoc"><nav aria-label="%s"><b>%s</b><ol>%s</ol></nav></aside><div class="gparts">%s'
              '<section class="gpart gend"><h2>%s</h2><p>%s</p><div class="hero-actions">%s<a class="pill ghost" href="%s">%s</a></div></section></div></div>'
              % (e(g["toc"]), e(g["toc"]), toc, parts, e(g["outro_h"]), e(g["outro_p"]), store, page_url(lang, "support"), e(t["f_support"]))
            + footer(t, lang, "guia").replace("</body>", GUIDE_SPY + CAMPAIGN + "</body>"))

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)

for lang in LANGS:
    t = S[lang]; d = ROOT if lang == HOME else os.path.join(ROOT, lang)
    write(os.path.join(d, "index.html"), landing(t, lang))
    write(os.path.join(d, "privacy", "index.html"), doc(t, lang, "privacy", t["privacy_t"], "".join("<h2>%s</h2><p>%s</p>" % (html.escape(h), p) for h, p in t["privacy_b"])))
    write(os.path.join(d, "support", "index.html"), doc(t, lang, "support", t["support_t"], "<p>%s</p><h2>%s</h2>%s" % (t["support_p"], html.escape(t["support_h"]), "".join("<details><summary>%s</summary><p>%s</p></details>" % (html.escape(q), html.escape(a)) for q, a in t["support_faq"]))))
    if lang in GUIDE: write(os.path.join(d, "guia", "index.html"), guide(t, lang))
    write(os.path.join(d, "terms", "index.html"), doc(t, lang, "terms", t["terms_t"], "".join("<h2>%s</h2><p>%s</p>" % (html.escape(h), p) for h, p in t["terms_b"])))
# The Spanish pages lived at /es/ for a day: those addresses now lead to the same page at the root.
for page in ["", "privacy", "support", "terms"]:
    to = page_url(HOME, page)
    write(os.path.join(ROOT, "es", page, "index.html") if page else os.path.join(ROOT, "es", "index.html"),
          '<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Tiquet</title><link rel="canonical" href="https://tiquet.securlabs.net%s">'
          '<meta http-equiv="refresh" content="0; url=%s"></head><body><a href="%s">Tiquet</a></body></html>' % (to, to, to))
print("built", len(LANGS), "languages")
