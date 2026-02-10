from airflow.sdk import dag, task


@dag(dag_id="versioned_dag")
def versioned_dag():
    @task.python
    def first_task():
        print("first task")

    @task.python
    def second_task():
        print("second task")

    @task.python
    def third_task():
        print("third task")

    @task.python
    def version():
        print("New task for versioning.")

    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    version = version()

    first >> second >> third >> version


# Instantiating the DAG
versioned_dag()
