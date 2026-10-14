# 1.25.1

- Personagegegevens verwijderd uit inwonereditor; eerder ingevulde velden behouden bij bewaren.
- Historie sorteerbaar op Onderdeel, Datum en Wijziging in beide richtingen; datum sorteert chronologisch.

# 1.25.0

- Woonplek-label en aankomstdatumknop bovenaan extra inwonergegevens.
- Bank/contant toevoegen of afnemen met bedragknoppen; bewaren registreert mutaties in kasboek, verwijderen draait saldo terug.
- Historie filteren op onderdeel, soort wijziging en datum; entries verwijderen met herstelkopie.
- Concrete betaalomschrijvingen zoals pandopbrengst, overnachtingen en onderhoud.

# 1.24.1

- Overbodige algemene nulbetalingen niet meer klaargezet of weergegeven in persoonsoverzichten en uitbetalingstotalen.
- Werkelijke salarisbetalingen behouden.

# 1.24.0

- DM beheert de bank zonder eigen saldo; gewone betalingen muteren inwonerbanksaldi.
- Overnachtingsgeld bij betalen direct naar banksaldo herbergeigenaar, uitgesloten van dubbele algemene uitbetaling.
- Salarissen apart contant verwerkt; nieuwe algemene uitbetalingen houden salariskosten niet nogmaals in.
- Bankmutaties opgeslagen en teruggedraaid bij verwijderen van betalingen.

# 1.23.2

- Eenmalige opschoning van foutieve oude Harptos-salarisregistraties met herstelkopie in kroniek.
- Eventuele contante verwerking teruggedraaid; correcte actuele verplichtingen behouden.

# 1.23.1

- Kasboek verplaatst naar eigen tabblad binnen Kanselarij.
- Alle gedane salarisbetalingen zichtbaar naast campagnebetalingen en losse registraties, inclusief eerdere periodes.

# 1.23.0

- Aankomstdatum zichtbaar op inwonersranglijst, bouwdatum op locatiekaarten.
- Nieuw Percelen-menu met naam, vakjes/plots, eigenaar en aanmaakdatum.
- Perceel bewerken via kaartje; directe knop voor aanmaakdatum en historie.

# 1.22.0

- Eigen Kasboek-pagina met alle salaris-, campagne- en losse betaalregistraties, inclusief Markdown-export.
- Betalingen verwijderen: contante salarissen terugboeken en verplichting heropenen; andere registraties verwijderen/heropenen.
- Controle op voldoende contant geld bij terugdraaien; kasboek alleen in DM-weergave.

# 1.21.1

- Salaris betalen direct in de uitbetalingsrij van iedere eigenaar, met totaal en namen van medewerkers.
- Rij blijft zichtbaar zonder andere openstaande bedragen; knop uitgeschakeld wanneer salaris al verwerkt is.
- Historische automatische boekingen hebben correct label Nog verrekenen met eigenaar.

# 1.21.0

- Betaal salaris per eigenaar, voor alle openstaande medewerkerslonen in zichtbare periodes.
- Uitbetalingstotalen met aparte kolommen Te betalen en Te ontvangen.
- Salarisactie controleert contant saldo en gekoppelde medewerkers; geen dubbele overdracht.

# 1.20.0

- Uitbetalingen toont openstaande totalen per inwoner/medewerker over verstreken periodes van de huidige maand.
- Totalen in één keer betaald/ontvangen markeren; salaris contant verrekenen met eigenaar.
- Onderliggende periodehistorie behouden en totaalexport toegevoegd.

# 1.19.2

- Dubbele hovervensters hersteld; verklaringen toegevoegd aan persoonsoverzicht.
- Salarisbetaling controleert en registreert afzonderlijk afboeking eigenaar en bijschrijving medewerker.
- Oude automatische boekingen kunnen handmatig met eigenaar worden verrekend zonder tweede NPC-bijschrijving.

# 1.19.1

- Nieuwe salarissen staan open en worden handmatig contant betaald door de eigenaar; saldo gaat van eigenaar naar medewerker.
- Betaalactie controleert contant saldo en voorkomt dubbele betaling; bestaande betaalde records behouden.
- Historie toont gewijzigde velden met oude en nieuwe waarden, inclusief eigendom, werkplek, geld en financiële instellingen.

# 1.19.0

- Betaald NPC-loon voor zichtbare periodes wordt eenmaal bij contant geld opgeteld; gemarkeerd tegen dubbele verwerking.
- Ingangsdatums & historie ook bereikbaar bij Inwoners en Locaties.
- Directe datumknoppen in inwoner- en pandeditor; duidelijke aankomst-, bouw- en perceellabels.

