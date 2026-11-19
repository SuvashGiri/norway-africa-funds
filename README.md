# Hard Currency, Local Finance

How Norway's development finance reaches African businesses, and who carries the currency risk.

**Live report:** https://suvashgiri.github.io/norway-africa-funds/

## What it covers
- Ghana: why zero local-currency contracts does not mean zero local-currency finance
- 260 Brands (Zambia): kwacha financing for a Norfund investee, hedged by TCX and subsidised, according to TCX
- An interactive DSCR calculator for a kwacha-earning SME in Zambia: currency fit alone does not establish repayment capacity
- Local-currency structures: GIP Ghana, Sun King (Kenya) and PEPT 2 (Côte d'Ivoire)
- Supporting analysis: USD loans in Norfund's September 2026 snapshot set against historical currency stresses since November 2021
- Three options for local-currency finance, with their costs and conditions
- Context from NBIM's public holdings

## Method and limits
Built from public sources only: Norfund's investment overview workbook, Norfund and company announcements, daily exchange rates from ValutaFX and Pound Sterling Live, and NBIM's holdings data. Country shares are reconstructed at instrument level. The DSCR calculator uses illustrative assumptions, not market quotes. See the report for full method, sources and limits.

## Reproduce
The `analysis` folder holds `compute.py`, the derived tables (`country_summary.csv`, `commitments_by_country_instrument_currency.csv`) and `fx_observations.csv` with every exchange rate and its source page. Download Norfund's workbook from https://www.norfund.no/investment-overview/ and run `python compute.py Norfunds-Investment-Overview-30.09.26.xlsx`.

Independent project by Suvash Giri, built with an AI assistant. Not affiliated with or endorsed by Norfund, NBIM or TCX.
