DAT120 øving 7: Gruppeprosjekt del 1
Læringsmål
Dere skal lære å jobbe med en litt større programmeringsoppgave i grupper. Dere skal lære
grunnleggende bruk av Git og Github.
Overordnet oppgavebeskrivelse
Emne- og studieplanrevisjon er en prosess som skjer hver høst. Studieprogramlederne og de
som underviser emnene ser på de ulike emnene og studieprogrammene våre og ser om det er
noe som skal endres, både i studieprogrammene og i de enkelte emnene. Mange av emnene
brukes på flere studieprogrammer, og en endring i ett emne kan derfor påvirke mange
studieprogrammer. Dette gjelder særlig om et emne flyttes fra høst til vår eller motsatt.
Dette prosjektet går ut på å lage et forenklet system for å lagre og redigere studieplaner. I del 1 av
prosjektet skal dere lage et program som lar dere legge inn emner og sette opp ett enkelt
studieprogram for et bachelorstudium i ingeniørfag.
Oppgaver
a) Github repo: En av dere lager et Github repository for denne øvingen. De andre inviteres
med i dette repositoryet.
b) Github samarbeid: Hver student i gruppa skal klone dette Github repositoryet til sin
lokale datamaskin og jobbe i denne mappa med øvingen. Koden dere skriver i denne
øvingen skal lastes opp til Github repoet. Dere kan gjerne jobbe på hver deres grein av
prosjektet og så flette (merge) dette inn i hovedgreinen (main branch) når dere er ferdige
med en deloppgave.
c) Oppgavefordeling: Tenk over hvordan dere skal fordele oppgavene mellom
gruppemedlemmene og hva som bør gjøres felles. Dere kan se på hvilke funksjoner dere
skal definere i de ulike deloppgavene og så tenke over hvilke av disse funksjonene som
kan skrives uavhengig av de andre.
d) Lag programmet: Programmet skal starte med å skrive ut menyen oppgitt i delkapitlet
«menyvalg». Delkapitlet «beskrivelse av hvert menyvalg» inneholder en beskrivelse av
hva hvert menyvalg skal gjøre. Implementer alle de obligatoriske menyvalgene, som er
alle menyvalgene som ikke er markert «frivillig». Hvis dere ønsker, kan dere også
implementere de frivillige menyvalgene
Menyvalgene

1. Lag et nytt emne
2. Legg til et emne i studieplanen
3. Skriv ut ei liste over alle registrerte emner
4. Skriv ut studieplanen med hvilke emner som er i hvert semester
5. Sjekk om studieplanen er gyldig eller ikke
6. Lagre emnene og studieplanen til fil
7. Les inn emnene og studieplanen fra fil
8. Avslutt
9. Frivillig: Slett et emne
10. Frivillig: Fjern et emne fra studieprogrammet uten å slette det fra emnelista
11. Frivillig: Legg til anbefalt valgemne
12. Frivillig: Fjern anbefalt valgemne
13. Frivillig: Legg til annet valgemne
14. Frivillig: Fjern annet valgemne
    Beskrivelse av hvert valg
15. Lag et nytt emne: Et emne skal ha minimum en emnekode, om emnet undervises høst
    eller vår, og antall studiepoeng. Dere kan lagre dette i tre lister, en for emnekoder, en for
    semester (høst eller vår) og en for antall studiepoeng, og hvor samme indeks i de tre
    listene representerer samme emne.
16. Legg til et emne i studieplanen: En studieplan består av seks semester nummeret 1-6
    hvor semester 1, 3 og 5 er høstsemester og semester 2, 4 og 6 er vårsemestre. Hvert
    semester kan representeres som ei liste med indekser inn i emne-listene. Dere skal også
    sjekke at et emne er lovlig i det semesteret brukeren prøver å legge det inn i. Det
    involverer følgende:
    o Sjekk at emnet ikke allerede er med i studieplanen. Et emne skal bare kunne
    legges til en gang.
    o Sjekk at emnet legges til i et gyldig semester. Høstemner skal bare kunne legges
    til i semester 1, 3 eller 5. Våremner skal bare kunne legges til i semester 2, 4 eller
17. o Sjekk at det er plass i semesteret til emnet. Et semester skal inneholder
    maksimalt 30 studiepoeng med emner.
18. Skriv ut ei liste over alle registrerte emner
19. Skriv ut studieplanen med hvilke emner som er i hvert semester
20. Sjekk om studieplanen er gyldig eller ikke. En studieplan er bare gyldig hvis hvert av de
    seks semestrene inneholder 30 studiepoeng emner. Er ikke studieplanen gyldig, skriv ut
    hvilke semestre som ikke er gyldige og hvor mange studiepoeng emner det er i det
    semesteret.
21. Lagre emnene og studieplanen til fil. Lag ei eller flere tekstfiler med denne
    informasjonen, det er opp til dere å finne ut hvilket format denne fila skal ha
22. Les inn emnene og studieplanen fra fil. Denne skal lese samme fil som bel skrevet i
    punkt 6.
23. Avslutt
24. Frivillig: Slett et emne
25. Frivillig: Fjern et emne fra studieprogrammet uten å slette det fra emnelista
26. Frivillig: Legg til anbefalt valgemne: Ett semester, typisk 5. semester, er satt av til
    valgemner. Det skal være maksimalt 5 anbefalte valgemner, som skal være på minimum
    40 studiepoeng totalt
27. Frivillig: Fjern anbefalt valgemne
28. Frivillig: Legg til annet valgemne: Det er ingen restriksjoner på antall og studiepoeng i
    andre valgemner, men de må være i riktig semester (høst for valgemner i 5. semester)
29. Frivillig: Fjern annet valgemne
    Merk: For å teste menyvalget «Sjekk om studieplanen er gyldig eller ikke» kan dere enten bare
    legge inn noen eksempelemner i semesteret for valgemner eller dere kan legge inn emner som
    for eksempel «Valgemne1, 10 studiepoeng, semester Høst» for å sjekke koden for om en
    studieplan er gyldig eller ikke. Bruk gjerne deres egen studieplan som eksempel når dere tester.
    Merk: Tenk over hvordan dere refererer til et emne i listene i studieplanen. Det er flere
    muligheter, inkludert følgende:

- Referer til en indeks i emnelistene. Dette gir enklest kode for å legge inn emner og skrive
  ut studieplanen, men skal dere ha mulighet for å slette emner så blir det mye
  vanskeligere. Om dere sletter et emne fra emnelistene så vil indeksene til alle emner
  som er etterpå i listene endre seg.
- Referer til en emnekode. Gjør dere dette må dere slå opp i lista for emnekoder for å finne
  indeksen til emnet for å finne de andre dataene om emnet (semester og studiepoeng),
  men sletting av emner blir mye enklere siden emnekoden til de andre emnene ikke
  endrer seg.
  Godkjenning
  Denne øvingen og øving 10 skal gjøres i grupper på inntil 4 studenter. Øvingen skal godkjennes
  ved å demonstrere det gruppa har lagd på samme vis som for de tidligere øvingene. I tillegg skal
  dere vise studentassistenten Github repo-et deres. Denne øvingen og øving 10 skal godkjennes
  bare en gang for hver gruppe, dere kan demonstrere en gang og så får alle i gruppa godkjent.
