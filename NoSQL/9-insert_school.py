#!/usr/bin/env python3
"""MongoDB school document insertion utilities."""


def insert_school(mongo_collection, **kwargs):
    """Insert a school document into MongoDB collection."""
    return mongo_collection.insert_one(kwargs).inserted_id