# 1.18.2

- Harptos-betaalkeuze volgt afgeronde tendays binnen de huidige maand, in plaats van cumulatieve campagnedagen.
- Op 26 Flamerule zijn alleen tenday 1 en 2 beschikbaar.
- Nieuwe Harptos-boekingen hebben een maand/jaar-sleutel; oude boekingen blijven in de back-up behouden.
- Latere periodes verborgen in betaal- en salarisoverzichten.

# 1.18.1

- Harptos gebruikt betaalperiodes van 10 dagen; gewone kalender behoudt 7 dagen.
- Overnachtingen, historische berekeningsmomenten, salarisperiodes en labels volgen de kalenderkeuze.
- Bestaande geregistreerde bedragen blijven behouden.

# 1.18.0

- Ingangsdatums en historie voor panden, inwoners en percelen; eigenaarwissels en uitbreidingen worden vastgelegd.
- Datums bewerken in Harptos of gewone kalender via Kanselarij → Ingangsdatums & historie.
- Nieuwe weekbetalingen en salarissen gebruiken de geregistreerde situatie op de laatste dag van de betaalweek.
- Bestaande gegevens starten voorlopig op dag 1, gemarkeerd voor controle; bestaande geboekte bedragen behouden.

# 1.17.3

- Alleen volledig verstreken campagneweken zijn beschikbaar voor betalingen.
- Dag 1–7: geen betaalweek; vanaf dag 8 week 1, vanaf dag 15 week 2.
- Salarissen en automatische betalingen volgen dezelfde grens; bestaande boekingen blijven behouden.

# 1.17.2

- Weekkeuze en losse betaalregistratie begrensd tot de huidige tijdlijnweek.
- Campagnedag 1 begint week 1; geen toekomstige weekbetalingen klaarzetten.
- Eerder gekozen toekomstige week teruggezet naar huidige week, historische betalingen behouden.

# 1.17.1

- Laatste tijdlijnentry bepaalt uitsluitend het aantal betaalweken.
- Ontbrekende salarisweken vanaf week 1 automatisch geboekt; geselecteerde inwonerbetalingen per verstreken week klaargezet.
- Bestaande bedragen en betaalstatus behouden; ontbrekende oude weken gebruiken huidige tarieven.
- Uitleg boven inwonersranglijst verwijderd.

# 1.17.0

- Medewerkersloon automatisch eenmaal per campagneweek als betaald geregistreerd, vanaf de huidige week.
- Betaalhistorie zichtbaar onder Uitbetalingen en in het persoonlijke medewerkersoverzicht/export.
- Reeds geregistreerde bedragen blijven behouden; geen dubbele loonkosten bij panden.

# 1.16.1

- NPC’s zonder woonplek worden nergens als automatische gasten van The Crossroads Rest weergegeven of berekend.

# 1.16.0

- Panden en percelen samengevoegd op één tabblad.
- Negatieve weekresultaten als te ontvangen betalingen, met directe ontvangstregistratie en juiste richting in persoonsoverzicht.
- Oude openstaande nulbetalingen bij negatief resultaat omgezet naar te ontvangen bedrag.
- Ingehuurde medewerkers gekoppeld aan bestaande inwoners of automatisch aangemaakte NPC’s, zonder dubbele telling.
- Bewerkbare leeftijd, ras en klas naast naam en omschrijving.

# 1.15.1

- Persoonsoverzicht met leesbare HTML-tabellen; Markdown blijft beschikbaar als export.
- Betaalregistratie verplaatst naar Uitbetalingen, inclusief ontvangen betalingen van inwoners.
- Grafieken uitsluitend binnen het tabblad Overzicht.
- Drie aangewezen uitlegteksten verwijderd.

# 1.15.0

- Locatiekaarten tonen gekoppelde medewerkers, meewerkende eigenaar en ingehuurd personeelsniveau.
- Kanselarij toont vijf inklapbare grafieken: inwoners, waarde, weekomzet, weekwinst en weekkosten.
- Dagstanden worden vanaf deze versie bewaard in de kroniek; geen verzonnen historische standen.
- Grafieken tonen de hele stad en datumpunten met waarden bij aanwijzen.

# 1.14.0

- Aanpasbaar overnachtingstarief onder Kanselarij → Tarieven, standaard 1 gp/nacht.
- Ontvangst van een betaalde campagne-uitbetaling apart bevestigen en heropenen.
- Persoonsoverzicht met eigendom, geld, weekresultaat en geregistreerde betalingen; spelerveilige Markdown-export zonder geheimen.
- Losse ontvangen/gedane betalingen per inwoner registreren, zonder automatische banksaldowijzigingen.

