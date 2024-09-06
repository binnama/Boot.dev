def trim_strongholds(strongholds):

    # Delete the first stronghold in the list
    del strongholds[0]

    # Delete the last 2 strongholds in the list
    del strongholds[-2:]

    return strongholds
