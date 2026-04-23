#!/usr/bin/env python3
"""MongoDB collection query utilities."""


def list_all(mongo_collection):
    """Return all documents from the MongoDB collection."""
    return list(mongo_collection.find())