# 1.13.0

- Inwoners zonder geldige slaapplek overnachten automatisch in The Crossroads Rest, 1 gp per nacht (7 gp per week).
- Verblijfskosten tellen mee in nettoresultaat; overnachtingen leveren inkomsten op voor de herberg en diens eigenaar.
- Automatisch verblijf zichtbaar op de ranglijst, Kanselarij-overzicht en berekeningsuitleg.
- Toewijzen van een slaapplek beëindigt automatisch verblijf; banksaldi en vastgelegde weekbetalingen blijven behouden.

# 1.12.2

- De eerste 16 perceelvakken tellen ook mee in de grondwaarde tegen het tarief voor het eerste plot.
- Delen van plots blijven naar verhouding gewaardeerd; rijkdom en Kanselarij gebruiken dezelfde grondwaarde.

# 1.12.1

- Kaart verschuiven door met de rechtermuisknop te slepen; browsercontextmenu op de kaart uitgeschakeld.

# 1.12.0

- Inwoners als verticale, genummerde ranglijst op rijkdom met woonplek, werkplek, bezittingen en weekresultaat.
- Kaart past automatisch in de beschikbare schermhoogte en reageert op scherm- en zijbalkformaat.
- Zoomknoppen, muiswielzoom, passend maken en verschuiven (knop, Shift-slepen of middelste muisknop).
- Kaartcoördinaten bij tekenen en selecteren blijven werken via de SVG-transformatie; export blijft de volledige kaart.

# 1.11.0

- Plots in bezit automatisch uit unieke perceelvakken / vakken per plot, inclusief fracties.
- Grondwaarde automatisch met gratis eerste plot en naar verhouding berekende prijsschijven; oude handmatige aantallen blijven in back-ups behouden.
- Kanselarij-overzicht sorteren op waarde, voornaam en perceelvakken, beide richtingen.
- Pandentabel sorteren met kolomkoppen.
- Financiële invoer automatisch opslaan; bewaarknoppen verwijderd.
- Nieuwe en bestaande regelprofielen gebruiken altijd werkafhankelijke opbrengst; keuzevak verwijderd.
- Grondtarieven gebruiken kortere plotlabels.

# 1.10.1

- Ingehuurde medewerkers tellen mee bij het inwonertotaal; een meewerkende eigenaar wordt niet nogmaals geteld.
- Uitsplitsing van geregistreerde inwoners en medewerkers bij aanwijzen van het inwonertotaal.

# 1.10.0

- Regelprofielen en personeelsniveaus omhoog/omlaag verplaatsen; volgorde wordt bewaard.
- Uitleg bij werkafhankelijke opbrengst en uitsplitsingen bij de Kanselarij-statistieken.
- Campagnedatum bovenin volgt de laatste zichtbare tijdlijngebeurtenis.
- Inwoners tonen eigendom, werkplek, geld en weekresultaat, gesorteerd op rijkdom.
- Bankgeld en contant geld handmatig aanpassen bij een inwoner, behouden in kroniekback-ups.
- Herstelde ontbrekende tariefvariabele bij eigenaarfactor en bewaren.

# 1.9.0

- Kanselarij vervangt Bezittingen & inkomsten.
- Losstaande grondstukken worden apart geregistreerd en overdraagbaar, met behoud van eigenaar en geometrie.
- Alles selecteren bij uitbetalingen en een overzicht van openstaande betalingen uit andere klaargezette weken.
- Weekbedragen worden vastgelegd en behouden bij tariefwijzigingen en heropenen.
- Harptos en gewone kalender met instelbare startdatum en datuminvoer voor gebeurtenissen.

# Wijzigingslog

## 1.8.0 — 2026-10-14

- Groene zijbalk inklapbaar; keuze blijft lokaal bewaard.
- Financiële pagina opgesplitst in Overzicht, Panden, Percelen, Tarieven en Uitbetalingen.
- Wekelijkse uitbetalingen met geselecteerde ontvangers, betaaldstatus, vastgelegd bedrag, heropenen en Markdown-weekoverzicht.
- Toevoegformulieren staan onder hun eigen tarief- en personeeltabel.
- Tarief- en personeelsregels verwijderen archiveert ze; bestaande panden behouden de berekening.
- Eigenaar kan naast personeel meewerken met standaard factor 2. De factor blijft aanpasbaar. Een eerdere personeelsregel Eigenaar wordt compatibel omgezet naar meewerken.
- Extra kosten tijdelijk verborgen en niet meegerekend; opgeslagen regels behouden.

