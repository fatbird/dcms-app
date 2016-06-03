Overview
========

This is a demo app for DCMS library.

Setup
=====

`manage.py migrate`
`manage.py runserver`

Everything else is in the web pages.

To run multiple instances via runserver, preface the manage.py command with
`DCMS_NODE=x`, where X is a number > 1:

    DCMS_NODE=2 manage.py runserver 127.0.0.1:8001
    
This uses a SQLite database ending in .2, so will require migrating as well if
it's not been done:

    DCMS_NODE=2 manage.py migrate

Multiple hosts can be configured in the settings file under `DCMS_NODES`. 
Currently, three are configured as so:

    DCMS_NODES = {
        1: {'host': 'http://localhost:8000', },
        2: {'host': 'http://localhost:8001', },
        3: {'host': 'http://localhost:8002', },
    }
    
Models in `core` that are to be used by DCMS are configured under `DCMS_TYPES`.

TODO
====

DCMS:
1. Authentication
1. Logging
1. Network Topology
