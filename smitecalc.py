# Copyright - Alexander Greenstein (KhaosComplex)
import pandas as pd
from math import isnan
from itertools import permutations

# Create and return the DataFrame from the file
def load_items(filename):
    return pd.read_excel(filename)

# Create the permutations of builds and returns the iterator
def create_builds(df, number_of_items):
    # Make a list of tuples out of the DataFrame
    smite_tuples = [tuple(x) for x in df.values]

    # Create a permutation list of all possible n-item build combinations
    return permutations(smite_tuples, number_of_items)

# Returns a n size list of the most efficient physical defense builds (r = raw phys stat)
def physical_defense_builds_r(df, builds, n):
    good_builds   = []
    price         = df.columns.get_loc('Price')
    phys_prot     = df.columns.get_loc('Phys Prot')
    item_name     = df.columns.get_loc('Item')
    unique_ratios = {}

    # Calculate the gold to stat ratios for each builds and remember the position from the original list
    for build in builds:
        total_price = 0
        total_phys  = 0
        for item in build:
            total_price += 0 if isnan(item[price]) else item[price]
            total_phys  += 0 if isnan(item[phys_prot]) else item[phys_prot]
        ratio = total_phys / total_price
        if not(ratio in unique_ratios):
            good_builds.append([total_phys/total_price, total_price, total_phys, build])
            unique_ratios[ratio] = ratio

    # Now sort and return the list of n most efficient builds in the proper format (item build)
    good_builds.sort(reverse=True)
    final_list = []
    for x in range(0, n):
        build = good_builds[x][-1]
        item_build = []
        for item in build:
            item_build.append(item[item_name])
        item_build.extend((good_builds[x][1], good_builds[x][2], round(good_builds[x][0],4)))
        final_list.append(item_build)

    return final_list

# Returns a n size list of the most efficient physical defense builds (e = effective health)
def physical_defense_builds_e(df, builds, n):
    good_builds         = []
    price               = df.columns.get_loc('Price')
    phys_prot           = df.columns.get_loc('Phys Prot')
    health              = df.columns.get_loc('Health')
    item_name           = df.columns.get_loc('Item')
    unique_effective_HP = {}

    # Calculate the gold to stat ratios for each builds and remember the position from the original list
    for build in builds:
        total_price  = 0
        total_phys   = 0
        total_HP     = 0
        for item in build:
            total_price += 0 if isnan(item[price]) else item[price]
            total_phys  += 0 if isnan(item[phys_prot]) else item[phys_prot]
            total_HP    += 0 if isnan(item[health]) else item[health]
        effective_HP = total_HP / (100 / (total_phys + 100))
        ratio        = effective_HP / total_price
        if not (ratio in unique_effective_HP):
            good_builds.append([ratio, total_price, effective_HP, total_phys, build])
            unique_effective_HP[ratio] = ratio

    # Now sort and return the list of n most efficient builds in the proper format (item build)
    good_builds.sort(reverse=True)
    final_list = []
    for x in range(0, n):
        build = good_builds[x][-1]
        item_build = []
        for item in build:
            item_build.append(item[item_name])
        item_build.extend((good_builds[x][1], good_builds[x][2], good_builds[x][3], round(good_builds[x][0], 4)))
        final_list.append(item_build)

    return final_list

# Returns a n size list of the most efficient magical defense builds (r = raw mag stat)
def magical_defense_builds_r(df, builds, n):
    good_builds   = []
    price         = df.columns.get_loc('Price')
    mag_prot      = df.columns.get_loc('Mag Prot')
    item_name     = df.columns.get_loc('Item')
    unique_ratios = {}

    # Calculate the gold to stat ratios for each builds and remember the position from the original list
    for build in builds:
        total_price = 0
        total_mag   = 0
        for item in build:
            total_price += 0 if isnan(item[price]) else item[price]
            total_mag   += 0 if isnan(item[mag_prot]) else item[mag_prot]
        ratio = total_mag / total_price
        if not(ratio in unique_ratios):
            good_builds.append([total_mag/total_price, total_price, total_mag, build])
            unique_ratios[ratio] = ratio

    # Now sort and return the list of n most efficient builds in the proper format (item build)
    good_builds.sort(reverse=True)
    final_list = []
    for x in range(0, n):
        build = good_builds[x][-1]
        item_build = []
        for item in build:
            item_build.append(item[item_name])
        item_build.extend((good_builds[x][1], good_builds[x][2], round(good_builds[x][0],4)))
        final_list.append(item_build)

    return final_list

# Returns a n size list of the most efficient magical defense builds (e = effective health)
def magical_defense_builds_e(df, builds, n):
    good_builds         = []
    price               = df.columns.get_loc('Price')
    mag_prot            = df.columns.get_loc('Mag Prot')
    health              = df.columns.get_loc('Health')
    item_name           = df.columns.get_loc('Item')
    unique_effective_HP = {}

    # Calculate the gold to stat ratios for each builds and remember the position from the original list
    for build in builds:
        total_price = 0
        total_mag   = 0
        total_HP    = 0
        for item in build:
            total_price += 0 if isnan(item[price]) else item[price]
            total_mag   += 0 if isnan(item[mag_prot]) else item[mag_prot]
            total_HP    += 0 if isnan(item[health]) else item[health]
        effective_HP = total_HP / (100 / (total_mag + 100))
        ratio        = effective_HP / total_price
        if not (ratio in unique_effective_HP):
            good_builds.append([ratio, total_price, effective_HP, total_mag, build])
            unique_effective_HP[ratio] = ratio

    # Now sort and return the list of n most efficient builds in the proper format (item build)
    good_builds.sort(reverse=True)
    final_list = []
    for x in range(0, n):
        build = good_builds[x][-1]
        item_build = []
        for item in build:
            item_build.append(item[item_name])
        item_build.extend((good_builds[x][1], good_builds[x][2], good_builds[x][3], round(good_builds[x][0], 4)))
        final_list.append(item_build)

    return final_list

# print the builds each on a separate line
def print_builds(builds):
    for build in builds:
        print(build)