## 1.7.0 — 2026-10-14

- Navigatie-iconen en teksten consistent uitgelijnd; bewonerskaarten hebben standaard gelijke afmetingen. Meer ruimte onder Wijzigingen bewaren.
- Gildes verwijderd uit navigatie en zichtbare exports; eerdere gildedata blijft behouden in de kroniek.
- Tent / hut hernoemd naar Tent, met behoud van profiel-id en ingestelde bedragen.
- Percelen hebben geen inkomsten, weekkosten of handmatige extra aanschafbedragen. Eerdere invoer blijft opgeslagen, maar telt niet mee.
- Totale omzet toont bruto-inkomsten; netto blijft apart. Waarde van de plaats omvat pandwaarden en gekochte extra plots, zonder eenmalige extra uitgaven.
- Financieel overzicht exporteren naar Markdown (standaard), CSV of JSON.
- Pandtype is een dropdown met financiële regelprofielen; bestaande vrije typen blijven behouden. Een keuze koppelt het pand aan het profiel.
- Nieuwe regelprofielen en personeelsniveaus toevoegen; namen zijn aanpasbaar.

## 1.6.0 — 2026-10-14

- Nieuw menu Bezittingen & inkomsten: panden en percelen per inwoner, bruto- en netto-opbrengst en weekkosten.
- Expliciete pand-eigendom, los van bewoning en werkplek.
- Aanpasbare tarieven uit de aangeleverde DDAC-basisregels voor woonruimte, werkplaatsen, modules, personeel, speciale gebouwen en extra plots. Startplot ingesteld op 16 vakjes.
- Werkplaatsen zonder personeel genereren standaard geen inkomen. Helpers, vakmannen en meesters bepalen loon en opbrengstfactor.
- Eigen aangepaste inkomsten, onderhoud en aanschafkosten per pand en perceel.
- Extra kosten per inwoner, per week of eenmalig, en JSON-export van het financiële overzicht.
- Bestaande kaart-, bewoners- en eigendomsgegevens behouden; nieuwe bedragen gaan mee in de volledige kroniekexport.

## 1.5.2 — 2026-10-14

- Selectiemodus opent panden en percelen direct voor bewerking.
- Tekenen en wissen staan bij elkaar voor het gekozen terreintype.
- De actieve bewerking blijft zichtbaar als de opties gesloten zijn, met een gemarkeerde gereedschapsknop.
- De balk boven de kaart verwijderd; perceelzichtbaarheid, informatie en exports staan in Weergave en export links.

## 1.5.1 — 2026-10-14

- Percelen verkleinen met een rasterpenseel via Perceel verkleinen of Vakken wissen in het gebouwenmenu.
- Alleen vakken van het gekozen perceel worden verwijderd; andere kaartlagen en eigendom blijven behouden.
- Het laatste vak wissen verwijdert het perceel. Ongedaan maken herstelt de verwijderde vakken en de eigenaar.

## 1.5.0 — 2026-10-14

- Percelen met een rasterpenseel tekenen over meerdere penseelstreken en daarna bewaren; bestaande percelen direct met het penseel uitbreiden.
- Percelen met dezelfde eigenaar samenvoegen tot één eigendomsgebied, zonder dubbele grenzen en labels; eerdere namen blijven in de gegevens bewaard. Aangrenzende vakken vormen één doorlopend gebied.
- Vrije pandvormen tekenen per vak als standaardoptie, met een expliciete knop Pand bewaren. L/T-sjablonen en uitbreiding van bestaande panden blijven beschikbaar.
- Extra gereedschapsopties openen over de kaart en klappen bij tekenen in, zonder het tekenvlak te verschuiven.
- Onderdeel-exports staan op de locaties-, inwoners- en gildespagina; percelenexport staat bij de kaart.
- Voorbeeldkaart heeft een afbeeldingicoon.
- PNG- en SVG-export van de volledige spelerskaart, zonder verborgen locaties, DM-geheimen, eigendomsgebieden en voorbeeldafbeelding.
- Bestaande invoer behouden met een lokale herstelkopie vóór omzetting.

## 1.4.0 — 2026-10-14

- Bewonersportretten uploaden, compact opslaan en als kleine afbeeldingen op bewonerskaarten tonen.
- Locaties, inwoners, gildes en percelen afzonderlijk exporteren als JSON of CSV. Volledige kroniekexport blijft beschikbaar.
- Plaatsnaam vervangt Dorpsnaam in de interface.
- Perceelnamen zijn optioneel; eigenaars blijven zichtbaar.
- Alle percelen zichtbaar/onzichtbaar maken met een schakelaar boven de kaart.
- Percelen uitbreiden met aansluitende rastervakken, ook in onregelmatige vormen; eigendom blijft behouden.
- Bestaande opslag en oudere gegevens blijven ondersteund. Voor omzetting naar deze versie wordt een lokale herstelkopie bewaard als de browseropslag ruimte heeft.

