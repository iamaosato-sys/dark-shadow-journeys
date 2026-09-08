# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "Dark Shadow Journeys"
DOMAIN = "https://www.darkshadowjourneys.com"
GA_ID = "G-XXXXXXXXXX"          # placeholder - replaced once the real GA4 property exists
GSC_VERIFY = "GSC-VERIFICATION-TOKEN-PLACEHOLDER"  # placeholder - replaced with real GSC meta content

NAV = [
    ("index.html", "Home"),
    ("destinations.html", "Destinations"),
    ("itineraries.html", "Itineraries"),
    ("ethics.html", "Our Ethics"),
    ("journal.html", "Journal"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

def head(title, description, slug, canonical_path):
    ga_snippet = ""
    if GA_ID and "XXXX" not in GA_ID:
        ga_snippet = f"""
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA_ID}');
  </script>"""
    gsc_meta = ""
    if GSC_VERIFY and "PLACEHOLDER" not in GSC_VERIFY:
        gsc_meta = f'\n  <meta name="google-site-verification" content="{GSC_VERIFY}" />'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{DOMAIN}/{canonical_path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{DOMAIN}/{canonical_path}">
<meta property="og:site_name" content="{SITE}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='6' fill='%23a8402f'/%3E%3C/svg%3E">
<link rel="stylesheet" href="styles.css">{gsc_meta}{ga_snippet}
</head>
"""

def nav_html(active):
    items = ""
    for href, label in NAV:
        cls = " active" if href == active else ""
        items += f'<li><a class="{cls.strip()}" href="{href}">{label}</a></li>'
    return f"""<header class="site">
  <div class="wrap nav">
    <a class="logo" href="index.html"><span class="mark"></span>Dark Shadow <b>Journeys</b></a>
    <ul class="links">{items}<li><a class="nav-cta" href="contact.html">Plan a Journey</a></li></ul>
    <button class="burger" aria-label="Menu">&#9776;</button>
  </div>
</header>
"""

def footer_html():
    return f"""<footer class="site">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>Dark Shadow Journeys</h4>
        <p style="max-width:320px;">A UK specialist in ethical dark tourism — journeys that bear witness, honour the dead, and deepen our understanding of human history. Every itinerary is researched and curated by a human specialist.</p>
      </div>
      <div>
        <h4>Destinations</h4>
        <ul>
          <li><a href="battlefields.html">Battlefields &amp; Conflict</a></li>
          <li><a href="genocide-memorials.html">Genocide &amp; Holocaust Memorials</a></li>
          <li><a href="nuclear-disaster.html">Nuclear &amp; Disaster Zones</a></li>
          <li><a href="witness-travel.html">Witness &amp; Humanitarian Travel</a></li>
          <li><a href="notorious-history.html">Crime &amp; Notorious History</a></li>
          <li><a href="death-rituals.html">Death Rituals &amp; Catacombs</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About</a></li>
          <li><a href="ethics.html">Our Ethics</a></li>
          <li><a href="itineraries.html">Itineraries</a></li>
          <li><a href="journal.html">Journal</a></li>
        </ul>
      </div>
      <div>
        <h4>Get In Touch</h4>
        <ul>
          <li><a href="contact.html">Enquire</a></li>
          <li><a href="mailto:hello@darkshadowjourneys.com">hello@darkshadowjourneys.com</a></li>
          <li>Fylde Coast, Lancashire, UK</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Dark Shadow Journeys. Registered in England &amp; Wales. Operating under a UK host travel agency ATOL umbrella.</span>
      <span>Aligned with the <a href="https://www.uclan.ac.uk/research/activity/institute-for-dark-tourism-research" target="_blank" rel="noopener">Institute for Dark Tourism Research, UCLan</a></span>
    </div>
  </div>
</footer>
<script src="script.js"></script>
</body>
</html>
"""

def page(slug, title, description, active_nav, body_html):
    html = head(title, description, slug, slug) + "<body>\n" + nav_html(active_nav) + body_html + footer_html()
    with open(os.path.join(ROOT, slug), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", slug)

PAGES_WRITTEN = []

# ---------- HOME ----------
home_body = """
<section class="hero">
  <div class="wrap hero-inner">
    <span class="eyebrow">UK Specialist &middot; Ethical Dark Tourism</span>
    <h1>Journeys into the places history would rather forget.</h1>
    <p class="lead">Dark Shadow Journeys designs deeply researched, ethically guided travel to the world's battlefields, memorials, disaster zones and sites of atrocity &mdash; for travellers who want to bear witness, not just take a photograph.</p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="contact.html">Start Planning a Journey</a>
      <a class="btn btn-outline" href="destinations.html">Explore Destinations</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="stat-row">
      <div class="stat"><b>$37.7bn</b><span>Global dark tourism market, 2026</span></div>
      <div class="stat"><b>6</b><span>Curated specialisms, worldwide</span></div>
      <div class="stat"><b>100%</b><span>Human-planned, human-guided</span></div>
      <div class="stat"><b>0</b><span>Selfie-culture itineraries</span></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Why Dark Shadow Journeys</span>
    <h2>Travel that means something, built by people who take it seriously.</h2>
    <p class="lead" style="max-width:760px;">Anyone can book a flight to Krak&oacute;w. Understanding what to feel, how to behave, and what it means to stand at Birkenau or Srebrenica or Pripyat takes context an algorithm cannot give you. That is the entire reason we exist.</p>
    <div class="grid grid-3" style="margin-top:40px;">
      <div class="card"><span class="tag">01</span><h3>Vetted, ethical guides</h3><p>Every local guide and ground operator is checked for accreditation, community standing, and a genuine connection to the place &mdash; never a generic city-tour reseller.</p></div>
      <div class="card"><span class="tag">02</span><h3>Emotional preparation</h3><p>You receive a pre-trip briefing on what to expect, how to behave, and how to process what you see &mdash; and a debrief afterwards, because these journeys stay with people.</p></div>
      <div class="card"><span class="tag">03</span><h3>Academically grounded</h3><p>Our framework is aligned with the Institute for Dark Tourism Research (iDTR) at UCLan &mdash; the world's only dedicated academic centre for this field.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Explore By Theme</span>
    <h2>Six ways the world remembers.</h2>
    <div class="grid grid-3">
      <div class="card"><span class="tag">Conflict</span><h3>Battlefields &amp; Conflict</h3><p>Normandy, the Somme, Berlin, Hiroshima, the Korean DMZ &mdash; the ground where the twentieth century was decided.</p><a class="more" href="battlefields.html">View destinations &rarr;</a></div>
      <div class="card"><span class="tag">Memory</span><h3>Genocide &amp; Holocaust Memorials</h3><p>Auschwitz-Birkenau, Kigali, Phnom Penh, Yad Vashem &mdash; travel as an act of remembrance and education.</p><a class="more" href="genocide-memorials.html">View destinations &rarr;</a></div>
      <div class="card"><span class="tag">Disaster</span><h3>Nuclear &amp; Disaster Zones</h3><p>Chernobyl, Fukushima, Bikini Atoll, Trinity Site &mdash; the frontier where human ambition met catastrophe.</p><a class="more" href="nuclear-disaster.html">View destinations &rarr;</a></div>
      <div class="card"><span class="tag">Witness</span><h3>Witness &amp; Humanitarian Travel</h3><p>Sarajevo, Srebrenica, Mostar, Robben Island, Belfast &mdash; recent history, told by the people who lived it.</p><a class="more" href="witness-travel.html">View destinations &rarr;</a></div>
      <div class="card"><span class="tag">History</span><h3>Crime &amp; Notorious History</h3><p>Alcatraz, Salem, Jonestown &mdash; handled as history, never as spectacle.</p><a class="more" href="notorious-history.html">View destinations &rarr;</a></div>
      <div class="card"><span class="tag">Ritual</span><h3>Death Rituals &amp; Catacombs</h3><p>The Paris Catacombs, the Capuchin Crypt, Edinburgh's vaults &mdash; how cultures have faced mortality itself.</p><a class="more" href="death-rituals.html">View destinations &rarr;</a></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="grid grid-2" style="align-items:center;">
      <div>
        <span class="eyebrow">Signature Itinerary</span>
        <h2>Sarajevo Survivor &mdash; 7 Days, Bosnia &amp; Herzegovina</h2>
        <p>Europe's most recent genocide, understood through the people who survived it: the siege tunnel, the War Childhood Museum, and a full day at the Srebrenica Memorial Centre and Cemetery. Bosnia remains almost entirely unserved by UK dark tourism specialists &mdash; and it may be the most quietly profound journey we offer.</p>
        <a class="btn btn-outline" href="itineraries.html">See the full itinerary &rarr;</a>
      </div>
      <div class="quote-block">&ldquo;Every journey is researched, curated, and supported by a human specialist who treats these places with the gravity they deserve.&rdquo;</div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <span class="eyebrow">Begin</span>
    <h2>Tell us what you want to understand.</h2>
    <p class="lead" style="max-width:600px;margin:0 auto 30px;">A short conversation is all it takes to start building an itinerary around the history that matters to you.</p>
    <a class="btn btn-primary" href="contact.html">Enquire Now</a>
  </div>
</section>
"""
page("index.html", f"{SITE} | UK Specialist in Ethical Dark Tourism", "UK specialist travel agent for ethical dark tourism: battlefields, genocide memorials, nuclear disaster zones and sites of historic atrocity, worldwide.", "index.html", home_body)

# ---------- DESTINATIONS HUB ----------
dest_body = """
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> / Destinations</div>
    <span class="eyebrow">Destinations</span>
    <h1>Six ways the world remembers.</h1>
    <p class="lead">Dark tourism is not one thing. Each of the categories below carries its own history, its own ethics, and its own kind of client. Choose a theme to see the sites we work with, who they tend to matter to, and how we approach them.</p>
  </div>
</section>
<section>
  <div class="wrap grid grid-3">
    <div class="card"><span class="tag">Conflict &amp; Battlefield</span><h3>Battlefields &amp; Conflict</h3><p>Normandy, Ypres, the Somme, Berlin, Hiroshima &amp; Nagasaki, Vietnam, the Falklands, the Korean DMZ.</p><a class="more" href="battlefields.html">Explore &rarr;</a></div>
    <div class="card"><span class="tag">Holocaust &amp; Genocide</span><h3>Genocide &amp; Holocaust Memorials</h3><p>Auschwitz-Birkenau, Krak&oacute;w, Dachau, Yad Vashem, Kigali, Phnom Penh.</p><a class="more" href="genocide-memorials.html">Explore &rarr;</a></div>
    <div class="card"><span class="tag">Nuclear &amp; Industrial</span><h3>Nuclear &amp; Disaster Zones</h3><p>Chernobyl &amp; Pripyat, Fukushima, Bikini Atoll, Trinity Site, Centralia.</p><a class="more" href="nuclear-disaster.html">Explore &rarr;</a></div>
    <div class="card"><span class="tag">Witness &amp; Humanitarian</span><h3>Witness &amp; Humanitarian Travel</h3><p>Srebrenica, Mostar, Sarajevo, Robben Island, Belfast's Troubles history.</p><a class="more" href="witness-travel.html">Explore &rarr;</a></div>
    <div class="card"><span class="tag">Crime &amp; Notorious History</span><h3>Crime &amp; Notorious History</h3><p>Alcatraz, Salem, Jonestown &mdash; handled as history, never spectacle.</p><a class="more" href="notorious-history.html">Explore &rarr;</a></div>
    <div class="card"><span class="tag">Death &amp; Ritual</span><h3>Death Rituals &amp; Catacombs</h3><p>The Paris Catacombs, the Capuchin Crypt, Edinburgh's vaults, New Orleans.</p><a class="more" href="death-rituals.html">Explore &rarr;</a></div>
  </div>
</section>
<section class="cta-band"><div class="wrap"><h2>Not sure where to start?</h2><p class="lead" style="max-width:560px;margin:0 auto 26px;">Belfast is our lowest-barrier introductory journey; Sarajevo is our signature. Tell us what draws you and we'll suggest a starting point.</p><a class="btn btn-primary" href="contact.html">Ask Us Where To Begin</a></div></section>
"""
page("destinations.html", f"Dark Tourism Destinations Worldwide | {SITE}", "Explore six categories of dark tourism worldwide: battlefields, genocide memorials, nuclear disaster zones, witness travel, notorious history and death rituals.", "destinations.html", dest_body)

def dest_page(slug, tag, title_h1, intro, sites, client_profile, our_approach, related_itinerary):
    site_items = "".join(f"<li><b>{name}</b> ({loc}) &mdash; {desc}</li>" for name, loc, desc in sites)
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="destinations.html">Destinations</a> / {title_h1}</div>
    <span class="eyebrow">{tag}</span>
    <h1>{title_h1}</h1>
    <p class="lead">{intro}</p>
  </div>
</section>
<section>
  <div class="wrap grid grid-2" style="align-items:start;">
    <div>
      <h2>Sites we work with</h2>
      <ul class="site-list">{site_items}</ul>
    </div>
    <div>
      <h2>Who this journey is for</h2>
      <p>{client_profile}</p>
      <h2 style="margin-top:36px;">Our approach here</h2>
      <p>{our_approach}</p>
      <a class="btn btn-outline" href="{related_itinerary}">See a related itinerary &rarr;</a>
    </div>
  </div>
</section>
<section class="cta-band"><div class="wrap"><h2>Ready to talk it through?</h2><a class="btn btn-primary" href="contact.html">Enquire About This Theme</a></div></section>
"""
    page(slug, f"{title_h1} | Dark Tourism | {SITE}", f"{intro[:150]}", slug, body)

dest_page(
  "battlefields.html", "Conflict &amp; Battlefield Tourism", "Battlefields &amp; Conflict",
  "The largest and most personal segment of dark tourism &mdash; ground where the twentieth century's wars were decided, and where many UK families still have a direct connection.",
  [
    ("Normandy D-Day Beaches", "France", "Omaha, Gold, Juno and Sword sectors; the American Cemetery; Pointe du Hoc."),
    ("Ypres &amp; the Somme", "Belgium / France", "The Menin Gate Last Post ceremony, Thiepval Memorial, preserved trench lines."),
    ("Berlin Wall Route", "Germany", "Checkpoint Charlie, the East Side Gallery, the Stasi Museum."),
    ("Hiroshima &amp; Nagasaki", "Japan", "The Peace Memorial Museum and the Atomic Bomb Dome."),
    ("Vietnam War Sites", "Vietnam", "The Cu Chi tunnels, the War Remnants Museum, Hue Citadel."),
    ("Korean DMZ", "South Korea", "One of the world's most heavily fortified borders, and a uniquely tense living history site."),
  ],
  "Families researching veteran relatives, history and military enthusiasts, school and university groups, and anniversary pilgrims &mdash; the 80th D-Day anniversary in 2024 showed this demand is not slowing down.",
  "We build itineraries around anniversaries, opening hours, and ceremony timings you'd otherwise miss, and connect you with licensed battlefield historians rather than generic coach-tour guides.",
  "itineraries.html#normandy"
)

dest_page(
  "genocide-memorials.html", "Holocaust &amp; Genocide Memorial Tourism", "Genocide &amp; Holocaust Memorials",
  "The single largest attraction type in dark tourism, and the one demanding the most careful, respectful handling &mdash; exactly the territory where a human specialist matters most.",
  [
    ("Auschwitz-Birkenau", "Poland", "Over two million visitors a year; advance booking and a licensed guide are required."),
    ("Krak&oacute;w Jewish Quarter", "Poland", "Schindler's Factory Museum and the Kazimierz district."),
    ("Treblinka, Majdanek &amp; Sobibor", "Poland", "Off the beaten track and powerful precisely because they are quieter."),
    ("Dachau", "Germany", "Often the first Holocaust memorial site visitors ever see, a short trip from Munich."),
    ("Yad Vashem", "Israel", "The world's primary Holocaust memorial, museum and research centre."),
    ("Kigali Genocide Memorial", "Rwanda", "The 1994 Tutsi genocide, and a country increasingly open and accessible to visitors."),
    ("Tuol Sleng &amp; Choeung Ek", "Cambodia", "The S-21 prison and the Killing Fields, near Phnom Penh."),
  ],
  "The Jewish diaspora, students and educators, people reconnecting with family history, and anyone seeking to bear witness. School and sixth-form history trips are a steady, serious part of this audience.",
  "We know entry requirements, guide licensing, and the difference between a weekday and weekend visit. We prepare clients emotionally before they go, and point them to debrief resources afterwards &mdash; work an algorithm simply cannot do.",
  "itineraries.html#auschwitz"
)

dest_page(
  "nuclear-disaster.html", "Nuclear &amp; Industrial Disaster Tourism", "Nuclear &amp; Disaster Zones",
  "The frontier where human ambition met catastrophe &mdash; sites with genuine pop-culture awareness (thanks in part to HBO's Chernobyl) and a fiercely engaged following.",
  [
    ("Chernobyl Exclusion Zone &amp; Pripyat", "Ukraine", "Currently closed due to the war; we are tracking reopening closely given the enormous pent-up demand."),
    ("Fukushima", "Japan", "Select areas are now open, including J-Village and Futaba Town, with growing official tour infrastructure."),
    ("Bikini Atoll", "Marshall Islands", "A UNESCO World Heritage nuclear test site, with scuba diving on the sunken test fleet."),
    ("Trinity Site", "USA", "The first nuclear bomb test, open to the public only twice a year."),
    ("Centralia", "USA", "A Pennsylvania town abandoned over an underground coal fire that has burned since 1962."),
  ],
  "Science and engineering enthusiasts, Cold War history buffs, and adventure travellers who want something that is legitimate and safe, not a trespassing stunt.",
  "We only work with licensed operators and current radiation-safety guidance, and we track site access in real time &mdash; several of these locations open, close, and change access rules with little warning.",
  "itineraries.html#fukushima"
)

dest_page(
  "witness-travel.html", "Grief, Memorial &amp; Humanitarian Witness Tourism", "Witness &amp; Humanitarian Travel",
  "Our most ethically robust and fastest-growing category: recent history, told by the people and communities who lived through it.",
  [
    ("Srebrenica", "Bosnia &amp; Herzegovina", "The Memorial Centre and Cemetery, central to understanding Europe's most recent genocide."),
    ("Mostar", "Bosnia &amp; Herzegovina", "A war-scarred city and the rebuilt Old Bridge &mdash; a powerful, visual testimony to recovery."),
    ("Sarajevo Siege Route", "Bosnia &amp; Herzegovina", "The Tunnel of Hope, the Olympic sites, and the city's wartime cemeteries."),
    ("Robben Island", "South Africa", "Nelson Mandela's prison, and living history told by former-prisoner guides."),
    ("Belfast Murals &amp; the Troubles", "Northern Ireland", "Black cab tours through the Falls Road and Shankill, and Crumlin Road Gaol."),
  ],
  "Travellers who want to understand a conflict within living memory, not just read about it. Bosnia in particular remains almost entirely unserved by UK specialists &mdash; it's accessible, affordable, and profound.",
  "Itineraries here are built in consultation with local memorial organisations, and we prioritise locally-owned guides and accommodation so your spending benefits the communities you're visiting.",
  "itineraries.html#sarajevo"
)

dest_page(
  "notorious-history.html", "Crime, Cults &amp; Notorious History Tourism", "Crime &amp; Notorious History",
  "A smaller, more loyal audience, and territory that needs very careful ethical positioning &mdash; we treat this as a historian's practice, not tabloid tourism.",
  [
    ("Alcatraz", "USA", "San Francisco's former federal prison, still selling out months in advance."),
    ("Jonestown", "Guyana", "Barely visited and logistically serious; a signature ultra-niche offering for the right client."),
    ("Salem", "USA", "The 1692 witch trials, and a strong UK and US audience for the history behind the legend."),
  ],
  "History-literate travellers who want context, not spectacle. We deliberately do not offer London 'Jack the Ripper' style routes &mdash; they are already saturated and lean towards voyeurism rather than history.",
  "We screen every site and operator in this category against one question: does this educate, or does it exploit? If the honest answer is the latter, it doesn't go on our itinerary.",
  "itineraries.html"
)

dest_page(
  "death-rituals.html", "Paranormal &amp; Death-Ritual Tourism", "Death Rituals &amp; Catacombs",
  "How cultures have faced mortality itself &mdash; often a lower-cost, gateway experience into deeper dark tourism.",
  [
    ("The Catacombs of Paris", "France", "Millions of remains beneath the city, one of the world's most visited ossuaries."),
    ("The Capuchin Crypt", "Italy", "Rome's chapels decorated with the bones of Capuchin friars."),
    ("Edinburgh's Vaults &amp; Greyfriars Kirkyard", "Scotland", "Underground vaults and a graveyard with a genuinely unsettling reputation."),
    ("Island of the Dolls", "Mexico", "A canal island covered in decaying dolls, hung as a tribute and a warning."),
    ("New Orleans Cemeteries", "USA", "Above-ground tombs and the city's Voodoo cultural history."),
  ],
  "Curious travellers taking their first step into dark tourism, as well as folklore and death-ritual enthusiasts looking for something more serious than a ghost-walk gimmick.",
  "We use this category as an accessible entry point, then introduce clients to deeper, more meaningful journeys once trust is established &mdash; never the other way around.",
  "itineraries.html"
)

# ---------- ITINERARIES ----------
def itin(anchor, title, subtitle, price, days):
    day_html = "".join(f'<div class="day"><b>Day {i+1}</b><span>{d}</span></div>' for i, d in enumerate(days))
    return f"""
<div class="itinerary" id="{anchor}">
  <div class="itinerary-head"><h3>{title}</h3><span class="price">{price}</span></div>
  <p style="margin-bottom:16px;color:var(--text-faint);">{subtitle}</p>
  {day_html}
</div>
"""

itins_body = """
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> / Itineraries</div>
    <span class="eyebrow">Sample Itineraries</span>
    <h1>Five starting points. Every one is a starting point, not a fixed package.</h1>
    <p class="lead">Every itinerary below is fully bespoke to your dates, budget and group size. Prices are per person, based on a small group of 4&ndash;6 unless noted.</p>
  </div>
</section>
<section>
  <div class="wrap">
""" + \
itin("normandy", "Normandy Witnessed", "5 days, France &mdash; for WWII anniversary pilgrims and family veterans.", "&pound;2,800&ndash;&pound;3,500pp", [
    "Caen Memorial Museum &mdash; context-setting for the Battle of Normandy",
    "American Cemetery, Omaha Beach and Pointe du Hoc",
    "British and Canadian sectors: Gold, Juno, Sword; Bayeux War Cemetery and Tapestry",
    "Arromanches 360&deg; cinema; the Longues-sur-Mer battery; Utah Beach",
    "Private archive research at the Caen Memorial for family veteran records",
]) + \
itin("sarajevo", "Sarajevo Survivor", "7 days, Bosnia &amp; Herzegovina &mdash; our signature journey, and Europe's most recent genocide understood through those who lived it.", "&pound;2,200&ndash;&pound;2,800pp", [
    "Arrive Sarajevo; neighbourhood walk; dinner in a local home",
    "War Childhood Museum; Sniper Alley; the Tunnel of Hope",
    "Srebrenica &mdash; the Memorial Centre and Cemetery (a full day; emotionally intense)",
    "Mostar; the Old Bridge; a war-damage walking tour with a local guide",
    "Blagaj and the Kravice Waterfalls &mdash; a decompression day",
    "Sarajevo food market; a meeting with a local NGO; free time",
    "Depart",
]) + \
itin("auschwitz", "Auschwitz &amp; Krak&oacute;w: Bearing Witness", "4 days, Poland &mdash; educational, and deeply ethical by design.", "&pound;1,600&ndash;&pound;2,200pp", [
    "Arrive Krak&oacute;w; Jewish Quarter walk; Schindler's Factory Museum",
    "Auschwitz I (licensed guided tour, morning); Birkenau (self-reflective walk, afternoon)",
    "Kazimierz market; a meeting with a local Jewish community historian; optional Wieliczka Salt Mine",
    "Depart",
]) + \
itin("fukushima", "Fukushima: The Zone", "8 days, Japan &mdash; for nuclear history and science enthusiasts, as Japan continues to expand access.", "&pound;4,500&ndash;&pound;6,500pp", [
    "Tokyo arrival",
    "Hiroshima Peace Memorial Museum",
    "Travel to the Fukushima region",
    "Licensed tour of open exclusion-zone areas; J-Village; Futaba Town",
    "Decontamination facility visit and briefing",
    "Travel to Kyoto",
    "Kyoto and debrief",
    "Depart",
]) + \
itin("belfast", "Belfast: Murals &amp; Memory", "3 days, Northern Ireland &mdash; our best-value introductory journey. UK mainland flight, no passport required.", "&pound;800&ndash;&pound;1,200pp", [
    "Black cab tour of the Falls Road and Shankill murals with a local driver-guide from both communities",
    "Titanic Belfast; the Peace Wall; Crumlin Road Gaol tour",
    "Free time; depart",
]) + """
  </div>
</section>
<section class="cta-band"><div class="wrap"><h2>None of these quite right?</h2><p class="lead" style="max-width:560px;margin:0 auto 26px;">Every itinerary here started as a conversation. Tell us the history you want to understand and we'll build around it.</p><a class="btn btn-primary" href="contact.html">Design My Itinerary</a></div></section>
"""
page("itineraries.html", f"Dark Tourism Itineraries | {SITE}", "Sample dark tourism itineraries: Normandy, Sarajevo, Auschwitz and Kraków, Fukushima, and Belfast. Fully bespoke, priced per person.", "itineraries.html", itins_body)

# ---------- ETHICS ----------
principles = [
  ("Education Before Entertainment", "Every itinerary is built to prioritise learning and remembrance over spectacle. If a stop exists only for a photograph, it doesn't belong on our itinerary."),
  ("Survivor and Descendant Respect", "In destinations where trauma is recent &mdash; Rwanda, Bosnia, Cambodia &mdash; itineraries are built in consultation with local memorial organisations, not designed remotely from a spreadsheet."),
  ("No Sensation, No Selfie Culture", "We brief every client on site etiquette before they travel: what to wear, how to behave, and what not to photograph. It is a core part of the service, not a footnote."),
  ("Legitimate Operators Only", "Every local guide is vetted for accreditation and a genuine connection to the community. We do not resell generic city-tour packages under a darker name."),
  ("Psychological Preparation", "You receive a pre-trip briefing document and a post-trip debrief, with counselling resources signposted where appropriate. These places affect people, and we don't pretend otherwise."),
  ("Economic Benefit to Communities", "Wherever possible we choose locally-owned accommodation, guides, and restaurants, so the communities connected to these histories see a direct benefit from your visit."),
]
principle_html = "".join(f'<div class="principle"><span class="num">{i+1:02d}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (t,d) in enumerate(principles))

ethics_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> / Our Ethics</div>
    <span class="eyebrow">Our Ethics</span>
    <h1>The ethical framework behind every journey we design.</h1>
    <p class="lead">Dark tourism sits close to real trauma, real grief, and real communities. This is the code we hold ourselves to &mdash; and the reason a human specialist beats any algorithm or booking engine in this space.</p>
  </div>
</section>
<section>
  <div class="wrap" style="max-width:820px;">
    {principle_html}
  </div>
</section>
<section class="alt">
  <div class="wrap" style="max-width:820px;">
    <span class="eyebrow">Academic Grounding</span>
    <h2>Aligned with the Institute for Dark Tourism Research</h2>
    <p>Our framework draws on the work of the <a href="https://www.uclan.ac.uk/research/activity/institute-for-dark-tourism-research" target="_blank" rel="noopener">Institute for Dark Tourism Research (iDTR) at the University of Central Lancashire</a> &mdash; the world's only dedicated academic centre for dark tourism scholarship, founded in 2012 by Dr Philip Stone and home to the <em>International Journal of Dark Tourism Studies</em>. We reference their published typologies and ethical frameworks directly in how we brief clients and vet destinations.</p>
    <div class="quote-block">Dark tourism is not about voyeurism. Done well, it is education, remembrance, and an act of respect &mdash; and that distinction is the whole of our business.</div>
  </div>
</section>
<section class="cta-band"><div class="wrap"><h2>Questions about how we handle a specific site?</h2><a class="btn btn-primary" href="contact.html">Ask Us Directly</a></div></section>
"""
page("ethics.html", f"Our Ethical Framework | {SITE}", "The ethical framework behind Dark Shadow Journeys, aligned with the Institute for Dark Tourism Research (iDTR) at UCLan.", "ethics.html", ethics_body)

# ---------- ABOUT ----------
about_body = """
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> / About</div>
    <span class="eyebrow">About</span>
    <h1>A UK specialist, built for one niche.</h1>
    <p class="lead">Dark Shadow Journeys exists because no major UK travel agency has built a dedicated, ethical dark tourism brand &mdash; and because the sites that matter most deserve more care than an OTA search box or a generic AI itinerary can give them.</p>
  </div>
</section>
<section>
  <div class="wrap grid grid-2">
    <div>
      <h2>What we do differently</h2>
      <p>We don't sell flights and hotels &mdash; you can already do that yourself. We sell context: pre-vetted ethical guides, curated sequences that build meaning across a trip, access to sites that require advance booking or licences, and the emotional preparation to actually take in what you're seeing.</p>
      <p>We operate under a UK host travel agency's ATOL umbrella, so your booking is protected exactly as it would be with any bonded UK agent.</p>
    </div>
    <div>
      <h2>Who it's for</h2>
      <p>History-literate travellers, families researching a veteran relative, educators and school groups, genealogy travellers reconnecting with family history, and anyone who has watched a documentary or read a book and thought: I need to go and see this for myself, properly.</p>
    </div>
  </div>
</section>
<section class="alt">
  <div class="wrap" style="max-width:760px;">
    <span class="eyebrow">Our Positioning</span>
    <div class="quote-block">Dark Shadow Journeys is the UK's specialist in ethical dark tourism &mdash; travel that bears witness, honours the dead, and deepens our understanding of human history. Every journey is researched, curated, and supported by a human specialist who treats these places with the gravity they deserve.</div>
  </div>
</section>
<section class="cta-band"><div class="wrap"><h2>Let's talk about your journey.</h2><a class="btn btn-primary" href="contact.html">Get In Touch</a></div></section>
"""
page("about.html", f"About | {SITE}", "About Dark Shadow Journeys, the UK's ethical dark tourism specialist travel agency, and the positioning behind it.", "about.html", about_body)

# ---------- JOURNAL ----------
articles = [
  ("why-dark-tourism-matters.html", "Why Dark Tourism Matters", "Thought leadership",
   "A counter-argument to the 'voyeurism' accusation dark tourism regularly faces.",
   """<p>Every time a documentary about Chernobyl or a genocide memorial trends online, the same criticism follows: isn't this just voyeurism dressed up as travel? It's a fair question, and it deserves a real answer rather than defensiveness.</p>
   <p>Dark tourism, done well, is one of the oldest forms of travel there is. Pilgrims have visited sites of martyrdom and mass death for centuries. What has changed is scale, speed, and the ease with which a place of real suffering can be reduced to a photo backdrop. The difference between remembrance and voyeurism is not the destination &mdash; it's the intent, the preparation, and the behaviour once you arrive.</p>
   <p>A visit to Auschwitz-Birkenau with a licensed guide, prepared beforehand for what you'll see and why, briefed on etiquette, and given space afterwards to process it, is fundamentally different from an unprepared drive-by stop between two more cheerful destinations. The site is the same. The visit is not.</p>
   <p>This is why the Institute for Dark Tourism Research at UCLan exists, and why we align our practice with their published frameworks. Dark tourism isn't inherently exploitative &mdash; but it can become exploitative fast, in the hands of an operator who doesn't take the responsibility seriously. That's the whole reason a specialist matters here.</p>"""),
  ("auschwitz-etiquette-guide.html", "What To Know Before You Visit Auschwitz-Birkenau", "Practical guide",
   "Practical, respectful guidance for one of the most visited &mdash; and most misunderstood &mdash; memorial sites in the world.",
   """<p>Auschwitz-Birkenau receives over two million visitors a year, and it shows: queues, timed entry, and a genuine risk of the visit feeling rushed if you don't plan properly. A few practical points make a real difference.</p>
   <p><b>Book your guide well in advance.</b> Independent entry without a guide is only permitted during limited hours; a licensed guide (booked through auschwitz.org) is required for most visiting slots, and popular dates sell out months ahead, especially around anniversaries.</p>
   <p><b>Dress and behave as you would at a cemetery.</b> Covered shoulders and knees are appropriate. Photography is permitted in most areas but never inside the buildings that display victims' personal belongings, and never posed or smiling photographs anywhere on site.</p>
   <p><b>Plan for the emotional weight, not just the logistics.</b> Most visitors underestimate how the site affects them. We recommend keeping the rest of that day light, and giving yourself time afterwards rather than moving straight on to the next stop on a tour.</p>
   <p><b>Auschwitz I and Birkenau are different visits.</b> Auschwitz I is the smaller, museum-format camp; Birkenau is the vast, largely open site most people picture. Seeing both, in sequence, on the same day is standard and recommended.</p>"""),
  ("beginners-guide-dark-tourism.html", "A Beginner's Guide to Dark Tourism", "Practical guide",
   "New to this kind of travel? Start here.",
   """<p>If you're new to dark tourism, the range of destinations &mdash; battlefields, genocide memorials, nuclear disaster zones, catacombs &mdash; can feel overwhelming, and the ethics of visiting some of them can feel genuinely uncertain. Here's how we'd suggest starting.</p>
   <p><b>Start closer to home and lower-intensity.</b> Belfast's murals, or the Paris Catacombs, are excellent first steps: real history, real gravity, but a gentler emotional register than Srebrenica or Auschwitz.</p>
   <p><b>Ask what you actually want from the visit.</b> Understanding a family connection to WWII is a different motivation from wanting to understand the Rwandan genocide, which is different again from scientific curiosity about Chernobyl. Being honest about your own motivation shapes the right itinerary.</p>
   <p><b>Travel with someone who has done the work.</b> The single biggest predictor of whether a dark tourism trip feels meaningful rather than uncomfortable is preparation: knowing the history before you arrive, knowing how to behave once you're there, and having somewhere to put what you've felt once you leave.</p>"""),
]

article_cards = ""
for slug, title, tag, summary, content in articles:
    article_cards += f'<div class="card"><span class="tag">{tag}</span><h3>{title}</h3><p>{summary}</p><a class="more" href="{slug}">Read &rarr;</a></div>'
    art_body = f"""
<section class="page-hero">
  <div class="wrap" style="max-width:760px;">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="journal.html">Journal</a> / {title}</div>
    <span class="eyebrow">{tag}</span>
    <h1>{title}</h1>
  </div>
</section>
<section><div class="wrap" style="max-width:760px;">{content}</div></section>
<section class="cta-band"><div class="wrap"><h2>Want a journey built around this?</h2><a class="btn btn-primary" href="contact.html">Enquire Now</a></div></section>
"""
    page(slug, f"{title} | Journal | {SITE}", summary, slug, art_body)

journal_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> / Journal</div>
    <span class="eyebrow">Journal</span>
    <h1>Research, etiquette, and thinking on ethical dark tourism.</h1>
    <p class="lead">Practical guides and thought pieces &mdash; written for travellers, not search engines, though we hope Google likes them too.</p>
  </div>
</section>
<section><div class="wrap grid grid-3">{article_cards}</div></section>
"""
page("journal.html", f"Journal | {SITE}", "Practical guides and thought leadership on ethical dark tourism, from etiquette at memorial sites to why this kind of travel matters.", "journal.html", journal_body)

# ---------- CONTACT ----------
faqs = [
  ("Is dark tourism disrespectful?", "Not when it's done properly. The difference between remembrance and voyeurism is preparation, guiding, and behaviour on site &mdash; which is the entire service we provide. See our <a href=\"ethics.html\">ethics framework</a> for the full detail."),
  ("Is my booking financially protected?", "Yes. We operate under a UK host travel agency's ATOL umbrella, so package bookings carry the same financial protection as any bonded UK travel agent."),
  ("Can you build a trip around a specific family history?", "Frequently &mdash; this is one of our most common enquiries, particularly for Normandy and other WWII sites. Tell us what you know and we'll research the rest."),
  ("Do you arrange group and school trips?", "Yes, including sixth-form history department trips, with the additional briefing materials that kind of group typically needs."),
  ("What if a site I want to visit is currently closed or restricted?", "We track access restrictions closely (Chernobyl and parts of Fukushima are current examples) and will tell you plainly if something isn't currently visitable, rather than booking around it."),
]
faq_html = "".join(f'<div class="accordion-item"><div class="accordion-q">{q}<span class="chev">+</span></div><div class="accordion-a"><p>{a}</p></div></div>' for q,a in faqs)

contact_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> / Contact</div>
    <span class="eyebrow">Get In Touch</span>
    <h1>Tell us what you want to understand.</h1>
    <p class="lead">A short conversation is usually enough for us to suggest a first shape for your journey. No obligation, no generic quote &mdash; a real reply from a person.</p>
  </div>
</section>
<section>
  <div class="wrap grid grid-2" style="align-items:start;">
    <form class="enquiry" id="enquiry-form">
      <div><label for="name">Name</label><input id="name" name="name" type="text" required></div>
      <div><label for="email">Email</label><input id="email" name="email" type="email" required></div>
      <div><label for="theme">Destination theme</label>
        <select id="theme" name="theme">
          <option>Battlefields &amp; Conflict</option>
          <option>Genocide &amp; Holocaust Memorials</option>
          <option>Nuclear &amp; Disaster Zones</option>
          <option>Witness &amp; Humanitarian Travel</option>
          <option>Crime &amp; Notorious History</option>
          <option>Death Rituals &amp; Catacombs</option>
          <option>Not sure yet</option>
        </select>
      </div>
      <div><label for="message">Tell us about the journey you have in mind</label><textarea id="message" name="message" required></textarea></div>
      <button class="btn btn-primary" type="submit" style="border:none;cursor:pointer;justify-self:start;">Send Enquiry</button>
      <p class="form-note">We typically reply within one working day. This form is a placeholder pending our booking system integration &mdash; enquiries can also be sent directly to hello@darkshadowjourneys.com.</p>
    </form>
    <div>
      <h2>Frequently Asked</h2>
      {faq_html}
    </div>
  </div>
</section>
"""
page("contact.html", f"Contact | {SITE}", "Get in touch with Dark Shadow Journeys to start planning an ethical dark tourism itinerary anywhere in the world.", "contact.html", contact_body)

print("ALL PAGES GENERATED")
