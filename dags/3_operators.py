from airflow.sdk import dag, task


@dag
def operators_dag():

    @task.python
    def first_task():
        print("first task")

    @task.python
    def second_task():
        print("second task")

    @task.python
    def third_task():
        print("third task")

    @task.bash
    def bash_task():
        return "echo 'Inside bash'"

    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    bash_task = bash_task()

    first >> second >> third >> bash_task


# Instantiating the DAG
operators_dag()
