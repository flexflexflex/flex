#!/usr/bin/env bash
cat deploy/targets.txt | vegeta attack -duration=5s -rate=1000 | vegeta report
