from managed_deepagents import define_schedule

schedule = define_schedule(
    cron="0 8 * * 1-5",
    timezone="America/Los_Angeles",
    prompt=(
        "Review durable memory for reusable research rules. "
        "Summarize anything useful, then list open questions for today."
    ),
)
