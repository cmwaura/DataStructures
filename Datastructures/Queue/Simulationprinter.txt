

we are going to implement a printing simulation using a queue system. In this sim
printing will be processed with a first come first serve manner. The conditions are
on the average day we have 10 students on average working in the printer lab an hour.
In addition to this the printer is only capable of processing 10 pages per minute and
these students need to print between 1-20 pages. what is the page rate that needs to
be used? To solve this we use probabilities.

For a student to print between 1-20 pages means that it is equally possible for a student
to print any number of pages and hence we can use a random int for that. However, what is
the chance that at any given second a print task is going to be created? To consider this
we need to assume that on average twenty tasks per hr means there will be one task every
3 minutes

20 tasks/1hr X 1 hr/3600 sec= 1 task/180 sec

hence we can simulate the chance a printing will occur by generating a random number between
1-180 inclusive. If the number is 180, then the task has been created.


### Main Simulation Steps

here is the main sim:
1) create a queue of print takes  and give each incoming task a timestamp upon its
arrival. The queue is empty at the start.

2) For each second(currentSecond):
    - Does a new print task get created? if so, add it to the queue with the timestamp of
    currentSecond
    -If the printer is not busy and if a task is waiting:
        - Remove the next task from the print queue and assign it to the printer
        - subtract the timestamp from the currentSecond to compute the waiting time for the
        task
        - Append the waiting time for that task to a list for later processing
        - Based on the # of pages in the print tasks figure out how much time is required
    - The printer now does one second of priniting if nessecary and subtracts one second of time
       required for that task
    - If the task has been completed, then the printer will no longer be busy
3) After simulation is complete compute the avg waiting time from the list of waiting times
generated.