## 1.3.0 — 2026-10-14

- Woningen en werkplaatsen tekenen als rechthoek, L- of T-vorm, met daken en botsingscontrole op de daadwerkelijk bezette vakken.
- Bestaande panden uitbreiden door een aansluitend deel te tekenen; naam, bewoners en stijl blijven behouden. Uitbreidingen ondersteunen ongedaan maken/opnieuw.
- Percelen volgen exact rastervakken. Bestaande vrije percelen worden naar buiten afgerond tot hele vakken.
- Percelen zijn rechtstreeks te openen via het gebouwenmenu om eigendom te wijzigen of ze te verwijderen.
- JPG, PNG of WebP laden als overtrekvoorbeeld, met instelbare doorzichtigheid en zichtbaarheid. Afbeeldingen worden verkleind voor lokale opslag en gaan mee in export/import.

## 1.2.2 — 2026-10-14

- Gereedschapsbalk en opties staan naast de kaart, zonder het tekenvlak te bedekken. Op kleine schermen staan ze erboven.
- Selecteren-knop verwijderd. Nieuwe locatie is verborgen in de kaart- en locatiesweergave; nieuwe gebouwen teken je op de kaart. Knoppen voor nieuwe inwoners, gildes en gebeurtenissen blijven beschikbaar.
- Menuopties, knoppen en formaatvelden opnieuw uitgelijnd.

## 1.2.1 — 2026-10-14

- Gereedschap vervangen door een smalle verticale knoppenbalk. Extra opties openen naast de gekozen knop en kunnen worden gesloten.
- Gum kiest standaard bomen; wissen raakt ook de randen van boomkronen. De ondergrondgum is duidelijk apart benoemd.
- Kaartformaat is achteraf aanpasbaar via de rasterknop. Bij verkleinen blijft inhoud buiten de kaart bewaard en wordt weer zichtbaar na vergroten.

## 1.2.0 — 2026-10-14

- Compact, inklapbaar gereedschapspaneel linksboven op de kaart; formaatinstellingen staan onder een uitklapmenu.
- Informatiepaneel standaard verborgen en met een knop te tonen/verbergen.
- Bomen vrij plaatsen en bosstroken tekenen, met gevarieerde boomkronen, schaduw en instelbare grootte. Bestaande rasterbossen worden behouden als vrije bomen; een aparte boomgum wist alleen bomen.
- Rechthoekige percelen vrij tekenen, benoemen en aan inwoners toekennen; eigendom wijzigen of een perceel verwijderen.
- Bomen en percelen worden bewaard, geëxporteerd en meegenomen in ongedaan maken/opnieuw.
- Vaste deuren op gebouwen verwijderd.

## 1.1.0 — 2026-10-14

- De tekenbalk blijft zichtbaar bij scrollen.
- Wegen en water zijn vrij te tekenen, los van het raster, met instelbare breedte.
- De gum kan afzonderlijk wegen, water of terrein wissen; andere lagen en gebouwen blijven behouden.
- Bestaande rasterwegen en rasterwater worden behouden op afzonderlijke lagen. Nieuwe lijnen kunnen over gewiste delen worden getekend.
- Panden hebben dakdetails, schaduw en automatische variatie. Bij bewerken zijn dakpannen, riet, leien en hout te kiezen.
- Bomen hebben gevarieerde loof- en naaldboomvormen, tinten en schaduw.
- Facties heten nu Gildes; bestaande gegevens en oudere exports blijven bruikbaar.
- Ongedaan maken, opnieuw uitvoeren, lokaal bewaren en export/import omvatten de nieuwe tekenlagen.

## 1.0.0 — 2026-10-14

Eerste vastgelegde versie van Fantasy Village Mapper. De bestaande prototypefuncties vormen de startversie; eerdere iteraties hebben geen afzonderlijke versienummers.

- Eigen dorpsnaam, stadskaart, locaties, inwoners, facties en tijdlijn.
- Kaartformaat in kolommen en rijen, met een optioneel raster.
- Gras, bos, water, wegen en bruggen tekenen per rastervak.
- Hele kaart vullen en rechthoeken vullen.
- Woningen en werkplaatsen tekenen en bewoners of medewerkers koppelen.
- DM- en spelersweergave, lokaal opslaan en export/import.
