#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""
import json


def class_to_json(obj):
    """Returns dict representation of a class object"""
    return obj.__dict__
