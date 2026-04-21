<h1 align="center">
  <br>
  <a href="https://www.bu.edu/spark/" target="_blank"><img src="https://www.bu.edu/spark/files/2023/08/logo.png" alt="BUSpark" width="200"></a>
  <br>
  Center for Career Development: Employer Engagement Analysis
  <br>
</h1>

<h4 align="center">Analyzing five years of BU Handshake data (Spring 2020 – Summer 2025) to understand employer engagement, student activity, and hiring outcomes for the BU Center for Career Development.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#project-description">Project Description</a> •
  <a href="#handoff-notes-for-the-next-team">Handoff Notes</a> •
  <a href="#methodology">Methodology</a> •
  <a href="#data-locations">Data Locations</a>
</p>

## Key Features

The analysis pipeline is organized as a series of Jupyter notebooks. Each notebook builds on the outputs of the previous one.

* **`milestone_1_clean&join_v2.ipynb`** — data cleaning and joining
  - Cleans and standardizes the Employer, Event, and Job datasets from Handshake
  - Defines the schema and produces a joined dataset keyed on `employer_id`
* **`milestone_1_cleaned_EDA_v3.ipynb`** — additional cleaning and exploratory data analysis
  - Creates derived fields (year columns, engagement buckets), documents data gaps, and establishes proxy measures for Phase 1 analysis
* **`ms2_employer_analysis_v2.ipynb` / `ms2_employer_analysis_v3.ipynb`** — Phase 1 employer engagement analysis
  - Computes core KPIs (JAY, Event Score, consistency), extended KPIs (EAY, EEB, EEC, ACI, SSI, EEIS), employer segmentation, and event/time trend analysis
  - Produces `employer_kpi.csv`, the master employer-level metrics table used downstream
* **`ms3_outcome_analysis_v1.ipynb`** — Phase 2 hiring outcomes analysis
  - Integrates FDS post-graduation outcomes with Handshake employer engagement
  - Bridges engagement rank (EEIS) with hiring rank (FDS) to classify employers as *Targeting Opportunities*, *Strong Converters*, or *Balanced*
  - Produces `ep_outcomes.csv`, the joint employer + outcomes dataset

