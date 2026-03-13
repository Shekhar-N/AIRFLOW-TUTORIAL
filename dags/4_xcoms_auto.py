from airflow.sdk import dag, task


@dag
# no need to explicitly mention dag id as the name of the function becomes dag_id
def xcoms_dag_auto():

    @task.python
    def first_task():
        print("Extracting data")
        extracted_data = {"data": [1, 2, 3, 4, 5]}
        return extracted_data

    @task.python
    def second_task(data: dict):
        print("Transforming data")
        transf_data = data["data"] * 2
        transf_data_dict = {"transf_data": transf_data}
        return transf_data_dict

    @task.python
    def third_task(data: dict):
        print("Transformed data : ")
        print(data["transf_data"])

    # Defining task dependencies
    first = first_task()
    second = second_task(first)
    third = third_task(second)

    # first >> second >> third


# Instantiating the DAG
xcoms_dag_auto()
