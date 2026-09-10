# AtmoSync Snowflake Setup

## Objective

Set up the Snowflake environment for the AtmoSync project.

## Database

Database:
ATMOSYNC_DB

## Schema

Schema:
RAW

## Raw Table

Table:
CONTAINER_TELEMETRY

## Telemetry Fields

- EVENT_ID
- CONTAINER_ID
- EVENT_TIMESTAMP
- TEMPERATURE
- HUMIDITY
- VIBRATION

## Access Role

Role:
ATMOSYNC_RAW_READER

## Day 1 Work

- Created Snowflake database structure
- Created RAW schema
- Designed raw container telemetry table
- Created raw-data reader role
- Documented Snowflake setup