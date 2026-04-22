#!/usr/bin/python3
"""MongoDB collection query utilities."""


def list_all(mongo_collection):
    """Return all documents from the MongoDB collection."""
    documents = mongo_collection.find()
    return list(documents)
