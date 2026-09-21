#!/usr/bin/env bash
docker info 2>/dev/null | grep -i "storage driver"
df -h /
