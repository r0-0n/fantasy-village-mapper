# Fantasy Village Mapper

Een webapp om een fantasiedorp te tekenen en te beheren, met gebouwen, inwoners, gildes en een campagnetijdlijn.

Huidige versie: **1.42.0**. De actuele versie staat in `VERSION`; wijzigingen staan in `CHANGELOG.md`.

## Starten

Serveer de map `dist` met een statische webserver. Er is geen installatie of build nodig. Bijvoorbeeld met Python: `python3 -m http.server 8765 --directory dist`. Open daarna `http://localhost:8765`.

Gegevens worden in de browser op dit apparaat opgeslagen. Gebruik export/import om je dorpskroniek te bewaren of over te zetten. De spelersweergave verbergt DM-informatie op het scherm; er zijn geen afzonderlijke spelersaccounts.

## Versiebeleid: A.B.C

Dit project gebruikt de volgende eigen indeling:

- **A**: verandering in het uitgangspunt van de app.
- **B**: nieuwe features.
- **C**: bugfixes en veranderingen aan bestaande functionaliteiten.

Verhoog per afgeronde wijziging de hoogste toepasselijke component één keer. Bij een verhoging van A worden B en C nul; bij een verhoging van B wordt C nul. Samenhangende wijzigingen voor één verzoek krijgen samen één versie. Alleen documentatie aanpassen of dezelfde broncode opnieuw verpakken verandert de versie niet.

Voorbeelden vanaf 1.0.0: een fout herstellen wordt 1.0.1, een nieuwe feature wordt 1.1.0 en een nieuw uitgangspunt wordt 2.0.0.

Houd `VERSION`, het zichtbare nummer in `dist/index.html` en `CHANGELOG.md` gelijk.

## Gegevens behouden bij updates

De app gebruikt dezelfde bestaande browseropslag (`tarnstead-v1`). Migraties voegen gegevens toe en behouden bestaande namen, verhalen, koppelingen, kaartlagen en afbeeldingen. Oudere volledige kroniekexports blijven importeerbaar. Blijf dezelfde URL gebruiken; opslag van een lokale HTML-download en een webadres is niet automatisch gedeeld. Maak met **Exporteer kroniek** een overdraagbare volledige reservekopie. Afzonderlijke JSON/CSV-exports van onderdelen zijn bedoeld voor gebruik buiten de app; voor terugzetten gebruik je de volledige kroniekexport.

## Bezittingen en inkomsten

Wijs een eigenaar aan panden toe en kies hun financiële regelprofiel. Bewoning en werkplek blijven aparte koppelingen. Het overzicht berekent verwachte inkomsten en kosten per campagneweek; eenmalige bouwkosten staan apart. Tarieven en bedragen per pand/perceel zijn aanpasbaar; gebruik Wijzigingen bewaren. Aankopen van extra plots voer je expliciet in, niet op basis van getekende oppervlakte. De startplot is op verzoek 16 rastervakken. Standaardtarieven komen uit DDAC - Tarnstead Basisregels; dit is een aanpasbaar campagneoverzicht, geen bijgehouden saldo.

Het financiële overzicht kan naar Markdown (standaard), CSV of JSON worden geëxporteerd. Omzet is bruto, netto is na weekkosten. De waarde van de plaats is de som van ingestelde pandwaarden en gekochte extra plots; eenmalige reparaties en andere extra kosten vallen daarbuiten. Percelen hebben geen eigen inkomsten, onderhoud of handmatig toegevoegde aanschafbedragen. Nieuwe tariefprofielen en personeelsniveaus zijn toevoegbaar. Oudere gildedata en perceelbedragen blijven bewaard in de volledige export, ook als ze niet meer in de interface of berekening voorkomen.

Het financiële overzicht heeft aparte tabbladen voor Overzicht, Panden, Percelen, Tarieven en Uitbetalingen. Kies zelf ontvangers en markeer de betaling per campagneweek; betaalde bedragen worden vastgelegd. De meewerkende eigenaar heeft standaard factor 2, die met de personeelsfactor wordt vermenigvuldigd. Tarieven verwijderen archiveert de regel voor nieuwe keuzes, terwijl bestaande panden hun berekening behouden. Extra kosten zijn tijdelijk uit de interface en berekening gehaald; oude invoer blijft opgeslagen.