See the [Methodology](#methodology) section for detailed per-notebook documentation.

## How To Use

To clone and run this application, you'll need <a href="https://git-scm.com" target="_blank">Git</a>. From your command line:

```bash
# Clone this repository
$ git clone [repo link]
```

**Run the notebooks in milestone order — always.** Each milestone consumes the previous milestone's CSV output:

```
milestone_1_clean&join_v2.ipynb   →  ep_joined.csv, ep_base_cleaned.csv
milestone_1_cleaned_EDA_v3.ipynb  →  (EDA, data-gap documentation — no new CSVs)
ms2_employer_analysis_v3.ipynb    →  employer_kpi.csv        (use v3, not v2)
ms3_outcome_analysis_v1.ipynb     →  ep_outcomes.csv
```

Create a new branch from `dev`, add changes on the new branch you just created. You will want to look into <a href="https://git-scm.com/docs/git-branch" target="_blank">git branch</a> and <a href="https://git-scm.com/docs/git-checkout" target="_blank">git checkout</a>.

```bash
# Create and Checkout a new branch if it doesn't exist
$ git checkout -b your-branch main
...
```

## Project Description

**Client:** Boston University Center for Career Development (CCD)

The BU Center for Career Development serves as the university's central resource for career education, employer engagement, and post-graduate outcomes for undergraduate and graduate students across all BU schools and colleges. The CCD supports students through career advising, skill-building resources, employer partnerships, and recruiting activities such as job and internship postings, career fairs, and employer-hosted events. A core component of the CCD's work is the use of Handshake as the primary platform for connecting students with employers and tracking engagement, applications, and hiring outcomes.

The **Employer Engagement Analysis Project** aims to help the CCD better understand how employers interact with BU students and offices through the university's career ecosystem. Using data collected from Handshake between Spring 2020 and Summer 2025, this project analyzes five years of employer activity — including job postings, event participation, and student applications — to identify patterns in engagement and hiring behavior. By integrating datasets that include employer information, event records, job posting data, and student participation, the team explores which employers are most active, which engagement activities generate the highest student interest, and which factors are most predictive of successful hiring outcomes.

### Research Questions

**Phase 1 — Engagement (Main Questions)**

* Who are the employers that BU has strong relationships with and should continue to engage with?
* Who are the employers that BU does not have strong relationships with, but should seek to build relationships with?

**Phase 1 — Engagement (Sub-Questions)**

* How many employers use Handshake?
* What events are the most common? Least common? What are the trends in employer event behavior?
* What types of jobs are the most common? Least common? What are the trends in jobs being posted on Handshake?
* What types of employers, events, and jobs garner the most student interest? Who are these students? Why might this be the case?
* How are students engaging with employers on Handshake? Who are the students using Handshake the most? Why might this be the case?
* What are the limitations of our data? (e.g., some students engage in employer activities outside of what we can measure.)
* Benchmarking and research: How do other colleges measure and track employer engagement? What metrics does NACE look at that should inform our employer engagement strategy?

**Phase 2 — FDS Outcomes Analysis (Main Question)**

* Over the last five years, how has a student's academic history and career development engagement (appointments, technology usage, employer event attendance, etc.) affected their settled rates (employment / graduate school)?

**Phase 2 — FDS Outcomes Analysis (Sub-Questions)**

* What types of employer engagement activities are most likely to result in a student being settled post-graduation?
* What factors most predict a student's settled rate?

### Project Milestones

1. **Data Cleaning** — Review and clean the Employer, Job, and Event datasets sourced from Handshake; define relationships between datasets and create a clear data schema with accompanying documentation.
2. **Phase 1 Analysis (Engagement)** — Explore employer engagement trends using the cleaned datasets, including employer activity on Handshake, job posting frequency, event participation, and student engagement.
3. **Phase 2 Analysis (Hiring Outcomes)** — Analyze how employer engagement correlates with hiring outcomes and student settled rates by integrating job application data, employer activity metrics, and available student engagement indicators.
4. **Dashboard Development** — Build an interactive dashboard using Python and Power BI that allows CCD staff to explore employer engagement, student participation, job postings, through drill-down views.
5. **Final Presentation** — Finalize and present the slide deck and interactive dashboard to the CCD Leadership Team, summarizing key findings, visualizations, data limitations, and strategic recommendations.

### Tech Stack

* **Python** — data cleaning, exploratory analysis, and modeling (`pandas`, `numpy`, `matplotlib`, `seaborn`)
* **Power BI** — interactive dashboard (Windows only via BU access)

## Handoff Notes for the Next Team

### What the Repo Consists Of

The repo is **notebook-first**: there is no packaged library, CLI, or pipeline runner. Each milestone is a standalone Jupyter notebook that reads CSVs and writes CSVs. See [Repo Structure](#repo-structure) above for the file map and [Key Outputs](#key-outputs) for the data flow.

### Next Tasks (For Future Teams)

Two concrete, high-priority handoff items:

1. **Load KPI data into Power BI.** The `.pbix` file is mostly done, but the next team should verify that `employer_kpi.csv` is loaded as the primary data source (and that any stale snapshots of it are replaced with the latest version produced by `ms2_employer_analysis_v3.ipynb`). If new KPIs are added in future analysis, update the Power BI data model to pull them in and extend the drill-down views accordingly.
2. **Clean and integrate the hiring outcome dataset.** The FDS outcomes data is cleaned and joined in `ms3_outcome_analysis_v1.ipynb`, but it isn't yet integrated into the Power BI dashboard. The next team should (a) review the cleaning in that notebook, (b) productionize `ep_outcomes.csv` as a second data source in Power BI alongside `employer_kpi.csv`, and (c) build dashboard views that expose the Engagement-to-Hiring Bridge (EEIS rank vs. hire rank, Targeting Opportunity / Strong Converter labels, per-employer hiring deep dives) so CCD staff can drill into it interactively.

Beyond those two, longer-running follow-ups that come out of our documented data gaps: resolving the salary unit ambiguity, strengthening the Handshake ↔ FDS employer name matching (currently substring-based), and adding a structured industry/job-type classification to the raw data.

### Things to Watch Out For

* **Don't use the raw joined dataset for counting.** `ep_joined.csv` is the full `employer × event × job` cross-product, so any `count()` over it double-counts. Always deduplicate on `events_id` / `jobs_id` before aggregating — this is why Milestone 2 section 9.1 recomputes event counts with `.nunique()`.
* **Treat salary fields as exploratory.** Units are inconsistent (hourly vs. annual vs. stipend), there are many zeros and placeholder `999999` values. SSI is included in the KPI table but should not be used as a primary ranking metric.
* **`ms2_employer_analysis_v3.ipynb` supersedes `v2`.** `v2` is kept in the repo for history; `v3` is the current version.
* **2025 data is a partial year.** Be careful with year-over-year trends that compare 2025 to full prior years.

## Methodology

### Milestone 1 — Data Cleaning & Joining

#### Data Cleaning

**General dataset cleaning**

* Load data with pandas
* Standardize column names
* Match the primary key / column name across datasets
* Lowercase all values in the datasets
* Drop fully empty rows

**Employer base cleaning**

* Drop duplicates
* Drop meaningless columns (e.g., `count` that is always 1)
* Rename to `employer_type`
* Split `employer_size` into min and max columns
* Reformat dates

**Employer event cleaning**

* Drop duplicates
* Convert student count to numeric type
* Rename date and medium columns
* Reformat dates

**Employer job cleaning**

* Drop duplicates
* Rename date, min, and max salary columns
* Convert salary from string to float
* Reformat dates

**Data gaps identified during cleaning**

* Many NaN values in min and max salary fields
* Student attendee count seems unusually low for some events
* Application count seems unusually low for some jobs
* Salary units appear inconsistent — some values (e.g., 50) suggest a different unit (hourly vs. annual vs. stipend)

**Joined dataset schema (subject to change)**

* Shared primary key across all three datasets: `employer_id`
* Final dataset = `employer × event × job`
* One-to-many relationship — an `employer_id` with many `events_id` and many `jobs_id` expands into multiple rows
* Every employer appears at least once
* Left joins preserve all employers, even those with zero events and zero jobs

1. Left join `ep_event` onto `ep_base`
   * If an employer has 3 events, that employer's row is duplicated 3 times
   * If an employer has 0 events, the event columns become NaN
2. Left join `ep_job` onto `ep_base_event`
   * If an employer has 5 jobs, each employer-event row is duplicated 5 times

#### Additional Cleaning & Prep

* Create year fields from date columns
* Convert `applications_count` and `student_attendees_count` to numeric
* Fill missing engagement metrics with 0 for aggregation
* Create application and attendance buckets for distribution analysis
* Verify employer-level aggregation before joins to prevent double counting

#### EDA

**Salary field notes**

* Salary units unclear (hourly vs. annual vs. stipend)
* Large number of 0 values (unpaid or missing)
* Extreme max values (999999) suggest placeholder entries
* Salary not used in Phase 1 trend analysis

**Additional data gaps identified**

* No hiring outcome variable
* No student-level identifiers or demographics
* No structured job type or industry classification
* No distinction between event registration and actual attendance
* 2025 data is a partial year

**Proxy measures used**

* Job postings as a proxy for employer activity
* `applications_count` as a proxy for student demand
* Event attendance as a proxy for engagement depth
* Multi-year activity as a proxy for sustained relationship

**Schema / join clarification**

* Aggregate jobs and events separately at the employer level
* Left joins preserve the full employer base
* Avoid raw `employer × event × job` cross-product in analysis
* NaN values indicate no recorded activity

### Milestone 2 — Employer Activity & Job Performance Analysis

#### 1. Library Imports & Setup

* Imports required libraries: `os`, `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`
* Loads the cleaned dataset (`ep_joined.csv`) into a Pandas DataFrame
* Displays the first 5 rows to preview structure and validate load

#### 2. Finding Zero-Application Job Examples (August 2025)

* Converts `job_creation_date` to datetime format
* Filters for jobs that:
  - Have 0 applications
  - Are from large employers (250+ employees or missing size) — an adequate number of employers had size ≥ 250, and many well-known employers had missing size values
  - Were created in August 2025 (most recent month in the dataset)
  - Are not associated with events (to isolate job postings)
* Removes duplicate job IDs to avoid double-counting
* Displays a sample of 15 jobs with job ID, title, employer name, application count, and creation date

**Purpose:** identify large-employer job postings that failed to receive any applications during a specific month.

#### 3. Employer Activity Analysis

**3.1 Jobs Posted Per Month** — extract month from `job_creation_date`, group and count unique postings, visualize with a Seaborn bar chart to show seasonal/monthly trends.

**3.2 Applications Per Month** — group by month, sum total applications, display as a line chart with markers to compare against job volume trends.

#### 4. Job Application Yield (JAY)

**4.1 Aggregation & Calculation** — group by employer to compute total unique jobs posted and total applications received; store in `employer_inf`. Calculate `JAY = Total Applications / Total Jobs`.

**4.2 JAY Insights** — top 10 and bottom 10 employers by JAY, summary statistics, and a scatter plot of total jobs vs. total applications.

**Purpose:** measure how effectively employers convert job postings into student applications.

#### 5. Event Participation Analysis

**5.1 Event & Attendance Aggregation** — filter invalid/empty event records; count total events per employer and sum total attendees; add to `employer_inf`; fill missing values with 0.

**5.2 Event Score Calculation** — `Event Score = Total Events + Total Attendees`; summary statistics; top/bottom 10 employers by event score; scatter plot of Event Score vs. JAY.

#### 6. Employer Consistency Analysis

**6.1 Active Years Calculation** — convert `job_creation_date` and `event_date` to datetime; calculate min/max active year per employer (jobs and events); compute active duration in years.

**6.2 Consistency Metrics**

* `consistency_jobs = active job years / total years`
* `consistency_events = active event years / total years`
* Histogram of job consistency distribution; top 10 most and least consistent employers.

#### 7. Consistency vs. Performance

Scatter plot comparing job consistency against JAY to evaluate whether long-term platform consistency leads to better job performance.

#### 8. Correlation Analysis

Computes correlation matrix over: Total Jobs, Total Applications, JAY, Total Events, Total Attendees, Event Score. Visualized with a Seaborn heatmap.

#### 9. KPI Engineering Extension & Advanced Metrics

Adds advanced engagement and performance KPIs:

* Event Attendance Yield (EAY) with deduplication
* Employer Engagement Breadth (EEB)
* Employer Engagement Consistency (EEC – unified)
* Application Concentration Index (ACI)
* Salary Signaling Index (SSI)
* Employer Engagement Intensity Score (EEIS)
* Employer type enrichment and segmentation

**9.1 Event Attendance Yield (EAY)** — `EAY = Total Student Attendees / Total Events Hosted`. Recomputes event counts using `events_id.nunique()` per employer to avoid duplication caused by the joined dataset structure. Filters valid event records, removes duplicate employer-event pairs, aggregates unique events and attendees, computes EAY, merges into `employer_inf`.

**9.2 Employer Engagement Breadth (EEB)** — `EEB = 1(Job Posting Activity) + 1(Event Hosting Activity)`.

* EEB = 2 → uses both jobs and events
* EEB = 1 → uses only one channel
* EEB = 0 → no activity

**9.3 Employer Engagement Consistency (EEC) – Unified** — `EEC = Active Years (Jobs OR Events) / Years Since First Activity`. Combines job and event activity into a single timeline, deduplicates employer-year combinations, computes active years, first/last year, total span, and EEC ratio.

**9.4 Application Concentration Index (ACI)** — `ACI = Max Applications on a Single Job / Total Applications`.

* ACI = 1.0 → all applications concentrated in one job
* Lower ACI → applications distributed across multiple postings

**9.5 Salary Signaling Index (SSI)** — `SSI = Average Salary Midpoint × JAY`, where salary midpoint = `(min_salary + max_salary) / 2`. Treated as exploratory due to known salary data quality limitations.

**9.6 Employer Engagement Intensity Score (EEIS)** — `EEIS = 0.25(Jobs) + 0.25(Events) + 0.25(Applications) + 0.25(Attendees)`. All components are min-max scaled to [0,1] before weighting.

* EEIS = 1.0 → most engaged employer across all channels
* EEIS = 0.0 → no engagement

#### 10. Employer Type Enrichment

* Loads `ep_base_cleaned.csv`
* Extracts `employer_type`, `employer_size_min`, `employer_size_max`
* Computes `employer_size_mid`
* Removes duplicate columns (for re-runs)
* Merges attributes into `employer_inf`
* Filters to active employers; aggregates average EEIS by employer type; filters to types with ≥5 employers; displays top 15 types by average EEIS

**10.1 Employer Type Insights** — minimum count threshold prevents skew from small samples; average EEIS reflects relative engagement intensity within sector; highlights differences across industries (e.g., high-engagement sectors like finance, consulting, and tech vs. large but lower-engagement sectors like government).

#### 11. Employer Segmentation: EEB × EEC

Segments employers using breadth (EEB) and consistency (EEC):

* **Core Partners** — high breadth, high consistency
* **Sporadic Multi-Channel** — high breadth, low consistency
* **Loyal Single-Channel** — low breadth, high consistency
* **Peripheral** — low engagement

Applies EEC threshold of 0.8. Produces bar charts of employer count by segment, average EEIS by segment, top 10 Core Partners by EEIS, and a summary table (count, avg EEIS, avg EEC, avg jobs).

#### 12. Full Employer KPI Summary Table

Consolidated KPI dataset covering:

* Job metrics (jobs, applications, JAY)
* Event metrics (events, attendees, EAY)
* Engagement metrics (EEB, EEC, EEIS)
* Distribution metrics (ACI)
* Compensation metrics (SSI)

Sorted by EEIS descending.

#### 13. Event Type Analysis

Categorizes events via keyword matching into standardized types: Career Fair, Info Session, Networking, Workshop/Webinar, Recruiting/Interview, Panel/Speaker, Open House/Coffee Chat, Other. Cleans event names (lowercase, strip), applies categorization, aggregates event count and total/average attendees, visualizes frequency and average attendance.

#### 14. Engagement Trends Over Time

**Jobs & Applications** — deduplicates jobs, extracts year, aggregates unique jobs, total applications, and active employers.

**Events** — deduplicates events, extracts year, aggregates unique events and total attendees.

Visualizations: jobs per year, applications per year, events per year, and active employers per year.

#### 15. Student Engagement Analysis

**15.1 Attendance per Event** — filters valid events, removes duplicates, log-scale histogram, displays mean/median/75th/95th percentiles.

**15.2 Applications per Job** — deduplicates jobs, filters non-zero applications, log-scale histogram, distribution statistics.

**15.3 Event Medium Analysis** — groups by `event_medium` (e.g., virtual, in-person); computes average attendees and event count; visualizes average attendance by medium.

### Milestone 3 — Student Outcome Analysis

#### 1. Library Imports & Setup

Initializes the analysis environment and loads the primary datasets:

* `FDS 2020–2024 Employer Outcomes (Anonymized).xlsx` — detailed student post-graduation outcomes (employment, demographics, industries, etc.)
* `employer_kpi.csv` — employer engagement and performance metrics from Milestone 2

Key steps: import libraries (`os`, `pandas`, `numpy`, `matplotlib.pyplot`, `matplotlib.ticker`, `seaborn`); set visualization defaults (Seaborn whitegrid, consistent DPI); load datasets; extract and clean key fields (graduation year from text, gender normalization, domestic/international status standardization); print dataset summaries.

#### 2. Data Cleaning & Standardization

**2.1 Graduation Year Extraction** — regex-extract 4-digit year from `Graduation Date`, convert to `Int64`.

**2.2 Demographic Normalization**

* Gender: Female → Woman, Male → Man
* International status: Y → International, ? → Unknown

**2.3 Employer KPI Integration** — loads `employer_kpi.csv`, confirms structure for cross-dataset comparison.

#### 3. Top Hiring Employers

Excludes Boston University, unknown employers, and self-employed entries. Computes top 20 employers by hire count; visualizes with horizontal bar chart with annotations.

#### 4. Industry & Job Function Analysis

**4.1 Industry Distribution** — top 15 industries by total hires (overall) and line-chart trends for top 8 industries across graduation years.

**4.2 Job Function Analysis** — top 15 job functions across all graduates (horizontal bar chart).

#### 5. Academic Background Analysis

**5.1 Outcomes by College** — aggregates outcomes by `Graduation Degree College_1` (bar chart).

**5.2 Major → Industry Mapping** — pivot table over top 10 majors × top 8 industries, visualized as a heatmap.

#### 6. Demographic Insights

* **6.1 Gender Distribution** — pie chart of gender proportions
* **6.2 Race/Ethnicity Distribution** — horizontal bar chart of IPEDS race/ethnicity categories
* **6.3 Domestic vs. International** — bar chart comparing domestic and international graduate outcomes
* **6.4 Industry by Gender** — gender breakdown within top 5 industries

#### 7. Geographic Outcomes

**7.1 U.S. Placement** — top 15 U.S. states by graduate outcomes (annotated bar chart).

**7.2 International Placement** — top 15 countries excluding U.S.

**7.3 Retention Metrics** — % of graduates staying in the U.S.; count of graduates working abroad.

#### 8. Year-over-Year Employment Trends

* **8.1 Total Outcomes by Year** — overall employment volume
* **8.2 Employment Type Trends** — full-time vs. part-time breakdown by year
* **8.3 Employment Category Trends** — organization, contract, freelancer, entrepreneur
* **8.4 Job Function Trends** — top 5 job functions tracked over time

#### 9. Employer Engagement vs. Hiring Outcomes (Bridge Analysis)

Connects Handshake engagement (EEIS) with actual hiring outcomes (FDS).

**9.1 Employer Matching & Normalization** — selects top 20 employers by EEIS rank; cleans employer names for fuzzy matching (lowercasing, removing suffixes like `Inc`, `LLC`); matches employers to FDS hiring data via substring search. Bridges two datasets that lack a direct key.

**9.2 Ranking Comparison**

For each employer, computes:

* EEIS Rank (engagement strength)
* FDS Hire Count
* FDS Hire Rank

Derived metric: `Rank Gap = Hire Rank − EEIS Rank`.

* Positive → hires more than expected
* Negative → underperforms relative to engagement

**9.3 Employer Classification**

* **Targeting Opportunity** — high engagement but low hiring conversion
* **Strong Converter** — high hiring relative to engagement
* **Balanced** — alignment between engagement and hiring

**9.4 Visual Analysis** — scatter plot of EEIS Rank vs. FDS Hires (color-coded by category); side-by-side bar comparison of engagement rank and hiring rank.

**9.5 Strategic Insights** — outputs two key employer groups (Targeting Opportunities and Strong Converters); includes job function breakdown for the top converting employer. Translates analysis into actionable recruiting strategy.

#### 10. Employer-Level Outcome Profiles

**10.1 Top Employer Deep Dive** — for the top 5 employers by FDS hires, shows job function distribution (horizontal bar chart of top roles) and yearly hiring trend.

### Joint Employer & Outcome Data Analysis

#### 1. Library Imports & Setup

Imports `os`, `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`. Loads:

* `ep_joined.csv` — job postings, employer engagement, and event activity
* `outcomes.csv` — student post-graduation outcomes

#### 2. Preparing and Merging Datasets (Creating `ep_outcomes.csv`)

**2.1 Cleaning Employer Name Fields** — lowercase, strip whitespace, store cleaned versions in `employer_name_clean` to prevent mismatches from capitalization or spacing.

**2.2 Avoiding Double Counting** — aggregate outcomes to the employer level; count total outcomes reported, full-time hires, and organizational hires; merge this aggregated table onto `ep_joined` using the cleaned employer name.

**2.3 Saving the Combined Dataset** — merged dataset saved as `ep_outcomes.csv`.

#### 3. Employer Activity & Engagement Metrics

**3.1 Aggregated Employer Metrics** — per employer: `total_jobs`, `total_applications`, `total_events`, `total_attendees`, `num_outcomes`, `num_fulltime_hires`.

**3.2 Engineered Variables**

* `JAY = Total Applications / Total Jobs`
* Event Score — combines event count and student attendance
* `Hiring Yield = Total Outcomes / Total Jobs`

#### 4. Visualizations & Insights

**4.1 Event Score vs. Student Hiring Outcomes** — scatter plot (Event Score vs. Total Student Outcomes) to evaluate whether event engagement correlates with hiring.

**4.2 JAY vs. Hiring Yield** — scatter plot to determine whether strong application performance translates into actual hiring.

**4.3 Applications vs. Outcomes** — scatter plot to assess whether employers receiving more applications ultimately hire more students.

**4.4 Correlation Heatmap** — correlations among job posting volume, application volume, event activity, student outcomes, hiring yield, event score, and full-time hires. Reveals which employer behaviors are most strongly associated with student hiring success.

## Data Locations

The project uses three main datasets sourced from BU Handshake data between Spring 2020 and Summer 2025, plus the BU First Destination Survey (FDS) data for Milestone 3.

<a href="dataset-documentation">Dataset Documentation</a>

**Raw inputs**

* **Employer base** — [link](https://drive.google.com/file/d/1cMYPqEBhehpngt3jGi3NjSvoUf-2eNmB/view?usp=drive_link)
  - Master list of organizations and employer attributes; cleaned to `ep_base_cleaned.csv`.
* **Employer events** — [link](https://drive.google.com/file/d/1deIBV-F40g3MKjLvFJfbjb9j67GBQHa_/view?usp=drive_link)
  - Career events and student attendance records.
* **Employer jobs** — [link](https://drive.google.com/file/d/1MwtrH_E3BTs_-3ZYJR96oiR0OVfnLwGD/view?usp=drive_link)
  - Job postings and application counts.
* **FDS 2020–2024 Employer Outcomes (Anonymized).xlsx** — [link](https://docs.google.com/spreadsheets/d/1d7kVvOUcr7ts809rlSvwCnJagX28I9jT/edit?usp=drive_link&ouid=115187330912941517955&rtpof=true&sd=true)
  - Student post-graduation outcomes: employment, demographics, industries, job functions.

**Intermediate / derived outputs**

* **`ep_joined.csv`** — [link](https://drive.google.com/file/d/1V7vOYtU-0DNX9hdK-m_pPGBGO_tVwEey/view?usp=drive_link)
  - Milestone 1 output; joined employer × event × job dataset (left joins preserve full employer base).
* **`ep_event_cleaned.csv`** — [link](https://drive.google.com/file/d/1HJu1S2euo4HJPzd8sCGlxKacwbcacO9K/view?usp=sharing)
  - Milestone 1 output; cleaned employer event data (deduplicated, attendee count numeric, dates reformatted).
* **`ep_job_cleaned.csv`** — [link](https://drive.google.com/file/d/1O5CPqhezYzIYzuRg6MrAWuUB5j78O-IF/view?usp=sharing)
  - Milestone 1 output; cleaned employer job posting data (deduplicated, salary converted to float, dates reformatted).
* **`ep_base_cleaned.csv`** — [link](https://drive.google.com/file/d/1ehgIkF8SAIuLZpWuEWGInh4NFemXAZT2/view?usp=sharing)
  - Milestone 1 output; cleaned employer base (deduplicated, `employer_size` split into min/max, dates reformatted, employer type renamed).
