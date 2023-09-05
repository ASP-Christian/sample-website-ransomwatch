#!/bin/bash
Xvfb :99 -ac -screen 0 1920x1080x16 -nolisten tcp &
firefox-esr --no-remote
