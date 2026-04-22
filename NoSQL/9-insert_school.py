#!/usr/bin/python3
"""MongoDB school document insertion utilities."""


def insert_school(mongo_collection, **kwargs):
    """Insert a school document into MongoDB collection."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
