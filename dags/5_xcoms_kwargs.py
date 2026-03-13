from airflow.sdk import dag, task


@dag
# no need to explicitly mention dag id as the name of the function becomes dag_id
def xcoms_dag_kwargs():

    @task.python
    def first_task(**kwargs):
        print("Extracting data")
        extracted_data = {"data": [1, 2, 3, 4, 5]}
        # Extracting 'ti' from kwargs to push XCOMS manually
        ti = kwargs["ti"]
        ti.xcom_push(key="result", value=extracted_data)

    @task.python
    def second_task(**kwargs):
        print("Transforming data")
        ti = kwargs["ti"]
        data = ti.xcom_pull(task_ids="first_task", key="result")
        transf_data = data["data"] * 2
        transf_data_dict = {"transf_data": transf_data}
        ti.xcom_push(key="result", value=transf_data_dict)

    @task.python
    def third_task(**kwargs):
        print("Transformed data : ")
        ti = kwargs["ti"]
        data = ti.xcom_pull(task_ids="second_task", key="result")
        print(data["transf_data"])

    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third


# Instantiating the DAG
xcoms_dag_kwargs()
