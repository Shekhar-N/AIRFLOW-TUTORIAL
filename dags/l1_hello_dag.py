from airflow.sdk import dag, task
from airflow.timetables.trigger import CronTriggerTimetable
from pendulum import datetime


@dag(
    dag_id="hello_dag",
    start_date=datetime(year=2026, month=2, day=18, tz="UTC"),
    # schedule="@daily",
    schedule=CronTriggerTimetable("0 0 * * *", timezone="UTC"),
    end_date=datetime(year=2026, month=2, day=19, tz="UTC"),
    is_paused_upon_creation=False,
    catchup=True,
)
def hello_dag():

    @task.python
    def print_hello():
        print("Hello, Airflow!")

    print_hello = print_hello()

    print_hello


# Instantiating the DAG
hello_dag()
