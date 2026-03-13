from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.trigger import CronTriggerTimetable


@dag(
    dag_id="multi_dags",
    start_date=datetime(year=2026, month=2, day=18, tz="IST"),
    schedule=CronTriggerTimetable("0 0 * * *", timezone="IST"),
    end_date=datetime(year=2026, month=2, day=19, tz="IST"),
    is_paused_upon_creation=True,
    catchup=True,
)
def multi_dags():

    @task.python
    def start():
        print("Starting the DAG")

    @task.python
    def process():
        print("Processing the DAG")

    @task.python
    def end():
        print("Ending the DAG")

    start_task = start()
    process_task = process()
    end_task = end()

    # Defining the task dependencies
    start_task >> process_task >> end_task


# Instantiating the DAG
multi_dags()
