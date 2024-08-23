def check_mount_rental(time_used, time_purchased):

    if (time_used >= time_purchased):
        result = "overtime charged"
    else:
        result = "no charges yet"

    return result
