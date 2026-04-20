# =========================================
# TASK: Students Points Aggregation
#
#
# Scenario:
# Prof. Jekyll keeps a text file with students' results.
# Each line contains:
#   first_name last_name points
# separated by whitespace.
#
# A student may appear multiple times.
#
# Example file:
# John   Smith   5
# Anna   Boleyn  4.5
# John   Smith   2
# Anna   Boleyn  11
# Andrew Cox     1.5
#
# Your tasks:
#
# 1. Ask the user for a filename.
# 2. Read the file.
# 3. Sum points for each student.
# 4. Print a sorted report:
#
# Andrew Cox     1.5
# Anna Boleyn    15.5
# John Smith     7.0
#
# Requirements:
#
# - Handle ALL possible errors:
#   • file does not exist
#   • file is empty
#   • incorrect data format
#
# - Program must terminate immediately on error
#   and show the error to the user.
#
# - Implement your own exception hierarchy:
#   • Base exception
#   • Bad line exception (wrong format)
#   • Empty file exception
#
# - Use a dictionary to store results.
#
# =========================================