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
Data Engineers

Schedule with Cron Expression
Schedule Interval: (1) datetime.timedelta and (2) Cron Expession

Cron Expression - is a string comprising five fields separated by whitespace that represents a set of times, normally as a schedule to execute some routine.
e.g.    15 14 1 * *
        min hr day(month) month day(week)

Cron Expression Preset
Preset      Meaning                                                             Cron
None        Don't schedule, use for exclusively externally triggered DAGs
@once       Schedule once and once only works                               
@hourly     Run once an hour at the beginning of the hour                       0 * * * *
@daily      Run once day at midnight                                            0 0 * * *
@weekly     Run once a week at midnight on Sunday morning                       0 0 * * 0
@monthly    Run once a month at midnight of the first day of the month          0 0 1 * *
@yearly     Run once a year at midnight of January 1                            0 0 1 1 *
##### NOTE: You can use crontab guru for interpretation


Aiflow Connection (Host, User, Password, etc.)
1. Database Servers (MySQL, PostgreSQL, ...)
2. Cloud Servers (AWS, Azure, ...)
3. Other


Two Ways To Install Python Independencies To Your Airflow Docker Container
1. Image Extending
2. Image Customizing

Property                                                Extending       CustomizingCan be built without airflow resources                  Yes             No
Uses familiar 'FROM' pattern of image building          Yes             No
Requires only basic knowledge about images              Yes             No
Builds quickly                                          Yes             No
Produces image heavily optimized for size               No              Yes
Can build from custom airflow sources (forks)           No              Yes
Can build on air-gaped system                           No              Yes


For Dependencies:
- every change in dependency, docker must be rebuild: 
        > docker build . --tag extending_airflow:latest
        > docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler