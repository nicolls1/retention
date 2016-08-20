#!/usr/bin/env python
import bisect
import sys
import time

def load_data(file_path):
    times = []
    ids = []
    start = time.time()
    with open(file_path, 'r') as f:
        for line in f:
            split_line = line.split(',')
            times.append(int(split_line[0]))
            ids.append(int(split_line[1]))
    print 'read time:', time.time()-start
    return times, ids

def count_retention(retention):
    counts = [0]*14
    for value in retention.values():
        counts[value-1] += 1
    return counts

def find_retention(file_path):
    times, ids = load_data(file_path)

    # convert dates into seconds so we can divide the data into chunks 
    day_cutoffs = [int(time.mktime(time.strptime(str(i)+" Jan 16", "%d %b %y")))-time.timezone for i in range(1, 16)]
    # find the indexes of the day cutoffs 
    index_cutoff = [bisect.bisect_left(times, day) for day in day_cutoffs]

    # list of sets where each set is the ids of the users for that day 
    daily_users = [set(ids[i:j]) for i, j in zip(index_cutoff[:-1], index_cutoff[1:])]

    day_counts = []
    # all users at the end of the first day have a one day streak
    retention_current = {id:1 for id in daily_users[0]}
    # add first day to the counts
    day_counts.append(count_retention(retention_current))

    for today in daily_users[1:]:
        retention_keys = set(retention_current.keys())

        # returning users
        retention_current = {id:retention_current[id]+1 for id in retention_keys & today}
        # new users
        retention_current.update({id: 1 for id in today - retention_keys})
    
        # add the day to the counts
        day_counts.append(count_retention(retention_current))
        
    # write output
    for i, day in enumerate(day_counts):
        print ','.join([str(i+1)]+[str(d) for d in day])

if __name__ == '__main__':
    start = time.time()
    find_retention(sys.argv[1])
    print 'duration:', time.time()-start
