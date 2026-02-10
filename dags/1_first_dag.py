from airflow.sdk import dag, task


@dag(dag_id="first_dag")
# no need to explicitly mention dag id as the name of the function becomes dag_id
def first_dag():

    @task.python
    def first_task():
        print("first task")

    @task.python
    def second_task():
        print("second task")

    @task.python
    def third_task():
        print("third task")

    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third


# Instantiating the DAG
first_dag()
