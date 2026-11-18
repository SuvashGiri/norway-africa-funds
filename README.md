# Hard Currency, Local Finance

How Norway's development finance reaches African businesses, and who carries the currency risk.

**Live report:** https://suvashgiri.github.io/norway-africa-funds/

## What it covers
- How currency shocks affect dollar debt service: a map of the largest fall found in each currency against the USD since November 2021, against Norfund's commitments and hard-currency loans
- Norfund's public portfolio by country, instrument and contract currency (Africa outside South Africa)
- Three structures where financing reaches local businesses in local currency: Ghana, Sun King (Kenya) and PEPT 2 (Côte d'Ivoire)
- An interactive DSCR calculator for a kwacha-earning SME in Zambia
- Three levers for action: price, choice and power tariffs
- Context from NBIM's public holdings

## Method and limits
Built from public sources only: Norfund's investment overview workbook, Norfund, TCX and company publications, and daily exchange rates. Country shares are reconstructed at instrument level. The DSCR calculator uses illustrative assumptions, not market quotes. See the report for full method, sources and limits.

## Reproduce
The `analysis` folder holds `compute.py`, the derived tables and `fx_observations.csv` with every exchange rate and its source. Download Norfund's workbook from https://www.norfund.no/investment-overview/ and run `python compute.py Norfunds-Investment-Overview-30.09.26.xlsx`.

Independent project by Suvash Giri, built with an AI assistant. Not affiliated with or endorsed by Norfund, NBIM or TCX.
