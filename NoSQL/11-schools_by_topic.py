#!/usr/bin/env python3
""" function that returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    schools = []

    for school in mongo_collection.find({"topics": topic}):
        schools.append(school)

    return schools
