# -*- coding: utf-8 -*-
"""
All site copy and settings, in English and Spanish.
Edit here, then run:  python3 tools/build_site.py
(Or edit the generated HTML directly; just don't re-run the build afterwards.)

Anything wrapped in ph("...") renders as a highlighted [CONFIRM WITH CLIENT: ...] marker.
"""

# ---------------------------------------------------------------- settings
SITE_URL = "https://www.arce-law.com"          # no trailing slash
FIRM = "Arce Law"
EMAIL = "info@arce-law.com"
PHONE_US_TEL = "+12062009513"
PHONE_US_DISPLAY = "(206) 200-9513"
PHONE_MX_TEL = "+523334084797"
PHONE_MX_DISPLAY = "(33) 3408-4797"
# Placeholder WhatsApp number (555-01xx is reserved for fiction). Digits only, with country code, no "+".
WHATSAPP_NUMBER = "15555550123"
# Create a free form at https://formspree.io and paste its ID here (looks like "xyzabcde").
FORMSPREE_ID = "YOUR_FORM_ID"
OG_IMAGE = "/assets/img/og-share-image-1200x630-PLACEHOLDER.jpg"


def ph(text):
    return f'<mark class="ph">[CONFIRM WITH CLIENT: {text}]</mark>'


TZ = ph("time zone")

# ---------------------------------------------------------------- page registry
# key -> slug per language ("" = language home)
SLUGS = {
    "home":        {"en": "",                             "es": ""},
    "realestate":  {"en": "mexico-real-estate",           "es": "bienes-raices-mexico"},
    "family":      {"en": "mexico-family-civil-law",      "es": "derecho-familiar-civil-mexico"},
    "poa":         {"en": "power-of-attorney-apostille",  "es": "poderes-notariales-apostilla"},
    "other":       {"en": "mexico-legal-representation",  "es": "representacion-legal-mexico"},
    "immigration": {"en": "us-immigration",               "es": "inmigracion-estados-unidos"},
    "llc":         {"en": "washington-llc-formation",     "es": "constitucion-llc-washington"},
    "about":       {"en": "about",                        "es": "nosotros"},
    "team":        {"en": "team",                         "es": "equipo"},
    "contact":     {"en": "contact",                      "es": "contacto"},
}
PRACTICE_KEYS = ["realestate", "family", "poa", "other", "immigration", "llc"]

# ---------------------------------------------------------------- SEO (title ≤ ~60, description ≤ ~160)
SEO = {
    "home": {
        "en": ("Arce Law | Legal Help in Mexico & the U.S., in English or Spanish",
               "Bilingual legal help for matters in Mexico (Jalisco, Michoacán, Colima) and the U.S. (Washington, Arizona): property, divorce, powers of attorney, immigration. Free consultation."),
        "es": ("Arce Law | Abogados en Jalisco, Michoacán, Colima y EE. UU.",
               "Abogados bilingües para asuntos legales en México y Estados Unidos: bienes raíces, divorcios, poderes notariales, apostillas e inmigración. Consulta gratuita."),
    },
    "realestate": {
        "en": ("Lawyer for Property in Mexico | Buy, Sell & Transfer | Arce Law",
               "Own or inherit property in Jalisco, Michoacán or Colima? We handle purchases, sales, title transfers, appraisals and property management, even while you live in the U.S."),
        "es": ("Abogado de Bienes Raíces en Jalisco, Michoacán y Colima | Arce Law",
               "Compraventa, escrituración, avalúos, traspasos y administración de inmuebles en Jalisco, Michoacán y Colima, aunque usted viva en Estados Unidos. Consulta gratuita."),
    },
    "family": {
        "en": ("Divorce, Custody & Wills in Mexico | Family Lawyer | Arce Law",
               "Family and civil matters in Mexico handled from the U.S.: divorce, child custody, wills, inheritance and evictions in Jalisco, Michoacán and Colima. In English or Spanish."),
        "es": ("Abogado Familiar en Jalisco | Divorcios, Custodia y Testamentos",
               "Divorcios, guarda y custodia, pensión alimenticia, testamentos, sucesiones y desalojos en Jalisco, Michoacán y Colima. Le atendemos aunque viva en EE. UU."),
    },
    "poa": {
        "en": ("Power of Attorney for Mexico & Apostille Services | Arce Law",
               "Need a power of attorney valid in Mexico or an apostilled U.S. or Mexican document? We prepare, review and guide you through notarization and apostille, step by step."),
        "es": ("Poder Notarial para México y Apostilla de Documentos | Arce Law",
               "Elaboración de poderes notariales válidos en México y trámite de apostilla para documentos de EE. UU. y México. Le guiamos paso a paso, desde donde esté."),
    },
    "other": {
        "en": ("Mexico Legal Representation: Business, Labor, Amparo | Arce Law",
               "Representation in Mexico for commercial and business disputes, criminal matters, labor claims, agrarian (ejido) issues and amparo proceedings. Bilingual service."),
        "es": ("Abogado en Jalisco: Mercantil, Penal, Laboral, Agrario y Amparo",
               "Representación legal en México en materia mercantil, penal, laboral, agraria (ejidos) y juicio de amparo, en Jalisco, Michoacán y Colima. Atención en español e inglés."),
    },
    "immigration": {
        "en": ("U.S. Immigration Help: Citizenship, Green Card, Visas | Arce Law",
               "Help with U.S. citizenship (naturalization), adjustment of status, family petitions and visas. Clear guidance in English or Spanish. Free consultation."),
        "es": ("Inmigración en EE. UU.: Ciudadanía, Residencia y Visas | Arce Law",
               "Trámites de inmigración en Estados Unidos: ciudadanía, ajuste de estatus (green card), peticiones familiares y visas. Atención en español. Consulta gratuita."),
    },
    "llc": {
        "en": ("Washington LLC Formation & Corporation Setup | Arce Law",
               "Form a Washington LLC or corporation the right way: name check, Certificate of Formation, registered agent, operating agreement, EIN and business license. English or Spanish."),
        "es": ("Cómo Abrir una LLC en Washington | Constitución de Empresas",
               "Le ayudamos a constituir su LLC o corporación en el estado de Washington: registro, agente registrado, acuerdo operativo, EIN y licencia comercial. Atención en español."),
    },
    "about": {
        "en": ("About Arce Law | Bilingual Legal Services in Mexico & the U.S.",
               "Learn about Arce Law, a bilingual legal practice helping families and businesses with matters in Mexico and the United States."),
        "es": ("Nosotros | Arce Law, Asesoría Legal Bilingüe México–EE. UU.",
               "Conozca Arce Law, un despacho bilingüe que ayuda a familias y empresas con asuntos legales en México y Estados Unidos."),
    },
    "team": {
        "en": ("Meet Our Team | Arce Law",
               "Meet the bilingual team at Arce Law who handle legal matters in Mexico (Jalisco, Michoacán, Colima) and the U.S. (Washington, Arizona)."),
        "es": ("Nuestro Equipo | Abogados Bilingües | Arce Law",
               "Conozca al equipo bilingüe de Arce Law que atiende asuntos legales en México (Jalisco, Michoacán, Colima) y Estados Unidos (Washington, Arizona)."),
    },
    "contact": {
        "en": ("Contact Arce Law | Free Consultation in English or Spanish",
               "Request a free consultation. Call the U.S. at (206) 200-9513 or Mexico at (33) 3408-4797, message us on WhatsApp, or send our secure intake form."),
        "es": ("Contacto | Consulta Gratuita en Español o Inglés | Arce Law",
               "Solicite su consulta gratuita. Llámenos en EE. UU. al (206) 200-9513 o en México al (33) 3408-4797, escríbanos por WhatsApp o envíe el formulario."),
    },
}

