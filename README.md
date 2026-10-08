# Mouse–Rat–Human Development Dataset

[![DOI](https://zenodo.org/badge/1206348570.svg)](https://doi.org/10.5281/zenodo.23246067)

A curated open dataset for translating developmental timing across **mouse, rat, and human**.

## Overview

This repository provides an open, curated dataset designed to facilitate **cross-species translation of developmental timing** between mouse, rat, and human.

The project integrates heterogeneous and non-standardized data from multiple sources into a unified framework, enabling the alignment of comparable biological events across species.

The dataset spans developmental stages from **prenatal periods to adulthood** and includes homologous structural, functional, and molecular milestones. These encompass sensory system maturation, neuroanatomical events, behavioral changes, and processes from other physiological systems.

The dataset expands a previously published **rat–human developmental dataset** by incorporating newly curated mouse developmental data obtained through systematic review of the empirical literature.

---

## Dataset Contents

The repository is organized as follows:

```text
data/           → curated dataset (CSV) and its data dictionary, with its own README/LICENSE for Zenodo
src/            → shared configuration, model definitions, and plotting utilities
*.ipynb         → analysis notebooks that generate each manuscript figure panel
figures/        → generated figures (not version-controlled; recreated by running the notebooks)
requirements.txt → Python dependencies
```

### Dataset Statistics

* **783 records** covering **371 unique developmental milestones**
* Milestones span both **Body** and **Brain** clusters
* Includes **prenatal and postnatal** developmental periods
* Species overlap (among the 371 unique milestones):

  * **179** shared exclusively between Human–Mouse
  * **167** shared exclusively between Human–Rat
  * **9** shared exclusively between Rat–Mouse
  * **16** common to all three species

---

## Metadata Structure

The dataset is structured with the following columns:

| Column      | Description                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------- |
| `Species`   | Species of the observation (`Human`, `Mouse`, or `Rat`)                                           |
| `Parameter` | Name of the developmental milestone                                                               |
| `DAF`       | Developmental age standardized as Days After Fertilization (fertilization = day 0)                |
| `GA(H+14)`  | Gestational age equivalent                                                                        |
| `Cluster`   | Tissue or physiological category (`Brain` or `Body`)                                              |
| `Obs`       | Methodological notes and additional observations                                                  |
| `Reference` | Bibliographic source                                                                              |
| `DOI`       | Digital Object Identifier of the source                                                           |
| `Quote`     | Traceability field containing supporting text, figure, or table excerpts from the original source |

---

## Data Collection, Curation, and Standardization

Data were compiled from previously published studies and systematically extracted from the scientific literature. A rigorous harmonization process was applied to standardize developmental events and enable cross-species comparisons.

### Standardization

Developmental ages originally reported using different temporal scales were converted to **Days After Fertilization (DAF)** using species-specific gestational durations:

| Species | Gestational duration used for DAF conversion |
| ------- | -------------------------------------------: |
| Human   |                                   268.2 days |
| Rat     |                                    22.5 days |
| Mouse   |                                      20 days |

For humans, **268.2 days after fertilization** corresponds to a mean gestational duration of **282.2 days** when the conventional 14-day difference between fertilization and gestational age is taken into account.

Additional standardization procedures included:

* Ages reported in postnatal days, weeks, months, or years were converted to DAF.
* Narrow age ranges were represented by their midpoint.
* Wider or explicitly bounded age ranges were recorded as separate start/end values when appropriate.
* Duplicate records corresponding to the same `Parameter + Species` combination were retained when they originated from different studies.
* When multiple observations were available for the same developmental milestone and species, the **mean** was used as the representative value for modeling.

### Curation Process

Each entry was:

1. Manually validated by a domain expert.
2. Cross-checked against the original source.
3. Standardized in terminology to minimize duplicate milestone names across species.
4. Retained only when a traceable original source was available.

Entries lacking a traceable primary source were excluded, even when they had been reported in previously curated datasets.

Potential outliers were flagged and removed only when supported by more robust or conflicting empirical sources.

---

## Intended Use Cases

This dataset can be used for:

* Cross-species comparison of developmental timelines.
* Modeling developmental time translation.
* Evaluating scaling laws and deviations from them.
* Testing **quarter-power scaling models** relating human and rodent developmental ages.
* Supporting research in translational developmental biology.
* Supporting comparative developmental neuroscience.
* Developing and evaluating animal models of human developmental processes.

---

## Citation and Related Work

If you use this dataset or code, please cite the accompanying publication:

> Amici E, Grimson R, Vazquez-Borsetti P. Open Dataset of Developmental Timelines for
> Corresponding Milestones in Mice, Rats, and Humans. (manuscript in preparation, 2026).

Please also cite the specific resource you used, archived on Zenodo with its own DOI:

* Dataset: [10.5281/zenodo.23244347](https://doi.org/10.5281/zenodo.23244347)
* Code (this repository): [10.5281/zenodo.23246067](https://doi.org/10.5281/zenodo.23246067)

### Related Work

The rat data included in this repository build upon a previously published rat–human
developmental resource:

> Campos Eusebi W, Iorii T, et al. Divergent Pattern of Development in Rats and Humans.
> Neurotoxicity Research. 2024. https://doi.org/10.1007/s12640-023-00683-y
> Companion dataset: [rat-and-human-comparative-development](https://github.com/Vazquez-Borsetti/rat-and-human-comparative-development)

The modeling framework (quarter-power model with an additive constant) used to translate
developmental time across species, applied to this dataset, is described in a companion
modeling paper (manuscript in preparation), with code and results available at:
[quarter-power-C-human-rodent-translation](https://github.com/Vazquez-Borsetti/quarter-power-C-human-rodent-translation)

---

## License

This project is released under the **Creative Commons Attribution-NonCommercial-ShareAlike
4.0 International License (CC BY-NC-SA 4.0)**.

See [`LICENSE`](LICENSE) for the full license text. Note that the `data/` folder is archived
independently on Zenodo and carries its own copy of the same license (see
[`data/LICENSE`](data/LICENSE)).

---

## Repository Structure

```text
.
├── data/
│   ├── dataset_mrh_0.9.csv   (curated dataset)
│   ├── DATA_DICTIONARY.md
│   ├── README.md             (Zenodo-ready dataset documentation)
│   └── LICENSE
├── src/                      (shared config, models, plotting utilities)
├── panel1and2.ipynb
├── panel3_0.2.ipynb
├── panel4D_0.4.ipynb
├── panel5D0.1.ipynb
├── requirements.txt
├── LICENSE
└── README.md
```

---


## Acknowledgments

This work builds upon developmental data generated and published by numerous researchers and research groups.

We acknowledge all original authors whose studies contributed observations to this dataset. All developmental observations were traced back to their original empirical sources whenever possible.