## Kanselarij en kalender
Losstaande stukken grond worden afzonderlijke percelen, ook bij dezelfde eigenaar. De eigenaar is per perceel aanpasbaar. Aangrenzende percelen van dezelfde eigenaar blijven samengevoegd.
Uitbetalingen: alles selecteren betreft de getoonde inwoners. Klaargezette weekbedragen worden bewaard en openstaande bedragen uit andere geregistreerde weken staan onder de weektabel. Niet geopende weken worden niet automatisch achteraf berekend. Selectie wissen verwijdert geen reeds klaargezette betalingen.
Bij Tijdlijn → Kalender instellen kies je Harptos of de gewone kalender en de startdatum van campagnedag 1. Bestaande gebeurtenissen houden hun campagnedag. Een betaalweek blijft zeven dagen.

## Rijkdom en volgorde
Met ↑ en ↓ wijzig je de volgorde van regelprofielen en personeelsniveaus. Inwoners staan op rijkdom: pandwaarden + gekochte extra grond + bank + contant. Bank en contant zijn handmatige saldi, los van geregistreerde uitbetalingen. Financiële inwonergegevens zijn alleen zichtbaar in DM-weergave. De datum bovenin toont de chronologisch laatste zichtbare gebeurtenis; zonder gebeurtenissen geldt de campagnedag.

## Automatische plots en opslag (1.42.0)
Plots in bezit = unieke vakjes van toegewezen percelen / vakken per plot (standaard 16). Fracties blijven behouden. Ook het eerste plot telt mee; alle plots worden naar verhouding gewaardeerd tegen de ingestelde prijsschijven, boven de laatste schijf geldt de laatste prijs. Oude handmatige aantallen worden behouden als historische gegevens maar niet meer gebruikt.
Financiële invoer wordt tijdens geldig invoeren automatisch opgeslagen; bij verlaten van het veld wordt de weergave bijgewerkt. Overzicht sorteer je via keuzelijsten; panden via de kolomkoppen. Alle profielen gebruiken de factoren van personeel en meewerkende eigenaar, ook bestaande profielen; handmatige opbrengstoverrides blijven behouden.

## Kaart en ranglijst (1.42.0)
Inwoners staan onder elkaar, rijkste bovenaan. Klik op een rij om de inwoner te bewerken. De kaart past binnen het scherm. Zoom met +, − of het muiswiel. Verschuif met de knop Verschuiven, Shift-slepen of de middelste muisknop. Passend maken toont de hele kaart. Zoomen verandert de kaartgegevens en exports niet.

Je kunt de kaart ook verschuiven door de rechtermuisknop ingedrukt te houden en te slepen.

Vanaf 1.42.0 telt ook het eerste plot mee in de grondwaarde: 16 vakjes tegen het eerste plot-tarief (standaard 500 gp). Delen worden naar verhouding berekend.

## Overnachtingen
Een inwoner zonder geldige toegewezen woonlocatie verblijft automatisch in The Crossroads Rest: 1 gp per nacht, 7 gp per week. De kosten worden meegenomen in het nettoresultaat. De herberg krijgt deze opbrengst bovenop de ingestelde pandopbrengst, ook bij een handmatige opbrengst. De eigenaar ontvangt die inkomsten via het pand. Een toegewezen woonlocatie beëindigt het automatische verblijf. Banksaldi veranderen niet automatisch; eerder klaargezette weekbedragen blijven behouden.

## Persoonsoverzicht en ontvangst
Onder Tarieven wijzig je het tarief per nacht. Bestaande weekmomentopnamen blijven behouden. Bij Uitbetalingen bevestig je eerst betaald en daarna ontvangen; heropenen van betaald wist ook de ontvangstbevestiging. Onder Overzicht → Persoonsoverzicht vind je eigendom, saldi en geregistreerde betalingen, met een Markdown-export zonder DM-geheimen. Losse betalingen kun je vanuit de inwoner als ontvangen of gedaan registreren. Deze registratie wijzigt banksaldi niet automatisch.

## Ontwikkeling van de stad
Onder de Kanselarij-kop staan vijf grafieken. De eerste stand begint bij gebruik van deze versie. Iedere campagnedag heeft één stand; wijzigingen op dezelfde dag werken die stand bij. Eerdere dagstanden blijven bewaard in de kroniekback-up. De grafieken tonen de hele stad; omzet, winst en kosten zijn verwachte weekbedragen. Locaties tonen inwoners met een gekoppelde werkplek, de meewerkende eigenaar en het ingehuurde niveau zolang daar geen naam voor is geregistreerd.