# ---------------------------------------------------------------- shared UI strings
UI = {
    "en": {
        "locale": "en_US", "other": "es", "other_label": "Español", "other_short": "ES",
        "switch_aria": "Ver esta página en español",
        "skip": "Skip to main content",
        "menu": "Menu", "services": "Services", "about": "About", "team": "Team", "contact": "Contact",
        "home": "Home",
        "cta": "Free Consultation",
        "call_us": "Call U.S.", "call_mx": "Call Mexico",
        "us_label": "U.S.", "mx_label": "Mexico",
        "hours_short": f"Mon–Fri 8:30am–5:00pm",
        "hours_days": "Monday–Friday", "hours_time": "8:30 am – 5:00 pm",
        "closed": "Saturday & Sunday", "closed_v": "Closed",
        "wa_label": "WhatsApp", "wa_aria": "Chat with us on WhatsApp",
        "wa_text": "Hello Arce Law, I would like a free consultation.",
        "learn": "Learn more",
        "footer_blurb": "Bilingual legal help for matters in Mexico and the United States.",
        "footer_firm": "Firm", "footer_services": "Services", "footer_contact": "Contact",
        "email": "Email", "hours": "Hours",
        "disclaimer": (
            "<strong>Legal disclaimer:</strong> The information on this website is for general informational purposes only "
            "and is not legal advice. Every situation is different; please consult with us about your specific matter. "
            "Contacting Arce Law through this website, by phone, by email or by WhatsApp does not create an attorney-client "
            "relationship. An attorney-client relationship is formed only after a written engagement agreement is signed. "
            "Please do not send confidential or time-sensitive information until that relationship has been established."
        ),
        "rights": "All rights reserved.",
        "faq": "Frequently asked questions",
        "process": "How it works",
        "what_we_do": "What we help with",
        "related": "Other services",
        "served": "Serving",
        "cta_title": "Talk to us about your case, free",
        "cta_text": "Tell us what's going on and we'll explain your options in plain language, in English or Spanish. No obligation.",
        "cta_call": "Call",
    },
    "es": {
        "locale": "es_MX", "other": "en", "other_label": "English", "other_short": "EN",
        "switch_aria": "View this page in English",
        "skip": "Saltar al contenido principal",
        "menu": "Menú", "services": "Servicios", "about": "Nosotros", "team": "Equipo", "contact": "Contacto",
        "home": "Inicio",
        "cta": "Consulta gratuita",
        "call_us": "Llamar a EE. UU.", "call_mx": "Llamar a México",
        "us_label": "EE. UU.", "mx_label": "México",
        "hours_short": "Lun a vie, 8:30 a 17:00 h",
        "hours_days": "Lunes a viernes", "hours_time": "8:30 a 17:00 h",
        "closed": "Sábado y domingo", "closed_v": "Cerrado",
        "wa_label": "WhatsApp", "wa_aria": "Escríbanos por WhatsApp",
        "wa_text": "Hola, Arce Law. Me gustaría solicitar una consulta gratuita.",
        "learn": "Ver más",
        "footer_blurb": "Asesoría legal bilingüe para asuntos en México y Estados Unidos.",
        "footer_firm": "Despacho", "footer_services": "Servicios", "footer_contact": "Contacto",
        "email": "Correo", "hours": "Horario",
        "disclaimer": (
            "<strong>Aviso legal:</strong> La información de este sitio web es de carácter general e informativo y no "
            "constituye asesoría legal. Cada caso es distinto; le invitamos a consultarnos sobre su situación particular. "
            "Comunicarse con Arce Law a través de este sitio, por teléfono, por correo electrónico o por WhatsApp no crea "
            "una relación abogado-cliente. Dicha relación se establece únicamente al firmar un contrato de prestación de "
            "servicios. Le pedimos no enviar información confidencial o urgente hasta que esa relación se haya formalizado."
        ),
        "rights": "Todos los derechos reservados.",
        "faq": "Preguntas frecuentes",
        "process": "Cómo trabajamos",
        "what_we_do": "En qué le ayudamos",
        "related": "Otros servicios",
        "served": "Atendemos",
        "cta_title": "Platíquenos su caso, sin costo",
        "cta_text": "Cuéntenos qué está pasando y le explicamos sus opciones con claridad, en español o en inglés. Sin compromiso.",
        "cta_call": "Llamar",
    },
}

MX_STATES = {"en": "Jalisco · Michoacán · Colima", "es": "Jalisco · Michoacán · Colima"}

