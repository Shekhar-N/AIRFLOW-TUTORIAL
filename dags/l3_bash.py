from airflow.sdk import dag, task
from pendulum import datetime


@dag(
    dag_id="bash_dag",
    start_date=datetime(year=2026, month=2, day=18, tz="UTC"),
    schedule="@daily",
    # schedule=CronTriggerTimetable("* * * * *", timezone="UTC"),
    end_date=datetime(year=2026, month=2, day=19, tz="UTC"),
    is_paused_upon_creation=False,
    catchup=True,
)
def bash_dag():
    @task.bash
    def print_date():
        return '''echo "Current date and time: $(date)"'''

    @task.bash
    def print_location():
        return '''echo "Current working directory: $(pwd)"'''

    @task.bash
    def list_files():
        return '''echo "Files in the current directory: $(ls)"'''

    print_date = print_date()
    print_location = print_location()
    list_files = list_files()

    print_date >> print_location >> list_files


# Instantiating the DAG
bash_dag()
