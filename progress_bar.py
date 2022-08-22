def print_progress_bar(iteration, total, prefix='', suffix='', usePercentage=False, decimals=1, length=80, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration      - Required  : current iteration (Int)
        total          - Required  : total iterations (Int)
        prefix         - Optional  : prefix string (Str)
        suffix         - Optional  : suffix string (Str)
        decimals       - Optional  : positive number of decimals in percent complete (Int)
        length         - Optional  : character length of bar (Int)
        fill           - Optional  : bar fill character (Str)
        printEnd       - Optional  : end character (e.g. "\r", "\r\n") (Str)
        usePercentage  - Optional  : show percentage instead of 'iteration/total' (Bool)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)

    if usePercentage:
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    else:
        print(f'\r{prefix} |{bar}| {iteration:>{len(f"{total}")}}/{total} {suffix}', end=printEnd)

    # Print New Line on Complete
    if iteration == total:
        print()

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=80, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {iteration:>{len(f"{total}")}}/{total} {suffix}', end=printEnd)

    # Print New Line on Complete
    if iteration == total:
        print()

def print_progress(iteration, total, prefix='', suffix='', decimals=1, printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    print(f'\r{prefix} {iteration}/{total} ({percent}%) {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

if __name__ == "__main__":
    pass