# ---------------------------------------------------------------- practice areas
PRACTICE = {
    # ------------------------------------------------------------ REAL ESTATE
    "realestate": {
        "icon": "home", "country": "mx",
        "en": {
            "name": "Mexican Real Estate",
            "card": "Buy, sell, transfer or manage property in Mexico, including homes you own or inherited while living in the U.S.",
            "h1": "Property in Mexico, handled from wherever you live",
            "lead": "Whether you are buying, selling, inheriting or simply need someone you trust to look after a property in Mexico, we take care of the legal work and the paperwork so you don't have to travel for every step.",
            "served": "Jalisco, Michoacán and Colima",
            "intro": [
                "Real estate in Mexico runs through notarios públicos, local property registries and municipal tax offices, and the requirements can change from one municipality to the next. For families living in the United States, keeping track of all of it from a distance is hard.",
                "We review the property's legal status before you commit, prepare and check the documents, coordinate with the notary, appraiser and authorities, and keep you updated in English or Spanish until the deed is registered.",
            ],
            "items": [
                ("Purchases and sales", "Title review, lien and tax checks, purchase agreements and closing before a notary."),
                ("Ownership transfers", "Transfers between family members, donations, and putting inherited property in the right name."),
                ("Appraisals (avalúos)", "We coordinate certified appraisals required for sales, transfers, taxes or court matters."),
                ("Property management", "Ongoing oversight of your property in Mexico: taxes, utilities, tenants and paperwork."),
                ("Title and registry problems", "Fixing irregular deeds, missing registrations and outstanding property taxes (predial)."),
            ],
            "steps": [
                ("Free consultation", "Tell us about the property and what you want to do. We'll explain the options and the documents involved."),
                ("Legal review", "We check the deed, the public registry, liens and taxes so there are no surprises."),
                ("Documents and power of attorney", "We prepare the paperwork and, if you can't travel, a power of attorney so we can act for you."),
                ("Notary and registration", "We coordinate the signing before the notary, pay the related taxes and follow up until the deed is registered."),
                ("Delivery", "You receive copies of everything, and the original documents are delivered or kept as you prefer."),
            ],
            "faqs": [
                ("Can I buy or sell property in Mexico while living in the U.S.?",
                 "Yes. In many cases you can grant a power of attorney so that someone acts on your behalf before the notary. We'll tell you exactly what's needed for your transaction and whether any step requires your presence."),
                ("Can foreigners or U.S. citizens own property in Mexico?",
                 "Yes. Inside the \"restricted zone\" (land near the coast and the borders), foreigners generally hold residential property through a bank trust (fideicomiso) or a Mexican company. Outside that zone, direct ownership is possible after a permit from the Ministry of Foreign Affairs. We'll explain which applies to your property."),
                ("I inherited a house in Mexico. What do I do?",
                 "Usually an inheritance (succession) process must be completed before the property can be put in your name or sold. It can be handled through a notary or a court depending on the case. We can review the documents and tell you the best route."),
                ("What costs should I expect besides your fees?",
                 "Typical costs include notary fees, the property acquisition tax, registry fees, appraisal and, for sellers, possible income tax on the gain. Amounts vary by municipality and value; we'll give you an estimate before you decide."),
            ],
        },
        "es": {
            "name": "Bienes raíces en México",
            "card": "Compra, venta, escrituración, traspasos y administración de inmuebles en México, aunque usted viva en Estados Unidos.",
            "h1": "Su propiedad en México, en buenas manos desde donde usted esté",
            "lead": "Ya sea que quiera comprar, vender, heredar o simplemente tener a alguien de confianza que cuide su propiedad en México, nosotros nos encargamos de la parte legal y de los trámites para que no tenga que viajar en cada paso.",
            "served": "Jalisco, Michoacán y Colima",
            "intro": [
                "Las operaciones inmobiliarias en México pasan por notarías, el Registro Público de la Propiedad y las oficinas de catastro y tesorería municipales, y los requisitos pueden cambiar de un municipio a otro. Para quienes viven en Estados Unidos, darle seguimiento a todo a distancia es complicado.",
                "Revisamos la situación legal del inmueble antes de que usted se comprometa, preparamos y verificamos la documentación, coordinamos con el notario, el perito valuador y las autoridades, y le mantenemos informado hasta que la escritura quede inscrita.",
            ],
            "items": [
                ("Compraventa de inmuebles", "Revisión de escrituras, gravámenes y adeudos, contratos de compraventa y firma ante notario."),
                ("Traspasos y escrituración", "Traspasos entre familiares, donaciones y regularización de propiedades heredadas a su nombre."),
                ("Avalúos", "Coordinamos avalúos con peritos certificados para compraventas, traspasos, impuestos o juicios."),
                ("Administración de propiedades", "Cuidamos su inmueble en México: predial, servicios, inquilinos y trámites."),
                ("Regularización de escrituras", "Corrección de escrituras irregulares, inscripciones pendientes y adeudos de predial."),
            ],
            "steps": [
                ("Consulta gratuita", "Platíquenos sobre el inmueble y lo que desea hacer. Le explicamos las opciones y los documentos necesarios."),
                ("Revisión legal", "Verificamos escritura, Registro Público, gravámenes y adeudos para evitar sorpresas."),
                ("Documentos y poder notarial", "Preparamos la documentación y, si no puede viajar, un poder para actuar en su nombre."),
                ("Firma y registro", "Coordinamos la firma ante notario, el pago de impuestos y damos seguimiento hasta la inscripción."),
                ("Entrega", "Le entregamos copia de todo y resguardamos o enviamos los documentos originales según prefiera."),
            ],
            "faqs": [
                ("¿Puedo comprar o vender una propiedad en México si vivo en Estados Unidos?",
                 "Sí. En muchos casos puede otorgar un poder notarial para que alguien firme en su nombre ante el notario. Le diremos exactamente qué se necesita en su caso y si algún paso requiere su presencia."),
                ("¿Un ciudadano estadounidense puede ser dueño de una propiedad en México?",
                 "Sí. En la llamada \"zona restringida\" (franja cercana a costas y fronteras), los extranjeros generalmente adquieren inmuebles residenciales mediante un fideicomiso bancario o una sociedad mexicana. Fuera de esa zona puede adquirirse directamente, con permiso previo de la Secretaría de Relaciones Exteriores. Le explicamos qué aplica a su caso."),
                ("Heredé una casa en México, ¿qué tengo que hacer?",
                 "Por lo general es necesario tramitar un juicio sucesorio (testamentario o intestamentario) antes de poner la propiedad a su nombre o venderla. Según el caso, puede hacerse ante notario o ante un juzgado. Revisamos sus documentos y le indicamos la mejor vía."),
                ("Además de los honorarios, ¿qué otros gastos hay?",
                 "Normalmente hay honorarios notariales, impuesto sobre adquisición de inmuebles, derechos de registro, avalúo y, para quien vende, posible ISR por la ganancia. Los montos varían según el municipio y el valor; le damos un estimado antes de que decida."),
            ],
        },
    },
    # ------------------------------------------------------------ FAMILY & CIVIL
    "family": {
        "icon": "family", "country": "mx",
        "en": {
            "name": "Family & Civil Law in Mexico",
            "card": "Divorce, child custody and support, wills, inheritance and evictions in Mexican courts.",
            "h1": "Family and civil matters in Mexico, handled with care",
            "lead": "Family matters are personal and often urgent. We represent you in Mexico, explain each step in plain language, and help you avoid unnecessary trips across the border.",
            "served": "Jalisco, Michoacán and Colima",
            "intro": [
                "Many of our clients live in the United States but still have family, property or a marriage registered in Mexico. A divorce, a custody arrangement or an inheritance there has to follow Mexican law and go through Mexican courts or notaries.",
                "We handle the case locally and keep you informed by phone, WhatsApp, video call or email. When your participation is required, we'll tell you in advance and help you plan for it.",
            ],
            "items": [
                ("Divorce", "Uncontested and contested divorce, including division of property and recognition of divorces obtained abroad."),
                ("Child custody and support", "Custody (guarda y custodia), visitation, child support (pensión alimenticia) and modifications."),
                ("Wills and inheritance", "Wills before a Mexican notary and succession proceedings, with or without a will."),
                ("Evictions and leases", "Lease agreements, collection of unpaid rent and eviction proceedings for property owners."),
                ("Other civil matters", "Civil registry corrections, contracts and collection of debts."),
            ],
            "steps": [
                ("Free consultation", "We listen to your situation and explain your options and what to realistically expect."),
                ("Document gathering", "We tell you which documents are needed (birth and marriage certificates, deeds, etc.) and help you obtain them."),
                ("Filing", "We prepare and file the case or the notarial procedure in the correct jurisdiction."),
                ("Representation", "We attend hearings and appointments for you and report back after each one."),
                ("Resolution", "We follow through until the judgment or deed is final and registered where needed."),
            ],
            "faqs": [
                ("Can I get divorced in Mexico if I live in the U.S.?",
                 "Often, yes. In many Mexican states a divorce can be granted even if only one spouse wants it, and much of the process can be handled by a representative with a power of attorney. Some hearings may require your participation, sometimes by video. We'll explain what applies to your case and state."),
                ("Is a divorce from the U.S. valid in Mexico?",
                 "A foreign divorce generally has to be recognized by a Mexican court (homologación) before it takes effect in Mexico, for example to update the civil registry or to remarry there. We handle that process."),
                ("Should I have a will in Mexico if I already have one in the U.S.?",
                 "If you own property in Mexico, a Mexican will made before a notary can make the inheritance much simpler for your family. We can coordinate it so it works alongside your U.S. estate plan."),
                ("How long does an eviction take?",
                 "It depends on the lease, the court and whether the tenant contests. We'll review your documents and give you a realistic estimate at the start."),
            ],
        },
        "es": {
            "name": "Derecho familiar y civil en México",
            "card": "Divorcios, guarda y custodia, pensión alimenticia, testamentos, sucesiones y desalojos.",
            "h1": "Asuntos familiares y civiles en México, atendidos con sensibilidad",
            "lead": "Los asuntos familiares son personales y muchas veces urgentes. Le representamos en México, le explicamos cada paso con claridad y le ayudamos a evitar viajes innecesarios.",
            "served": "Jalisco, Michoacán y Colima",
            "intro": [
                "Muchos de nuestros clientes viven en Estados Unidos, pero tienen familia, bienes o un matrimonio registrado en México. Un divorcio, una custodia o una herencia en México deben seguir la ley mexicana y tramitarse ante juzgados o notarías mexicanas.",
                "Nosotros llevamos el asunto en México y le mantenemos al tanto por teléfono, WhatsApp, videollamada o correo. Cuando se requiera su participación, se lo avisamos con anticipación y le ayudamos a organizarse.",
            ],
            "items": [
                ("Divorcio", "Divorcio voluntario e incausado, liquidación de la sociedad conyugal y reconocimiento de divorcios del extranjero."),
                ("Guarda, custodia y pensión", "Guarda y custodia, régimen de convivencias, pensión alimenticia y sus modificaciones."),
                ("Testamentos y sucesiones", "Testamento público ante notario y juicios sucesorios testamentarios e intestamentarios."),
                ("Arrendamiento y desalojos", "Contratos de arrendamiento, cobro de rentas y juicios de desahucio para propietarios."),
                ("Otros asuntos civiles", "Rectificación de actas, contratos y cobranza."),
            ],
            "steps": [
                ("Consulta gratuita", "Escuchamos su situación y le explicamos sus opciones y lo que puede esperar de forma realista."),
                ("Documentación", "Le indicamos qué documentos se necesitan (actas, escrituras, etc.) y le ayudamos a conseguirlos."),
                ("Presentación", "Preparamos y presentamos la demanda o el trámite notarial en la jurisdicción correcta."),
                ("Representación", "Acudimos a audiencias y citas en su nombre y le informamos después de cada una."),
                ("Resolución", "Damos seguimiento hasta que la sentencia o escritura quede firme e inscrita donde corresponda."),
            ],
            "faqs": [
                ("¿Me puedo divorciar en México si vivo en Estados Unidos?",
                 "En muchos casos, sí. En varios estados de México el divorcio procede aunque solo uno de los cónyuges lo solicite, y buena parte del trámite puede llevarla un representante con poder notarial. Algunas audiencias pueden requerir su participación, a veces por videollamada. Le explicamos qué aplica en su caso."),
                ("¿Mi divorcio de Estados Unidos es válido en México?",
                 "Por lo general, una sentencia de divorcio extranjera debe reconocerse ante un juez mexicano (homologación) para surtir efectos en México, por ejemplo para anotarla en el Registro Civil o volver a casarse. Nosotros llevamos ese trámite."),
                ("Si ya tengo testamento en EE. UU., ¿necesito uno en México?",
                 "Si tiene bienes en México, un testamento público ante notario mexicano puede facilitar mucho la herencia para su familia. Podemos coordinarlo para que sea compatible con su planeación en Estados Unidos."),
                ("¿Cuánto tarda un juicio de desahucio?",
                 "Depende del contrato, del juzgado y de si el inquilino se defiende. Revisamos sus documentos y le damos un estimado realista desde el inicio."),
            ],
        },
    },
    # ------------------------------------------------------------ POA & APOSTILLE
    "poa": {
        "icon": "stamp", "country": "both",
        "en": {
            "name": "Powers of Attorney & Apostille",
            "card": "Powers of attorney valid in Mexico and apostilles for U.S. and Mexican documents.",
            "h1": "Powers of attorney and apostilles, done right the first time",
            "lead": "A power of attorney lets someone you trust act for you in Mexico. An apostille makes a document from one country valid in the other. Small mistakes in either can cost weeks; we help you get them right.",
            "served": "Mexico and the U.S.",
            "intro": [
                "Most of our property, inheritance and court work for clients in the U.S. starts with a power of attorney (poder notarial). Mexican notaries and courts are strict about its wording, its scope and how it was signed and certified.",
                "Both Mexico and the United States belong to the Hague Apostille Convention, so public documents such as birth certificates, divorce decrees and notarized powers can be apostilled for use in the other country. We tell you which authority issues the apostille for each document and handle the process when possible.",
            ],
            "items": [
                ("Powers of attorney for Mexico", "General or specific powers for property, lawsuits, banking or family matters, drafted to meet Mexican requirements."),
                ("Signing options", "Guidance on signing at a Mexican consulate or before a U.S. notary with apostille, whichever fits your case."),
                ("U.S. documents for Mexico", "Apostille of Washington, Arizona and other state documents for use in Mexico."),
                ("Mexican documents for the U.S.", "Apostille of Mexican birth, marriage and other certificates for use in the U.S."),
                ("Translations", "Coordination of certified translations when the receiving authority requires them."),
            ],
            "steps": [
                ("Tell us the purpose", "What the power or document will be used for determines how it must be drafted and certified."),
                ("Drafting and review", "We draft the power of attorney or review your document and list exactly what's needed."),
                ("Signing", "We guide you through signing at the consulate or before a notary, with an appointment checklist."),
                ("Apostille", "We submit to, or guide you through, the correct state or federal authority for the apostille."),
                ("Delivery and use", "We receive the document in Mexico and, if needed, have it formalized before a Mexican notary."),
            ],
            "faqs": [
                ("Where do I sign a power of attorney for Mexico if I live in the U.S.?",
                 "Two common options: at a Mexican consulate, which can act as a notary, or before a U.S. notary followed by an apostille from the Secretary of State of that U.S. state. Which one is better depends on what the power will be used for; we'll recommend the right route."),
                ("What is an apostille?",
                 "An apostille is a certificate that confirms a public document is authentic so it can be used in another country that belongs to the Hague Convention. It is issued by the government of the country (and often the state) where the document was issued, not by the country where it will be used."),
                ("Does the document need to be translated?",
                 "Often, yes. Mexican authorities usually require an official Spanish translation of English documents, and U.S. agencies require English translations of Spanish documents. We'll tell you when it's needed."),
                ("How long is a power of attorney valid?",
                 "It depends on how it is drafted. A power can be granted for a specific act or for a set period, and it can be revoked. We'll draft it so it covers what you need and nothing more."),
            ],
        },
        "es": {
            "name": "Poderes notariales y apostilla",
            "card": "Poderes notariales válidos en México y apostilla de documentos de EE. UU. y de México.",
            "h1": "Poderes notariales y apostillas, bien hechos desde la primera vez",
            "lead": "Un poder notarial permite que una persona de su confianza actúe por usted en México. La apostilla hace que un documento de un país sea válido en el otro. Un pequeño error en cualquiera de los dos puede costar semanas; le ayudamos a hacerlo bien.",
            "served": "México y Estados Unidos",
            "intro": [
                "La mayoría de los trámites de propiedades, herencias y juicios para clientes que viven en Estados Unidos empieza con un poder notarial. Las notarías y los juzgados en México son estrictos con su redacción, sus alcances y la forma en que se firmó y certificó.",
                "Tanto México como Estados Unidos forman parte de la Convención de La Haya sobre la Apostilla, por lo que documentos públicos como actas de nacimiento, sentencias de divorcio y poderes notariales pueden apostillarse para usarse en el otro país. Le indicamos qué autoridad apostilla cada documento y, cuando es posible, hacemos el trámite por usted.",
            ],
            "items": [
                ("Poderes notariales para México", "Poderes generales o especiales para inmuebles, juicios, trámites bancarios o familiares, redactados conforme a la ley mexicana."),
                ("Opciones de firma", "Le orientamos para firmar en un consulado de México o ante notario en EE. UU. con apostilla, según su caso."),
                ("Documentos de EE. UU. para México", "Apostilla de documentos de Washington, Arizona y otros estados para usarse en México."),
                ("Documentos mexicanos para EE. UU.", "Apostilla de actas de nacimiento, matrimonio y otros documentos mexicanos para usarse en EE. UU."),
                ("Traducciones", "Coordinamos traducciones certificadas o por perito cuando la autoridad las requiere."),
            ],
            "steps": [
                ("Cuéntenos para qué es", "El uso que tendrá el poder o el documento define cómo debe redactarse y certificarse."),
                ("Redacción y revisión", "Redactamos el poder o revisamos su documento y le decimos exactamente qué se necesita."),
                ("Firma", "Le guiamos para firmar en el consulado o ante notario, con una lista de lo que debe llevar a su cita."),
                ("Apostilla", "Tramitamos o le guiamos ante la autoridad estatal o federal correcta para la apostilla."),
                ("Entrega y uso", "Recibimos el documento en México y, si hace falta, lo protocolizamos ante notario mexicano."),
            ],
            "faqs": [
                ("Si vivo en Estados Unidos, ¿dónde firmo un poder para México?",
                 "Hay dos opciones comunes: en un consulado de México, que puede actuar como notario, o ante un notario estadounidense con apostilla de la Secretaría de Estado de ese estado. La mejor opción depende del uso que tendrá el poder; le recomendamos la vía adecuada."),
                ("¿Qué es una apostilla?",
                 "Es una certificación que confirma que un documento público es auténtico para que pueda usarse en otro país miembro de la Convención de La Haya. La emite el gobierno del país (y muchas veces del estado) donde se expidió el documento, no el país donde se va a usar."),
                ("¿El documento necesita traducción?",
                 "Con frecuencia, sí. Las autoridades mexicanas suelen pedir traducción oficial al español de documentos en inglés, y las de EE. UU. piden traducción al inglés de documentos en español. Le avisamos cuándo es necesario."),
                ("¿Cuánto tiempo es válido un poder notarial?",
                 "Depende de cómo se redacte. Un poder puede otorgarse para un acto específico o por un plazo determinado, y puede revocarse. Lo redactamos para que cubra lo que usted necesita y nada más."),
            ],
        },
    },
    # ------------------------------------------------------------ OTHER MX
    "other": {
        "icon": "scales", "country": "mx",
        "en": {
            "name": "Other Mexico Representation",
            "card": "Commercial and business, criminal, labor, agrarian (ejido) and amparo matters in Mexico.",
            "h1": "Representation in Mexico beyond family and property",
            "lead": "Business disputes, labor claims, criminal proceedings, ejido land and constitutional amparo cases each follow their own rules and courts. We represent you and keep you informed in the language you prefer.",
            "served": "Jalisco, Michoacán and Colima",
            "intro": [
                "Some matters don't fit neatly into one category, or start in one area and lead to another. Having a team that knows the local courts and agencies, and that can explain them to you in English or Spanish, makes a real difference.",
                "We start by understanding what's at stake, explain the realistic options, and agree on a plan before taking any step.",
            ],
            "items": [
                ("Commercial and business", "Contracts, company formation in Mexico, collections and commercial disputes."),
                ("Criminal", "Defense and representation of victims within Mexico's accusatory criminal system."),
                ("Labor", "Representation of employers and workers, including mandatory conciliation and labor court claims."),
                ("Agrarian", "Ejido and communal land rights, transfers of parcel rights and agrarian court proceedings."),
                ("Amparo", "Constitutional amparo lawsuits to protect your rights against acts of authority."),
            ],
            "steps": [
                ("Free consultation", "We listen, review any documents and tell you honestly whether and how we can help."),
                ("Strategy", "We explain the procedure, timelines and costs, and agree on a plan with you."),
                ("Action", "We file, negotiate or appear on your behalf before the court or authority."),
                ("Updates", "You receive updates after every relevant development, in English or Spanish."),
                ("Close-out", "We follow through on the outcome, including enforcement or appeals if appropriate."),
            ],
            "faqs": [
                ("What is an amparo?",
                 "An amparo is a federal lawsuit in Mexico used to protect constitutional rights against acts or laws of an authority, for example an arrest order, a fine or a government decision. Deadlines to file are short, so it's important to act quickly."),
                ("I have a labor dispute in Mexico. Do I have to go to court right away?",
                 "In most cases, no. Since Mexico's labor reform, most claims must first go through a mandatory conciliation stage before a labor court case can be filed. We represent you in both stages."),
                ("Can I sell or transfer ejido land?",
                 "Ejido land has special rules. Parcel rights can be transferred only under certain conditions, and turning ejido land into private property requires a specific procedure. We'll review the documents and explain what's possible."),
                ("Can you help if I'm in the U.S. and the criminal case is in Mexico?",
                 "Yes, we can review the situation and, where appropriate, represent you or a family member in Mexico. Criminal matters are time-sensitive, so please contact us as soon as possible."),
            ],
        },
        "es": {
            "name": "Otros asuntos legales en México",
            "card": "Asuntos mercantiles, penales, laborales, agrarios (ejidos) y juicio de amparo en México.",
            "h1": "Representación legal en México más allá de lo familiar y lo inmobiliario",
            "lead": "Un conflicto mercantil, una demanda laboral, un proceso penal, un asunto ejidal o un juicio de amparo tienen reglas y tribunales propios. Le representamos y le mantenemos informado en el idioma que prefiera.",
            "served": "Jalisco, Michoacán y Colima",
            "intro": [
                "Algunos asuntos no encajan en una sola materia, o empiezan en una y terminan en otra. Contar con un equipo que conoce los juzgados y dependencias locales, y que se lo explica con claridad, hace la diferencia.",
                "Primero entendemos qué está en juego, le explicamos las opciones reales y acordamos un plan con usted antes de dar cualquier paso.",
            ],
            "items": [
                ("Mercantil y empresarial", "Contratos, constitución de sociedades en México, cobranza y juicios mercantiles."),
                ("Penal", "Defensa y asesoría a víctimas dentro del sistema penal acusatorio."),
                ("Laboral", "Representación de patrones y trabajadores, incluida la conciliación prejudicial y los juicios laborales."),
                ("Agrario", "Derechos ejidales y comunales, cesión de derechos parcelarios y juicios ante tribunales agrarios."),
                ("Amparo", "Juicio de amparo para proteger sus derechos frente a actos de autoridad."),
            ],
            "steps": [
                ("Consulta gratuita", "Le escuchamos, revisamos sus documentos y le decimos con honestidad si podemos ayudarle y cómo."),
                ("Estrategia", "Le explicamos el procedimiento, los tiempos y los costos, y acordamos un plan."),
                ("Acción", "Presentamos, negociamos o comparecemos en su nombre ante el juzgado o la autoridad."),
                ("Seguimiento", "Le informamos de cada avance importante, en español o en inglés."),
                ("Cierre", "Damos seguimiento al resultado, incluida su ejecución o los recursos que procedan."),
            ],
            "faqs": [
                ("¿Qué es un juicio de amparo?",
                 "Es un juicio federal que protege sus derechos constitucionales frente a actos o leyes de una autoridad, por ejemplo una orden de aprehensión, una multa o una resolución de gobierno. Los plazos para promoverlo son cortos, por eso es importante actuar rápido."),
                ("Tengo un conflicto laboral en México, ¿tengo que ir directo a juicio?",
                 "En la mayoría de los casos, no. Desde la reforma laboral, casi todos los asuntos deben pasar primero por una etapa de conciliación obligatoria antes de presentar demanda ante el tribunal laboral. Le representamos en ambas etapas."),
                ("¿Puedo vender o ceder un terreno ejidal?",
                 "Las tierras ejidales tienen reglas especiales. Los derechos parcelarios solo pueden cederse bajo ciertas condiciones, y convertir una parcela en propiedad privada (dominio pleno) requiere un procedimiento específico. Revisamos sus documentos y le explicamos qué es posible."),
                ("Vivo en Estados Unidos y el asunto penal es en México, ¿me pueden ayudar?",
                 "Sí. Podemos revisar la situación y, cuando proceda, representarle a usted o a su familiar en México. Los asuntos penales son urgentes; comuníquese con nosotros cuanto antes."),
            ],
        },
    },
    # ------------------------------------------------------------ IMMIGRATION
    "immigration": {
        "icon": "globe", "country": "us",
        "en": {
            "name": "U.S. Immigration",
            "card": "Citizenship, adjustment of status (green card), family petitions and visas.",
            "h1": "U.S. immigration, explained clearly in your language",
            "lead": "Immigration paperwork is detailed and the stakes are high. We help you understand your options, prepare complete applications and stay on top of every notice and deadline.",
            "served": "Clients in Washington State, Arizona and beyond (U.S. immigration is federal)",
            "intro": [
                "U.S. immigration is handled by federal agencies such as U.S. Citizenship and Immigration Services (USCIS) and the Department of State. Each benefit has its own eligibility rules, forms, evidence and fees, and a missing document can mean months of delay.",
                "We review your history first, tell you honestly what you may qualify for, and then prepare and track your case from filing to decision.",
            ],
            "items": [
                ("Citizenship (naturalization)", "Eligibility review, Form N-400, and preparation for the interview and civics test."),
                ("Adjustment of status", "Applying for a green card from inside the U.S., including work and travel permits."),
                ("Family petitions", "Petitions for spouses, children, parents and siblings."),
                ("Visas", "Guidance on family-based and other visa options and consular processing."),
                ("Renewals and replacements", "Green card renewal, removal of conditions and replacement documents."),
            ],
            "steps": [
                ("Free consultation", "We review your immigration history and goals and explain which options may be available."),
                ("Eligibility and plan", "You receive a clear list of forms, evidence and government fees for your case."),
                ("Preparation", "We prepare the application, review every document and translation, and check for issues before filing."),
                ("Filing and tracking", "We file with the government and track receipts, biometrics appointments and notices."),
                ("Interview and decision", "We help you prepare for any interview and advise you on next steps after the decision."),
            ],
            "faqs": [
                ("Can you guarantee my application will be approved?",
                 "No one can honestly guarantee an immigration result; decisions are made by the government. What we can do is review your eligibility carefully, prepare a complete application and help you avoid common mistakes."),
                ("Is a \"notario\" the same as a lawyer?",
                 "No. In the United States, a notary public is not a lawyer and is not authorized to give legal advice or represent you in immigration matters. Only licensed attorneys and accredited representatives may do so. Be cautious of anyone offering immigration help without those credentials."),
                ("How long does the process take?",
                 "Processing times vary by benefit and office and change often. USCIS publishes current estimates on its website, and we'll tell you what to expect for your specific case."),
                ("I have a past immigration or criminal issue. Can I still apply?",
                 "Possibly, but it's essential to review it before filing anything. Some issues can be overcome and others create serious risks. Tell us about it during your consultation so we can advise you properly."),
            ],
        },
        "es": {
            "name": "Inmigración en Estados Unidos",
            "card": "Ciudadanía, ajuste de estatus (green card), peticiones familiares y visas.",
            "h1": "Inmigración en Estados Unidos, explicada con claridad y en su idioma",
            "lead": "Los trámites migratorios son detallados y lo que está en juego es mucho. Le ayudamos a entender sus opciones, preparar solicitudes completas y estar al pendiente de cada aviso y fecha límite.",
            "served": "Clientes en Washington, Arizona y otros estados (la inmigración es materia federal)",
            "intro": [
                "La inmigración en Estados Unidos está a cargo de dependencias federales como el Servicio de Ciudadanía e Inmigración (USCIS) y el Departamento de Estado. Cada trámite tiene sus propios requisitos, formularios, pruebas y cuotas, y un documento faltante puede significar meses de retraso.",
                "Primero revisamos su historial, le decimos con honestidad para qué podría calificar y luego preparamos y damos seguimiento a su caso hasta la resolución.",
            ],
            "items": [
                ("Ciudadanía (naturalización)", "Revisión de requisitos, Formulario N-400 y preparación para la entrevista y el examen de civismo."),
                ("Ajuste de estatus", "Solicitud de residencia permanente (green card) desde Estados Unidos, con permisos de trabajo y de viaje."),
                ("Peticiones familiares", "Peticiones para cónyuges, hijos, padres y hermanos."),
                ("Visas", "Orientación sobre visas familiares y otras opciones, y trámite consular."),
                ("Renovaciones y reposiciones", "Renovación de green card, remoción de condiciones y reposición de documentos."),
            ],
            "steps": [
                ("Consulta gratuita", "Revisamos su historial migratorio y sus metas y le explicamos qué opciones podría tener."),
                ("Requisitos y plan", "Le damos una lista clara de formularios, pruebas y cuotas de gobierno para su caso."),
                ("Preparación", "Preparamos la solicitud, revisamos cada documento y traducción, y detectamos problemas antes de enviarla."),
                ("Envío y seguimiento", "Enviamos la solicitud y damos seguimiento a recibos, citas de biométricos y avisos."),
                ("Entrevista y resolución", "Le preparamos para la entrevista y le orientamos sobre los siguientes pasos."),
            ],
            "faqs": [
                ("¿Me pueden garantizar que aprueben mi solicitud?",
                 "Nadie puede garantizar honestamente un resultado migratorio; la decisión la toma el gobierno. Lo que sí hacemos es revisar a fondo su elegibilidad, preparar una solicitud completa y ayudarle a evitar errores comunes."),
                ("¿Un \"notario\" es lo mismo que un abogado?",
                 "No. En Estados Unidos, un notario público no es abogado y no está autorizado para dar asesoría legal ni representarle en asuntos migratorios. Solo pueden hacerlo abogados con licencia y representantes acreditados. Tenga cuidado con quien ofrezca trámites migratorios sin esas credenciales."),
                ("¿Cuánto tarda el trámite?",
                 "Los tiempos varían según el trámite y la oficina, y cambian con frecuencia. USCIS publica estimados actualizados en su sitio web y le diremos qué esperar en su caso."),
                ("Tuve un problema migratorio o penal en el pasado, ¿todavía puedo aplicar?",
                 "Posiblemente, pero es indispensable revisarlo antes de presentar cualquier solicitud. Algunos problemas tienen solución y otros implican riesgos serios. Coméntenoslo en su consulta para orientarle correctamente."),
            ],
        },
    },
    # ------------------------------------------------------------ WA LLC
    "llc": {
        "icon": "building", "country": "us",
        "en": {
            "name": "Washington LLC & Corporation Formation",
            "card": "Start your business the right way: LLC or corporation formation in Washington State.",
            "h1": "Form your Washington LLC or corporation with confidence",
            "lead": "Starting a business is exciting. Setting it up correctly from day one protects you and saves headaches later. We guide you through every step, in English or Spanish.",
            "served": "Washington State",
            "intro": [
                "In Washington, LLCs and corporations are formed by filing with the Secretary of State, and most businesses also need a state business license, a federal tax ID (EIN) and an internal agreement between the owners. Each step has its own requirements.",
                "We help you choose the right structure, file the formation documents, and set up the basics so your business is ready to open a bank account, sign contracts and hire.",
            ],
            "items": [
                ("Entity selection", "Understanding the practical differences between an LLC and a corporation for your situation."),
                ("Name availability", "Checking that your business name is available and meets state rules."),
                ("Formation filing", "Certificate of Formation (LLC) or Articles of Incorporation (corporation) with the Secretary of State."),
                ("Operating agreement or bylaws", "The internal rules for owners: ownership, decisions, and what happens if someone leaves."),
                ("EIN and business license", "Federal tax ID and Washington business license registration, plus a compliance calendar for annual reports."),
            ],
            "steps": [
                ("Free consultation", "We talk about your business, your partners and your goals."),
                ("Structure and name", "We recommend a structure and confirm your name is available."),
                ("Filing", "We prepare and file the formation documents and designate a registered agent."),
                ("Internal documents", "We draft your operating agreement or bylaws and initial resolutions."),
                ("Ready to operate", "We help with the EIN and business license and give you a list of ongoing obligations."),
            ],
            "faqs": [
                ("Do I need to be a U.S. citizen to form an LLC in Washington?",
                 "No. U.S. citizenship and residency are generally not required to form an LLC. Non-residents may face extra steps for the EIN and for opening a bank account, and we'll explain them."),
                ("What is a registered agent?",
                 "Every Washington LLC and corporation must have a registered agent with a physical address in Washington to receive official legal notices. It can be an owner who lives in the state or a commercial service."),
                ("LLC or corporation: which is better?",
                 "It depends on how many owners you have, how you plan to pay yourself, and whether you'll seek investors. Taxes are an important part of the decision, so we may suggest you also consult your accountant."),
                ("What do I have to do after the LLC is formed?",
                 "Washington requires an annual report and renewal with the Secretary of State, and you'll need to keep your business license, tax registrations and registered agent up to date. We'll give you a simple checklist."),
            ],
        },
        "es": {
            "name": "Constitución de LLC y corporaciones en Washington",
            "card": "Abra su empresa correctamente: constitución de LLC o corporación en el estado de Washington.",
            "h1": "Constituya su LLC o corporación en Washington con seguridad",
            "lead": "Emprender es emocionante. Hacerlo bien desde el primer día le protege y le ahorra problemas después. Le acompañamos en cada paso, en español o en inglés.",
            "served": "Estado de Washington",
            "intro": [
                "En Washington, las LLC y las corporaciones se constituyen mediante un registro ante la Secretaría de Estado (Secretary of State). La mayoría de los negocios también necesita una licencia comercial estatal, un número de identificación fiscal federal (EIN) y un acuerdo interno entre los socios. Cada paso tiene sus propios requisitos.",
                "Le ayudamos a elegir la estructura adecuada, presentar los documentos de constitución y dejar listo lo básico para que su negocio pueda abrir una cuenta bancaria, firmar contratos y contratar personal.",
            ],
            "items": [
                ("Tipo de empresa", "Le explicamos las diferencias prácticas entre una LLC y una corporación en su situación."),
                ("Disponibilidad del nombre", "Verificamos que el nombre de su negocio esté disponible y cumpla con las reglas del estado."),
                ("Registro de constitución", "Certificate of Formation (LLC) o Articles of Incorporation (corporación) ante la Secretaría de Estado."),
                ("Acuerdo operativo o estatutos", "Las reglas internas entre socios: participación, decisiones y qué pasa si alguien se retira."),
                ("EIN y licencia comercial", "Número fiscal federal y licencia comercial de Washington, más un calendario de reportes anuales."),
            ],
            "steps": [
                ("Consulta gratuita", "Platicamos sobre su negocio, sus socios y sus metas."),
                ("Estructura y nombre", "Le recomendamos una estructura y confirmamos que el nombre esté disponible."),
                ("Registro", "Preparamos y presentamos los documentos de constitución y designamos un agente registrado."),
                ("Documentos internos", "Redactamos su acuerdo operativo o estatutos y las resoluciones iniciales."),
                ("Listo para operar", "Le ayudamos con el EIN y la licencia comercial y le damos una lista de obligaciones continuas."),
            ],
            "faqs": [
                ("¿Necesito ser ciudadano estadounidense para abrir una LLC en Washington?",
                 "No. Por lo general no se requiere ciudadanía ni residencia para constituir una LLC. Quienes no residen en EE. UU. pueden tener pasos adicionales para obtener el EIN y abrir una cuenta bancaria; se los explicamos."),
                ("¿Qué es un agente registrado (registered agent)?",
                 "Toda LLC y corporación en Washington debe tener un agente registrado con domicilio físico en el estado para recibir notificaciones legales oficiales. Puede ser un socio que viva en Washington o un servicio comercial."),
                ("¿Qué me conviene más, LLC o corporación?",
                 "Depende de cuántos socios tenga, cómo planea pagarse y si buscará inversionistas. Los impuestos son parte importante de la decisión, por lo que también le podemos sugerir consultar a su contador."),
                ("¿Qué tengo que hacer después de abrir la LLC?",
                 "Washington exige un reporte anual y la renovación ante la Secretaría de Estado, y debe mantener al día su licencia comercial, registros fiscales y agente registrado. Le damos una lista sencilla."),
            ],
        },
    },
}

