# Mouse–Rat–Human Development Dataset

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
data/   → curated dataset(s)
code/   → scripts for data processing and analysis
docs/   → additional documentation
```

### Dataset Statistics

* **784 records** covering **371 unique developmental milestones**
* Milestones span both **Body** and **Brain** clusters
* Includes **prenatal and postnatal** developmental periods
* Species overlap:

  * **178** milestones shared between Human–Mouse
  * **167** shared between Human–Rat
  * **9** shared between Rat–Mouse
  * **17** common to all three species

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

If you use this dataset, please cite the accompanying publication:

> **[Placeholder for companion paper citation]**

### Related Work

The rat data included in this repository build upon a previously published rat–human developmental resource:

> **[[rat-and-human-comparative-development](https://github.com/Vazquez-Borsetti/rat-and-human-comparative-development)]**

---

## License

This project is currently released under the **MIT License**.

See [`LICENSE`](LICENSE) for the full license text.

---

## Repository Structure

```text
.
├── data/
│   └── curated developmental dataset(s)
│
├── CODE
├── LICENSE
└── README.md
```

---



## Acknowledgments

This work builds upon developmental data generated and published by numerous researchers and research groups.

We acknowledge all original authors whose studies contributed observations to this dataset. All developmental observations were traced back to their original empirical sources whenever possible.