Vanaf 1.42.0 toont het persoonsoverzicht HTML; Export MD levert Markdown. Losse betalingen registreer je uitsluitend onder Uitbetalingen, met richting vanuit de Kanselarij (van inwoner ontvangen of aan inwoner betaald). De betaalhistorie blijft vanuit de inwoner weergegeven. Grafieken staan onder Overzicht.

## Medewerkers en ontvangen weekbedragen
Personeel wordt aan een inwoner gekoppeld; zonder bestaande medewerker ontstaat een NPC met een voorlopige naam. Bewerk naam, leeftijd, ras, klas en omschrijving via Inwoners of de personeelscel. De NPC telt één keer mee en krijgt geen automatische herbergkosten. Negatieve weekresultaten zijn bedragen die de Kanselarij van de inwoner ontvangt; de ontvangst staat als gedane betaling in diens overzicht. Historische betaalde bedragen blijven behouden.

## Automatisch medewerkersloon
Vanaf de huidige campagneweek wordt het ingestelde personeelsloon eenmaal per week per pand als betaald geregistreerd voor de gekoppelde medewerker. Bij vooruitgaan worden overgeslagen weken vanaf de startweek verwerkt tegen de dan geldende personeelsinstellingen; historische gegevens van vóór deze functie worden niet verzonnen. Bestaande boekingen blijven behouden bij loonwijzigingen. De hoogste campagnedag of tijdlijndag bepaalt de week (zeven dagen). Uitbetalingen toont Medewerkersloon; het persoonsoverzicht/export bevat deze ontvangsten. De bestaande loonkosten blijven bij het pand; banksaldi worden nog steeds handmatig bijgehouden.

Vanaf 1.42.0 bepaalt uitsluitend de hoogste campagnedag in de tijdlijn de betaalweek: dag 1–7 is week 1, dag 8–14 week 2. Salarissen worden vanaf week 1 tot die week verwerkt; geselecteerde inwonerbetalingen worden klaargezet. Ontbrekende oude weken gebruiken huidige tarieven. Bestaande betalingen blijven behouden, ook bij terugzetten of verwijderen van een tijdlijnentry. Zonder entries worden geen automatische nieuwe weken gemaakt.

Vanaf 1.42.0 zijn alleen volledig verstreken weken beschikbaar. De datum van de laatste tijdlijnentry, vertaald naar de ingestelde Harptos-startdatum, bepaalt verstreken dagen: dag 8 opent week 1, dag 15 week 2. De lopende week is uitgesloten.

## Ingangsdatums en historie
Kanselarij → Ingangsdatums & historie toont aanmaak en wijzigingen van panden, inwoners en percelen. Bestaande gegevens hebben een voorlopige datum dag 1, expliciet te controleren. Nieuwe wijzigingen gebruiken de laatste tijdlijndatum; datums zijn achteraf instelbaar. Weekbetalingen gebruiken de situatie op dag 7, 14 enzovoort, zonder verdeling binnen de week. Reeds geboekte bedragen blijven behouden; historische tariefwijzigingen vóór deze versie zijn niet bekend.

Bij Harptos geldt vanaf 1.42.0 een tenday van 10 campagnedagen: dag 11 opent periode 1, dag 21 periode 2. De gewone kalender blijft 7 dagen gebruiken. Ingestelde opbrengsten en personeelslonen gelden per gekozen periode; overnachtingen blijven per nacht. Bestaande boekingen blijven behouden.

NPC-loon wordt vanaf 1.42.0 contant verwerkt. Betaalde, zichtbare periodes zonder verwerkingsmarkering tellen eenmaal bij contant geld op. Datums wijzig je bij Inwoners/Locaties → Ingangsdatums & historie, of met de datumknop in een bewerkvenster. Klik vervolgens op de datum in de historie.

Vanaf 1.42.0 betaal je medewerkers handmatig bij Uitbetalingen → Medewerkersloon → Eigenaar betaalt contant. De eigenaar moet voldoende contant geld hebben. De betaling trekt contant geld van de eigenaar af en telt het bij de medewerker op. Eerdere betaalde records worden niet teruggedraaid. De historie noemt gewijzigde velden met oude en nieuwe waarden.