# ---------------------------------------------------------------- team
# Source: old site (arce-law.com/home, /gilberto, /alejandra), lightly copyedited.
# Facts are the firm's own published claims; ph() marks what still needs confirmation.
TEAM_MEMBERS = [
    {
        "name": "Gilberto Arce",
        "photo": "team-gilberto-arce-800x1000.jpg",
        "en": {
            "role": "Founder / Attorney",
            "summary": "Founded ARCE Law in 2009. Former head of the immigration legal department at the Mexican Consulate, focused on immigration and on U.S. clients with legal matters in Mexico.",
            "education": "Law degree, University of Guadalajara",
            "licensing": "Admitted to the Washington State Bar Association (2008); member, American Bar Association "
                         + ph("WSBA license type and number. The old bio calls him a 'Foreign Law Consultant', a limited license"),
            "languages": ph("languages spoken"),
            "bio": [
                "Gilberto, a Foreign Law Consultant, founded ARCE Law in 2009 to provide new and unique legal services in immigration and international law. He specializes in navigating complex immigration issues and in representing U.S. companies and individuals who invest, do business or have pending legal matters in Mexico. He received his law degree from the University of Guadalajara. Before his assignment to the Mexican Consulate, he practiced criminal and civil law with a private firm in Mexico.",
                "As a Consular Officer and Legal Advisor with domestic and international experience, Gilberto managed a variety of programs, including the Visa and Dual Citizenship Department, where he helped Mexican citizens apply for official government documents. As the Consulate's official liaison with the U.S. Department of Homeland Security, he worked closely with Immigration and Customs Enforcement on immigration and criminal matters. He also managed outreach programs, provided legal advice and consular assistance to Mexican citizens in immigration and criminal cases, and coordinated the safe repatriation of Mexican nationals and minors.",
                "Gilberto spent seven of his eight years at the Consulate as head of its immigration legal department, where he handled approximately 100 cases a month involving Mexican national petitioners and detainees in immigration proceedings, working with both petitioners and assigned defense counsel.",
                "Since 2007 he has also worked with various law firms as a consulting attorney in foreign and immigration law. In 2008, Gilberto was admitted to the Washington State Bar Association and became a member of the American Bar Association.",
            ],
        },
        "es": {
            "role": "Fundador / Abogado",
            "summary": "Fundó ARCE Law en 2009. Fue titular del departamento jurídico migratorio del Consulado de México; se enfoca en inmigración y en clientes de EE. UU. con asuntos legales en México.",
            "education": "Licenciatura en Derecho, Universidad de Guadalajara",
            "licensing": "Admitido en la Barra de Abogados del Estado de Washington (2008); miembro de la American Bar Association "
                         + ph("tipo y número de licencia WSBA. La biografía anterior dice 'Foreign Law Consultant', que es una licencia limitada"),
            "languages": ph("idiomas"),
            "bio": [
                "Gilberto, consultor en derecho extranjero (Foreign Law Consultant), fundó ARCE Law en 2009 para ofrecer servicios legales nuevos y especializados en materia migratoria y de derecho internacional. Se especializa en resolver asuntos migratorios complejos y en representar a empresas y personas de Estados Unidos que invierten, hacen negocios o tienen asuntos legales pendientes en México. Es licenciado en Derecho por la Universidad de Guadalajara. Antes de incorporarse al Consulado de México, ejerció en materia penal y civil en un despacho privado en México.",
                "Como funcionario consular y asesor jurídico, con experiencia nacional e internacional, Gilberto estuvo a cargo de diversos programas, entre ellos el Departamento de Visas y Doble Nacionalidad, donde apoyó a ciudadanos mexicanos en el trámite de documentos oficiales. Como enlace oficial entre el Consulado y el Departamento de Seguridad Nacional de Estados Unidos (DHS), colaboró de cerca con el Servicio de Inmigración y Control de Aduanas (ICE) en asuntos migratorios y penales. También coordinó programas de acercamiento con la comunidad, brindó asesoría legal y protección consular a mexicanos en casos migratorios y penales, y coordinó la repatriación segura de connacionales y menores.",
                "Durante siete de sus ocho años en el Consulado encabezó el departamento jurídico de asuntos migratorios, donde atendía aproximadamente 100 casos al mes de peticionarios y detenidos mexicanos en procesos migratorios, en coordinación con los propios peticionarios y con sus abogados defensores.",
                "Desde 2007 colabora con distintos despachos como abogado consultor en derecho extranjero y migratorio. En 2008 fue admitido en la Barra de Abogados del Estado de Washington y se incorporó a la American Bar Association.",
            ],
        },
    },
    {
        "name": "Alejandra Gomez Arce",
        "photo": None,
        "placeholder": "team-alejandra-gomez-arce-800x1000-PLACEHOLDER.jpg",
        "en": {
            "role": "Co-Founder / Attorney",
            "summary": "Co-founder of ARCE Law US and principal of ARCE Law Mexico. Attorney since 1984 in civil, family, commercial and criminal law.",
            "education": "Law degree, University of Guadalajara (1976); degree in accounting, University of Guadalajara (1994)",
            "licensing": "Attorney in Mexico since 1984; member, Jus Semper Loquitur of Jalisco, A.C. " + ph("cédula profesional number"),
            "languages": ph("languages spoken"),
            "bio": [
                "Alejandra Gomez Arce is the co-founder of ARCE Law US and the principal of ARCE Law Mexico. An attorney since 1984, she has experience in civil, family, commercial and criminal law, and has dedicated her practice to helping people resolve their conflicts with passion and dedication.",
                "Her career in law began in 1971 in the criminal department of the State Judicial Branch. She graduated from the University of Guadalajara School of Law in 1976 and, in 1994, also earned a degree in accounting from the University of Guadalajara School of Business.",
                "She is an active member of the professional attorneys' association Jus Semper Loquitur of Jalisco, A.C. From 2007 to 2009 she was the principal of AMS Law Mexico.",
            ],
        },
        "es": {
            "role": "Cofundadora / Abogada",
            "summary": "Cofundadora de ARCE Law US y titular de ARCE Law México. Abogada desde 1984 en materia civil, familiar, mercantil y penal.",
            "education": "Licenciatura en Derecho, Universidad de Guadalajara (1976); Licenciatura en Contaduría, Universidad de Guadalajara (1994)",
            "licensing": "Abogada en México desde 1984; miembro de Jus Semper Loquitur de Jalisco, A.C. " + ph("número de cédula profesional"),
            "languages": ph("idiomas"),
            "bio": [
                "Alejandra Gomez Arce es cofundadora de ARCE Law US y titular de ARCE Law México. Abogada en ejercicio desde 1984, cuenta con experiencia en materia civil, familiar, mercantil y penal, y ha dedicado su práctica a ayudar a las personas a resolver sus conflictos con pasión y entrega.",
                "Su trayectoria en el derecho comenzó en 1971 en el área penal del Poder Judicial del Estado. Se tituló de la Facultad de Derecho de la Universidad de Guadalajara en 1976 y, en 1994, obtuvo además la licenciatura en Contaduría por la misma universidad.",
                "Es miembro activo de la asociación profesional de abogados Jus Semper Loquitur de Jalisco, A.C. De 2007 a 2009 fue titular de AMS Law México.",
            ],
        },
    },
    {
        "name": "Ivan Bono",
        "photo": None,
        "placeholder": "team-ivan-bono-800x1000-PLACEHOLDER.jpg",
        "en": {"role": "Consulting Attorney", "summary": ph("2–3 sentence bio"),
               "education": ph("law school, degree, year"), "licensing": ph("cédula profesional / bar admission"),
               "languages": ph("languages spoken")},
        "es": {"role": "Abogado consultor", "summary": ph("biografía breve, 2–3 oraciones"),
               "education": ph("universidad, título, año"), "licensing": ph("cédula profesional / licencia"),
               "languages": ph("idiomas")},
    },
    {
        "name": "Fernanda Zavala",
        "photo": None,
        "placeholder": "team-fernanda-zavala-800x1000-PLACEHOLDER.jpg",
        "en": {"role": "Consulting Attorney", "summary": ph("2–3 sentence bio"),
               "education": ph("law school, degree, year"), "licensing": ph("cédula profesional / bar admission"),
               "languages": ph("languages spoken")},
        "es": {"role": "Abogada consultora", "summary": ph("biografía breve, 2–3 oraciones"),
               "education": ph("universidad, título, año"), "licensing": ph("cédula profesional / licencia"),
               "languages": ph("idiomas")},
    },
]
