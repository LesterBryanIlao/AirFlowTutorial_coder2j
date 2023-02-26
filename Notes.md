What is Airflow?
- starts in 2014
- manage complex workflows
- top-level Apache project (2019)
- Workflow management platform
- wirtten in Python

Workflow?
- sequence of tasks
- defined as DAG (Directed Acyclic in Graph) in Airflow

Task 
- unit of work within a DAG
- a node in the DAG graph written in python
- the goal is to achieve a specific thing
- uses a method called "Operator"

Operator
- determines what is going to be done

Execution Date - the logical state and time which the DAG Run, and its task instances, are running for.

Task Life Cycle
- 11 different kinds of stages:
> no_status         > success               > up_for_retry
> scheduled         > upstream_failed       > failed
> queued            > up_for_reschedule     > shutdown
> running           > skipped

no_status: scheduler created empty task instance
scheduled: scheduler determined task instance needs to run
removed: task is removed
upstream_failed: the task's upstream task failed
skipped: task is skipped

queued: scheduler sent task to executor to run on the queue

running: 
success, failed, and shutdown > up_for_retry

SUMMARY: 
no_status >> scheduledr > scheduled >> executor > queued >> worker > running > success

Basic Architecture
Data Engineer