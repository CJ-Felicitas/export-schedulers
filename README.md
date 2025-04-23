# export-schedulers

A simple Python script that exports all AWS EventBridge Schedulers and saves them as individual JSON files.


- Exports all schedulers in the specified AWS region
- Saves each scheduler's full JSON details to the `schedulers/` folder
- Supports pagination to fetch all results
- Works on Linux and Windows

---

## Requirements

- Python 3.10 or higher
- AWS access key with permissions for `scheduler:ListSchedules` and `scheduler:GetSchedule`

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/export-schedulers.git
cd export-schedulers
```

### 2. Set up a virtual environment

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```cmd
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set up environment variables

Create a `.env` file in the project root with the following content:

```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_DEFAULT_REGION=ap-southeast-1
```

Make sure the credentials have permission to access the AWS EventBridge Scheduler service.

---

### 5. Run the script

```bash
python export.py
```

This will:
- Fetch all schedulers
- Save them to the `schedulers/` folder
- Display a total count and confirmation message

---

## Output

Each scheduler will be saved as a separate `.json` file inside the `schedulers/` directory using the scheduler's name as the filename.

---

## Example Output

```bash
Exporting: daily-job-processor
Exporting: weekly-report-job

TOTAL NUMBER OF SCHEDULERS FOUND: 2
EXPORT COMPLETE
```

---

