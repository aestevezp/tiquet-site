# -*- coding: utf-8 -*-
# Tiquet, "Com funciona" guide, Catalan. Translated from guide_es.py. The app has no Catalan interface yet,
# so every UI name in «» is kept exactly as the app shows it in Spanish (Scripts/es_translations.py).

GUIDE_CA = {
    "title": "Com funciona Tiquet",
    "kicker": "Guia",
    "h1": "Com funciona Tiquet, part per part",
    "intro": (
        "Què fa per tu cada part de l’app, com es fa servir i uns quants trucs per treure’n profit. "
        "El que està marcat com a Plus necessita Tiquet Plus o la seva prova de 14 dies. "
        "El que està marcat «Des de la versió 1.1» arriba amb aquesta actualització. "
        "L’app encara no està en català: els noms dels botons apareixen en castellà, tal com els veuràs."
    ),
    "toc": "En aquesta guia",
    "cta": "Mira com funciona cada part",
    "free": "Gratis", "plus": "Plus", "mix": "Gratis i Plus", "v11": "Des de la versió 1.1",
    "steps_h": "Com es fa", "tips_h": "Trucs", "faq_h": "Preguntes",
    "sections": [
        {
            "id": "empezar",
            "title": "Primers passos",
            "short": "Primers passos",
            "tier": "free",
            "v11": False,
            "shot": "home",
            "hook": (
                "Tiquet guarda el que casa teva té contractat, el que paga i el que caduca, i t’avisa abans que "
                "un termini et costi diners. No necessites compte ni connectar el banc: n’hi ha prou amb els teus papers."
            ),
            "steps": [
                "Necessites un iPhone o un iPad amb iOS o iPadOS 27. L’app està en castellà i en anglès.",
                "Per veure-la plena abans de posar-hi res teu, toca «Probar con datos de ejemplo» a l’Inici buit o a «Ajustes». És una casa inventada que no toca les teves dades; en surts amb «Salir».",
                "Comença pel que més t’importa: una assegurança o una subscripció, des de «Añadir» › «Contrato».",
                "Després, el tiquet d’alguna cosa amb garantia o termini de devolució, i un extracte del teu banc perquè Tiquet trobi el que es repeteix.",
                "Si véns d’un altre iPhone, «Restaurar una copia» a l’Inici buit recupera la teva còpia de seguretat.",
            ],
            "tips": [
                "Apple Intelligence és opcional. Sense, Tiquet llegeix els tiquets amb reconeixement de text i regles, te’ls deixa marcats per revisar, i «Pregunta» continua responent quant s’ha gastat en què.",
                "Amb Apple Intelligence, el model d’Apple llegeix millor tiquets i pòlisses i respon preguntes obertes, sempre al dispositiu.",
            ],
            "faq": [
                ("He de crear un compte?", "No. No hi ha compte de Tiquet ni cap contrasenya per recordar."),
            ],
        },
        {
            "id": "tickets",
            "title": "Tiquets, factures i PDF",
            "short": "Tiquets i factures",
            "tier": "free",
            "v11": False,
            "shot": None,
            "hook": (
                "Fes una foto al tiquet o envia-li la factura que t’ha arribat per correu, i Tiquet apunta la botiga, el dia, "
                "l’import i els articles. La foto queda com a prova encara que el paper tèrmic s’esborri."
            ),
            "steps": [
                "Toca «Añadir» i tria: «Cámara» escaneja i redreça el paper, amb diverses pàgines si el tiquet és llarg; «Fotos» n’admet fins a 30 alhora; «Archivo» obre un PDF o una imatge; «A mano», quan no hi ha paper.",
                "Des del Mail, Fitxers o Fotos, mantén premut l’adjunt, toca Compartir i tria Tiquet. Quan obres l’app, el llegeix.",
                "Abans de desar veus què ha entès. Si alguna cosa no quadra, toca «¿Algo mal leído? Corrígelo».",
                "El que arriba en lot o s’ha llegit sense Apple Intelligence porta l’avís «Guardado sin que lo revisaras». Compara-ho amb la foto i toca «Está bien».",
            ],
            "tips": [
                "Pots compartir fins a 20 fitxers d’un cop. Des de la versió 1.1 es llegeixen en l’ordre en què els envies.",
                "Des de la 1.1, el tiquet d’una botiga té «Web de la tienda, para su icono». L’escrius un cop i tots els seus tiquets i càrrecs porten la icona.",
                "Si deses a mà un tiquet repetit (mateixa botiga, dia i import), Tiquet t’ho pregunta abans.",
                "Des de la 1.2, cada pagament amb Apple Pay es pot apuntar sol com un tiquet, amb el seu comerç i la seva categoria. S’activa un cop: a Dreceres, «Automatització» › «+» › «Transacció», marca les teves targetes, tria «Executa immediatament» i afegeix l’acció de Tiquet «Apuntar un pago con tarjeta» (a Comercio, Importe i Tarjeta, les de la transacció). Els passos i l’interruptor per desactivar-ho són a «Ajustes» › «De tu banco». Quan importes l’extracte, aquell pagament no es compta dues vegades, i si escaneges el tiquet de paper n’ocupa el lloc.",
            ],
            "faq": [],
        },
        {
            "id": "garantias",
            "title": "Devolucions i garanties",
            "short": "Devolucions i garanties",
            "tier": "free",
            "v11": False,
            "shot": None,
            "hook": (
                "Quan alguna cosa s’espatlla o no et convenç, el difícil és saber si encara hi ets a temps. Tiquet treu els terminis "
                "de devolució i de garantia del tiquet i t’avisa abans que es tanquin."
            ),
            "steps": [
                "Desa el tiquet de la compra. A la seva fitxa, «Tus derechos» et diu fins quan dura la garantia legal i fins quan pots tornar-ho.",
                "La devolució surt del tiquet o, si no la imprimeix, de la política de les grans cadenes. Si ho has comprat en línia, la llei et dona 14 dies des de l’entrega.",
                "Per a alguna cosa que vulguis seguir, com un mòbil o una bici, toca «Registrar como cosa». Si el tiquet porta diverses línies, entra a l’article i toca «Registrar este artículo como cosa»: s’emporta el seu preu, la seva foto i la data de devolució.",
                "Les garanties vigents són juntes a «Contratos», a «Garantías en vigor», amb la més propera a dalt.",
            ],
            "tips": [
                "T’avisa 3 dies i 1 dia abans que es tanqui una devolució, i un mes abans que s’acabi la garantia d’una cosa.",
                "A Espanya la garantia legal és de 3 anys per al que s’ha comprat des del 2022. Reclama al venedor, no només al fabricant.",
                "«Tus derechos, con sus fuentes» diu d’on surt cada data. És informació, no assessorament jurídic.",
            ],
            "faq": [
                ("Per què el tiquet del súper no té garantia?", "Tiquet només posa garantia quan el paper la menciona i el que s’ha comprat en pot tenir: mai al menjar, a la benzina ni a un àpat fora de casa."),
            ],
        },
        {
            "id": "banco",
            "title": "Extractes del banc",
            "short": "Extractes del banc",
            "tier": "mix",
            "v11": False,
            "shot": None,
            "hook": (
                "Tiquet no es connecta al teu banc. Tu descarregues els moviments com a fitxer i els hi dones, i amb això veu "
                "el que pagues cada mes, el que portes pagat a cada empresa i el que es repeteix."
            ),
            "steps": [
                "Al web o a l’app del teu banc, exporta els moviments en Excel, CSV o PDF: cal una data, un concepte i un import. Si fas servir targeta de crèdit, exporta’n també l’extracte.",
                "Obre’l amb «Añadir» › «Archivo», o comparteix-lo amb Tiquet.",
                "Et diu quantes línies són noves; res no s’afegeix dues vegades. Si el fitxer no porta l’any, et demana l’«Año del último pago».",
                "Abans de desar, «Así ha leído Tiquet este archivo» mostra quina columna és la data, el concepte i l’import, amb tres línies per comprovar-ho. Si el teu banc escriu les compres en positiu, Tiquet els dona la volta i ho diu amb «El archivo pone los gastos en positivo»; si surten al revés, canvia aquest interruptor: ho recorda per a aquell banc.",
                "Des de la 1.2: si Tiquet no entén les columnes, o les ha llegit malament, toca «Elegir las columnas» («¿No se ha leído bien? Elige las columnas» si ja l’ha llegit): veus cada columna amb els primers valors i dius quina és la data, el concepte, l’import (o càrrec i abonament), el saldo, la divisa o una columna de signe D/H. Ho recorda per als fitxers següents d’aquell banc.",
                "A «Lo que se sigue cobrando» surten les empreses que et cobren a un ritme constant. Les que activis passen a ser contractes.",
            ],
            "tips": [
                "Transferències, Bizum i efectiu es guarden, però no compten com a despesa. Els números de targeta es retallen a les quatre últimes xifres.",
                "Des de la 1.1 pots enviar diversos extractes junts i s’importen un rere l’altre. A la 1.0, d’un en un.",
                "Amb «Recordarme lo que solo puedo hacer yo», a «Ajustes» › «Avisos», el dia 3 et recorda que portis el mes anterior si et falta. Des de la 1.2 ho mira banc per banc i targeta per targeta, diu quin falta i també ho mostra a «Requiere atención», perquè Vigilància no es quedi sense veure res.",
                "Amb Plus: «Entra y sale» compara el que entra amb el que surt.",
            ],
            "faq": [
                ("Quins bancs funcionen?", "Gairebé tots. Tiquet busca les columnes pels títols o, si no n’hi ha, pel que contenen; entén càrrec i abonament en dues columnes i els extractes en PDF, i reconeix el format de BBVA, Banc Sabadell, ING, Revolut i Andbank. Si el teu encara no es llegeix bé, «Envíanos la forma del archivo» prepara un correu sense cap dada teva: cada xifra passa a ser un 9 i cada paraula, la seva llargada. Des de la 1.2 també llegeix els extractes de targeta de crèdit en PDF que parteixen un moviment en diverses línies, deixa fora el «saldo anterior» i no compta com a despesa el pagament amb què se salda la targeta."),
            ],
        },
        {
            "id": "contratos",
            "title": "Contractes i assegurances",
            "short": "Contractes i assegurances",
            "tier": "free",
            "v11": False,
            "shot": "contracts",
            "hook": (
                "Cada assegurança, subscripció o rebut de casa com una fitxa: el que costa, el que portes pagat, quan "
                "es renova, fins quan pots donar-lo de baixa i a qui trucar el dia que passa alguna cosa."
            ),
            "steps": [
                "Toca «Añadir» › «Contrato», o el + de la pestanya «Contratos». Escriu amb qui és i quant costa.",
                "Toca «Adjuntar la póliza o el contrato» i escaneja el paper o tria una foto o un PDF. Tiquet llegeix número, prima, cobertura, assegurats i telèfon de sinistres, i només omple el que no havies escrit.",
                "Amb extractes importats, mira «En tu banco, aún sin ficha» a «Contratos»: un toc crea la fitxa d’un càrrec que es repeteix.",
                "Per a un mòbil a terminis, posa el «Número de pagos». Per a una prova gratis, activa «Prueba gratis» i tria quan «Empieza a cobrar».",
            ],
            "tips": [
                "Una assegurança porta 30 dies de preavís: a Espanya pots oposar-te a la renovació amb un mes d’antelació. Canvia-ho si el teu contracte diu una altra cosa.",
                "En un contracte anual, un mes abans de l’últim dia per dir que no t’arriba «buen momento para comparar», amb la pujada si el teu banc la mostra. Després, avisos 7 dies i 1 dia abans.",
                "«Llamar para dar un parte» i «Copiar el número de póliza» són a dalt de tot de la fitxa.",
                "Tiquet mai guarda contrasenyes: només apuntes on és l’accés.",
            ],
            "faq": [],
        },
        {
            "id": "subidas",
            "title": "On gastar menys",
            "short": "On gastar menys",
            "tier": "plus",
            "v11": False,
            "shot": None,
            "hook": (
                "Les pujades no avisen: l’assegurança que cada any costa una mica més, la subscripció que ja no fas servir. "
                "Tiquet posa els teus propis números l’un al costat de l’altre i et diu quina pregunta fer."
            ),
            "steps": [
                "Importa extractes d’almenys un any: una pujada es veu comparant el mateix càrrec en anys diferents.",
                "A l’«Inicio», obre la targeta «Dónde gastar menos».",
                "Cada troballa diu què s’ha vist, per què pot importar, què podries fer i quants diners hi passen a l’any, com a estimació.",
                "Toca «Ver los cargos» per veure cada pagament que hi ha darrere, any a any. Quan ho hagis revisat, toca «Ya lo he mirado».",
            ],
            "tips": [
                "Busca sis coses: un contracte que ha pujat, una protecció que ja ha costat molt en comparació amb el que protegeix, una garantia de pagament mentre dura la legal, comissions del banc, subscripcions de més d’un any i peatges o aparcaments molt freqüents.",
                "Tiquet mai recomana una companyia, una cobertura ni una baixa. No coneix preus de mercat: et dona les teves xifres i la pregunta.",
                "La pujada d’un contracte també es veu gratis a la seva fitxa, a «Precio de cada cargo, año a año».",
                "Des de la 1.1, «La cesta» fa el mateix amb els preus del súper.",
            ],
            "faq": [],
        },
        {
            "id": "sime",
            "title": "Si em passa res",
            "short": "Si em passa res",
            "tier": "free",
            "v11": False,
            "shot": None,
            "hook": (
                "Si demà no hi ets per explicar-ho, sap la teva parella quines assegurances teniu, amb qui i a quin número trucar? "
                "Tiquet prepara aquests papers ara, mentre tot va bé."
            ),
            "steps": [
                "Des de la 1.2, quan passa alguna cosa: «¿A quién llamo?» a «Contratos» (o digues a Siri «A quién llamo en Tiquet») mostra les teves assegurances pel que ha passat (llar, cotxe, salut, mòbil…) amb la companyia, el número de pòlissa i un botó per trucar a sinistres.",
                "A «Contratos», toca «Compartir» a dalt, o ves a «Ajustes» › «Compartir con los de casa».",
                "Tria «Hoja de casa (PDF)» o «Hoja de casa, con precios». Es fa al dispositiu.",
                "Imprimeix-la o envia-la a algú de confiança, i guarda-la on la puguin trobar.",
                "Perquè la teva parella tingui el mateix al seu Tiquet, toca «Compartir con los de casa» i envia-li el fitxer de casa per AirDrop. Quan l’obri, el seu Tiquet hi afegeix el que falta i actualitza el que vas canviar després.",
            ],
            "tips": [
                "El full porta cada assegurança i contracte: companyia, número de pòlissa, qui està assegurat, què cobreix, el telèfon per donar un part, el contacte, on es guarda l’accés, quan es renova i si la pòlissa és a Tiquet. Després, el que està en garantia i els documents que caduquen.",
                "Mai porta contrasenyes ni el número dels teus documents. Els preus, només a la versió amb preus.",
                "El fitxer de casa porta contractes, assegurances amb les seves pòlisses i garanties: ni tiquets ni banc. No està xifrat i no s’actualitza sol, així que torna a enviar-lo quan canviïs alguna cosa.",
                "Des de la 1.2, si canvies un contracte després d’enviar el fitxer de casa, «Contratos» t’avisa: «El fichero del hogar está desactualizado», i el tornes a enviar amb «Reenviar».",
            ],
            "faq": [],
        },
        {
            "id": "vigilar",
            "title": "Vigilància: alguna cosa estranya?",
            "short": "Vigilància",
            "tier": "free",
            "v11": False,
            "shot": "watch",
            "hook": (
                "Un Bizum que no vas fer o un cobrament doble es veuen millor amb la història de casa teva al costat. Vigilància "
                "compara cada moviment dels teus extractes amb el que acostumes a fer i et pregunta si el reconeixes."
            ),
            "steps": [
                "Importa els teus extractes. Vigilància revisa els últims 120 dies al dispositiu, amb regles i sense IA.",
                "El que trobi surt a la targeta «Vigilancia» de l’«Inicio» i encapçala «Requiere atención». La pantalla completa és a «De tu banco» › «Vigilancia: ¿algo raro?».",
                "Si el reconeixes, toca «Es mío» i Tiquet ho aprèn a tots els teus dispositius. Per a diversos alhora, «Todos son míos».",
                "Amb «No lo reconozco», et diu què has de fer: trucar al banc i bloquejar la targeta, demanar que te’l tornin, denunciar-ho i canviar la contrasenya.",
            ],
            "tips": [
                "Sis senyals: un Bizum alt a algú nou; diversos Bizum el mateix dia a gent nova; una transferència a un compte mai vist; un càrrec en una altra moneda sense cap viatge al voltant; un càrrec mínim a internet seguit d’un altre de més gran; i un cobrament doble.",
                "Per a un pagament que no vas autoritzar tens fins a 13 mesos per avisar el banc, però com més aviat, millor.",
                "Tiquet no contacta amb ningú, ni tan sols amb el teu banc.",
            ],
            "faq": [
                ("M’avisa tan bon punt passa alguna cosa?", "No. Només veu un moviment quan n’importes l’extracte, així que sempre arriba després. Complementa les alertes del teu banc, no les substitueix."),
            ],
        },
        {
            "id": "lugares",
            "title": "Llocs: restaurants i bars",
            "short": "Llocs",
            "tier": "mix",
            "v11": False,
            "shot": "places",
            "hook": (
                "Els teus tiquets de restaurant es converteixen en el teu propi mapa: on vau menjar, què vau demanar, què us va encantar "
                "i a quin lloc tornar. Sense escriure ressenyes: el tiquet ja diu el plat i el preu."
            ),
            "steps": [
                "Desa el tiquet d’un restaurant o d’un bar i va a «Sitios», a la fitxa del seu lloc. «Estoy aquí ahora» el situa al mapa amb la teva posició.",
                "Al tiquet, posa estrelles a «El sitio» (valen per a totes les visites) i obre cada plat de «Lo que pedisteis» per respondre «¿Lo pedirías otra vez?» i afegir «Fotos del plato».",
                "El «Resumen» de «Sitios» mostra «Vuestros habituales», els «Viajes» que detecta sol i el que tens «Cerca de casa».",
                "Cada lloc reuneix les seves visites, el que ha costat, els plats «Para volver a pedir», el seu telèfon, «Reservar o ver la carta» i «Abrir en Mapas».",
                "Amb Plus, «Traerlos a Sitios» porta els restaurants dels teus extractes i els busca a Apple Maps.",
            ],
            "tips": [
                "Pregunta per una ciutat o una regió: «¿Qué sitios me gustaron en Cantabria?». Tiquet busca aquest nom a Apple Maps per situar-lo; aquesta pregunta necessita Apple Intelligence.",
                "«¿Dónde me encantaron las bravas?» es respon sense Apple Intelligence, amb les estrelles que vas donar a aquell plat.",
                "Si un lloc surt amb dos noms, fes servir «Es el mismo sitio que otro…».",
            ],
            "faq": [],
        },
        {
            "id": "cesta",
            "title": "La cistella i la llista de la compra",
            "short": "Cistella i llista de la compra",
            "tier": "mix",
            "v11": True,
            "shot": "basket",
            "hook": (
                "Cada tiquet del súper guarda els seus articles amb el preu. Tiquet compara el mateix a la mateixa botiga, et diu "
                "quant ha pujat la teva cistella habitual i t’ajuda a no oblidar el que et toca comprar."
            ),
            "steps": [
                "Desa els tiquets del súper. Amb dos de la mateixa botiga amb les mateixes coses ja es pot comparar.",
                "A l’«Inicio», la targeta «La cesta y la lista de la compra» obre «La cesta», amb els apartats «Suben», «Bajan» i «Más barato en tus otras tiendas».",
                "Un producte mostra cada preu que vas pagar, per unitat o per quilo. El que s’ha llegit malament va a «Precios que parecen mal leídos» i no compta: obre’n el tiquet i corregeix la línia.",
                "A la «Lista de la compra», escriu tres lletres i et suggereix el que ja vas comprar, amb la botiga i l’últim preu. També et proposa el que toca reposar.",
                "A la botiga, toca cada cosa per ratllar-la; la pantalla no s’apaga mentre la fas servir. En acabar, «Quitar lo tachado».",
            ],
            "tips": [
                "La cistella va amb Plus, al costat de «Dónde gastar menos». La llista de la compra és gratis.",
                "Afegeix el widget «Lista de la compra» a la pantalla d’inici i ratlla des d’allà el que vas agafant, sense obrir l’app.",
                "Digues a Siri «Lista de la compra en Tiquet», o escriu a «Pregunta» «hazme la lista de la compra»: funciona sense Apple Intelligence.",
                "La llista es guarda en aquest dispositiu i no se sincronitza per iCloud.",
            ],
            "faq": [],
        },
        {
            "id": "preguntar",
            "title": "Pregunta",
            "short": "Pregunta",
            "tier": "mix",
            "v11": False,
            "shot": "ask",
            "hook": (
                "Pregunta amb les teves paraules i Tiquet respon amb els teus tiquets, extractes i contractes. Les xifres les calcula "
                "l’app; el model d’Apple només les explica, i tot passa al dispositiu."
            ),
            "steps": [
                "Toca «Pregunta sobre tu dinero…» a dalt de l’«Inicio» i escriu, o toca el micròfon per dictar.",
                "Per començar, toca una idea: «¿Cuánto llevamos en la compra este mes?» o «¿Qué puedo devolver todavía?».",
                "Sota la resposta surten targetes amb els pagaments que la sostenen. Toca’n una per veure’ls.",
                "Si demanes un canvi, com posar estrelles o canviar el pressupost, veus l’abans i el després. Res no canvia fins que toques «Confirmar», i es pot desfer.",
                "Per seguir el fil, comença per «y»: «¿Y el año pasado?».",
            ],
            "tips": [
                "Sense Apple Intelligence, l’app respon sola quant en alguna cosa, en una botiga o en una etiqueta («¿Cuánto nos costó el viaje a Roma?»), on vas prendre un plat i quan toca el proper pagament d’un contracte.",
                "«¿Qué puedo devolver todavía?» i «¿Qué sigue en garantía?» els respon l’app al moment, amb tot el que continua obert, el més urgent primer.",
                "Amb Apple Intelligence, a més: llocs a prop teu o en una regió, i «cena Can Pere 42 ayer» per crear un tiquet que revises abans de desar.",
                "Gratis tens 5 preguntes al dia a cada dispositiu, sobre el que és gratis a l’app. Amb Plus, sense límit.",
                "Amb el mode discret, cada resposta espera darrere de «Importes ocultos. Mostrar esta respuesta».",
            ],
            "faq": [],
        },
        {
            "id": "inicio",
            "title": "L’Inici i el que ve",
            "short": "Inici, widgets i Siri",
            "tier": "mix",
            "v11": False,
            "shot": "coming",
            "hook": (
                "Quan obres l’app, l’«Inicio» et diu si has de fer alguna cosa, com va el mes i què ve. Fora de l’app, "
                "els widgets i Siri t’ho expliquen sense haver-la d’obrir."
            ),
            "steps": [
                "«Requiere atención» va a dalt: devolucions, renovacions, garanties, tiquets per revisar. Mantén premut un avís per a «Hecho» o «Recordármelo mañana».",
                "Tria Mes, Año o Fechas a dalt: totes les targetes segueixen aquell període.",
                "«Próximos cargos» mostra el que es cobra aviat. Amb Plus, «Semana a semana, mes a mes» obre «Lo que viene»: dotze mesos, càrrec a càrrec, i cada previsió diu en què es basa.",
                "Amb Plus, gira l’iPhone per veure «Horizonte»: el que s’ha gastat, cap on va el mes i el que ve. «¿Y si quito…?» apaga un contracte i torna a dibuixar l’any.",
                "Amb Plus, «El Mes» treu un número per cada mes acabat, com un diari de casa, per compartir en PDF.",
                "«Organizar esta pantalla», al final, canvia l’ordre de les targetes o amaga les que no facis servir.",
            ],
            "tips": [
                "Widgets: «Este mes», «Próximo cargo», «Seguros a mano», «Buenos sitios cerca» i «Lista de la compra». El control «Añadir un tique» va al Centre de control, a la pantalla bloquejada o al botó d’acció.",
                "Pregunta a Siri «¿Cuándo se renueva el seguro de hogar en Tiquet?» o «¿Cómo voy este mes en Tiquet?».",
            ],
            "faq": [],
        },
        {
            "id": "cosas",
            "title": "Coses i documents que caduquen",
            "short": "Coses i documents",
            "tier": "free",
            "v11": False,
            "shot": None,
            "hook": (
                "El que val la pena seguir, com el mòbil, el portàtil o la bici, i els papers que caduquen, en una pestanya. "
                "El dia que et roben alguna cosa o has de renovar el DNI, ho tens a mà."
            ),
            "steps": [
                "Des d’un tiquet, toca «Registrar como cosa». O a «Cosas», toca + › «Añadir una cosa».",
                "A la seva fitxa, escaneja el número de sèrie o l’IMEI de la caixa o l’etiqueta, i fes una foto del producte i una altra de la seva etiqueta. És el primer que demanen la policia i les asseguradores.",
                "Si te’l van vendre amb una assegurança, toca «Añadir seguro o garantía extendida» i queda enllaçada.",
                "Per a un document, a «Cosas» toca + › «Añadir un documento que caduca»: DNI, passaport, carnet de conduir, ITV, targeta sanitària, carnet de família nombrosa, permís de residència o un altre. Apunta de qui és i fins quan és vàlid.",
            ],
            "tips": [
                "Un document t’avisa 60 i 15 dies abans de caducar (la ITV, 30 i 7), i surt a «Requiere atención» i a «Plazos».",
                "El seu número és opcional, s’amaga en mode discret i mai s’imprimeix al full de casa.",
                "Esborrar una cosa no n’esborra l’assegurança: Tiquet pregunta abans i et diu què es queda.",
            ],
            "faq": [],
        },
        {
            "id": "etiquetas",
            "title": "Etiquetes, pressupost i estalvi",
            "short": "Etiquetes i pressupost",
            "tier": "mix",
            "v11": False,
            "shot": None,
            "hook": (
                "Una etiqueta ajunta el que va junt encara que arribi per camins diferents: «Viaje a Roma» suma l’hotel escanejat, "
                "el vol de l’extracte i l’assegurança de viatge. El pressupost et diu si el mes va bé."
            ),
            "steps": [
                "En un tiquet, un contracte o una cosa, afegeix una etiqueta a «Etiquetas». Quan llegeix un tiquet, Tiquet te’n suggereix alguna.",
                "Els pagaments del banc reben la seva etiqueta sols. Els que es queden sense esperen a «Clasificar»: un toc etiqueta tots els pagaments d’aquell comerç, passats i futurs.",
                "Si alguna cosa està mal arxivada, «Revisar la clasificación» ho corregeix per comerç o per grup, i es pot desfer.",
                "A «Ajustes» › «Presupuesto mensual», posa el que voleu gastar en un mes normal, amb tot inclòs.",
                "Amb Plus, a la targeta «Ahorrando para» toca «Nuevo objetivo»: quant, per a quan i les paraules que el teu banc posa a les transferències a la guardiola.",
            ],
            "tips": [
                "Cada pagament compta un cop a l’etiqueta: el tiquet i la seva línia del banc són el mateix pagament.",
                "Les persones de casa també serveixen d’etiqueta: «todo lo de Marta» és una pantalla.",
                "Tiquet mai calcula el pressupost a partir dels teus ingressos. És una xifra, no vint.",
            ],
            "faq": [],
        },
        {
            "id": "privacidad",
            "title": "Privadesa i les teves dades",
            "short": "Privadesa",
            "tier": "free",
            "v11": False,
            "shot": None,
            "hook": (
                "Els teus tiquets, contractes i extractes es queden al teu dispositiu. No hi ha compte, ni connexió amb el teu banc, "
                "ni servidors nostres: no rebem ni els teus extractes ni els teus imports."
            ),
            "steps": [
                "A «Ajustes», la targeta «Tus datos se quedan contigo» explica on és cada cosa i què fa servir connexió.",
                "Per tenir l’iPhone i l’iPad iguals, activa «Sincronizar con iCloud» a «Ajustes» › «iPhone y iPad, a la par», a cada dispositiu amb el teu compte d’Apple. Fa servir el teu iCloud privat, que el desenvolupador no pot llegir.",
                "Per endur-t’ho tot, «Ajustes» › «Copia y restauración» › «Exportar todo»: un .zip amb tiquets, fotos, pòlisses, moviments i fulls de càlcul.",
                "Per esborrar-ho tot, en aquesta pàgina toca «Borrar todo lo que hay en Tiquet» i escriu BORRAR. Amb iCloud activat, s’esborra també dels teus altres dispositius.",
                "L’ull de dalt de l’«Inicio» activa el mode discret: cada import passa a •••.",
            ],
            "tips": [
                "Fan servir connexió: el teu iCloud, si l’actives; Apple Maps, amb el nom d’un lloc, una adreça o una coordenada; el web d’una empresa, un cop, per al seu logo; i l’App Store per a Plus.",
                "La còpia no està xifrada: guarda-la en un lloc segur.",
                "Tiquet només demana la teva ubicació quan toques «Estoy aquí ahora» o preguntes per llocs a prop teu.",
            ],
            "faq": [],
        },
        {
            "id": "plus",
            "title": "Gratis i Plus",
            "short": "Gratis i Plus",
            "tier": "mix",
            "v11": False,
            "shot": "month",
            "hook": (
                "Guardar i trobar és gratis per sempre. Plus afegeix el que t’ajuda a entendre i a gastar menys, "
                "amb un sol pagament i sense subscripció."
            ),
            "steps": [
                "Gratis: tiquets, garanties i devolucions amb els seus avisos; contractes i assegurances amb els seus; «Si me pasa algo»; Vigilància; iCloud i la còpia; Inici, Llocs, Contractes i Coses; 5 preguntes al dia.",
                "Plus: «Dónde gastar menos», «Entra y sale» i els teus comptes, nous objectius d’estalvi, «Lo que viene» a 12 mesos i «Horizonte», «El Mes», llocs des del teu banc i preguntes sense límit. Des de la 1.1, també «La cesta».",
                "Per provar-lo, ves a «Ajustes» › «Tiquet Plus» i toca «Pruébalo todo gratis 14 días». No es cobra res ni es renova sol.",
                "Si et convenç, compra’l un cop: 9,99 €, preu de llançament a Espanya. En un altre dispositiu, toca «Restaurar compras».",
            ],
            "tips": [
                "Res del que guardes es bloqueja mai. Quan s’acaba la prova, les funcions de Plus es tanquen i el que és teu continua aquí.",
                "Plus funciona amb En Família: es comparteix la compra, no les teves dades. La prova és individual.",
                "Amb les dades d’exemple ho veus tot, també el que és de Plus, abans de decidir.",
            ],
            "faq": [
                ("Què passa quan s’acaben els 14 dies?", "Continues amb el que és gratis, sense cap càrrec. Els objectius que vas crear continuen a la vista i els llocs portats del banc continuen a Llocs."),
            ],
        },
    ],
    "outro_h": "Et falta alguna cosa?",
    "outro_p": (
        "Tiquet és gratis a l’App Store d’Espanya. Si alguna cosa no funciona com esperes, o trobes a faltar una funció, "
        "escriu-nos des de la pàgina de suport."
    ),
}
