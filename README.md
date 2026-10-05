# Bank Telemarketing Targeting

Which customers should a bank call first? An analysis of 45,211 telemarketing
contacts to help a campaign team prioritize outreach under a limited call budget.

> 🚧 Work in progress

## Data

- **Source:** Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing* [Dataset].
  UCI Machine Learning Repository. https://doi.org/10.24432/C5K306
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- The file `data/bank-full.csv` is unmodified from the original source.

## Acknowledgement

The project idea was inspired by
[Rajverma1718/bank-marketing-analysis](https://github.com/Rajverma1718/bank-marketing-analysis).
All code in this repository is my own.

## Run locally

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python explore.py
```