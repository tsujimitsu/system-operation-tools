#!/bin/bash

# #####################################################
# login_sourceip_check.sh
#
version="1.0.0"
#
# HISTORY:
#
# * 2016.02.24 - v1.0.0 = First Creation
#
# #####################################################

# Purpose:
# -----------------------------------------------------
# check wrong server login
# This program check result about "last" command.
# -----------------------------------------------------

script_name="login_sourceip_check.sh"
script_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
utils_path="${script_path}/login_sourceip_check.conf"
logfile="${script_path}/login_sourceip_check.log"
tmpdir="/tmp/${script_name}.$RANDOM.$$"

(umask 077 && mkdir "${tmpdir}") || {
    die "Could not create temporary directory! Exiting."
}

if [ -f "${utils_path}" ]; then
    source "${utils_path}"
else
    echo "Please find the utils file and add a reference to it in this script."
    exit 1
fi

# Trap cleanup
function trap_cleanup() {
    echo ""
    if [ -d "${tmpdir}" ]; then
        rm -rf "{tmpdir}"
    fi
    die "Exit trapped."
}

# Safe exit
function safe_exit() {
    if [ -d "${tmpdir}" ]; then
        rm -rf "${tmpdir}"
    fi
    trap - INT TERM EXIT
    exit
}

# Main logic
function main_script() {
    last | egrep -v 'system boot|^wtmp|^$' | awk '{print $3}' | sort | uniq
}


# Usage
function usage {
cat <<EOF

ex) run program
./login_sourceip_check.sh

ex) display usage
./login_sourceip_check.sh -h

ex) run debug mode
./login_sourceip_check.sh -d

EOF
}


# Option
while [ $# -gt 0 ]; do
    case ${1} in
        -h|--help) usage >&2; safe_exit ;;
        -v|--version) echo "$(basename ${0}) $version"; safe_exit ;;
        -d|--debug) set -x ;;
        *) die "[ERROR] Invalid option '${1}'" ;;
    esac
    shift
done


trap trap_cleanup EXIT INT TERM
set -o errexit

# Run main script
main_script

# Exit cleanly
safe_exit
