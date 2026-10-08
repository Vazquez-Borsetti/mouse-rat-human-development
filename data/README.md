# Open Dataset of Developmental Timelines for Corresponding Milestones in Mice, Rats, and Humans

A curated, open-access dataset of general and neurodevelopmental milestones in **mouse**,
**rat**, and **human**, compiled through a systematic review of the empirical literature.

## Authors

* Eugenia Amici (1)
* Rafael Grimson (2)
* Pablo Vazquez-Borsetti (1)

1. Instituto de Biologia Celular y Neurociencia (IBCN), Universidad de Buenos Aires and
   Consejo Nacional de Investigaciones Cientificas y Tecnicas (CONICET), Argentina.
2. 3iA (Instituto de Investigacion e Ingenieria Ambiental), UNSAM/CONICET, Buenos Aires,
   Argentina.
   
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23244347.svg)](https://doi.org/10.5281/zenodo.23244347)
## Overview

Translating developmental time across species is essential for the appropriate design and
interpretation of preclinical neurodevelopmental research, yet no open, unified resource
previously integrated high-quality developmental milestone data for mouse, rat, and human.

This archive provides a curated, open-access dataset of general and neurodevelopmental
milestones spanning these three species, expanding a previously published rat-human database
(Campos Eusebi et al., 2024; see "Related Work" below) with newly compiled mouse data.
Following a systematic literature search, **783 records** covering **371 unique developmental
milestones** were extracted, standardized to Days After Fertilization (DAF), and validated
through a structured curation and quality-control process.

Milestones span **prenatal and postnatal** developmental periods and encompass sensory system
maturation, neuroanatomical events, behavioral changes, and processes from other physiological
systems, classified into **Body** and **Brain** tissue clusters.

Species overlap among the 371 unique milestones:

* 179 shared exclusively between Human and Mouse
* 167 shared exclusively between Human and Rat
* 9 shared exclusively between Rat and Mouse
* 16 common to all three species

## Files in This Archive

| File | Description |
| --- | --- |
| `dataset_mrh_0.9.csv` | The curated dataset: 783 rows x 11 columns, one row per (Species, Parameter, Reference) age record. |
| `DATA_DICTIONARY.md` | Detailed column-by-column data dictionary, including types, cardinality, and usage notes. |
| `README.md` | This file. |
| `LICENSE` | License terms for the dataset (CC BY-NC-SA 4.0). |

## Dataset Columns

| Column | Description |
| --- | --- |
| `Species` | Species of the observation: `Human`, `Mouse`, or `Rat`. |
| `Parameter` | Name/description of the developmental milestone, standardized across sources to avoid duplicate naming of the same event. |
| `DAF` | **Days After Fertilization** — standardized developmental age, with fertilization defined as day 0. Primary age variable used throughout the analyses. |
| `GA(H+14)` | Human **Gestational Age**, counted from the last menstrual period (LMP), computed as `DAF + 14`. Only populated for `Species == Human`. |
| `Cluster` | Tissue/domain classification of the milestone: `Brain` or `Body`. Missing only for the `Birth` reference rows. |
| `Obs` | Free-text curator notes (e.g., justification for excluding/adjusting a value, discrepancies with the cited source, data-quality caveats). |
| `Reference` | Bibliographic citation (author, year) for the source of the record. |
| `DOI` | Digital Object Identifier of the reference, used as a unique key for reference-level aggregation. |
| `link` | Alternative URL to the source when no DOI is available (e.g., scanned books). |
| `Quote` | Traceability field: verbatim excerpt from the source text and/or reference to a supporting figure/table. |
| `Data_curator` | Name of the person/team who curated the record (used for provenance). |

See `DATA_DICTIONARY.md` for full details, including cardinality and missing-data counts per
column.

## Data Collection, Curation, and Standardization

Data were compiled from previously published studies and systematically extracted from the
scientific literature, following a structured search across international scientific databases
to identify developmental milestones for humans, rats, and mice (English-language articles
only).

**Standardization.** Developmental ages originally reported using different temporal scales
were converted to Days After Fertilization (DAF) using species-specific gestational durations:

| Species | Gestational duration used for DAF conversion |
| --- | ---: |
| Human | 268.2 days |
| Rat | 22.5 days |
| Mouse | 20 days |

For humans, 268.2 days after fertilization corresponds to a mean gestational duration of 282.2
days once the conventional 14-day difference between fertilization and gestational age (LMP)
is taken into account.

Additional standardization procedures included:

* Ages reported in postnatal days, weeks, months, or years were converted to DAF.
* Narrow age ranges were represented by their midpoint.
* Wider or explicitly bounded age ranges were recorded as separate start/end values when
  appropriate.
* Duplicate records corresponding to the same `Parameter` + `Species` combination were
  retained when they originated from different studies (not averaged in this raw file; the
  mean is computed downstream as the representative value for modeling).

**Curation.** Each entry was manually validated by a domain expert, cross-checked against the
original source, standardized in terminology to minimize duplicate milestone names across
species, and retained only when a traceable original source was available. Entries lacking a
traceable primary source were excluded, even when previously reported in other curated
datasets. Potential outliers were flagged and removed only when supported by more robust or
conflicting empirical sources.

## Intended Use Cases

This dataset can be used for:

* Cross-species comparison of developmental timelines.
* Modeling developmental time translation between mouse, rat, and human.
* Evaluating scaling laws (including quarter-power models) and deviations from them.
* Supporting research in translational developmental biology and comparative developmental
  neuroscience.
* Informing the design and interpretation of animal models of human developmental processes.

## How to Cite

If you use this dataset, please cite the companion publication:

> Amici E, Grimson R, Vazquez-Borsetti P. Open Dataset of Developmental Timelines for
> Corresponding Milestones in Mice, Rats, and Humans. (manuscript in preparation, 2026).

Please also cite this Zenodo archive directly:

> Amici E, Grimson R, Vazquez-Borsetti P. Open Dataset of Developmental Timelines for
> Corresponding Milestones in Mice, Rats, and Humans [Data set]. Zenodo, 2026.
> https://doi.org/10.5281/zenodo.23244347

### Related Work

This dataset expands a previously published rat-human developmental resource:

> Campos Eusebi W, Iorii T, et al. Divergent Pattern of Development in Rats and Humans.
> Neurotoxicity Research. 2024. https://doi.org/10.1007/s12640-023-00683-y
> Companion dataset: https://github.com/Vazquez-Borsetti/rat-and-human-comparative-development

The modeling framework (quarter-power model with an additive constant) used to translate
developmental time across species, applied to this dataset, is described in a companion
modeling paper (manuscript in preparation), with code and results available at:
https://github.com/Vazquez-Borsetti/quarter-power-C-human-rodent-translation

The full codebase and version history of this dataset are maintained at:
https://github.com/Vazquez-Borsetti/mouse-rat-human-development

## License

This dataset is released under the **Creative Commons Attribution-NonCommercial-ShareAlike
4.0 International License (CC BY-NC-SA 4.0)**. See `LICENSE` in this folder for the full
terms.

## Acknowledgments

This work builds upon developmental data generated and published by numerous researchers and
research groups. We acknowledge all original authors whose studies contributed observations to
this dataset. All developmental observations were traced back to their original empirical
sources whenever possible.

## Contact

For questions, corrections, or contributions, please contact the corresponding author
(Pablo Vazquez-Borsetti, IBCN, Universidad de Buenos Aires / CONICET) or open an issue on the
GitHub repository linked above.
