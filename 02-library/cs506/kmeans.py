from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    if not points:
        raise ValueError('points should not be empty')
    ret = []
    for i in range(len(points[0])):
        ret.append(0)
    for point in points:
        for i in range(len(point)):
            ret[i] += point[i]
    for i in range(len(ret)):
        ret[i] = ret[i]/len(points)
    return ret


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    k = 0;
    for i in range(len(assignments)):
        if assignments[i] > k:
            k = assignments[i]

    points_after_assignment = []
    for i in range(k+1):
        points_after_assignment.append([])

    for i in range(len(assignments)):
        points_after_assignment[assignments[i]].append(dataset[i])

    centers = []
    for i in range(len(points_after_assignment)):
        centers.append(point_avg(points_after_assignment[i]))

    return centers


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    if not a or not b:
        raise ValueError('lengths must not be zero')
    if len(a) != len(b):
        raise ValueError('lengths must be equal')
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i])**2
    return sum**(1/2)


def distance_squared(a, b):
    if not a or not b:
        raise ValueError('lengths must not be zero')
    if len(a) != len(b):
        raise ValueError('lengths must be equal')
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i])**2
    return sum


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    ret = []
    included = []
    while k > len(ret):
        temp = random.randint(0, len(dataset)-1)
        if temp not in included:
            ret.append(dataset[temp])
            included.append(temp)
    return ret


def cost_function(clustering):
    cost = 0
    for each in clustering:
        centroid = point_avg(clustering[each])
        for point in clustering[each]:
            cost += distance_squared(point, centroid)
    return cost


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    start_point = generate_k(dataset, 1)
    distances = []
    for point in dataset:
        distances.append(distance_squared(start_point[0], point))
    
    for distance in distances:
        distance = distance**2

    choice_pool = []
    for i in range(len(dataset)):
        for distance in distances:
            choice_pool.append(dataset[i])

    ret = []
    for i in range(k):
        ret.append(random.choice(choice_pool))

    return ret


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
