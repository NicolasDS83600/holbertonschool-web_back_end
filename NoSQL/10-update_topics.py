#!/usr/bin/env python3
"""MongoDB update utilities."""


def update_topics(mongo_collection, name, topics):
    """Update topics field of a school document."""
    return mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
