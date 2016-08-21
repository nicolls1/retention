#!/usr/bin/env python
import bisect
import pandas
import re
import sys
import time

MAX_STREAK = 14

def load_data(file_path):
    #start = time.time()
    with open(file_path, 'r') as f:
        data = pandas.read_csv(f, header=None, skiprows=None).values
    times = data[:,0]
    ids = data[:,1]
    #print 'read time:', time.time()-start
    return times, ids

def add_new_day():
    return [0]*MAX_STREAK

def add_ended_streaks(active_streaks, ended_keys, day_counts):
    for key in ended_keys:
        day_counts[-active_streaks[key]][active_streaks[key]-1] += 1
    return day_counts

def find_retention(file_path):
    times, ids = load_data(file_path)

    # convert dates into seconds so we can divide the data into chunks 
    day_cutoffs = [int(time.mktime(time.strptime(str(i)+" Jan 16", "%d %b %y")))-time.timezone for i in range(1, 16)]
    # find the indexes of the day cutoffs 
    index_cutoff = [bisect.bisect_left(times, day) for day in day_cutoffs]

    # list of sets where each set is the ids of the users for that day 
    daily_users = [set(ids[i:j]) for i, j in zip(index_cutoff[:-1], index_cutoff[1:])]

    # day_counts will track the number of streaks for each day. 
    # We will add a new day everyday
    day_counts = []
    day_counts.append(add_new_day())
    # all users at the end of the first day have a one day streak
    active_streaks = {id:1 for id in daily_users[0]}

    for today in daily_users[1:]:
        # all user ids that have a streak going
        retention_keys = set(active_streaks.keys())

        # Find streaks that ended today and for each key look up how long the streak
        # has been going on for. Then add one to the streak length in the day that it started.
        day_counts = add_ended_streaks(active_streaks, retention_keys - today, day_counts)

        day_counts.append(add_new_day())
        # returning users should have their count incremented
        active_streaks = {id:active_streaks[id]+1 for id in retention_keys & today}
        # new users should have a streak set to one
        active_streaks.update({id: 1 for id in today - retention_keys})

    # any active streaks at the end need to get added to the output
    add_ended_streaks(active_streaks, set(active_streaks.keys()), day_counts)
        
    # write output
    for i, day in enumerate(day_counts):
        print ','.join([str(i+1)]+[str(d) for d in day])

if __name__ == '__main__':
    #start = time.time()
    find_retention(sys.argv[1])
    #print 'duration:', time.time()-start
