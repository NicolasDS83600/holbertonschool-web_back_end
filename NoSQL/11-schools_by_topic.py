#!/usr/bin/env python3
"""MongoDB school topic search utilities."""


def schools_by_topic(mongo_collection, topic):
    """Find schools with a specific topic."""
    return list(mongo_collection.find({"topics": topic}))
