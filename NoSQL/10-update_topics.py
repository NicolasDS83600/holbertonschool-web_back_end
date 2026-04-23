#!/usr/bin/env python3
"""MongoDB update utilities."""


def update_topics(mongo_collection, name, topics):
    """Update topics field of a school document."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
