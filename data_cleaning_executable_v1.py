import os
import pandas as pd
import numpy as np

# =========================
# Load data
# =========================
DATA_DIR = "."

EMPLOYER_BASE_FILE = "Employer Base Dataset (Spring 2020 - Summer 2025).csv"
EMPLOYER_EVENT_FILE = "Employer Event Dataset (Spring 2020 - Summer 2025).csv"
EMPLOYER_JOB_FILE  = "Employer Job Dataset (Spring 2020 - Summer 2025).csv"

ep_base  = pd.read_csv(os.path.join(DATA_DIR, EMPLOYER_BASE_FILE))
ep_event = pd.read_csv(os.path.join(DATA_DIR, EMPLOYER_EVENT_FILE))
ep_job   = pd.read_csv(os.path.join(DATA_DIR, EMPLOYER_JOB_FILE))

# =========================
# General cleaning
# =========================
def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

ep_base = clean_columns(ep_base)
ep_event = clean_columns(ep_event)
ep_job = clean_columns(ep_job)

ep_base = ep_base.rename(columns={"id": "employer_id"})
ep_event = ep_event.rename(columns={"employers_id": "employer_id"})

for df in (ep_base, ep_event, ep_job):
    if "employer_id" in df.columns:
        df["employer_id"] = df["employer_id"].astype(str).str.strip()

def lower_strings(df):
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda s: s.str.lower().str.strip())
    return df

ep_base = lower_strings(ep_base)
ep_event = lower_strings(ep_event)
ep_job = lower_strings(ep_job)

for name, df in [("base", ep_base), ("event", ep_event), ("job", ep_job)]:
    df.replace(r"^\s*$", np.nan, regex=True, inplace=True)

ep_base  = ep_base.dropna(how="all")
ep_event = ep_event.dropna(how="all")
ep_job   = ep_job.dropna(how="all")

# =========================
# Employer base cleaning
# =========================
ep_base = ep_base.drop_duplicates(subset="employer_id")

ep_base = ep_base.drop(columns=[c for c in ep_base.columns if c.startswith("unnamed")], errors="ignore")
ep_base = ep_base.drop(columns=["count"], errors="ignore")

ep_base = ep_base.rename(columns={
    "name.1": "employer_type",
    "name_1": "employer_type"
})

if "employer_size" in ep_base.columns:
    size_split = ep_base["employer_size"].astype(str).str.split(" - ", n=1, expand=True)
    ep_base["employer_size_min"] = pd.to_numeric(size_split[0], errors="coerce")
    ep_base["employer_size_max"] = pd.to_numeric(size_split[1] if size_split.shape[1] > 1 else np.nan, errors="coerce")
    ep_base = ep_base.drop(columns=["employer_size"])

date_col = None
for c in ["created_at_date", "created_at"]:
    if c in ep_base.columns:
        date_col = c
        break

if date_col:
    ep_base[date_col] = pd.to_datetime(ep_base[date_col], errors="coerce")
    ep_base = ep_base.rename(columns={date_col: "employer_creation_date"})

# =========================
# Employer event cleaning
# =========================
if "events_id" in ep_event.columns:
    ep_event = ep_event.drop_duplicates(subset="events_id")

if "student_attendees_count" in ep_event.columns:
    ep_event["student_attendees_count"] = pd.to_numeric(
        ep_event["student_attendees_count"],
        errors="coerce"
    )

ep_event = ep_event.rename(columns={
    "events_start_date_date": "event_date",
    "event_medium_name": "event_medium"
})

if "event_date" in ep_event.columns:
    ep_event["event_date"] = pd.to_datetime(ep_event["event_date"], errors="coerce")

# =========================
# Employer job cleaning
# =========================
if "jobs_id" in ep_job.columns:
    ep_job = ep_job.drop_duplicates(subset="jobs_id")

ep_job = ep_job.rename(columns={
    "jobs_created_at_date": "job_creation_date",
    "job_salaries_min_salary_in_dollars": "min_salary",
    "job_salaries_max_salary_in_dollars": "max_salary",
    "applications": "applications_count"
})

if "job_creation_date" in ep_job.columns:
    ep_job["job_creation_date"] = pd.to_datetime(ep_job["job_creation_date"], errors="coerce")

for col in ["min_salary", "max_salary", "applications_count"]:
    if col in ep_job.columns:
        ep_job[col] = pd.to_numeric(ep_job[col], errors="coerce")

# =========================
# Save cleaned base, event, job datasets
# =========================
ep_base.to_csv("ep_base_cleaned.csv", index=False)
ep_event.to_csv("ep_event_cleaned.csv", index=False)
ep_job.to_csv("ep_job_cleaned.csv", index=False)

# =========================
# Joining datasets
# =========================
ep_base_event = ep_base.merge(
    ep_event,
    on="employer_id",
    how="left",
    suffixes=("", "_event")
)

ep_full = ep_base_event.merge(
    ep_job,
    on="employer_id",
    how="left",
    suffixes=("", "_job")
)

ep_full = ep_full.drop_duplicates()

# =========================
# Save joined dataset
# =========================
ep_full.to_csv("ep_joined.csv", index=False)
