# Vlastní EPG (TV program) – CZ/SK

Na GitHubu se 2× denně samo stáhne TV program na 3 dny dopředu pro 140 kanálů
(viz `channels.xml`). Výsledek je pak vždy na stejné adrese a stačí ji jednou zadat do přehrávače.

Zdroje dat: m.tv.sms.cz, webtv.sk, mujtvprogram.cz (přes open-source nástroj iptv-org/epg).

## Nastavení (jednorázově, asi 5 minut)

1. Založ si účet na https://github.com (zdarma).
2. Klikni na **+ → New repository**, název třeba `epg`, nastav **Public** a klikni na **Create repository**.
3. Klikni na **uploading an existing file** a přetáhni tam obsah rozbaleného ZIPu
   (soubory `channels.xml`, `README.md` a složku `.github`). Pak klikni na **Commit changes**.
   - Pozor: složka `.github` začíná tečkou a na Windows nebo Macu může být skrytá. Když ji nevidíš,
     vytvoř na GitHubu soubor přes **Add file → Create new file**. Jako název zadej
     `.github/workflows/epg.yml` a vlož do něj obsah toho souboru.
4. Otevři záložku **Actions** → **Aktualizace EPG** → **Run workflow**. Potrvá to zhruba 5–15 minut.
5. Až to doběhne (zelená fajfka), tvoje EPG adresa bude:

   ```
   https://raw.githubusercontent.com/TVOJE-JMENO/epg/epg/guide.xml
   ```
   Komprimovaná verze (menší, pokud ji přehrávač umí): `.../epg/epg/guide.xml.gz`

   `TVOJE-JMENO` nahraď svým uživatelským jménem na GitHubu.

## Když se program u některého kanálu nezobrazí

Přehrávač páruje EPG s kanály podle `tvg-id` v playlistu (M3U), případně podle názvu.
V `channels.xml` je u každého kanálu:
- `xmltv_id` (např. `Nova.cz`) – takové ID musí mít kanál v playlistu v `tvg-id`, **nebo**
- text mezi značkami (např. `Nova`) – podle toho párují přehrávače, které párují podle názvu.

Když se to neshoduje, stačí v `channels.xml` na GitHubu (ikona tužky) přepsat `xmltv_id`
nebo název na to, co je v playlistu. Při dalším běhu se to projeví.

## Kanály bez dostupného zdroje
KVIFF.TV, JOJ +1, Kanál 1, Šlágr Premium, VH1, Music Box Classic/Hits/Dance/Sexy,
Real Madrid TV, iVodárenství. Ani jeden ze tří zdrojů je nemá.
(Music Box má jen jednu společnou verzi „Music Box“.)