## Stadsinstellingen en overschrijvingen (1.42.0)
Links bij Stadsinstellingen kies je een Lord Protector (Burgemeester) en het gebouw voor automatische overnachtingen. Beide kunnen later naar een PC en diens pand worden gewijzigd. De eigenaar van het geselecteerde pand ontvangt het overnachtingsgeld. Zonder gekozen gebouw worden geen nieuwe automatische overnachtingskosten berekend; al geboekte bedragen blijven behouden.
Onder Uitbetalingen staat Bankoverschrijving met Van, Naar, bedrag en omschrijving. Alle inwoners, ook NPC’s, kunnen geld overmaken. De bankmutatie staat in het kasboek en beide persoonlijke overzichten. Verwijderen uit het kasboek draait beide saldi terug. In het persoonsoverzicht kun je een onterechte betalingsverplichting verwijderen; die wordt niet opnieuw klaargezet. Er wordt een bevestiging gevraagd voordat een uitgevoerde betaling wordt teruggedraaid.

## Bediening (1.42.0)
Panden is de nieuwe naam van Locaties. Plaatsnaam en kalender vind je onder Stadsinstellingen. De verplichte keuzes blijven Lord Protector en overnachtingsgebouw; zodra beide ingevuld zijn klapt het blok na een wijziging in. Je kunt het daarna opnieuw openen. Kaartinstellingen blijven bij de kaart; financiële tarieven blijven rechts in de Kanselarij. Prullenbakken verwijderen en potloodjes wijzigen; bij aanwijzen staat de volledige actie, ook beschikbaar voor schermlezers. De Lord Protector heeft een gouden kroon.

## Financiële status (1.42.0)
Overzicht toont per inwoner bank, contant, panden, grond, rijkdom, te betalen en te ontvangen. Klik op een kolomkop om te sorteren, of gebruik de keuzelijsten. Openstaande bedragen omvatten geregistreerde, niet betaalde periodes en salarissen; toekomstige en vervallen regels tellen niet mee. Rijkdom toont bezittingen plus saldi, los van deze nog openstaande bedragen.
Via Bekijken / exporteren krijg je de actuele spelerstatus met openstaande bedragen. Markdown en een zelfstandige afdrukbare HTML-export zijn beschikbaar, zonder DM-geheimen of wijzigingsknoppen. Geld overmaken doe je bij Uitbetalingen; historie en verwijderen vind je bij Kasboek. Verwijderen draait uitgevoerde geldmutaties terug na saldocontrole. In de pandentabel herstelt Automatisch de berekening van alleen het betreffende handmatig aangepaste veld.

Versie 1.42.0: horizontale kaartwerkbalk, flexibele inwonerkaarten, portretten en echte perceelaantallen in het financiële overzicht. Pand- en perceelkaarten openen instellingen; het vizier gaat naar de kaartpositie. Panden tonen eigenaar, medewerkers, bewoners en waarde; percelen tonen ook welke panden er geheel of gedeeltelijk op staan. Grondprijzen blijven op dezelfde standaardmaat berekend.

Versie 1.42.0 voegt een ingebouwd SVG-logo/favicon, portrethouders en een werkplekveld toe. Woon-, werk- en eigendomskoppelingen vragen om een ingangsdatum. Historie bevat entiteitwijzigingen; geldmutaties staan in het kasboek. Grafieken volgen de unieke tijdlijndatums en berekenen daarvoor de historische situatie.

Versie 1.42.0: onder Kanselarij → Akten maak je zes soorten akten. Kies een PC/NPC of vul een externe naam in; dat maakt geen inwoner aan. Een huwelijk verschijnt bij de gekoppelde inwoners. Akten bewaren namen, datum, autoriteit en geselecteerd eigendom als momentopname. Download de HTML of open Afdrukversie / PDF en kies in de browser voor afdrukken of opslaan als PDF. De volledige kroniekexport bevat het aktenregister. Geld, eigendom en inwonerstatus veranderen niet automatisch door een akte.

Versie 1.42.0: upload een eigen stadswapen of zegel onder Stadsinstellingen. Dit wordt gebruikt bij het genereren van akten; het app-logo blijft apart. Ingetrokken akten kunnen worden verwijderd en via het statusfilter worden hersteld als ingetrokken akte. Bij personen staan partner en gekoppelde akten; registreren en beheren gebeurt in de Kanselarij.

Versie 1.42.0: Harptos-datumkiezer met dagenraster. Alleen de tijdlijn kan vooruit; andere registraties zijn begrensd op de huidige campagnedatum. Historie opnieuw beginnen behoudt de huidige stad, geld en administratie, maar wist de wijzigingshistorie en gebruikt de huidige situatie als uitgangspunt voor vroegere berekeningen. Maak zo nodig eerst de aangeboden backup. Akten verwijderen is definitief; de eerdere prullenbak kan via de aparte opruimknop definitief worden gewist.
